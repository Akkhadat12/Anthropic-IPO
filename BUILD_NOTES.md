# Build notes — Anthropic IPO capacity ledger

**Status:** Deployed to a public Vercel production URL and verified. Ready for independent QA per [05_QA.md](05_QA.md).

## Build facts

| Item | Value |
| --- | --- |
| Branch | `research-ipo-financials-models-2026` |
| Stack | Vite 8, three.js 0.186 (vanilla, no framework), Playwright-core for local checks only |
| Build | `npm install && npm run build` → `dist/` (Vercel auto-detects Vite) |
| Public production URL | https://anthropic-ipo-capacity-ledger.vercel.app (Vercel project `anthropic-ipo-capacity-ledger`, target `production`, deployment `dpl_CJnwxicNfbv6ctqVGyKMPdbVCCY7`) |
| Deployed commit | `349c3cd67d4217496d3dae1b0ac7338647af1e85` (shown as `349c3cd` in the Sources overlay footer). Later commits on the branch are documentation only |
| Build date | 2026-09-29 |

## Visual direction comparison (04 §Prototype step 1)

Both directions are live behind `?dir=a` and `?dir=b` and share geometry, data, and interaction. Screenshots: [build-notes/screens/](build-notes/screens/) (`a-*` = Daylight ledger, `b-*` = Night blueprint; `desk` = 1920×1080, `phone` = 390×844; A captured for cover, models, capacity only).

| | A. Daylight ledger | B. Night blueprint (chosen) |
| --- | --- | --- |
| Look | Warm paper field, ink edges, matte planes | Dark field, luminous edges, glowing accents |
| Strength | Reads like an accounting ledger | Status colors and depth separate clearly; real photo pops |
| Weakness | Ground and slabs read flat and grey; less depth on video | Slightly more “tech” than “finance” |

**Chosen: B.** For a 16:9 YouTube recording, contrast and depth cues matter more than paper metaphor, and five status classes must stay distinguishable. Each status also has a distinct badge shape (solid, dashed, pill, double, dotted) so meaning never relies on color alone.

## Requirement coverage

- Nine scenes, order and IDs per 04: `cover, demand, retained, models, statements, capacity, scenarios, filing, close`. `document.body.dataset.scene` exposes the settled scene, `dataset.busy` the transition state.
- Presenter-controlled only; no autoplay. Space advances one stop (ignored while a transition runs, so rapid presses cannot skip or stack). `R` → cover from anywhere, including mid-transition and from the overlay. `Esc` closes the overlay. Space inside the overlay does not advance. On `close`, Space does nothing; **Restart** is explicit.
- Primary target per scene exists two ways: a clickable 3D object with a pulsing halo, and an equivalent text button in the dock. Scene rail allows rehearsal jumps.
- In-scene selectors that do not advance: Opus/Sonnet toggle (`models`), three scenario paths (`scenarios`, selectable by button or by clicking a path), five disclosure gates (`filing`).
- Sources / caveats overlay per scene: status class, direct source link, caveat; focus trap; focus returns to the opener.
- Reduced motion (OS setting or `?motion=reduced`): same destinations, instant camera, no pulse.
- Narrow screens (<760px or aspect <0.9): labels become a stacked list above the dock, camera pulls back, secondary depth flattens.
- Data lives in [src/data.js](src/data.js) and mirrors [references/chart-data.csv](references/chart-data.csv) one-to-one, with source IDs and caveats. Nothing is interpolated: no year-by-year commitment bars, no channel split, no forecast values.
- Visible text is English only. Real assets: the two AWS Project Rainier images from `references/`, attributed on the page and in the overlay.
- Direct landing supported: `/?scene=capacity` (used for QA screenshots).

## Production verification (2026-09-29)

- `GET /` and `/img/project-rainier-interior.png` return 200 with no login. Page title is “Anthropic IPO: Capacity Ledger”; this is a separate Vercel project from the historical `anthropic-ipo-two-clocks` (main).
- `node tools/flow.mjs https://anthropic-ipo-capacity-ledger.vercel.app`: all 38 checks passed against the live URL.

## Local verification performed

- `node tools/flow.mjs <url>`: 38 checks, all passed on the final build. Covers the Space route, rapid Space, every primary click destination, `R` mid-transition and from overlay, overlay open/close/Space/Escape, scenario / gate / model selectors staying in scene, 3D doorway click, reduced-motion route, and zero console errors.
- `node tools/shot.mjs <url> <dir> <a|b> <scenes>`: desktop and phone captures of every scene.
- Not tested: real touch device, Safari/Firefox, hardware GPU performance (headless software GL only).

## Known limitations and decisions for QA

1. **Do not confuse projects.** The historical `anthropic-ipo-two-clocks` deployment is not this build.
2. **Source URLs copied from the handoff.** They were not re-opened by the builder; 05_QA requires QA to reopen each.
3. **Space on in-scene selector buttons** activates them natively (Enter also works); Space elsewhere advances.
4. **Phone 3D is context only.** Facts are carried by the stacked label list; the 3D objects are small at 390px by design.
5. **Corridor ribbon** in `capacity` is qualitative (demand above floor). It encodes no magnitude.
6. **`06_SCENE_RATIONALE`** (Thai Google Doc / .docx with scene screenshots) is not created yet; it depends on the deployed build.
7. `?dir=a` remains available as an alternate direction; it is not the shipped default.
