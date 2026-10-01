# Isolated-runtime Builder verification — 2026-10-01

Result: **BLOCKED_FROM_STAGE=BUILDING**. No rendered page or screenshot was obtained. Independent QA was not started because the Builder gate did not pass. This is not QA_PASS or Windows verification.

## Scope and identity

- Separate scratch clone of the authorized project branch; initial HEAD `c11466e2c4a3ac8f7cf5186e0a17db02d33b8f5b`.
- Frozen source worktree: `e2210041c93b8cbf5588eada5058fef60d0f6ad9`.
- Rebuilt `0.1.1-provisional` using committed `scripts/package.py`; 544,191 bytes, SHA-256 `e36c0843d8287046c9427f12abd729aef73d26337696f7044670d189c1cee327`, exactly matching the recorded delivered archive identity.
- This run tested a **source rebuild**, not a newly downloaded Library/Drive copy. Library materialization resolved the expected backing file/version/size but its current transfer helper returned `library file transfer failed: download failed`; no readable destination file was created. The failed transfer was not bypassed. Drive was not downloaded again.
- Existing Library identity `libfile_79c9420a13d08191bbd00696b3f02cdc`, backing file `file_000000006e0082108bb491cdd292bf80`, and Drive identity `1bPfzQVZOwyVdFtf_ct-sIUspe-u-py6a` are unchanged. No new ZIP version/upload is needed for this evidence-only update.
- Linux, Python 3.12.14, Node v24.19.0, Chromium 151.0.7922.173 (Debian 13).
- No project AGENTS.md or .agents skill files were present in this clone; mounted /workspace/.agents was empty. Project README, workflow, build/QA instructions and existing test harness were consulted.

## Browser capability blocker

First normal headless launch failed before a page existed:

```text
chromium --headless --disable-gpu --dump-dom about:blank
Failed to create headless user data directory container.
exit 1
```

A second launch used only a writable, isolated profile directory:

```text
chromium --headless --disable-gpu --user-data-dir=/workspace/scratch/anthropic-browser-profile --dump-dom about:blank
chrome_crashpad_handler: --database is required
FATAL:sandbox/linux/suid/client/setuid_sandbox_host.cc:166
The SUID sandbox helper binary was found, but is not configured correctly.
Rather than run without sandboxing I'm aborting now.
You need to make sure that /usr/lib/chromium/chrome-sandbox is owned by root and has mode 4755.
exit 134
```

Read-only inspection found `/usr/lib/chromium/chrome-sandbox` mode `-rwsr-xr-x`, owner/group `nobody:nogroup`, rather than root. No chmod/chown, sandbox-disabling flags, namespace changes, package installs, escalation, proxy, public hosting or permission changes were attempted. No separate callable browser connector was exposed in this task. Earlier success on another project does not establish supported browser capability in this runtime.

## Test matrix

| Check | Result | Evidence / scope |
|---|---|---|
| Frozen-source reproducible ZIP | PASS | 544,191 bytes and exact recorded SHA-256 |
| Manifest and clean extraction | PASS | 16 entries, all listed hashes, required launcher/app/credits paths; tests/archive_check.py |
| Static scenes/assets/language | PASS_STATIC_ONLY | 9 scenes, 23 endpoints, asset hashes match, English; tests/static_check.py |
| State machine | PASS | node --test tests/state.test.mjs: 3/3; forward route, reset/back, held/modifier/editable input rules |
| Helper integration/security | PASS | python3 -m unittest discover -s tests/launcher -v: 15/15 in 6.348 s; fixture scope, including occupied ports, concurrent starts, integrity, traversal, path and cross-instance safety |
| Rebuilt ZIP extracted app HTTP | PASS | All 10 app payload hashes match over loopback; extracted-runtime.json |
| Extracted Python launch/repeat/status/stop/restart | PASS_LINUX_ONLY | Unrelated working directory; exact unmodified packaged helper; ready 8775, restart 8776, final stopped state; extracted-runtime.json |
| Local assets/fonts included | PASS_STATIC_HTTP_ONLY | Manifest and HTTP hashes; browser offline requests not observed |
| 23 rendered endpoints at 1920x1080, 1280x720, non-16:9 | BLOCKED | Browser aborted before page creation; no screenshots |
| Visible/semantic English in running browser | BLOCKED | Static language check is not browser acceptance |
| Overlap/clipping/letterboxing/clean canvas | BLOCKED | No rendered geometry |
| Pointer/theme/fullscreen | BLOCKED | No rendered/input evidence |
| Space/R, repeated/interrupted browser inputs | BLOCKED | Pure state tests passed; DOM/event behavior untested |
| Motion/transitions/reduced motion/30-second holds | BLOCKED | No running browser |
| Browser offline/fallback/performance | BLOCKED | No running browser |
| Independent QA | NOT_RUN | Must follow completed Builder gate with separate reviewer |
| Windows START.bat/STOP.bat | NOT_RUN | Linux Python execution does not execute Windows launchers |
| Owner Windows smoke/rehearsal/acceptance | NOT_RUN | Remains required before COMPLETE |

## Continuation

Use the same branch and exact source/archive identity on a runtime whose **supported sandboxed browser launch succeeds**. Do not disable its sandbox or alter host security to clear this gate. Complete all required Builder render/input/offline checks, fix/version only if actual defects are found, then hand the exact package to a separate independent QA reviewer. Retain the existing Drive links. Final owner Windows execution and rehearsal remain pending. No current owner-document accessibility readback is claimed here.

The mounted Mob-Control repository was not edited and its final git status remains clean. Only scoped project evidence and live workflow metadata are published on the authorized branch; runtime, content, citations, metrics, narration and asset identity are unchanged.
