#!/usr/bin/env python3
"""Verified, loopback-only static package launcher. Python 3.10+, stdlib only.

No installation, shell commands, public binding, process killing, or telemetry.
The manifest is an integrity inventory, not a cryptographic signature.
"""

import argparse
import contextlib
import hashlib
import hmac
import http.client
import json
import mimetypes
import os
from pathlib import Path, PurePosixPath
import re
import secrets
import socket
import stat
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote_to_bytes, urlsplit
import webbrowser

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
DEFAULT_PORT = 8765
STATE_DIR = ROOT / ".local-server"
MAX_TOTAL = 256 * 1024 * 1024
MAX_FILES = 10000
SCHEMA = 1
HEX64 = re.compile(r"^[0-9a-f]{64}$")


class LaunchError(Exception):
    pass


def folder_id():
    return hashlib.sha256(os.path.normcase(str(ROOT)).encode("utf-8")).hexdigest()


def is_link(info):
    # Junctions and other reparse points are also forbidden on Windows.
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0) & 0x400)


def checked_parts(relative):
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise LaunchError("Invalid package path")
    if any(ord(c) < 32 or c == ":" for c in relative):
        raise LaunchError("Invalid package path")
    parts = relative.split("/")
    if any(p in ("", ".", "..") for p in parts) or PurePosixPath(relative).is_absolute():
        raise LaunchError("Invalid package path")
    return parts


def safe_read(relative, limit=MAX_TOTAL):
    """Read a regular file beneath ROOT without following links.

    POSIX opens each directory relative to a descriptor with O_NOFOLLOW.
    Windows rejects every reparse component and checks the opened identity.
    A hostile process with the same filesystem authority is outside the model.
    """
    parts = checked_parts(relative)
    if os.open in os.supports_dir_fd and hasattr(os, "O_NOFOLLOW"):
        directory = os.open(str(ROOT), os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        fd = None
        try:
            for part in parts[:-1]:
                nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                              dir_fd=directory)
                os.close(directory)
                directory = nxt
            fd = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                         dir_fd=directory)
            before = os.fstat(fd)
            if not stat.S_ISREG(before.st_mode) or before.st_size > limit:
                raise LaunchError("Package file is not a permitted regular file: " + relative)
            with os.fdopen(fd, "rb") as stream:
                fd = None
                data = stream.read(limit + 1)
        finally:
            if fd is not None:
                os.close(fd)
            os.close(directory)
    else:
        path = ROOT
        for part in parts:
            path = path / part
            info = path.lstat()
            if is_link(info):
                raise LaunchError("Links/reparse points are not permitted: " + relative)
        before = path.lstat()
        if not stat.S_ISREG(before.st_mode) or before.st_size > limit:
            raise LaunchError("Package file is not a permitted regular file: " + relative)
        with path.open("rb") as stream:
            opened = os.fstat(stream.fileno())
            if (before.st_dev, before.st_ino) != (opened.st_dev, opened.st_ino):
                raise LaunchError("Package file changed while opening: " + relative)
            data = stream.read(limit + 1)
    if len(data) > limit:
        raise LaunchError("Package size limit exceeded")
    return data


def read_manifest():
    raw = safe_read("manifest.json", 4 * 1024 * 1024)
    try:
        manifest = json.loads(raw)
    except (ValueError, UnicodeError) as exc:
        raise LaunchError("manifest.json is invalid") from exc
    if not isinstance(manifest, dict):
        raise LaunchError("manifest.json must be an object")
    for key in ("PROJECT_ID", "PACKAGE_VERSION", "BUILD_COMMIT"):
        value = manifest.get(key)
        if not isinstance(value, str) or not value.strip() or len(value) > 200:
            raise LaunchError("Missing or invalid manifest field: " + key)
    files = manifest.get("files")
    if not isinstance(files, dict) or not files or len(files) > MAX_FILES:
        raise LaunchError("Manifest files must map package-relative paths to SHA-256 hashes")
    if "app/index.html" not in files:
        raise LaunchError("Manifest does not include app/index.html")
    for name, digest in files.items():
        checked_parts(name)
        if name == "manifest.json" or name.startswith(".local-server/"):
            raise LaunchError("Manifest contains a prohibited transient/self entry")
        if not isinstance(digest, str) or not HEX64.fullmatch(digest):
            raise LaunchError("Invalid SHA-256 for: " + name)
    return manifest, hashlib.sha256(raw).hexdigest()


