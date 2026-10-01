# Anthropic IPO — current Design specification

This filled topic specification is authoritative for Design 1.1 (Visual-aligned). The v1.7 master contract below is retained for reference; its angle-bracket fields are template examples, not unresolved live Design choices. Content and narration remain unchanged. This is a specification-only handoff, not a Visual Plan, rendered concept approval, implementation, or runtime QA.

## Visual-aligned language and cover amendment

Owner decision on 2026-10-01: English visible scene text, Thai narration (“เป็น english แบบเดิม”). Canvas copy in Visual 1.0 supersedes the earlier Thai proposals; Thai remains correct for spoken script, rationale and owner documents. All in-app semantic/alt/accessibility and fallback/error text is English; HTML lang=en. English words count by whitespace, with punctuation excluded and hyphenated compounds counted once. All-state ordinary/excluded/total ledgers are exact in 03. Minimum visible type is 36px; English line height is 1.25 with full glyph padding. The reference frames are static concepts, not runtime output.

The coordinator accepted the authentic relevant-image alternative: CC BY 2.0 photograph of Dario Amodei at TechCrunch Disrupt, 20 September 2023. Generic Anthropic text is not a reconstructed logo. Use A01 with same-source offline fallback A01F, no crop, no recoloring/mirroring; full creator/copyright/license/change credit accompanies the package via README_TH and rationale. No credits UI is added to the recording canvas. The photo must never be described as a 2026 IPO-event photograph. Official logos remain unlicensed for this handoff and must not ship. Asset/font provenance and binary hashes are in assets/manifest.json. Any earlier pending-cover wording below describes the original Design-only checkpoint and is superseded only by this verified Visual asset selection.

## Identity and design intent

~~~yaml
PROJECT_ID: anthropic-ipo-20261001-0426
BRANCH: project/anthropic-ipo-20261001-0426
CONTENT_INPUT_COMMIT: 501f48afb1bddf098de95fa75f995dbd016d54c5
CONTENT_HANDOFF_COMMIT: 87d4628046d15a1ab887be99b37eafe3489ce71d
CONTENT_ARTIFACT_COMMIT: 6384d754ade1c931cae7dba2e62a5aab9234badc
DESIGN_VERSION: "1.1"
ON_CANVAS_LANGUAGE: English
NARRATION_LANGUAGE: Thai
QUICK_START_LANGUAGE: Thai
OWNER_DOCUMENT_LANGUAGE: Thai
DOCUMENT_LANG_ATTRIBUTE: en
WEB_LANGUAGE: English
DESIGN_INTENT: "An editorial financial explanation: isolate the evidence, distinguish its clock and definition, then ask what it can prove."
AUDIENCE: Thai general audience
CANVAS: 1920x1080
ASPECT_RATIO: "16:9"
SAFE_AREA: "x=96..1824; y=54..1026. Preferred text zone x=144..1776; y=108..972."
BACKGROUND: "#F5F1E8 warm paper; neutral evidence field"
FOREGROUND: "#202722 ink; primary text and measured evidence"
ACCENT_PRIMARY: "#226B5C deep teal; documented demand or positive operating signal, never certainty of future returns"
ACCENT_SECONDARY: "#965038 clay; obligation, cost boundary or conditional pressure, never automatic failure"
MUTED: "#576158 secondary evidence; remains fully readable"
POINTER_COLOR: "#354F91 indigo; presenter attention only, never a data category"
FONT_PRIMARY: "Noto Sans 400/600 for English canvas/numerals; Noto Sans Thai 400/600 for Thai owner-document source only; no Thai runtime text; package both with OFL"
FONT_FALLBACK: "Packaged Noto Sans Thai/Noto Sans first; Tahoma, Arial, sans-serif emergency system fallback only"
TYPE_SCALE: "display 96; focal number 120; concept 64; data value 56; direct label 40; minimum label 32 logical px"
MIN_LABEL_SIZE: 32
LINE_HEIGHT: "English/numerals 1.25; no clipping; Thai owner documents are separate"
MAX_TEXT_WIDTH: "0.58 of canvas (1114 px) for a focal phrase; 0.80 only for one data group"
SPACING_SCALE: [12, 24, 36, 48, 72, 96, 144]
OBJECT_STYLE: "Flat 2D editorial geometry; 3–4 px ink outlines; square ends; no glass, glow, beveled tiles or decorative shadows"
DATA_ENCODING: "Position and direct labels first; magnitude only within the same metric, period and unit; no decorative area scaling"
COMPOSITION_GRID: "12 invisible columns; 96 px outer margin; 24 px gutters; focal anchors at x=480, 960, 1440"
MOTION_EASING: "cubic-bezier(0.22,1,0.36,1); controlled deceleration, no bounce/overshoot"
ENTRY_DURATION_MS: 500
REVEAL_DURATION_MS: 650
SETTLE_DURATION_MS: 200
EXIT_DURATION_MS: 350
HOLD: indefinite_until_presenter_input
REDUCED_MOTION: "Immediate identical semantic endpoint; optional opacity-only fade <=100 ms, no translation"
AUDIO_POLICY: "Live Thai narration; no soundtrack, sound effects, autoplay audio or synthetic voice"
POINTER_MODE: theme_adaptive_presenter_dot
POINTER_DIAMETER_CSS_PX: 14
POINTER_EDGE_OR_HALO: "2 CSS px #F5F1E8 inner edge and 1 CSS px #202722 outer edge; static, no glow"
COVER_ASSET_STYLE: authentic_original_image_required
COVER_IMAGE_PLACEMENT: "Authentic licensed 2023 founder photo x=192,y=220,w=840,h=560; generic Anthropic name and English question to right x=1152; exact geometry in Visual Plan"
DELIVERY_MODE: LOCAL_ZIP
TARGET_OS: Windows
OFFLINE_AFTER_SETUP: true
PUBLIC_DEPLOYMENT_REQUIRED: false
COVER_ASSET_ID: A01_DARIO_TECHCRUNCH_2023_CC_BY_2_0
COVER_ASSET_VERIFICATION: VERIFIED_PHOTO_AND_CREDITS; logos not cleared
FONT_BINARY_AND_RENDER_VERIFICATION: VERIFIED_BINARY_AND_STATIC_STORYBOARD; browser runtime pending Build
~~~

The story is a sequence of questions, not a dashboard. Use open space, direct labels and purposeful juxtaposition. No equal-weight card grid, corporate pitch-deck chrome, hero statistics strip, investment-terminal imitation, speculative stock ticker or repeated title-and-bullets layout. Do not treat Anthropic's visual identity as endorsement of this independent explanation.

## Hierarchy, composition and English typography

- Maintain one dominant subject per beat, approximately 45–65% of the usable width. A supporting item may use at most 25%; the eye should not need to choose between simultaneous animations.
- Preferred reading direction is left-to-right for relationships and top-to-bottom for qualification. Use the same anchor when a later beat changes evidentiary status. Empty space represents separation, not a quantified distance.
- A scene may have one focal phrase plus its explanatory object, or a directly labeled data group. Do not add a standing header, footer or source strip. Sources and full caveats remain in the narration, accessible description, source register and eventual rationale; indispensable period/definition caveats stay beside displayed data.
- No repeated panel boxes around unrelated subjects. A document silhouette is allowed only for an actual document-status concept and must not imitate an inspected confidential filing. It needs a truthful label; don't display fabricated document text.
- Essential objects stay inside the 5% safe area. Text prefers the larger inner margin. Keep at least 24 logical px around glyph bounds and 48 px between unrelated label groups. Fit the complete line box, including tone marks and descenders; never crop by tight bounding rectangles.
- English canvas text uses meaningful editorial line breaks. Never split a word, fiscal-year label or value-plus-unit. No synthetic bold or condensed width. Thai shaping checks apply to owner documents, not an unapproved canvas override.
- Numbers use the same aligned numeral style within a scene; decimal and grouping conventions must match source precision. No animated counting through invented intermediate figures. Prefer million-dollar units consistent with narration; if a billion-dollar shorthand is used, Visual must document conversion and prominently supply its unit. Do not show extra significant digits.
- At 1280×720 the stage scales to two-thirds, so a 32 logical px minimum is about 21 CSS px. Smaller viewports preserve the exact 16:9 layout with neutral paper letterboxing; no portrait reflow, cropping or scrollbar. Mobile is not a separate redesign target for this owner-approved desktop recording artifact. Do not claim small-phone label readability is verified.
- Backdrop and letterbox share paper color. All text sits on plain paper, never across a busy photo or transparent gradient. Official images may retain their native background if usage rules require it.

