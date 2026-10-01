# BUILD_NOTES — Anthropic IPO local package

## Status
Provisional build, not runtime-certified and not READY_FOR_QA. No independent QA_PASS is claimed. The user selected LOCAL_ZIP for Windows; no public hosting is required or used. Main, old branches and legacy/ remain unchanged.

## Reproduce from BUILD_COMMIT
Obtain the exact source SHA recorded in delivery/package-identity.json. With Python >=3.10 installed: `python scripts/build.py`; `python tests/static_check.py`; `python scripts/package.py 0.1.0-provisional`; `python tests/archive_check.py delivery/anthropic-ipo-20261001-0426-0.1.0-provisional-local.zip`. Node is optional for developer tests: `node --test tests/state.test.mjs`. No pip/npm install or network is required for build/package or ordinary launch. Source JavaScript is bundled by simple deterministic concatenation, no third-party toolchain.

The ZIP root has prebuilt app/, START.bat, STOP.bat, serve.py, README_TH.md, CREDITS.txt and manifest.json. Manifest records exact BUILD_COMMIT, version and per-file SHA-256; the archive hash is external to avoid self-reference. ZIP entries are sorted with fixed date and permissions. Technical source, caches, old projects, unlicensed logos, source research captures and credentials are excluded.

## Controls and state
Space is complete forward flow. During reveal/transition it settles only that endpoint. Next deliberate Space reveals/advances. R immediately cancels finite animations/timers and resets S01. Left Arrow goes to the prior scene final hold (S01 remains b0). F requests/exits fullscreen; rejection only updates English semantic status. Modifier shortcuts, held repeats and editable fields are ignored. No visible navigation, source panel, credit overlay, progress or hints. No clicks required.

23 endpoints, 9 scenes, unchanged approved exact object/copy ledger. Crossfade 350ms + 200ms settle; reveal 650ms + 200ms settle. Reduced motion immediate. Holds have no animation loop or auto-advance. Pointer changes only on mouse events: 14 CSS px indigo #354F91, 2px paper edge and 1px ink outer edge. Non-blocking, hidden outside stage/blur/touch; native cursor hidden only when active. Its viewport geometry remains unchanged by logical stage scaling.

## Cover and licensed payload
A01 is the authenticated 2023 TechCrunch photograph of Dario Amodei, shown full-frame fit-contain with no crop. It is not an IPO-event photo. First HTML includes it; R restores it. First image failure uses A01F once, then a semantic-only English failure message. A double image failure is a defect, not substitute imagery. Complete title, author/provider/copyright, source/license and actual proportional JPEG resize are retained in CREDITS.txt, README_TH and rationale. Both Noto WOFF derivatives and corresponding OFL files ship. Manifest hashes match reviewed assets.

## Verification and capability boundary
Observed environment: cloud Linux, Python 3.12.14. Static build, JS/Python syntax, pure state-machine tests and asset/language checks run. Browser plugin is absent; installed Playwright/Chromium was attempted according to frontend-testing guidance. Chromium terminated before page creation with `socket() failed: Operation not permitted`. A reviewed sandbox escalation produced the same result. Supported CUA cloud browser rejected local `file://` because only HTTP/HTTPS are allowed. These are actual verified capability blockers; no security flags, proxy or public deployment workaround is used.

Helper integration/security worker passed 15/15 real Python TCP loopback tests on Linux. This does not certify the actual extracted presentation ZIP. Chromium process startup is restricted, not Python TCP serving. Actual browser render, performance measurement, 30-second hold, reduced-motion browser exercise, pointer hotspot/contrast, fullscreen, offline network trace, extracted-package presentation and Windows START/STOP remain to verify. Tests/browser_check.py is a prepared unexecuted test harness, not test evidence. Planned performance target is <2000ms ready on a recorded desktop host, stable hold without live animation/timers. Cross-browser and small-phone readability are unverified; desktop recording is the approved scope.

## Continuation
Use exact delivered ZIP/hash and BUILD_COMMIT. The supported existing cloud browser may inspect the actual package over its permitted HTTP loopback URL; file:// remains disallowed. Extract fresh; validate manifest before running. A permitted executor must execute serve.py start/status/stop, occupied-port/repeat-start/restart/path-with-Thai tests and browser_check.py against extracted loopback app; inspect all scene/reveal states and proper fallback, repeat/modified keys, pointer, reduced motion and fullscreen. Run independent QA only after Builder’s required checks are complete. Windows launchers must be run on actual Windows when available; until then WINDOWS_LAUNCHER_TEST_RESULT and OWNER_WINDOWS_SMOKE_RESULT remain NOT_RUN. The owner must rehearse Thai narration: 560 seconds is editorial only.

The package/rationale URLs and exact source/archive identities are recorded in delivery/package-identity.json and WORKFLOW_STATUS.md after verified upload, not guessed here.