def load_payload(manifest):
    files = {}
    total = 0
    for name, expected in manifest["files"].items():
        data = safe_read(name, MAX_TOTAL - total)
        total += len(data)
        if not hmac.compare_digest(hashlib.sha256(data).hexdigest(), expected):
            raise LaunchError("Integrity check failed: " + name + "; extract a clean ZIP")
        if name.startswith("app/"):
            path = "/" + name[4:]
            if path.startswith("/_local/"):
                raise LaunchError("Reserved app path: " + name)
            mime = mimetypes.guess_type(name)[0] or "application/octet-stream"
            # Avoid Windows registry MIME variations for executable browser assets.
            suffix = PurePosixPath(name).suffix.lower()
            mime = {".js": "text/javascript", ".mjs": "text/javascript",
                    ".css": "text/css", ".html": "text/html",
                    ".json": "application/json", ".svg": "image/svg+xml",
                    ".woff2": "font/woff2"}.get(suffix, mime)
            if mime.startswith("text/") or mime in ("application/json", "image/svg+xml"):
                mime += "; charset=utf-8"
            files[path] = (data, mime)
    return files


def prepare_state_dir():
    try:
        STATE_DIR.mkdir(mode=0o700)
    except FileExistsError:
        pass
    info = STATE_DIR.lstat()
    if is_link(info) or not stat.S_ISDIR(info.st_mode):
        raise LaunchError(".local-server must be an ordinary writable directory")
    if os.name != "nt":
        if info.st_uid != os.getuid() or info.st_mode & 0o077:
            raise LaunchError(".local-server must belong to you and have mode 700")


def state_file_read(name, limit=16384):
    return safe_read(".local-server/" + name, limit)


@contextlib.contextmanager
def operation_lock():
    prepare_state_dir()
    path = STATE_DIR / "operation.lock"
    if path.exists() and is_link(path.lstat()):
        raise LaunchError("Unsafe operation lock")
    fd = os.open(str(path), os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0), 0o600)
    locked = False
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise LaunchError("Unsafe operation lock")
        if os.fstat(fd).st_size == 0:
            os.write(fd, b"0")
        deadline = time.monotonic() + 25
        while True:
            try:
                if os.name == "nt":
                    import msvcrt
                    os.lseek(fd, 0, os.SEEK_SET)
                    msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                locked = True
                break
            except OSError:
                if time.monotonic() >= deadline:
                    raise LaunchError("Another start/stop is busy; wait and retry")
                time.sleep(0.1)
        yield
    finally:
        if locked:
            if os.name == "nt":
                import msvcrt
                os.lseek(fd, 0, os.SEEK_SET)
                msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def read_state():
    try:
        state = json.loads(state_file_read("state.json"))
    except FileNotFoundError:
        return None
    except (ValueError, UnicodeError) as exc:
        raise LaunchError("Invalid launcher state; no processes were stopped") from exc
    if not isinstance(state, dict) or state.get("schema") != SCHEMA:
        raise LaunchError("Invalid launcher state")
    if state.get("folder_id") != folder_id():
        # A copied package must never control the original extraction's server.
        return None
    if type(state.get("port")) is not int or not 1024 <= state["port"] <= 65535:
        raise LaunchError("Invalid state port")
    for key in ("token", "instance", "manifest_sha256"):
        if not isinstance(state.get(key), str) or not HEX64.fullmatch(state[key]):
            raise LaunchError("Invalid state identity")
    if type(state.get("pid")) is not int or state["pid"] <= 0:
        raise LaunchError("Invalid state process identity")
    return state


def write_state(state):
    path = STATE_DIR / ("state-" + secrets.token_hex(8) + ".tmp")
    fd = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(state, stream, sort_keys=True)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(str(path), str(STATE_DIR / "state.json"))
    finally:
        with contextlib.suppress(FileNotFoundError):
            path.unlink()


def public_identity(state):
    return {key: state[key] for key in (
        "schema", "folder_id", "instance", "manifest_sha256", "pid", "port")}


def request_control(state, method="GET", path="/_local/identity"):
    conn = http.client.HTTPConnection(HOST, state["port"], timeout=1.0)
    try:
        conn.request(method, path, body=b"" if method == "POST" else None,
                     headers={"Authorization": "Bearer " + state["token"]})
        response = conn.getresponse()
        body = response.read(16385)
        if response.status != 200 or len(body) > 16384:
            return None
        result = json.loads(body)
        return result if result == public_identity(state) else None
    except (ConnectionRefusedError, ConnectionResetError, http.client.HTTPException,
            ValueError, UnicodeError):
        return None
    except TimeoutError as exc:
        raise LaunchError("A local server did not answer; no process was stopped. Retry shortly") from exc
    finally:
        conn.close()


