"""Run: python3 -m unittest discover -s tests -v (no third-party packages)."""
import contextlib
import hashlib
import http.client
import importlib.util
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve()
SOURCE = next(path for path in (HERE.parents[1], HERE.parents[2] / 'delivery')
              if (path / 'serve.py').is_file())
spec = importlib.util.spec_from_file_location('local_helper', SOURCE / 'serve.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


class PathRules(unittest.TestCase):
    def test_rejects_absolute_traversal_windows_ads_and_controls(self):
        for value in ('../secret', '/etc/passwd', 'app/../secret', 'app//file',
                      'app\\file', 'C:/secret', 'app/x:secret', 'app/./x', 'app/x\x00', ''):
            with self.subTest(value=value):
                with self.assertRaises(helper.LaunchError):
                    helper.checked_parts(value)

    def test_accepts_spaces_and_thai(self):
        self.assertEqual(helper.checked_parts('app/ภาพ ของฉัน.svg'), ['app', 'ภาพ ของฉัน.svg'])

    def test_runtime_minimum_is_enforced(self):
        saved = sys.version_info
        try:
            sys.version_info = (3, 9, 0)
            self.assertEqual(helper.main(), 2)
        finally:
            sys.version_info = saved


class LauncherIntegration(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='แพ็กเกจ with spaces ')
        self.root = Path(self.temp.name)
        self.roots = [self.root]
        self.create_package(self.root)

    def create_package(self, root):
        root.mkdir(parents=True, exist_ok=True)
        (root / 'app').mkdir()
        for name in ('serve.py', 'START.bat', 'STOP.bat', 'README_TH.md'):
            shutil.copyfile(SOURCE / name, root / name)
        (root / 'app/index.html').write_text('<!doctype html><html lang="en">Verified presentation</html>', encoding='utf-8')
        (root / 'app/ภาพ sample.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"/>', encoding='utf-8')
        names = ('serve.py', 'START.bat', 'STOP.bat', 'README_TH.md', 'app/index.html', 'app/ภาพ sample.svg')
        manifest = {'PROJECT_ID': 'anthropic-test', 'PACKAGE_VERSION': '1.0-test',
                    'BUILD_COMMIT': 'a' * 40, 'LOCAL_RUNTIME': 'Python 3.10+',
                    'files': {name: hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names}}
        (root / 'manifest.json').write_text(json.dumps(manifest), encoding='utf-8')

    def tearDown(self):
        for root in self.roots:
            self.command('stop', root=root, check=False)
        self.temp.cleanup()

    def command(self, *args, root=None, check=True):
        root = root or self.root
        result = subprocess.run([sys.executable, '-I', str(root / 'serve.py'), *args],
                                cwd=str(SOURCE), capture_output=True, text=True, timeout=35)
        if check:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def start(self, **kw):
        self.command('start', '--no-browser', **kw)
        return self.state(kw.get('root'))

    def state(self, root=None):
        return json.loads(((root or self.root)/'.local-server/state.json').read_text())

    def request(self, path='/', method='GET', headers=None, body=None, state=None):
        state = state or self.state()
        conn = http.client.HTTPConnection('127.0.0.1', state['port'], timeout=3)
        try:
            conn.request(method, path, body=body, headers=headers or {})
            response = conn.getresponse()
            return response.status, response.read(), dict(response.getheaders())
        finally:
            conn.close()

    def test_start_ready_repeat_stop_restart_and_foreign_cwd(self):
        first = self.start()
        code, body, headers = self.request()
        self.assertEqual(code, 200)
        self.assertIn(b'Verified presentation', body)
        self.assertEqual(headers['X-Content-Type-Options'], 'nosniff')
        repeat = self.command('start', '--no-browser')
        self.assertIn('Already running:', repeat.stdout)
        self.assertEqual(first['pid'], self.state()['pid'])
        self.command('status')
        self.command('stop')
        self.assertFalse((self.root/'.local-server/state.json').exists())
        self.assertEqual(self.command('status', check=False).returncode, 1)
        self.command('stop')  # Idempotent
        again = self.start()
        self.assertNotEqual(first['instance'], again['instance'])

    def test_occupied_port_preserves_unrelated_listener(self):
        with socket.socket() as occupied:
            occupied.bind(('127.0.0.1', 0))
            occupied.listen()
            port = occupied.getsockname()[1]
            self.command('start', '--no-browser', '--port', str(port))
            self.assertNotEqual(self.state()['port'], port)
            self.command('stop')
            self.assertEqual(occupied.getsockname()[1], port)
            with socket.create_connection(('127.0.0.1', port), timeout=1):
                pass

    def test_concurrent_starts_reuse_one_instance(self):
        cmd = [sys.executable, '-I', str(self.root/'serve.py'), 'start', '--no-browser']
        one = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        two = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out1, err1 = one.communicate(timeout=35)
        out2, err2 = two.communicate(timeout=35)
        self.assertEqual(one.returncode, 0, out1 + err1)
        self.assertEqual(two.returncode, 0, out2 + err2)
        self.assertEqual((out1 + out2).count('Already running:'), 1)
        self.assertEqual((out1 + out2).count('Ready:'), 1)
        self.assertEqual(self.request()[0], 200)

    def test_http_security_and_no_unlisted_or_parent_files(self):
        state = self.start()
        (self.root/'app/private.txt').write_text('not in manifest')
        for path in ('/manifest.json', '/serve.py', '/.local-server/state.json',
                     '/private.txt', '/app/index.html', '/directory/'):
            with self.subTest(path=path):
                self.assertIn(self.request(path)[0], (400, 404))
        for path in ('/../manifest.json', '/%2e%2e/manifest.json',
                     '/%2e%2e%2fmanifest.json', '/%5c..%5csecret', '/x:secret',
                     '/%00', '/%ZZ', '//etc/passwd', '/a//b'):
            with self.subTest(path=path):
                self.assertIn(self.request(path)[0], (400, 404))
        self.assertEqual(self.request(headers={'Host': 'attacker.example'})[0], 403)
        self.assertEqual(self.request(headers={'Origin': 'https://attacker.example'})[0], 403)
        self.assertEqual(self.request(headers={'Sec-Fetch-Site': 'cross-site'})[0], 403)
        self.assertEqual(self.request('/_local/identity')[0], 403)
        self.assertEqual(self.request('/_local/stop', 'POST', body=b'')[0], 403)
        auth = {'Authorization': 'Bearer ' + state['token']}
        self.assertEqual(self.request('/_local/identity', headers=auth)[0], 200)
        self.assertEqual(self.request('/_local/stop', 'POST', headers=auth, body=b'bad')[0], 403)
        self.assertEqual(self.request()[0], 200)
        self.assertEqual(self.request('/%E0%B8%A0%E0%B8%B2%E0%B8%9E%20sample.svg')[0], 200)
        self.assertEqual(self.request('/', 'HEAD')[1], b'')

    def test_verified_payload_is_immutable_in_memory(self):
        self.start()
        original = self.request()[1]
        (self.root/'app/index.html').write_text('changed after startup')
        self.assertEqual(self.request()[1], original)

    def test_integrity_failure_fails_before_readiness(self):
        (self.root/'app/index.html').write_text('tampered')
        result = self.command('start', '--no-browser', check=False)
        self.assertEqual(result.returncode, 2)
        self.assertIn('Integrity check failed', result.stderr)
        self.assertFalse((self.root/'.local-server/state.json').exists())

    def test_manifest_traversal_rejected(self):
        path = self.root/'manifest.json'
        manifest = json.loads(path.read_text())
        manifest['files']['../secret'] = '0' * 64
        path.write_text(json.dumps(manifest))
        result = self.command('start', '--no-browser', check=False)
        self.assertEqual(result.returncode, 2)
        self.assertIn('Invalid package path', result.stderr)

    @unittest.skipUnless(hasattr(os, 'symlink'), 'symlinks unsupported')
    def test_manifest_listed_symlink_to_outside_is_rejected(self):
        outside = self.root/'outside.txt'
        outside.write_text('outside app')
        link = self.root/'app/leak.txt'
        try:
            link.symlink_to(outside)
        except OSError:
            self.skipTest('symlink privilege unavailable')
        path = self.root/'manifest.json'
        manifest = json.loads(path.read_text())
        manifest['files']['app/leak.txt'] = hashlib.sha256(outside.read_bytes()).hexdigest()
        path.write_text(json.dumps(manifest))
        result = self.command('start', '--no-browser', check=False)
        self.assertEqual(result.returncode, 2)
        self.assertFalse((self.root/'.local-server/state.json').exists())

    @unittest.skipUnless(hasattr(os, 'symlink'), 'symlinks unsupported')
    def test_symlinked_app_directory_is_rejected(self):
        (self.root/'app').rename(self.root/'real-app')
        try:
            (self.root/'app').symlink_to(self.root/'real-app', target_is_directory=True)
        except OSError:
            self.skipTest('symlink privilege unavailable')
        result = self.command('start', '--no-browser', check=False)
        self.assertEqual(result.returncode, 2)
        self.assertFalse((self.root/'.local-server/state.json').exists())

    def test_stop_rejects_changed_instance_without_signals(self):
        saved = self.start()
        path = self.root/'.local-server/state.json'
        changed = dict(saved, instance='0' * 64, pid=1)
        path.write_text(json.dumps(changed))
        try:
            result = self.command('stop')
            self.assertIn('No matching package server', result.stdout)
            self.assertEqual(self.request(state=saved)[0], 200)
        finally:
            path.write_text(json.dumps(saved))

    def test_copied_state_never_controls_other_extraction(self):
        original = self.start()
        second = self.root/'สำเนา package'
        self.create_package(second)
        self.roots.append(second)
        (second/'.local-server').mkdir(mode=0o700)
        shutil.copyfile(self.root/'.local-server/state.json', second/'.local-server/state.json')
        self.command('stop', root=second)
        self.assertEqual(self.request(state=original)[0], 200)
        other = self.start(root=second)
        self.assertNotEqual(original['port'], other['port'])
        self.assertNotEqual(original['instance'], other['instance'])
        self.command('stop', root=second)
        self.assertEqual(self.request(state=original)[0], 200)

    def test_changed_manifest_requires_orderly_stop_before_start(self):
        original = self.start()
        path = self.root/'manifest.json'
        manifest = json.loads(path.read_text())
        manifest['PACKAGE_VERSION'] = 'new-version'
        path.write_text(json.dumps(manifest))
        result = self.command('start', '--no-browser', check=False)
        self.assertEqual(result.returncode, 2)
        self.assertIn('different package version', result.stderr)
        self.assertEqual(self.request(state=original)[0], 200)
        self.command('stop')
        updated = self.start()
        self.assertNotEqual(original['manifest_sha256'], updated['manifest_sha256'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