## Semantic color and accessibility

Color is a secondary cue. Ink means evidence, teal highlights demand/positive operating signals, clay highlights obligations/cost constraints. These meanings stay constant across scenes; teal must not mean buy and clay must not mean sell. Indigo is reserved for the pointer.

Every distinction also has a direct label and/or meaningful line treatment:
- Reported completed-period evidence: solid outline plus exact period and metric.
- Preliminary result: solid outline with the visible qualification beside the metric. A solid shape alone never implies audited.
- Outlook: open/dashed boundary plus the explicit outlook label, never a filled "achieved" bar.
- Unknown information: explicit unknown label or an open question, not a zero, empty financial bar or negative outcome.
- Analysis/scenario: explicitly labeled as a scenario; consistent geometry and visual weight, no probability-sized branches.
These treatments do not replace words where the financial distinction is necessary. Styling alone is not a legend.

Calculated sRGB contrast on #F5F1E8: ink #202722 13.55:1; muted #576158 5.72:1; teal #226B5C 5.60:1; clay #965038 5.32:1; indigo #354F91 6.95:1. All specified text pairs exceed 4.5:1. These are token calculations, not image-background or browser-render tests. Do not lower essential-text opacity. Do not place teal on clay. Meaningful strokes need >=3:1 against the adjacent fill; if a later asset/background changes, recheck that pair.

Provide a concise semantic scene description for assistive technology: what the visual shows, relevant value/period/definition, uncertainty, and main takeaway. Expose settled scene/beat descriptions without reading each animation frame. No focusable hidden buttons or focus popups on the canvas. Thai narration and the owner reading editions supply longer equivalents; English in-app semantic descriptions remain separately required. All key distinctions must survive grayscale and reduced motion; no hover-only evidence or pointer-dependent continuation.

Font sources, checked 1 October 2026:
- Noto Sans Thai: https://github.com/google/fonts/tree/main/ofl/notosansthai
- Thai license: https://raw.githubusercontent.com/google/fonts/main/ofl/notosansthai/OFL.txt
- Noto Sans: https://github.com/google/fonts/tree/main/ofl/notosans
- Latin license: https://raw.githubusercontent.com/google/fonts/main/ofl/notosans/OFL.txt

Both license files identify SIL OFL 1.1. Visual/Builder must pin actual files and source revision, retain notices, record local paths/hashes and verify Thai/Latin coverage from those binaries. Expected English specimen includes “Sustainable profits?”, “Preliminary”, “Cash flow”, “Q2 2026”, “>US$11,500” and “80%”. The fallback is recovery, not permission to ship missing fonts. Do not use runtime Google Fonts or other network font requests.

## Financial encoding contract

Each displayed numerical claim is a tuple: claim ID, metric name, period/as-of, unit/denominator, evidence status, value/qualifier. Keep those necessary labels attached through every reveal and hold. Data labels may use the essential-label exception only when the visual would otherwise be false or undecodable. Explanation paragraphs do not become data labels by being small.

- FY2025 recognized revenue, Q2 2026 preliminary recognized revenue and end-July annualized run-rate must never share a revenue-comparison axis, connected growth line, sized circles, stacked total or implied ratio. Align date/definition groups typographically, not by magnitude. If using duration spans, length encodes only verified calendar duration and must be labeled accordingly.
- Publication date and reporting period are different clocks. The later Reuters headline must not move FY2025 after Q2 on a period timeline. A reporting-date layer, if genuinely needed, must be a separately labeled layer; prefer narration over a second visual clock.
- Net loss and its reported non-cash component belong to FY2025. A conceptual inclusion bracket is allowed; a calculated residual, subtraction animation, numeric waterfall or labeled cash-burn remainder is not. Do not animate money disappearing.
- Q2 positive adjusted operating income is preliminary. Q3 is outlook. No unlabeled positive bar, numeric profit size, net-income number or green cash-flow conclusion can be inferred.
- The reported gross-margin exclusion statement belongs only to gross margin. Prefer keeping the >80% figure in narration unless Visual can preserve all indispensable metric/exclusion labels legibly. If shown, isolate it from adjusted operating income; no shared profit funnel or all-cost wedge.
- Commitments are cumulative multiyear obligations. No equal annual payment blocks, annual-average computation, debt-due-now pile or sum with overlapping partnership announcements. A non-quantitative contract span must explicitly communicate approximate multiyear scope, not a maturity schedule.
- No current revenue-mix pie chart, unnamed real customer logos, inferred retention distribution, utilization percentage or fabricated forecast series. Historical customer concentration needs FY2025 attached. Claude Code February evidence cannot become current total-company mix.
- Comparisons/scenarios without quantified evidence use equal visual weight, no numeric axes, no implied likelihood ordering and no winner badge. A metaphor is not self-labeling: use a short explicit schematic/scenario label within ordinary-copy budget, or choose a literal conceptual arrangement instead.

## Medium rules and scene-family guidance

Prefer simple 2D vector/DOM graphics and the authentic opening image. Design does not select a framework. No 3D/WebGL, rendered datacenter world, animation video or simulated terminal is justified by this story: depth adds no supported data dimension. Real media is used for authentic identity/evidence only, with suitable rights; no AI-generated company/product reconstruction.

This table gives allowed visual jobs and forbidden implications, not final layouts or beat inventories. Agent 3 owns precise geometry, copy ledger, assets and all nine per-scene state plans.

| Scene | Design job and appropriate family | Locked factual/visual boundary |
|---|---|---|
| S01 | Authentic company identity with a single open sustainability question, static on first paint | Verified authentic licensed photo; 4 English question words plus generic company name = 5. No triumphant chart or collapse imagery |
| S02 | Document-status/evidence boundary; distinguish submitted draft from unknown offer terms | No bell-ringing, live ticker, SEC approval stamp or invented S-1 facsimile. Submission is not completed listing |
| S03 | Period-and-definition comparison with typographic/date anchors | No common magnitude axis across FY2025, Q2 and run-rate; keep preliminary/as-of visible if figures are shown |
| S04 | Concrete job-to-payment concept; focus on why repeat use matters | If illustrative work is shown, label it illustrative within ordinary-copy budget. No invented successful-task KPI, real customer identity, current mix or retention |
| S05 | Conceptual separation of accounting loss and cash | Historical FY2025 kept attached; no residual calculation, numeric reconciliation or disappearing-money metaphor |
| S06 | Evidence-status distinction and unanswered path to net income/cash | Positive preliminary operating signal genuinely visible; outlook explicitly distinct. Gross-margin exclusions cannot migrate to another metric |
| S07 | Capacity benefit first, then multiyear contractual constraint | No apparent actual rack counts, payment calendar, summed overlap or all-debt-now encoding. Approximate 80% must retain its actual contractual denominator if shown |
| S08 | Clearly labeled conditional alternatives, revealed with equal weight | Three narrated possibilities retained; no probabilities, numeric forecast, unmarked scale or unequal animation implying a preferred outcome |
| S09 | Evidence questions brought into one closing relationship | Keep revenue quality, profit-to-cash and obligations-over-time understandable; no investment verdict or new numerical claim |