class LocalServer(ThreadingHTTPServer):
    allow_reuse_address = False
    daemon_threads = True
    block_on_close = False
    request_queue_size = 16

    def server_bind(self):
        if self.server_address[0] != HOST:
            raise LaunchError("Only 127.0.0.1 is permitted")
        if os.name == "nt" and hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()

    def get_request(self):
        sock, address = super().get_request()
        sock.settimeout(5)
        return sock, address


class Handler(BaseHTTPRequestHandler):
    server_version = "LocalPresentation"
    sys_version = ""
    protocol_version = "HTTP/1.0"

    def log_message(self, fmt, *args):
        # No URLs, tokens, user text, or browser request headers in logs.
        pass

    def reply(self, status, data=b"", mime="text/plain; charset=utf-8"):
        self.send_response(status)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cross-Origin-Resource-Policy", "same-origin")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; "
                         "style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; "
                         "font-src 'self'; media-src 'self' blob:; connect-src 'none'; "
                         "object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'")
        self.end_headers()
        if self.command != "HEAD" and data:
            self.wfile.write(data)

    def allowed(self):
        origin = "http://" + HOST + ":" + str(self.server.server_port)
        if self.client_address[0] != HOST:
            return False
        if self.headers.get_all("Host", []) != [origin[7:]]:
            return False
        if self.headers.get("Origin") not in (None, origin):
            return False
        if self.headers.get("Sec-Fetch-Site") == "cross-site":
            return False
        return True

    def authenticated(self):
        values = self.headers.get_all("Authorization", [])
        return len(values) == 1 and hmac.compare_digest(
            values[0], "Bearer " + self.server.state["token"])

    def clean_path(self):
        parsed = urlsplit(self.path)
        if parsed.scheme or parsed.netloc or parsed.fragment or not parsed.path.startswith("/"):
            raise LaunchError("Invalid request path")
        if re.search(r"%(?![0-9a-fA-F]{2})", parsed.path):
            raise LaunchError("Invalid percent encoding")
        path = unquote_to_bytes(parsed.path).decode("utf-8", "strict")
        if path == "/":
            return "/index.html"
        checked_parts(path[1:])
        return path

    def do_GET(self):
        if not self.allowed():
            return self.reply(403, b"Forbidden")
        try:
            path = self.clean_path()
        except (LaunchError, ValueError, UnicodeError):
            return self.reply(400, b"Invalid path")
        if path.startswith("/_local/"):
            if path != "/_local/identity" or not self.authenticated():
                return self.reply(403, b"Forbidden")
            return self.reply(200, json.dumps(public_identity(self.server.state)).encode("utf-8"),
                              "application/json")
        payload = self.server.payload.get(path)
        if payload is None:
            return self.reply(404, b"Not found")
        return self.reply(200, payload[0], payload[1])

    do_HEAD = do_GET

    def do_POST(self):
        if (not self.allowed() or not self.authenticated() or
                self.path != "/_local/stop" or
                self.headers.get_all("Content-Length", []) != ["0"] or
                self.headers.get("Transfer-Encoding") is not None):
            return self.reply(403, b"Forbidden")
        self.reply(200, json.dumps(public_identity(self.server.state)).encode("utf-8"),
                   "application/json")
        threading.Thread(target=self.server.shutdown, daemon=True).start()

    def do_OPTIONS(self):
        self.reply(405, b"Method not allowed")


def bind_server(preferred):
    ports = list(range(preferred, min(preferred + 20, 65535) + 1)) + [0]
    for port in ports:
        try:
            return LocalServer((HOST, port), Handler)
        except OSError as exc:
            # Bind directly, never probe-then-bind or kill a port owner.
            if getattr(exc, "errno", None) not in (13, 48, 98, 10013, 10048):
                raise
    raise LaunchError("No loopback port could be opened")


