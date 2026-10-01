# Local helper Builder self-check

This is a Builder self-check, not independent QA and not final archive/runtime acceptance.

## Executed environment and result

- Environment: Linux, Python 3.12.14, standard library only
- Date: 2026-10-01
- Command: `python3 -m unittest discover -s tests -v`
- Result: 15 tests PASS, 5.763 seconds in the first complete run
- These were real subprocess and loopback HTTP integration tests against generated test fixtures. No runtime installation, network downloads, escalation, or workaround around a denied socket was used
- The final Anthropic presentation ZIP and rendered browser visuals were not the fixture under test
- `WINDOWS_LAUNCHER_TEST_RESULT=NOT_RUN`: Windows was unavailable. The .bat scripts were inspected, not executed
- `APP_RENDERING_TEST_RESULT=NOT_RUN`: these tests do not certify visual rendering, application behavior, or the final archive

## Executed coverage

1. Python minimum version gate
2. Reject absolute/traversal/backslash/alternate-data-stream/control-character package paths
3. Unicode Thai and space paths
4. Readiness, exact app bytes, repeat start reuse, status, orderly stop, idempotent stop, restart, unrelated working directory
5. Occupied-port selection leaves the unrelated listening socket live
6. Concurrent starts reuse one server under a cross-process operation lock
7. Deny Host-header DNS rebinding, cross-origin/cross-site requests, unauthenticated control, bad stop body, non-manifest assets and package/state source reads
8. Encoded traversal and malformed UTF-8/path handling; HEAD and Unicode URL asset serving
9. Verified bytes remain immutable in memory after underlying app modification
10. Tampered manifest-listed bytes fail before readiness
11. Manifest traversal fails before startup
12. Symlinked listed file and symlinked app directory fail before readiness (Linux symlinks executed; Windows junction checks inspected only)
13. Altered instance/PID state cannot stop an authentic running server
14. Copied state in another extraction cannot stop the original server; separate extraction gets a distinct server
15. A changed manifest requires orderly stop before starting the new version

## Runtime and assembly contract

- Install Python 3.10+ once from the official Python distribution; ordinary startup uses no dependencies beyond its standard library
- Include `app/`, `START.bat`, `STOP.bat`, `serve.py`, `README_TH.md`, `manifest.json`
- Manifest fields: string PROJECT_ID, PACKAGE_VERSION, BUILD_COMMIT, LOCAL_RUNTIME; `files` is an object mapping package-relative paths to lowercase SHA-256 hex
- Include launcher/payload hashes; exclude manifest itself, `.local-server/`, tests, caches and logs from manifest/runtime ZIP
- Startup validates every listed file, then holds only verified app bytes in RAM. The 256 MiB aggregate manifest payload cap is deliberate
- App script files must be external local scripts. CSP allows local scripts/assets, inline CSS, data/blob images, local/blob media; it denies external requests and inline JavaScript
- Package identity combines the canonical extraction folder, exact manifest digest, random instance and secret token; PID is diagnostic identity only
- The child binds directly to 127.0.0.1, tries the preferred port and the next 20 ports, then a kernel-assigned loopback port
- Stop is an authenticated HTTP request with identity verification. No PID/port process killing, signals, firewall settings or browser-security changes
- Store transient runtime state under `.local-server/` and ignore/exclude it from Git and packaging

## Honest security limitations

The manifest is an unsigned integrity inventory. A malicious archive or an attacker with the user's account/filesystem authority can alter the helper, manifest and state together. Windows inherits the extraction folder's ACLs; use a trusted private local folder. POSIX directory traversal uses O_NOFOLLOW and descriptor-relative reads; Windows denies reparse points and checks opened file identity, but its behavior remains unexecuted here. Browser navigation/opening and Windows missing-runtime detection have not been exercised. Stopping an unresponsive server is deliberately conservative: the launcher reports the blocker rather than killing any process.

Pending before final delivery: independent exact-archive identity/extraction and real-browser app checks, target Windows start/stop/restart/offline execution, then owner rehearsal/acceptance.