A content arrow is optional and rare: maximum two visible at once, 3 logical px, small arrowhead, no circular button background or edge placement. It may show sequence or dependency only. A broken link signifies missing reconciliation only when explicitly identified; it must not suggest cash cannot exist. On S05 prefer separation rather than a directional flow that implies computed cash. No navigation arrow is allowed.

## Copy contract for Visual

Retain Content's meaning and stable scene IDs. Ordinary copy includes headings, model/entity labels, explanatory labels, scenario/metaphor markers, image text, wordmarks and attribution across every reveal, including repeated copies. The 0–8 target is scene-wide, not per beat. Content proposals are candidates, not a reason to add another heading. If a schematic needs a label, shorten/replace the proposed headline rather than add it above eight.

Content candidate ordinary counts: S01 5; S02 5; S03 4; S04 8; S05 5; S06 4; S07 5; S08 8; S09 5 (English Visual 1.0). English tokenization is recorded in 03_VISUAL_PLAN.md; no Thai canvas-language exception exists. English multiword labels count as individual words. Punctuation is not a word; a mathematical relationship still needs to be inventoried as a visible mark. Source attribution counts as ordinary unless it is an indispensable data identity, with a specific reason.

In 03_VISUAL_PLAN.md enumerate exact ordinary copy, segmented tokens, count, every excluded label with necessity, excluded count and total. Preserve signs such as “>”, “Nearly”, “About”, period labels and uncertainty. A numeric visual without these qualifications fails truthfulness even if it is sparse. Prefer fewer displayed figures with richer narration to a crowded chart. Do not shrink text, rasterize prose, cycle synonyms or hide crucial caveats in tooltips to pass the budget.

## Motion grammar and stable-state behavior

Motion is presenter-triggered, never a clock for narration. No auto-advance and no display timeout. The 560-second editorial budget is not a playback duration or a measured rehearsal.

| Pattern | Trigger / semantic job | Affected subject and motion | Timing / settled endpoint | Reduced motion |
|---|---|---|---|---|
| Establish | Scene entry; orient the eye | One subject opacity 0→1; optional <=24 logical px translation for a new group only | 500 ms + 200 ms settle; fixed anchor, full opacity | Immediate same anchor/opacity |
| Reveal relationship | Space from a hold; introduce one next spoken idea | Add one label/object or draw one semantic connector; preserve prior necessary context | 650 ms + 200 ms settle; completed geometry and full labels | Immediate full relationship |
| Qualify evidence | Space from a hold; distinguish preliminary/outlook/unknown | Reveal attached status label or boundary; do not resize a number or move its period | 500 ms + 200 ms settle; qualifier remains visible | Immediate identical qualification |
| Shift attention | Space from a hold; move focus between existing groups | Ink outline emphasis or accent change; do not dim indispensable text below contrast minimum | 500 ms + 200 ms settle; only one active focal accent | Immediate identical emphasis |
| Exit | Space only at final held beat; change scene | 350 ms crossfade without sliding the entire canvas or morphing incompatible metrics | Next scene establishes then holds | Immediate next semantic initial state |
| Hold | Completion or Space during active motion | No transforms, opacity changes, blinking, counters, camera movement or rendering loop | Indefinite until deliberate input | Same hold |

Every intermediate reveal also settles and holds. Visual must list initial, each reveal endpoint and final endpoint, what survives, what leaves, narration cue, transition reason and exit. S01 initial cover is already meaningful and contains the authentic asset; no blank entrance/preloader. R immediately cancels pending motion and restores that state. Never interpolate between different financial metrics as though one transforms numerically into another.

An initial scene may be wholly static. Duration tokens are upper editorial defaults, not a requirement to animate all objects. If two operations occur as one beat, they explain one relationship and finish within 850 ms; otherwise split into presenter-controlled beats. The pointer follows actual mouse movement independently and remains still during a stationary hold.

## Hidden input contract

- Spacebar is the complete forward route. A discrete keydown during active motion completes only the current beat to its semantic endpoint. A later discrete keydown from hold reveals the next beat or, at the last beat, advances one scene.
- Ignore held-key repeat events; one press cannot queue a cascade. Ignore editable/text-entry targets and Ctrl/Alt/Meta combinations. Prevent page scroll only when actually consuming the presentation Spacebar.
- R is mandatory. It cancels every active transition/timer and returns to S01 initial cover. Repeated R is idempotent. No stale callback may reintroduce the interrupted scene.
- At S09 final hold, Spacebar stays on that hold; it does not wrap, exit or show a completion panel.
- Optional Left Arrow returns to the preceding scene's final held state; optional F enters/exits browser fullscreen on deliberate input. Absence is acceptable; if included, document and test. Browser-owned fullscreen notices are outside app control.
- Optional P may toggle the dot; it never becomes necessary for forward flow. No visible hint, tooltip, control, help drawer, menu, progress marker, scene number, playback bar, source panel or navigation arrow appears.
- Inputs behave identically under reduced motion. Visual objects are never required click targets. Touch/keyboard-only use has no pointer dependency; this is not a promise of a new touch-navigation interface.

## Presenter pointer

One 14 CSS px indigo dot uses the static dual edge above. The actual mouse hotspot is its center in viewport CSS coordinates. It is outside the scaled logical-canvas transform so stage fitting/fullscreen does not magnify it. No interpolation lag, trail, pulsing, spring or ambient animation.

Show only for a mouse inside the fitted 16:9 stage, not in letterbox space. Hide on leave/window blur. Hide the native cursor only while custom pointer rendering is working inside the stage; restore outside, on failure or when the dot is toggled off. Dot uses pointer-events:none and aria-hidden=true, takes no focus and never changes scene state or captures input. It remains at the mouse position through R reset if still inside the stage. Keyboard-only and touch operation do not create a synthetic mouse dot.

The paper and ink edges preserve a contour over both dark and light portions of an authentic image. Actual cover contrast, tracking, stage boundaries, blur recovery and failure restoration remain Builder/QA tests; calculated indigo-on-paper contrast is not sufficient evidence for them.

## Authentic first-cover contract

Preferred asset is one official Anthropic or Claude wordmark/mark with verifiable original file provenance, not a recreated text logo. Use exactly one brand wordmark if keeping the Content question. Fit-contain with original aspect ratio; no stretching, recoloring, masking, 3D extrusion or redesign. Asset clear-space requirements take priority over suggested placement; adjust surrounding geometry, not the trademark.

The chosen authentic founder photograph is the dominant identifying object on the left, and the English question sits to its right in two short lines. Use the exact Visual Plan geometry. The old upper-middle logo placement is superseded by this narrow licensed-image adaptation. No faux IPO badge, ticker, dollar pile, AI robot stock art, fabricated launch scene or chart-shaped flourish. The cover must be present on initial state and R reset, normal and reduced-motion.

Visual must resolve:
1. Exact official source page and direct original asset URL, retrieval date, rights/usage basis and any attribution constraints.
2. Asset identity, local offline path, file type/dimensions/hash and actual pixels inspected.
3. Permitted crop/fit and clear space, displayed resolution, wordmark/image text inventory.
4. A second verified authentic fallback or a deterministic reuse of the same independently packaged authentic asset where allowed; never a generated substitute. If no usable authentic asset is available, block READY_FOR_BUILD.
5. Proposed S01 composition and all-scene copy/contrast implications.

The candidate from Content is https://www.anthropic.com/news/confidential-draft-s1-sec . This is a provenance starting point, not proof of a downloadable license. Company ownership/trademark does not by itself establish broad redistribution permission. Design does not declare asset rights or availability verified. If attribution requires extra visible copy, revise the headline within budget or route the conflict; do not hide required credit.

## Performance and verification targets for later stages

