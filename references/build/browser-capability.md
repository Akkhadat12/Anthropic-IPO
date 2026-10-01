# Browser capability evidence — Builder

2026-10-01 UTC. This is a capability/attempt record, not rendered verification or independent QA.

1. Installed Playwright attempted Chromium at `/usr/bin/chromium` in headless mode using the existing sandbox configuration. Chromium terminated before page creation: `FATAL:chrome/browser/process_singleton_posix.cc:297 ... socket() failed: Operation not permitted (1)`.
2. A reviewed `require_escalated` attempt returned the same error; no page, screenshot, console, performance or UI result was obtained.
3. The supported existing CUA cloud browser was inspected using its documented API. Opening the local presentation `file://` URL was rejected by URL policy: only HTTP/HTTPS schemes are allowed. This path was stopped, not rewritten to evade the policy.
4. A real cleanly extracted package was launched with the Python helper, which returned `Ready: http://127.0.0.1:8765/`. A single supported browser navigation to that HTTP loopback URL returned `net::ERR_BLOCKED_BY_CLIENT`; no rendered page was obtained. No alias/proxy/public host or browser/network protection change was attempted.
5. Python TCP serving is demonstrably supported independently of Chromium process startup. All 15 helper integration tests passed, then the final v0.1.1 archive was separately extracted and exercised with readiness, all app payload HTTP byte hashes, repeated start/status/stop/restart. The server was stopped after the test. Exact evidence: extracted-runtime-provisional.json. Background lifetime across shell tool calls is not guaranteed; no claim that the temporary server remains running is made.

Pending: browser geometry and clipping; all scene/reveal rendering; clean canvas during actual interactions; reduced motion; >30-second holds; pointer hotspot/contrast/blur/failure; fullscreen; image and font load failures; browser offline network observation; startup/motion performance. Windows START.bat/STOP.bat execution is NOT_RUN on this Linux executor.

Use the exact delivered archive on a permitted browser-capable executor. Do not mark READY_FOR_QA until Builder's required checks are complete; independent QA remains a separate actor/gate. A source/static test or existing Visual storyboard does not replace these checks.