def run_server():
    prepare_state_dir()
    bootstrap = json.loads(sys.stdin.buffer.readline(16385))
    if (not isinstance(bootstrap, dict) or
            not HEX64.fullmatch(str(bootstrap.get("token", ""))) or
            not HEX64.fullmatch(str(bootstrap.get("instance", "")))):
        raise LaunchError("Invalid server bootstrap")
    manifest, digest = read_manifest()
    if digest != bootstrap.get("manifest_sha256"):
        raise LaunchError("Manifest changed during startup")
    preferred = bootstrap.get("port")
    if type(preferred) is not int or not 1024 <= preferred <= 65535:
        raise LaunchError("Invalid preferred port")
    payload = load_payload(manifest)
    server = bind_server(preferred)
    state = {"schema": SCHEMA, "folder_id": folder_id(), "manifest_sha256": digest,
             "pid": os.getpid(), "port": server.server_port,
             "token": bootstrap["token"], "instance": bootstrap["instance"]}
    server.payload = payload
    server.state = state
    try:
        write_state(state)
        server.serve_forever(poll_interval=0.1)
    finally:
        server.server_close()
        try:
            current = read_state()
            if current and current["instance"] == state["instance"]:
                (STATE_DIR / "state.json").unlink()
        except (FileNotFoundError, LaunchError, OSError):
            pass


def launch(preferred, open_browser):
    with operation_lock():
        _, digest = read_manifest()
        old = read_state()
        if old and request_control(old):
            if old["manifest_sha256"] != digest:
                raise LaunchError("A different package version is running here; run STOP.bat first")
            state = old
            reused = True
        else:
            bootstrap = {"token": secrets.token_hex(32), "instance": secrets.token_hex(32),
                         "manifest_sha256": digest, "port": preferred}
            log_path = STATE_DIR / "server.log"
            if log_path.exists() and is_link(log_path.lstat()):
                raise LaunchError("Unsafe launcher log file")
            fd = os.open(str(log_path), os.O_WRONLY | os.O_CREAT | os.O_TRUNC |
                         getattr(os, "O_NOFOLLOW", 0), 0o600)
            with os.fdopen(fd, "wb") as log:
                kwargs = {"start_new_session": True} if os.name != "nt" else {
                    "creationflags": subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP}
                child = subprocess.Popen([sys.executable, "-I", str(ROOT / "serve.py"), "_serve"],
                                         cwd=str(ROOT), stdin=subprocess.PIPE, stdout=log,
                                         stderr=log, **kwargs)
                child.stdin.write(json.dumps(bootstrap).encode("utf-8") + b"\n")
                child.stdin.close()
            deadline = time.monotonic() + 20
            state = None
            while time.monotonic() < deadline:
                if child.poll() is not None:
                    try:
                        detail = state_file_read("server.log", 16384).decode("utf-8", "replace").strip()
                    except (OSError, LaunchError):
                        detail = "See .local-server/server.log"
                    raise LaunchError("Server did not start. " + detail)
                candidate = read_state()
                if (candidate and candidate["instance"] == bootstrap["instance"]
                        and request_control(candidate)):
                    state = candidate
                    break
                time.sleep(0.1)
            if state is None:
                # No arbitrary PID termination, including on a startup timeout.
                raise LaunchError("Readiness timed out; retry status or STOP.bat. No process was killed")
            reused = False
        url = "http://" + HOST + ":" + str(state["port"]) + "/"
        print(("Already running: " if reused else "Ready: ") + url, flush=True)
    if open_browser:
        try:
            if not webbrowser.open(url, new=2):
                print("Browser did not open automatically. Open the Ready URL above.")
        except webbrowser.Error:
            print("Browser did not open automatically. Open the Ready URL above.")
    return 0


def stop():
    with operation_lock():
        state = read_state()
        if not state or not request_control(state):
            print("No matching package server is running. No other process was touched.")
            return 0
        if not request_control(state, "POST", "/_local/stop"):
            raise LaunchError("Server identity was not confirmed; nothing was terminated")
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            current = read_state()
            if not current or current["instance"] != state["instance"]:
                print("Stopped this package's server.")
                return 0
            time.sleep(0.1)
        raise LaunchError("Stop was requested but completion is unverified; no process was killed")


def status():
    with operation_lock():
        state = read_state()
        if state and request_control(state):
            print("Running: http://" + HOST + ":" + str(state["port"]) + "/")
            return 0
        print("Not running")
        return 1


def main():
    if sys.version_info < (3, 10):
        print("Python 3.10 or newer is required. Install once from https://www.python.org/downloads/", file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("start", "stop", "status", "_serve"))
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error("--port must be between 1024 and 65535")
    try:
        if args.command == "_serve":
            run_server()
            return 0
        if args.command == "start":
            return launch(args.port, not args.no_browser)
        return stop() if args.command == "stop" else status()
    except (LaunchError, OSError, ValueError) as exc:
        print("Launcher error: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