These are targets, not observed results:
- After loopback server readiness, meaningful S01 including the local authentic asset and fonts within 2 seconds on the recorded QA desktop/browser; no network-dependent logo/font swap.
- Input response begins within 100 ms, with state changes deterministic under rapid input. No narration-disrupting stalls over 100 ms during tested transitions; record actual conditions and measured observations.
- A stationary hold has no continuing scene animation or needless requestAnimationFrame loop. Pointer updates occur on events only. Test every scene hold for >=30 seconds plus inspect timer/state behavior.
- No unexpected external runtime requests, browser console errors, missing assets or full-page scrolling at 1920×1080, 1280×720 and one non-16:9 viewport.
- All essential copy remains readable and unclipped with packaged fonts and fallback failure exercised. Record grayscale, reduced-motion and pointer-over-image checks.
- Independent QA must evaluate the exact downloaded ZIP. Design calculations and specification review are not package/Windows evidence.

## Decisions and exceptions

| ID | Requirement | Topic choice / rationale | Check or downstream proof |
|---|---|---|---|
| DS01 | Narration-first / clean canvas | Editorial evidence composition, no dashboards or persistent UI | AC-002, AC-005, AC-007 |
| DS02 | Truthful metrics | Separate period/definition groups, no cross-basis magnitude chart | C02/C03/C06; AC-001 |
| DS03 | Accounting integrity | No computed loss-to-cash waterfall; preliminary/outlook distinction retained | C02/C03/C04/C09/C12 |
| DS04 | English canvas readability | Locally packaged Noto pair, minimum 32 logical px, generous diacritic space | Font sources checked; binary/render test pending |
| DS05 | Semantic color | Ink/teal/clay with labels and line styles; pointer-only indigo | Contrast calculations above; grayscale/image tests pending |
| DS06 | Stable narration | Every reveal settles/holds; no auto-time or looping | AC-008..AC-012 pending runtime |
| DS07 | Authentic opening | One original official asset; no generated reconstruction | AC-013/AC-023 pending Visual asset verification |
| DS08 | Visible pointer | 14 CSS px exact-tracking dot with static contrasting edges | AC-022 pending runtime |
| DS09 | Ordinary copy | 0–8 across all states; wordmarks/metaphor labels count | Visual exact ledger required, AC-006 |
| DS10 | Media economy | 2D plus authentic identity; no gratuitous 3D or motion video | Simplest adequate mechanism for financial definitions |
| DS11 | Desktop canvas | Fixed 16:9 fitted stage, no mobile reflow | Owner-approved artifact scope; AC-004 |
| DS12 | Local delivery | Offline assets; no hosting requirement or external font loads | Builder package identity and AC-017/021 pending |

No owner rule exception is introduced. The presenter dot is the existing v1.7 narrow clean-canvas exception.

## Design gate review

Review date: 2026-10-01 UTC. Scope: specification inspection and token calculation, not rendered/asset/runtime verification.

| Gate | Result | Concrete evidence |
|---|---|---|
| Correct incoming state/identity | PASS | Remote README followed by WORKFLOW_STATUS; READY_FOR_DESIGN, expected Content handoff/source, exact branch and folder |
| Required upstream inputs | PASS | Full nine-scene narration, source/claim registers, Design role contract and AC-001..AC-023 read; claims unchanged |
| Filled tokens/hierarchy | PASS | Numeric safe areas, type/spacing tokens, roles, minimum contrast and medium decisions above |
| Truthful boundary review | PASS | S03 incompatible scales barred; S05 residual barred; S06 metric exclusions isolated; S07 payment allocation barred; S08 unquantified scenarios |
| Motion/hold/keys | PASS_SPECIFICATION | Trigger/endpoint/reduced-motion grammar, repeat input/reset/final boundary specified |
| Cover and pointer | PASS_SPECIFICATION | Exact composition and pointer tokens specified; authentic file/rights delegated explicitly, no fabricated readiness |
| Copy safeguards | PASS_SPECIFICATION | Candidate counts checked against Content; all-state ledger and exclusions required from Visual |
| Preservation | PASS | No Content/Visual/Build/QA criteria, owner artifacts, main or historical branches altered by Design |
| Runtime/package/Windows/owner rehearsal | NOT_RUN | No implementation or package exists; 9:20 remains editorial estimate |

Design is ready for Visual specification and asset verification. It is not ready for Build. No essential owner design decision is missing. Pending downstream work is exact S01 asset rights/provenance/offline materialization, font binary verification, final scene geometry/copy/state ledger and all Build/QA checks.

Next actor: Agent 3 — Visual Director. Read README and current WORKFLOW_STATUS first, then 01_CONTENT.md, this file, 03_VISUAL_PLAN.md, 04_BUILD.md, 05_QA.md and both registers. Fill the Visual Plan without changing claims or building. Keep the same branch and owner folder 1ck20putxcHJuhwAwS8ryHpKuIMAqYBiz.

---

# Master instructions retained from v1.7

# 02_DESIGN_SYSTEM.md — Agent 2: Design

Design defines how the presentation behaves. Translate narration into a consistent visual language without rewriting the story.

## Shared contract — mandatory for every agent

This is one of five reusable workflow templates, version 1.7, dated 2026-10-01. The master copies live in 00_WORKFLOW, the reusable template library:
https://drive.google.com/drive/folders/1WcszSRTyebajZj1FuLE-wCuKehyInE8n

For a topic, Agent 1 copies all five templates into the chosen GitHub repository and fills their project sections. The five master templates remain reusable. Topic-specific technical files are maintained in GitHub; do not mirror them back into Drive.

### Drive organization — templates and project outputs

~~~yaml
WORKFLOW_FOLDER: https://drive.google.com/drive/folders/1WcszSRTyebajZj1FuLE-wCuKehyInE8n
WORKFLOW_FOLDER_ID: 1WcszSRTyebajZj1FuLE-wCuKehyInE8n
TEMPLATE_LIBRARY_URL: https://drive.google.com/drive/folders/1WcszSRTyebajZj1FuLE-wCuKehyInE8n
WEB_LANGUAGE: English
NARRATION_LANGUAGE: Thai
OWNER_DOCUMENT_LANGUAGE: Thai
QUICK_START_LANGUAGE: Thai
TOPIC_DRIVE_PARENT: https://drive.google.com/drive/folders/153uw4BMBT78VS6TQgGelanIzXPomkzZt
TOPIC_DRIVE_PARENT_ID: 153uw4BMBT78VS6TQgGelanIzXPomkzZt
~~~

00_WORKFLOW contains only START_HERE.md and the five reusable workflow specifications. Agent 1 reads all six here before bootstrap. Do not create topic folders or owner outputs in 00_WORKFLOW.

01_PROJECTS is the only default parent for future owner folders. Agent 1 creates <Topic Name> - <PROJECT_ID> under this exact parent, then records the returned OWNER_DRIVE_FOLDER URL/ID in README.md and WORKFLOW_STATUS.md. The parent and topic-folder identity are different fields.

Later agents reuse that exact recorded owner folder and ID; never create new/final/v2/replacement/duplicate topic folders. Keep the same four owner-facing documents and the current runnable ZIP package there; technical workspace files stay in GitHub and are not mirrored into each project folder. Do not recreate or relocate an existing run's folder merely because the library was reorganized.

### FRESH bootstrap and continuation are distinct

- Entry through START_HERE.md is always BOOTSTRAP_MODE=FRESH. Agent 1 receives the workflow folder, TOPIC and GITHUB_REPOSITORY and starts a new assignment even in an old repo. Old README/status is historical context, never current state or an instruction to resume.
- Inspect the actual default branch and existing branches first. Generate a unique PROJECT_ID and create a new uniquely named normal Git branch from an appropriate existing base, preserving repository history and compatible infrastructure. Record DEFAULT_BRANCH, the chosen base/commit, BRANCH and exact BRANCH_URL. A name such as project/<topic>-<date-or-project-id> is recommended, not mandatory. Never automatically reuse an old assignment branch.
- Main/default branch is READ-ONLY BY DEFAULT for FRESH work; write there only on an explicit owner instruction. Never reset, delete, rename, overwrite or force-push an old branch; never delete Git history or the repository. All agents work only on this assignment's exact branch unless the workflow explicitly changes it. An interrupted bootstrap retries its already created branch; a later branch-URL continuation never creates another assignment.
- On the new branch initialize fresh README.md, WORKFLOW_STATUS.md and the five current specifications. Start PLANNING/Content with no inherited thesis, scenes, narration, Drive folder, workflow stage, QA findings/pass, build/deployment identity, production verification, blockers or NEXT_ACTOR/NEXT_ACTION. Reuse compatible tooling/configuration, not stale assignment values. Consult old content only as historical/reference material when explicitly useful and revalidate it.
- Cleanup is limited to files clearly belonging to the previous assignment and only on the new branch. Preserve .gitignore, package-manager setup, reusable tooling, repository settings, compatible framework/deployment configuration and CI/CD as appropriate. Never change old branches or main/default during cleanup. If ownership or compatibility is unclear, preserve the file and document the ambiguity and handling in references/bootstrap-notes.md; do not delete blindly. Record the chosen base and scoped cleanup there.
- Persist/push this run's PROJECT_ID and branch in seed README/status before cloud creation. Agent 1 creates one owner folder per PROJECT_ID under 01_PROJECTS, named <Topic Name> - <PROJECT_ID> for recovery; another FRESH run is separate. Retries recover the same recorded folder. Later agents reuse the exact OWNER_DRIVE_FOLDER and OWNER_DRIVE_FOLDER_ID and cannot create replacements.
- Initialize DELIVERY_MODE=LOCAL_ZIP, PUBLIC_DEPLOYMENT_REQUIRED=false, PACKAGE_STATE=NOT_BUILT, PACKAGE_IDENTITY=NOT_VERIFIED, OPEN_FINDINGS=[] and QA_RESULT=NOT_RUN. Vercel/hosting credentials are not required. Preserve old deployments and provider configuration; do not deploy or change them for a local assignment.
- An old public URL, deployed build, archive or QA pass is not evidence for this assignment. Builder creates a versioned prebuilt ZIP, records BUILD_COMMIT, package SHA-256, manifest and verified download identity. All fix cycles replace the current package with a new identified version while preserving finding history.
- An exact BRANCH_URL plus “Continue this project from the current workflow state.” always continues its recorded PROJECT_ID. Later agents discover roles from README/status and follow REQUIRED_INPUTS. BOOTSTRAP_MODE=FRESH describes how the run began; it never tells later agents to restart, reset findings, create another branch or create a new folder.

### Start, identity, and scope

1. For continuation of an initialized run, open README.md first on the supplied GitHub branch, then open the latest committed WORKFLOW_STATUS.md immediately after. Read NEXT_ACTOR and NEXT_ACTION and infer your workflow role from repository state before doing any work. Verify PROJECT, REPOSITORY, BRANCH, BRANCH_URL, PROJECT_ID, STAGE, required inputs, OPEN_FINDINGS, BLOCKERS, OWNER_DRIVE_FOLDER, DELIVERY_MODE, PACKAGE_DOWNLOAD_URL, PACKAGE_SHA256, and LOCAL_RUNTIME. The owner supplies only the current branch URL and “Continue this project from the current workflow state.”; the owner does not assign later agents their roles.
2. After FRESH bootstrap has chosen its new branch, or for a continuation request, clone or locate that exact repo and check out that exact branch. A local checkout path is machine-specific; all durable file references are relative to the repo root. Never depend on chat memory, another agent's temporary directory, or an owner's machine path.
3. Read all project files required by the discovered stage and its REQUIRED_INPUTS, plus upstream specifications and the acceptance criteria in 05_QA.md, before work. Perform the recorded stage. Do not silently change the thesis, content, design rules, branch, Drive folder, or package/runtime identity.
4. Respect recorded owner decisions. Raise a reasoned objection when evidence contradicts a proposed claim. Do not agree merely to please the owner. Never ask the owner to repeat the role, instructions, thesis, project paths, Drive folder, package link, findings, scene numbers, or build status already recorded in the repository. The owner acts as dispatcher and decision-maker, not as a relay between agents. Ask only for essential missing decisions or access that the repo cannot supply; continue independent work.
5. Record unresolved values as UNSET, NOT_CREATED_YET, NOT_BUILT, or NOT_VERIFIED, with the next action. Never invent repo URLs, folder IDs, commit hashes, source evidence, access, package or QA success.
6. Work sequentially on the active branch. Detect upstream changes before committing; preserve others' changes, avoid force-pushes, and resolve conflicts explicitly. An agent handoff is durable only after the commits are pushed and their files are readable on the remote branch.

### Local ↔ Cloud execution and capability-aware handoff

- Roles are independent of execution location. Content, Design, Visual, Builder and QA may run locally or in cloud environments. Choose an executor with the capabilities needed for the current task; do not force Cloud=Research or Local=Build.
- Builder and QA remain independent reviewers even if both use the same type of environment or the same Windows machine. Changing location alone does not make Builder's self-check independent QA.
- Before a switch, save work, commit/push durable source/specifications/reports and update status with exact artifact identity, actual execution environment, unfinished tasks and next action. Verify the remote branch is readable. Uncommitted files, another machine's checkout, cloud session memory and localhost URLs are not a handoff.
- On receipt, read remote README/status on the exact assignment branch; fetch and check out/update from the latest remote state before edits. Inspect dirty local work first and preserve it; never reset, overwrite or blindly pull over it. Resolve divergent work explicitly. Work sequentially on the branch, and recheck remote changes before committing/pushing.
- All portable references use repo-relative paths or observed persistent artifact URLs. Record package source/version/SHA-256. Local absolute paths may appear only in environment-specific run evidence or command examples, never as the next executor's required file location.
- Record EXECUTION_MODE=LOCAL/CLOUD/UNKNOWN and actual OS/runtime/browser where observed. Unknown values stay NOT_VERIFIED. Record what was executed separately from code inspection, assumptions and owner reports; do not invent installed tools, credentials or test results.
- Check only services needed by the current subtask using safe reads or already authorized operations. Record READ_VERIFIED, WRITE_VERIFIED, READ_ONLY, BLOCKED, NOT_VERIFIED or NOT_REQUIRED with scope/evidence. A successful read does not establish write access. Do not create/delete test resources or broaden permissions just to probe access.
- Missing Drive access does not prevent independent source work or package tests. Record the pending publication/document subtask and route it to a capable executor on the same branch with the same folder/file IDs. It does not make required owner artifacts optional: do not advance a stage gate or mark delivery complete until its required artifacts are verified.
- An intermediate handoff is allowed with the current unfinished stage preserved (for example BUILDING), explicit PENDING_SERVICE_TASKS and NEXT_ACTOR/NEXT_ACTION. Do not mark that stage complete merely to switch agents. If the core task cannot proceed, set BLOCKED and retain BLOCKED_FROM_STAGE.
- A Windows local agent may execute START.bat/STOP.bat and target-browser checks against the exact delivered archive. A cloud agent with actual Windows access may do the same; a Linux/macOS cloud run cannot certify Windows execution. Record actual Windows evidence and archive hash, not execution location as a proxy for OS.
- Resume existing verified work when source/package bytes are unchanged. Complete the pending environment-specific checks and affected regressions; do not rebuild/restart the assignment solely because the executor changes. Changed runtime/assets/launchers require a new package identity and independent affected QA.
- If a Windows check fails after a scoped cloud pass, record a stable finding and route Builder → independent QA retest. Preserve the previous evidence, but invalidate affected readiness/pass claims for that package. Keep owner acceptance separate from technical test evidence.

### Language contract — English canvas, Thai owner editions

~~~yaml
WEB_LANGUAGE: English
NARRATION_LANGUAGE: Thai
OWNER_DOCUMENT_LANGUAGE: Thai
QUICK_START_LANGUAGE: Thai
~~~

- All app-authored audience-facing presentation text is English: first cover, titles, annotations, diagram/chart labels, legends, units expressed in words, permitted attribution and any fallback/error text inside the Webapp. Keep the existing 0–8-word ordinary-copy target and clean-canvas rules.
- On-page semantic descriptions, alternative text and accessible labels are English as well. Set the presentation document language to en. Browser/OS-owned interface text is outside this app contract.
- Proper names, authentic brand wordmarks, numerals, currency/unit symbols and standard technical abbreviations retain their correct form. This is not permission to add Thai or mixed-language explanatory text to the canvas.
- Audit text baked into images/video/screenshots and every reveal/hold/reset/fallback state. Prefer an authentic English-language asset/version or an appropriate truthful crop if source material contains other-language prose. Do not redraw, translate or materially edit an official logo/real image in a way that misrepresents it. An indispensable non-English source inscription requires an explicit recorded owner exception before it is used; do not silently relax English-only.
- Spoken narration, both reading/research PDFs, final scene rationale and the owner quick-start are Thai by default. English technical terms and exact original source titles/quotations may remain where needed for precision. Editable narration/rationale remain Thai Google Docs.
- Technical workflow specifications, source code and agent QA/build reports are not audience canvas or owner reading editions; their working language does not determine WEB_LANGUAGE.
- Record any explicit owner language override and affected artifacts in status. Do not infer language from a topic, folder, execution environment, Thai narration or source publisher.

### Drive ownership and storage

- Only Agent 1 (Content/Research) may create the per-topic owner folder for a FRESH assignment. Create at most one folder per PROJECT_ID directly under the recorded TOPIC_DRIVE_PARENT=01_PROJECTS, named <Topic Name> - <PROJECT_ID>. Never create it in WORKFLOW_FOLDER=00_WORKFLOW. Reuse a folder only when verified as this same run during continuation/bootstrap recovery; never import an older run's folder. Commit/push its returned URL/ID before owner-document writes.
- Record the real OWNER_DRIVE_FOLDER URL and OWNER_DRIVE_FOLDER_ID immediately in README.md and WORKFLOW_STATUS.md. The library/root folder and the per-topic folder are different fields.
- Agents 2–5 must reuse the exact topic folder recorded in the latest committed WORKFLOW_STATUS.md. They must never create a second assignment folder, including a “new”, “final”, “v2”, duplicate, or replacement folder.
- Before every Drive write, read the latest committed folder ID/URL and verify folder access. Missing, conflicting, or inaccessible folder records are a blocker; later agents request Agent 1 to repair the record rather than guessing or creating a replacement.
- Preserve existing sharing and ownership. “Folder owner” here identifies the workflow creator; it does not instruct agents to transfer Google Drive ownership or broaden permissions.
- GitHub owns README.md, WORKFLOW_STATUS.md, 01–05 specifications, BUILD_NOTES.md, references/, assets/, src/, dependency lockfiles, and qa/ evidence. Use repo-relative paths.
- Drive owns the owner's reading, rehearsal, and rationale deliverables: 01_KNOWLEDGE_SUMMARY.pdf, 02_RESEARCH_AND_ANALYSIS.pdf, 03A_NARRATION_SCRIPT (editable Thai Google Doc), 06_SCENE_RATIONALE (final Thai Google Doc), and the current <PROJECT_ID>-<PACKAGE_VERSION>-local.zip package. Other Drive documents require an explicitly owner-facing purpose.
- Research notes and narration in 01_CONTENT.md are canonical authoring inputs. Drive reading documents are owner-facing editions generated from those inputs; log their source commit and refresh them when the inputs change. Owner edits in Drive must be reconciled into GitHub before downstream work continues.
- Before creating a Drive deliverable, consult its recorded file ID. Update the existing file when possible, preserving its identity. If replacement is necessary, record the superseded ID and current ID; do not leave several files ambiguously marked current.
- Every Drive artifact record includes file ID, observed URL, MIME/type, responsible agent, state, source commit, and last verification time. In-progress or failed writes cannot be marked READY.
- Secrets and credential values never belong in Markdown, Git, Drive, screenshots, or logs. Record environment variable names and configuration state only.

### Handoff and evidence

Deliverables and status must agree. Use this procedure:

1. Finish the stage's artifacts; verify its exit criteria. Commit and push the artifacts. Let the real resulting SHA be D.
2. Update WORKFLOW_STATUS.md with ARTIFACT_COMMIT=D, what was checked, evidence paths, Drive IDs/URLs, blockers, next actor, explicit next action, and exact required files. Preserve unrelated records.
3. Commit and push the status update as a separate handoff commit H. Do not put H's own hash inside H: that creates a self-referential hash problem. Record D in status and report the remote branch URL and H to the owner.
4. LAST_VERIFIED_COMMIT means the exact commit actually inspected. BUILD_COMMIT, PACKAGE_SHA256 and QA_TESTED_COMMIT have separate meanings; record only observed identities. Documentation-only status changes do not invalidate a tested package. Changed runtime source/assets/dependencies/launchers require a newly built package and affected QA.
5. Read back the remote status and verify recorded Drive artifacts. A failed push, upload, package build, or check stays PENDING/FAILED/BLOCKED with the reason and recovery action. Never advance a stage merely because a file exists.

Transitions:
PLANNING → READY_FOR_DESIGN → READY_FOR_VISUAL → READY_FOR_BUILD → BUILDING → READY_FOR_QA → QA.
If checks pass with no unresolved material findings: QA → QA_PASS.
If checks fail: QA → QA_FAIL → FIXING → READY_FOR_QA → QA. Repeat the fix/retest loop until QA_PASS.
Agent 4 publishes BUILDING or FIXING before implementation; Agent 5 publishes QA before testing. Only Agent 5 may set QA_PASS after independent retesting. QA never changes runtime code or builds fixes to close its own findings. Builder never marks its own build QA_PASS.
For access/missing decisions: set STAGE=BLOCKED and retain BLOCKED_FROM_STAGE; after resolution resume that stage.
After QA_PASS: owner final review/rehearsal and Windows smoke check → COMPLETE when agreed delivery is verified and decisions are recorded. A cloud/browser pass is scoped to its actual environment, not proof that START.bat/STOP.bat worked on Windows. Preserve useful work if owner-machine verification is pending; report it explicitly.

Upstream changes invalidate affected downstream artifacts. Record INVALIDATED_BY_COMMIT, reset their status to STALE, and route NEXT_ACTOR to the earliest affected stage. Do not build from stale content or claim QA on an earlier package.

### Formal findings and local package contract

- Every material QA finding has a stable project-wide ID QA-001, QA-002, etc.; allocate monotonically and never renumber or reuse it. Each record includes scope, severity, expected/observed behavior, evidence, correction, tested source/package identity and state.
- Finding states: OPEN, FIX_IN_PROGRESS, FIXED_PENDING_RETEST, REOPENED, CLOSED. Only independent QA closes a finding after retest; keep all unresolved material IDs in OPEN_FINDINGS.
- Builder owns code, launchers, build notes, package assembly and identity. At QA_FAIL it publishes FIXING, records per-ID fix commits/responses, builds a new version of the same assignment's ZIP, verifies its SHA-256 and refreshes affected owner documents.
- QA independently downloads/extracts the exact identified package into a clean directory, verifies its SHA-256/manifest, runs the prebuilt payload through loopback HTTP, and tests that package rather than the developer checkout. It records actual source identity, archive hash, environment, commands and evidence. A prior package's pass cannot transfer to changed runtime bytes.
- Cloud QA uses its own localhost. Its localhost URL is temporary and is not an owner-download link or a portable handoff reference. The owner runs the downloaded package on their own Windows computer.
- The required delivery is a prebuilt static Webapp ZIP with START.bat, STOP.bat, a Thai quick-start guide, packaged assets, a standard-library local server helper, and a manifest. Choose one tested runtime (Python 3 by default, or a documented compatible Node.js launcher); disclose the one-time prerequisite. Ordinary launches must not require npm install, a build, credentials, Vercel or network downloads.
- Bind the server only to 127.0.0.1. Support paths with spaces and Thai characters, occupied ports, repeat starts, missing runtime, readiness before opening a browser, and stopping only the package-owned process. Do not terminate unrelated processes or weaken browser security.
- Default OFFLINE_AFTER_SETUP=true: images, fonts, media, scripts and data needed for presentation are packaged. Test with external requests unavailable after initial runtime setup. Never substitute a generated image for authentic factual material.
- Store the current ZIP as the fifth owner-facing deliverable in the exact recorded topic Drive folder. Update its recorded file ID where possible and verify a usable observed download/file URL. If Drive delivery is blocked, preserve the repo and package; report the delivery blocker rather than claiming completion.
- Record DELIVERY_MODE, TARGET_OS, LOCAL_RUNTIME, BUILD_COMMIT, PACKAGE_VERSION, PACKAGE_PATH, PACKAGE_MANIFEST_PATH, PACKAGE_FILE_ID, PACKAGE_DOWNLOAD_URL, PACKAGE_SHA256, PACKAGE_STATE, QA_TESTED_COMMIT, QA_TESTED_PACKAGE_SHA256, QA_RESULT, OWNER_WINDOWS_SMOKE_RESULT and NEXT_ACTION. Never fabricate hashes, links or Windows test results.
- Public hosting is optional only upon a separate explicit owner request. It is not an entry/exit criterion for LOCAL_ZIP Build or QA; unavailable Vercel access must not block this route. Preserve historical cloud deployments.
- Presentation pointer and first cover are required: the pointer uses a theme-appropriate high-contrast color; S01 is the first cover and uses a verified authentic relevant image/official logo/character asset. These are detailed in Design/Visual/QA; the pointer is the explicit narrow exception to the otherwise clean canvas.

### Universal continuation prompt

~~~text
Continue this project from the current workflow state:
<the actual BRANCH_URL>

Open README.md first, then immediately open WORKFLOW_STATUS.md from that branch.
Verify the repo/branch, follow NEXT_ACTOR and NEXT_ACTION, and read the recorded required inputs and 05_QA.md.
Use repo-relative paths. Reuse the exact OWNER_DRIVE_FOLDER and package identity in status.
Fetch the latest branch, preserve local uncommitted work, inspect recorded environment/capabilities and finish pending subtask checks without restarting the assignment.
Discover your role from NEXT_ACTOR and NEXT_ACTION; do not ask me to assign it.
Do not ask me to repeat instructions, role, paths, thesis, Drive/package URLs, QA findings, or build status already recorded.
Complete the stage, verify its exit criteria, push its artifacts, and push an updated WORKFLOW_STATUS.md.
Return the branch URL, handoff commit, next action, and any real blocker.
~~~

The prompt is sufficient only when the agent has access to the repo and the services required by its stage. Missing credentials are reported precisely; they are never assumed.

## Role, inputs, and outputs

Required inputs: README.md, WORKFLOW_STATUS.md, 01_CONTENT.md, this template, and 05_QA.md. Read the full narration, claim boundaries, and owner decisions.

Output: a filled 02_DESIGN_SYSTEM.md on the same GitHub branch. No new Drive folder. No technical design document in the topic Drive folder. No implementation or new factual claims.

## Non-negotiable presentation rules

0. **Language:** all audience-facing Webapp copy and semantic/accessibility descriptions are English. Thai is for narration and owner documents. Enforce the shared media-text/proper-name rules; do not infer canvas language from narration.
1. **Narration-first:** the owner's voice carries the explanation. Visual timing follows the spoken idea and the presenter can settle, hold, pause narration during a stable hold, return to cover, and advance. Do not force an automatic slideshow to outrun narration.
2. **Visual-first:** the scene's primary meaning comes from composition, objects, relationships, scale, or evidence. No document-like pages, paragraph slides, bullet stacks, or repeating the script onscreen.
3. **16:9 desktop recording is the primary target:** use a 16:9 logical canvas, default reference size 1920×1080. Fit it into other browser sizes with neutral letterboxing; do not stretch, crop essential content, or reflow into a vertical slide.
4. **Default visible copy target: 0–8 words per scene, excluding essential chart/data labels.** Zero is valid. Count ordinary headings, annotations, image text, logo wordmarks, and attribution across all reveals; do not evade the target by cycling through prose. Repeated copies count again. Only indispensable data labels, axes/units, values, and legends needed to read a truthful chart/data visual may be excluded; record their exact copy and necessity separately. The exception is not a license for dense labels or prose. Numeric values each consume one item when included in ordinary copy; attached units remain one item if presented as one label. An explicitly approved Thai-canvas override uses meaningful linguistic word segmentation, not whitespace-only counting. Record ordinary, excluded, and total counts in 03_VISUAL_PLAN.md.
5. **Clean canvas:** no visible control panel, navigation bar, page/scene numbers, progress bar/dots, Next/Back buttons, UI/navigation arrows, playback bar, persistent menu, keyboard-hint overlay, persistent help/source panel, header/footer, watermark, developer overlay, or competing UI chrome. Explanatory content arrows are allowed for cause/effect, flow, dependencies, transfer, sequence or direction of change: give each a clear semantic job, use the minimum needed, keep it subordinate to the focal subject, and never style it as a navigation control or decorative clutter.
The only clean-canvas exception is the required presenter pointer described below. It is not navigation, explanatory content, visible text or a developer overlay; do not add other UI under this exception.

6. **Hidden keyboard controls:** controls work without visible buttons, tooltips, help panels, or focusable offscreen buttons appearing. Document shortcuts in README.md/BUILD_NOTES.md and owner narration cues outside the audience canvas.
7. **Purposeful motion:** movement must explain a change, relationship, emphasis, or transition. The normal motion pattern is Transition → Reveal → Settle → Hold. Every scene specifies its transition/entry, reveal, settle, hold, and exit. Settle ends explanatory motion; hold remains stable until the presenter acts. No perpetual drifting, spinning, bouncing, parallax, auto-advance, or decorative particle loops.
8. **Truthful visuals:** proportions, chart encodings, relative sizes, and timing must not imply unsupported facts. Distinguish metaphor from measured data in narration and rationale. Do not present generated reconstructions as real evidence.
9. **One focal subject per beat:** support a clear takeaway with deliberate negative space. Do not compete with narration through several simultaneous focal animations.
10. **Accessible and robust:** ensure readable contrast, non-color-only distinctions, meaningful semantic descriptions, and a reduced-motion treatment. Provide longer accessible explanations in owner/reading documents without adding on-canvas UI.

Do not solve the ordinary-copy target by making labels tiny or moving readable text into a background image. Split an overloaded scene, simplify its encoding, or move detail into narration/owner documents. Retain indispensable data labels at readable sizes and document their exclusion. Clicking visual objects is optional and must never be required to continue the presentation. Any resulting scene split requires Agent 1 content alignment, stable scene IDs, and downstream updates.

## Fillable topic design specification

~~~yaml
PROJECT_ID: <from status>
CONTENT_INPUT_COMMIT: <verified SHA>
DESIGN_VERSION: <version>
WEB_LANGUAGE: English
DOCUMENT_LANG_ATTRIBUTE: en
DESIGN_INTENT: <how the visual language serves the thesis>
CANVAS: 1920x1080
ASPECT_RATIO: "16:9"
SAFE_AREA: "5% per edge by default; essential text/objects stay inside"
BACKGROUND: <hex token and meaning>
FOREGROUND: <hex token and use>
ACCENT_PRIMARY: <hex token and semantic meaning>
ACCENT_SECONDARY: <hex token and semantic meaning>
MUTED: <hex token>
FONT_PRIMARY: <font family with Latin coverage for English canvas, license/source; Thai coverage only if explicitly overridden>
FONT_FALLBACK: <offline-safe fallback>
TYPE_SCALE: <sizes on reference canvas; use as tokens>
MIN_LABEL_SIZE: <default 32 logical px; justify topic exception>
LINE_HEIGHT: <token>
MAX_TEXT_WIDTH: <canvas fraction>
SPACING_SCALE: <consistent values>
OBJECT_STYLE: <geometry/material/light/edge treatment>
DATA_ENCODING: <scale, units, categorical distinction>
COMPOSITION_GRID: <anchors and alignments>
MOTION_EASING: <curve and why>
ENTRY_DURATION_MS: <default 400–700, tune for meaning>
REVEAL_DURATION_MS: <default 500–900, tune for meaning>
SETTLE_DURATION_MS: <default 150–300, tune for meaning>
EXIT_DURATION_MS: <default 300–500, tune for meaning>
HOLD: indefinite_until_presenter_input
REDUCED_MOTION: <immediate or brief fade to same semantic endpoint>
AUDIO_POLICY: <live narration default; no unsolicited soundtrack>
POINTER_MODE: theme_adaptive_presenter_dot
POINTER_COLOR: <theme-appropriate high-contrast color; red is not mandatory>
POINTER_DIAMETER_CSS_PX: 14
POINTER_EDGE_OR_HALO: <subtle contrasting outline/halo for varied image backgrounds>
COVER_ASSET_STYLE: authentic_original_image_required
COVER_IMAGE_PLACEMENT: <dominant authentic asset, safe area, crop and hierarchy>
~~~

Defaults are starting points, not performance claims or requirements to animate every element. Adjust based on rehearsal and document decisions.

### Hierarchy and composition

Describe dominant focal size, supporting object limits, placement, contrast, safe-area boundaries, and how an eye should move through a reveal. Make English labels, numerals and symbols legible. Thai glyph/diacritic checks apply to owner editions or an explicitly recorded canvas-language exception. Avoid brand-like decorative chrome.

### Medium decision rules

| Medium | Choose when | Avoid when |
|---|---|---|
| 2D diagram | Relationships/mechanisms are clearer through layout | Decorative complexity substitutes for explanation |
| Chart | Verified data comparisons are central | Data/units are missing or too many labels are needed |
| Real image/video | Authentic evidence/context matters | Crop or generation creates a false factual implication |
| 3D/WebGL | Spatial structure, scale, or physical mechanism needs depth | A flat visual communicates equally well |
| Hybrid | Each layer has a distinct explanatory role | Layers compete for attention |

### Motion grammar

For each motion pattern specify semantic job, trigger, affected object, duration, easing, settled geometry, hold appearance, and reduced-motion equivalent.

~~~text
ENTRY: establish the scene's focal subject.
REVEAL: show one narration-linked relationship/change.
SETTLE: finish movement and reach the semantic endpoint.
HOLD: remain stable, silent, and inspectable for as long as needed.
EXIT: transition only after deliberate presenter advance.
~~~

Static scenes may enter directly into HOLD. If several reveal beats exist, each reaches its own stable hold before the next beat.

### Hidden keyboard contract

Use this shared default unless a recorded owner preference requires a consistent update to 03–05:

| Key | Action |
|---|---|
| Spacebar — mandatory | During active motion, may first complete/settle the current transition or beat; in hold, reveal next beat or advance scene at final beat |
| R — mandatory | Cancel active motion and return to the cover (first scene) initial state |
| Left Arrow — optional | Previous scene in its settled final state, if implemented |
| F — optional | Request/exit browser fullscreen from a deliberate user gesture, if implemented |

Spacebar and R are the only mandatory controls. Left Arrow and F are optional conveniences; their absence is not a defect. No other keys are required by the default contract. Spacebar alone must support the complete forward narration flow. Clicking visual objects is optional. No shortcut glyphs or instructions appear on the canvas. Browser-owned fullscreen messages cannot be removed by the app; wait for them to clear before recording. Ignore text-entry targets and modifier combinations; do not intercept browser shortcuts. Repeated keys must not skip scenes unpredictably. Reduced motion uses the same input semantics.

## Presenter pointer and authentic first cover

The owner selected LOCAL_ZIP, a presenter pointer whose color suits the theme, and a first cover using real relevant imagery. These preferences override a blanket ban on pointer overlays while all other clean-canvas rules remain.

- Use one small presenter dot, default 14 CSS px diameter, with a theme-appropriate high-contrast fill and a subtle contrasting outline/halo where needed. Specify actual tokens and verify visibility over both the cover image and other scene backgrounds.
- Track the mouse hotspot directly in viewport CSS coordinates. Do not scale the dot unexpectedly with the logical canvas or introduce easing lag, a trail, pulsation or continuous decorative motion.
- Show it only when a mouse is inside the stage. Hide the native cursor only where the custom dot is functioning; restore it on stage exit or renderer failure. Hide the dot on pointer leave/window blur. Touch/keyboard-only use must work without it.
- The dot must use pointer-events:none and aria-hidden=true; it cannot block hover/click, take focus, trigger scene navigation or change slide/beat state. It remains at the mouse position during a held scene, including R reset; no permanent animation loop is required when stationary.
- If a toggle is useful, optional P may show/hide the dot and is documented outside the canvas. It is never required for forward flow.
- S01 is always the first cover, not an empty preloader or technical screen. Show a verified authentic relevant image such as an official logo, original character artwork, or real product/event/person photograph in its initial state. A simple composition around the image is allowed; its authenticity must remain clear.
- Do not redraw/generate a logo, invent character artwork, or use an AI-generated reconstruction as the required authentic opening asset. Decorative styling cannot materially alter the asset or create a false affiliation.
- Source, rights, offline path, suitable resolution, crop and an authentic fallback must be recorded. If a valid asset is unavailable, report the asset blocker; do not silently replace it with generated artwork.
- Keep ordinary cover text/wordmarks within the copy budget. R returns to the cover initial state with its authentic image visible. Reduced motion preserves both cover meaning and exact pointer tracking.

## Decisions and exceptions

| Decision ID | Requirement | Topic choice | Reason tied to narration | Verified constraint |
|---|---|---|---|---|
| DS01 | <rule> | <token/pattern> | <why> | <check> |

The non-negotiable rules stay in force. If an owner explicitly changes a rule, record the instruction, consequence, and affected files in status; do not silently add exceptions.

## Exit criteria and handoff

- Tokens, hierarchy, canvas behavior, font coverage, motion grammar, medium rules, hidden keys, theme-adaptive pointer and authentic cover composition are specified concretely.
- Ordinary scene copy targets 0–8 words; essential chart/data label exclusions are minimal, justified, and truth-preserving.
- All hold states are stable; reduced motion preserves meaning.
- Forbidden UI/navigation arrows remain absent; any explanatory content arrows have a minimal documented semantic role and cannot resemble controls.
- Publish artifacts then status: STAGE=READY_FOR_VISUAL; NEXT_ACTOR=Agent 3 — Visual Director.
- NEXT_ACTION: “Read 01_CONTENT.md, 02_DESIGN_SYSTEM.md, 04_BUILD.md and 05_QA.md. Fill 03_VISUAL_PLAN.md scene by scene, including assets, reveal/settle/hold states, word counts, and factual boundaries. Do not build yet.”


