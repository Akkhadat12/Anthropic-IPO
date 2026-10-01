# Anthropic IPO — Visual Plan 1.0

This filled specification is the live Visual handoff. The retained v1.7 master beneath it is the workflow contract, not unresolved placeholders. All nine Thai narration scenes and financial claims are unchanged. The owner explicitly chose English on-canvas text (2026-10-01: “เป็น english แบบเดิม”); this supersedes the earlier Thai visual-copy proposals. This stage authors composition, copy, assets and still-state concepts; it does not implement the presentation or claim package/runtime QA.

## Identity and approved cover substitution

- PROJECT_ID: anthropic-ipo-20261001-0426
- Branch: project/anthropic-ipo-20261001-0426
- Content financial/narration source: 501f48afb1bddf098de95fa75f995dbd016d54c5
- Design input: aa74da74a0103a59ca7f2d53b2bc180191b55ed2
- Incoming handoff: 12623fdb09076fec741aa368897923dd9f90eab3
- WEB_LANGUAGE: English
- DOCUMENT_LANG_ATTRIBUTE: en
- NARRATION_LANGUAGE: Thai
- OWNER_DOCUMENT_LANGUAGE: Thai
- QUICK_START_LANGUAGE: Thai
- LANGUAGE_EXCEPTIONS: NONE
- Visual version: 1.1 (v1.7 migration); nine scenes; 560-second editorial budget, not measured narration
- Assets: assets/manifest.md and assets/manifest.json
- Exact geometry/copy/state data: references/visual-scenes.json
- Review: references/visual-review/review.md; independent-review.md; contact-sheet.png
- Pointer: 02_DESIGN_SYSTEM.md#presenter-pointer, unchanged 14 CSS-px indigo dot with light inner/dark outer edge
- Delivery: future prebuilt LOCAL_ZIP for Windows; no public hosting or Vercel requirement

The official press-kit logo is authentic but no general usable permission was established under the company's trademark guidelines. Do not use or package it. The coordinator approved the already permitted authentic relevant image alternative: a real licensed photograph of Dario Amodei at TechCrunch Disrupt on 20 September 2023, by Kimberly White/Getty Images for TechCrunch. This is identity/editorial context, not a photograph of an IPO announcement or a current event. The exact file and CC BY 2.0 conditions are verified in the asset manifest. Generic “Anthropic” in the presentation font is ordinary text, not a recreated wordmark. The scoped Content/Design cover-field addenda align this substitution without altering narration or the thesis.

## Universal semantic and interaction contract

Coordinate system is 1920×1080 logical px; text x/y are top-left unless alignment says center/right. Object geometry is exact in the JSON and each section. Keep all essential bounds inside x=96..1824,y=54..1026; the fitted stage is proportionally letterboxed at 1280×720 and a non-16:9 viewport. The approved desktop-recording scope excludes a separately reflowed mobile design. No mobile readability claim is made.

Ink #202722 is evidence; teal #226B5C demand/positive signal; clay #965038 costs/obligations; muted #576158 supporting context; paper #F5F1E8. Indigo #354F91 is pointer-only. Every uncertainty distinction has actual text plus geometry, not color alone. Strokes 4 logical px. Typography uses Noto Sans 400 with native optional 600 emphasis at the same text bounds; no synthetic bold. The reference still renderer uses pinned Noto Sans. Thai is retained in narration and owner rationale only. All runtime accessible/semantic descriptions, alt text, labels and fallback/error text are English. Builder must verify final CSS font loads and complete line boxes with the shipped binaries. Minimum scene text is 36 logical px, exceeding the 32-px design minimum.

One real photo plus editable 2D vector/text layers is sufficient. No 3D, spheres, financial particle effects, chart tiles, camera moves, stock footage, audio, or fake interfaces. Only S04 uses two thin content arrows: work→value-for-money question→repeat-payment question. They encode a conditional business dependency, never a measured conversion or navigation. Brackets mean conceptual inclusion (S05) or multiyear scope (S07), not numeric lengths. Dashed lines have local explicit meaning: unknown terms, outlook boundary, or scenario/question prompts; never a measured time/value scale.

Every scene's b0 is its entry endpoint. Every object has a reveal beat. At bN, all objects whose beat <=N are at their listed coordinates and full opacity. No prior object disappears or resizes; no numerical interpolation. For S01, b0 is static and visible immediately, including the real photo. Other entry groups may fade 0→1 over 500ms and settle 200ms; no translation is necessary. Space from a held beat adds precisely the next group over 650ms then 200ms settle, easing cubic-bezier(0.22,1,0.36,1). Each settled endpoint holds indefinitely. Narrative duration is never an animation timer.

Space during active motion completes only the current endpoint; a later discrete Space reveals the next beat or advances one scene from final hold. Ignore event.repeat and editable targets/modifiers. No queued cascade. R cancels all in-flight work and restores S01 b0 with photo already visible; repeated R is idempotent. Space on final S09 hold is a no-op. Optional Left returns to the prior scene's final settled beat (S01 boundary stays b0); optional F changes browser fullscreen only. Neither optional key is needed for forward narration. No object click is required. No visible controls, hints, scene numbers, footer, source strip, credits panel, help or progress UI on the recording canvas.

Scene exit is a 350ms crossfade to next b0, not a flying slide or financial morph. If Space settles that transition, it stops at next b0, without revealing the next beat. Reduced motion uses immediate identical endpoints and the same hold/keyboard logic. All source details, credit links and full caveats live in the accompanying documents/credits; essential visible period/metric qualifiers stay with their figures at every beat.

Pointer rule applies to every state: event-position tracking only, no smoothing/trail/pulse, pointer-events:none, no focus, hide native cursor only inside an active mouse stage and restore outside/blur/failure. Its static pale and dark edges maintain separation over the photo's black, skin, shirt and light areas. Still pointer samples are design evidence only; actual tracking, hotspot, fullscreen, exit/blur and failure tests remain Build/QA.

## Count method and analytical layer review

Counts below are scene-wide inventories of text instances across every reveal. A retained DOM text object counts once, a new repeated label counts again (S06 uses separate Positive and Expected positive text objects). English whitespace-word tokenization is explicitly listed; punctuation is excluded and hyphenated compounds count as one word. No Thai visible copy remains. English hyphenated run-rate/non-cash is one word; English multiword metric names count per word. Punctuation, inequality signs, brackets and question marks are separately visible nonword marks. No bitmap text is omitted: S01's full photo has only defocused, undecodable background printing, and no added wordmark. If a different crop makes text legible, recount before use.

Ordinary headings, scenario/illustration labels and entity names are never excluded. Excluded text is only the minimal value/metric/unit/period/status needed to decode an evidence group; every exclusion has a local reason. Narrated financial figures not present in the geometry must not be added by Builder. There are no magnitude charts. Numeric typography and position do not encode amount, frequency, probability or duration. All financial values remain USD millions, exactly as the Thai narration. Missing data means unknown, never zero.

The Visual Director performed the embedded-layer specialist pass: S03 incompatible-clock comparison; S05 accounting inclusion; S06 evidence-status comparison; S07 contract-horizon concept; S08 unquantified conditional alternatives. Each layer's job, data/encoding, fallback, accessibility and QA are below. An independent reviewer checks the full set separately. No modelled forecast or fabricated observation enters the plan.

## Scene index

| Scene | Ordinary | Essential excluded | Total | Beats | Editorial seconds | Claims |
|---|---:|---:|---:|---:|---:|---|
| S01 | 5 | 0 | 5 | 1 | 30 | C02, C03, C04, C05 |
| S02 | 5 | 3 | 8 | 2 | 55 | C01, C02, C10 |
| S03 | 4 | 19 | 23 | 3 | 75 | C02, C03, C06 |
| S04 | 8 | 0 | 8 | 3 | 65 | C07, C08, C11 |
| S05 | 5 | 14 | 19 | 3 | 65 | C02, C12 |
| S06 | 4 | 16 | 20 | 3 | 75 | C03, C04, C09, C12 |
| S07 | 5 | 8 | 13 | 2 | 75 | C05, C13 |
| S08 | 8 | 0 | 8 | 3 | 60 | A01 |
| S09 | 5 | 0 | 5 | 3 | 60 | C10, C11, C12, A01 |

## Exact scene specifications

### S01

Content reference: 01_CONTENT.md, stable scene S01. Claim IDs: C02, C03, C04, C05.

Takeaway: Identify the company and pose the approved sustainability question without a verdict.

Medium: authentic photograph plus 2D text. Depth/camera/lighting: NOT_APPLICABLE. Content arrows: NONE.

Thai rationale draft for future 06_SCENE_RATIONALE: เปิดด้วยภาพถ่ายจริงของผู้ร่วมก่อตั้งในงานปี 2023 เพื่อบอกว่าเรากำลังพูดถึงใคร วางภาพซ้ายและคำถามขวา เว้นที่ว่างให้คำถาม ไม่มีภาพสำเร็จหรือล้มเหลวชี้นำคำตอบ

Composition and visual semantics: exact anchors below; one focal group per revealed beat. Existing evidence remains full contrast while the newly revealed group receives attention. Negative space separates distinct evidence, never a measured gap.

| Object | Kind | Entry beat | Geometry / appearance |
|---|---|---:|---|
| authentic-photo | asset | 0 | x=192, y=220, 840×560, contain original aspect; A01 |
| company | text | 0 | x=1152, y=275, 72px, left, #202722; Anthropic |
| question-a | text | 0 | x=1152, y=465, 64px, left, #202722; Fast growth. |
| question-b | text | 0 | x=1152, y=565, 58px, left, #202722; Sustainable profits? |

Copy ledger:

| Copy | Segmentation | Count | Class and reason |
|---|---|---:|---|
| Anthropic | Anthropic | 1 | Ordinary |
| Fast growth. | Fast / growth | 2 | Ordinary |
| Sustainable profits? | Sustainable / profits | 2 | Ordinary |

Scene-wide count: 5 ordinary + 0 essential = 5. No extra canvas attribution, titles or labels may be added.

| Beat | Exact spoken cue | Visual job / endpoint | Duration and hold |
|---|---|---|---|
| b0 | ถ้าบริษัท AI มีรายได้โตเร็วมาก | Static authentic identity and open question present on first meaningful paint; all narration stays on this hold. All objects with beat ≤ 0 are fully visible and stationary. | Static from first paint; indefinite hold |

Exit: 350ms crossfade to S02 b0; semantic link is the next narrated question. All entry/reveal/settle/hold, cancellation, rapid-input, reduced-motion and optional-back behavior use the universal contract above.

Accessible settled description: Identify the company and pose the approved sustainability question without a verdict. No profit conclusion, IPO celebration, generated mark or endorsement claim. Provide the current state’s displayed values/labels as text to assistive technology; do not announce animation frames.

Data/encoding: Nonquantitative identity or concept; no scale, axes, baseline or inferred dataset.

Narrated detail remains in the complete unchanged scene: all full narration and source caveats; the canvas is a cue, not a replacement script. Do not fill quiet holds with additional graphics.

Factual boundary: No profit conclusion, IPO celebration, generated mark or endorsement claim.

Assets/fallback: A01 original local photo, A01F byte-identical independently packaged fallback, F01/F02 fonts with notices. Main image decode/path failure switches once to A01F; both failing is a visible asset defect to fix, never permission to fabricate a logo. Full image fitted without crop; no baked readable text.

Scene assertions: AC-003/005/006/013/022/023: first paint and R show actual licensed photo, 5 ordinary tokens, no logo; correct person/event credit, complete uncropped photo, no UI or text over photo. Exercise image-path failure using packaged fallback. All scenes additionally map to AC-004/007/008/010/011/012/014/022 for fitted stage, clean canvas, keys, 30-second holds, reset, reduced motion, noncolor decoding and pointer. These are required downstream tests, not passed runtime results.

### S02

Content reference: 01_CONTENT.md, stable scene S02. Claim IDs: C01, C02, C10.

Takeaway: Submitted draft and unknown offering terms are different evidence states.

Medium: editable 2D text/vector evidence composition. Depth/camera/lighting: NOT_APPLICABLE. Content arrows: NONE.

Thai rationale draft for future 06_SCENE_RATIONALE: เอกสารเส้นเดียวหมายถึงการยื่นร่าง ไม่ทำหน้าปลอมของ S-1 ข้อความอีกฝั่งแยกสิ่งที่ยังไม่รู้ โดยไม่ใช้ตราอนุมัติหรือวันเข้าตลาดที่ไม่ได้ยืนยัน

Composition and visual semantics: exact anchors below; one focal group per revealed beat. Existing evidence remains full contrast while the newly revealed group receives attention. Negative space separates distinct evidence, never a measured gap.

| Object | Kind | Entry beat | Geometry / appearance |
|---|---|---:|---|
| draft | rect | 0 | x=270, y=270, w=550, h=490, stroke=#202722 |
| submitted | text | 0 | x=545, y=495, 58px, center, #226B5C; Draft submitted |
| date | text | 0 | x=545, y=610, 40px, center, #576158; 1 June 2026 |
| unknown | text | 1 | x=1300, y=505, 56px, center, #202722; Offer price unknown |
| terms-boundary | line | 1 | x1=1010, y1=660, x2=1590, y2=660, stroke=#576158, dash=12 10 |

Copy ledger:

| Copy | Segmentation | Count | Class and reason |
|---|---|---:|---|
| Draft submitted | Draft / submitted | 2 | Ordinary |
| 1 June 2026 | 1 / June / 2026 | 3 | Essential: Exact date of C01 submission; not a listing date. |
| Offer price unknown | Offer / price / unknown | 3 | Ordinary |

Scene-wide count: 5 ordinary + 3 essential = 8. No extra canvas attribution, titles or labels may be added.

| Beat | Exact spoken cue | Visual job / endpoint | Duration and hold |
|---|---|---|---|
| b0 | เริ่มจากสถานะ IPO ก่อน | Establish conceptual document, submitted wording and event date. All objects with beat ≤ 0 are fully visible and stationary. | Entry 500+200ms; indefinite hold |
| b1 | แต่ยังไม่ได้แปลว่ามีวันขายหุ้น | Reveal unknown price at right; no connecting arrow or timeline. Hold through Reuters provenance and the public-document research limit. All objects with beat ≤ 1 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |

Exit: 350ms crossfade to S03 b0; semantic link is the next narrated question. All entry/reveal/settle/hold, cancellation, rapid-input, reduced-motion and optional-back behavior use the universal contract above.

Accessible settled description: Submitted draft and unknown offering terms are different evidence states. Document outline is conceptual, not the confidential filing; no offer date, ticker, price, SEC approval or claim financial information is absent. Provide the current state’s displayed values/labels as text to assistive technology; do not announce animation frames.

Data/encoding: Nonquantitative identity or concept; no scale, axes, baseline or inferred dataset.

Narrated detail remains in the complete unchanged scene: all full narration and source caveats; the canvas is a cue, not a replacement script. Do not fill quiet holds with additional graphics.

Factual boundary: Document outline is conceptual, not the confidential filing; no offer date, ticker, price, SEC approval or claim financial information is absent.

Assets/fallback: F01/F02 local fonts; all shapes are inline editable vector/DOM. No network media, WebGL or generated image. Missing primary font uses the packaged companion where covered, then system emergency fallback with a QA failure until actual font loading is restored.

Scene assertions: AC-001/002/005/006: date remains with submitted draft; dashed unknown-price line has no false completed-IPO implication. Document has no fabricated body text or approval seal. All scenes additionally map to AC-004/007/008/010/011/012/014/022 for fitted stage, clean canvas, keys, 30-second holds, reset, reduced motion, noncolor decoding and pointer. These are required downstream tests, not passed runtime results.

### S03

Content reference: 01_CONTENT.md, stable scene S03. Claim IDs: C02, C03, C06.

Takeaway: Three figures belong to different periods and definitions; compare labels, never magnitude.

Medium: editable 2D text/vector evidence composition. Depth/camera/lighting: NOT_APPLICABLE. Content arrows: NONE.

Thai rationale draft for future 06_SCENE_RATIONALE: ตัวเลขแต่ละชุดอยู่คนละบรรทัดและมีงวดติดกัน ไม่ทำแท่งสูงขึ้นหรือกราฟโต เพื่อไม่ให้คนดูเอาทั้งปี ไตรมาส และ run-rate ไปหารเทียบกัน

Composition and visual semantics: exact anchors below; one focal group per revealed beat. Existing evidence remains full contrast while the newly revealed group receives attention. Negative space separates distinct evidence, never a measured gap.

| Object | Kind | Entry beat | Geometry / appearance |
|---|---|---:|---|
| thesis | text | 0 | x=192, y=130, 60px, left, #202722; Different periods. Different meanings. |
| period0 | text | 0 | x=192, y=330, 42px, left, #202722; FY2025 |
| metric0 | text | 0 | x=192, y=403, 40px, left, #576158; Full-year revenue |
| value0 | text | 0 | x=1728, y=356, 60px, right, #202722; Nearly US$4,600 million |
| period1 | text | 1 | x=192, y=575, 42px, left, #226B5C; Q2 2026 |
| metric1 | text | 1 | x=192, y=648, 40px, left, #576158; Quarterly revenue · preliminary |
| value1 | text | 1 | x=1728, y=601, 60px, right, #226B5C; >US$11,500 million |
| period2 | text | 2 | x=192, y=820, 42px, left, #202722; End-July 2026 |
| metric2 | text | 2 | x=192, y=893, 40px, left, #576158; Annualized run-rate |
| value2 | text | 2 | x=1728, y=846, 60px, right, #202722; >US$65,000 million |

Copy ledger:

| Copy | Segmentation | Count | Class and reason |
|---|---|---:|---|
| Different periods. Different meanings. | Different / periods / Different / meanings | 4 | Ordinary |
| FY2025 | FY2025 | 1 | Essential: Exact fiscal/as-of clock attached to this figure. |
| Full-year revenue | Full-year / revenue | 2 | Essential: Metric basis and preliminary/annualized qualifier prevent false comparison. |
| Nearly US$4,600 million | Nearly / US$4,600 / million | 3 | Essential: Source figure, inequality/approximation, USD million unit; same font size does not encode amount. |
| Q2 2026 | Q2 / 2026 | 2 | Essential: Exact fiscal/as-of clock attached to this figure. |
| Quarterly revenue · preliminary | Quarterly / revenue / preliminary | 3 | Essential: Metric basis and preliminary/annualized qualifier prevent false comparison. |
| >US$11,500 million | US$11,500 / million | 2 | Essential: Source figure, inequality/approximation, USD million unit; same font size does not encode amount. |
| End-July 2026 | End-July / 2026 | 2 | Essential: Exact fiscal/as-of clock attached to this figure. |
| Annualized run-rate | Annualized / run-rate | 2 | Essential: Metric basis and preliminary/annualized qualifier prevent false comparison. |
| >US$65,000 million | US$65,000 / million | 2 | Essential: Source figure, inequality/approximation, USD million unit; same font size does not encode amount. |

Scene-wide count: 4 ordinary + 19 essential = 23. No extra canvas attribution, titles or labels may be added.

| Beat | Exact spoken cue | Visual job / endpoint | Duration and hold |
|---|---|---|---|
| b0 | ชุดแรก Reuters รายงานปลายเดือนกันยายน | Show first row only with full period/metric/unit tuple, plus title. All objects with beat ≤ 0 are fully visible and stationary. | Entry 500+200ms; indefinite hold |
| b1 | ชุดที่สอง Bloomberg รายงาน | Add second row without changing first; keep preliminary label present from its first frame. Hold through newer reporting-period explanation. All objects with beat ≤ 1 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |
| b2 | ส่วนชุดที่สาม Reuters รายงาน | Add third row with annualized definition visible immediately. All three remain stationary through run-rate explanation and warning about division. All objects with beat ≤ 2 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |

Exit: 350ms crossfade to S04 b0; semantic link is the next narrated question. All entry/reveal/settle/hold, cancellation, rapid-input, reduced-motion and optional-back behavior use the universal contract above.

Accessible settled description: Three figures belong to different periods and definitions; compare labels, never magnitude. No common axis, lengths, circles, line, ratio, annualized Q2, or cross-period growth calculation. Run-rate is not FY revenue or backlog. Provide the current state’s displayed values/labels as text to assistive technology; do not announce animation frames.

Data/encoding: Exact value/period/metric tuples are the essential-label rows above and references/visual-scenes.json, traced to the claim register. Position is typographic grouping only, not a quantitative axis. No baseline, area, length or growth scale applies. Missing results are unknown, not zero.

Narrated detail remains in the complete unchanged scene: source publication dates, news-date versus fiscal-period explanation and invalid growth division warning. Do not fill quiet holds with additional graphics.

Factual boundary: No common axis, lengths, circles, line, ratio, annualized Q2, or cross-period growth calculation. Run-rate is not FY revenue or backlog.

Assets/fallback: F01/F02 local fonts; all shapes are inline editable vector/DOM. No network media, WebGL or generated image. Missing primary font uses the packaged companion where covered, then system emergency fallback with a QA failure until actual font loading is restored.

Scene assertions: AC-001/002/005/006: every row appears with full tuple; Q2 preliminary and July annualized run-rate remain visible; no shared axis/connecting line/sized marks. Review all three beats at 1280×720. All scenes additionally map to AC-004/007/008/010/011/012/014/022 for fitted stage, clean canvas, keys, 30-second holds, reset, reduced motion, noncolor decoding and pointer. These are required downstream tests, not passed runtime results.

### S04

Content reference: 01_CONTENT.md, stable scene S04. Claim IDs: C07, C08, C11.

Takeaway: Paying repeatedly is a question about work usefulness and retention, not established current revenue mix.

Medium: editable 2D text/vector evidence composition. Depth/camera/lighting: NOT_APPLICABLE. Content arrows: S04 only; the two explicitly specified dependency arrows, 3px final runtime stroke, no surrounding controls.

Thai rationale draft for future 06_SCENE_RATIONALE: ภาพงานเป็นเพียงตัวอย่างกลไก ไม่แสดงลูกค้าจริงหรือสัดส่วนรายได้ การเผยคำถามเรื่องจ่ายซ้ำทำให้หลักฐานผลิตภัณฑ์กับหลักฐานรักษาลูกค้าแยกจากกัน

Composition and visual semantics: exact anchors below; one focal group per revealed beat. Existing evidence remains full contrast while the newly revealed group receives attention. Negative space separates distinct evidence, never a measured gap.

| Object | Kind | Entry beat | Geometry / appearance |
|---|---|---:|---|
| customer | text | 0 | x=192, y=150, 72px, left, #202722; Customers |
| schematic | text | 0 | x=192, y=290, 36px, left, #576158; Illustrative |
| work | rect | 0 | x=240, y=450, w=390, h=270, stroke=#202722 |
| code-left | path | 0 | d=M 365 510 L 315 580 L 365 650, stroke=#202722 |
| code-right | path | 0 | d=M 510 510 L 560 580 L 510 650, stroke=#202722 |
| work-slash | line | 0 | x1=470, y1=515, x2=405, y2=645, stroke=#202722 |
| work-label | text | 0 | x=435, y=775, 48px, center, #202722; Work |
| value-question | text | 1 | x=995, y=530, 44px, center, #226B5C; Worth paying for? |
| work-value-arrow | path | 1 | d=M 675 580 L 755 580 M 740 570 L 755 580 L 740 590, stroke=#202722, width=3 |
| repeat-question | text | 2 | x=1530, y=530, 52px, center, #226B5C; Pay again? |
| value-repeat-arrow | path | 2 | d=M 1225 580 L 1355 580 M 1340 570 L 1355 580 L 1340 590, stroke=#202722, width=3 |

Copy ledger:

| Copy | Segmentation | Count | Class and reason |
|---|---|---:|---|
| Customers | Customers | 1 | Ordinary |
| Illustrative | Illustrative | 1 | Ordinary |
| Work | Work | 1 | Ordinary |
| Worth paying for? | Worth / paying / for | 3 | Ordinary |
| Pay again? | Pay / again | 2 | Ordinary |

Scene-wide count: 8 ordinary + 0 essential = 8. No extra canvas attribution, titles or labels may be added.

| Beat | Exact spoken cue | Visual job / endpoint | Duration and hold |
|---|---|---|---|
| b0 | แล้วลูกค้าจ่ายเงินให้ Claude เพราะอะไร? | Establish clearly illustrative coding work and customer identity; no measured task outcome. All objects with beat ≤ 0 are fully visible and stationary. | Entry 500+200ms; indefinite hold |
| b1 | เครื่องมือที่ช่วยให้งานเสร็จเร็วขึ้น | Reveal the explicit value-for-money question and first dependency arrow; value is conditional, not measured. All objects with beat ≤ 1 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |
| b2 | แต่ต้องพิสูจน์ว่าลูกค้าเดิมอยู่ต่อ | Reveal repeat-payment question and second dependency arrow. Hold through FY2025 concentration and continued-payment question. All objects with beat ≤ 2 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |

Exit: 350ms crossfade to S05 b0; semantic link is the next narrated question. All entry/reveal/settle/hold, cancellation, rapid-input, reduced-motion and optional-back behavior use the universal contract above.

Accessible settled description: Paying repeatedly is a question about work usefulness and retention, not established current revenue mix. Schematic only; no measured task success, actual customer logos, retention, pie chart or concentration implied by icon count. February/2025 numbers stay in narration with original periods. Provide the current state’s displayed values/labels as text to assistive technology; do not announce animation frames.

Data/encoding: Nonquantitative identity or concept; no scale, axes, baseline or inferred dataset.

Narrated detail remains in the complete unchanged scene: February Claude Code >2,500 million run-rate, product-only enterprise denominator, FY2025 concentration and current retention gaps. Do not fill quiet holds with additional graphics.

Factual boundary: Schematic only; no measured task success, actual customer logos, retention, pie chart or concentration implied by icon count. February/2025 numbers stay in narration with original periods.

Assets/fallback: F01/F02 local fonts; all shapes are inline editable vector/DOM. No network media, WebGL or generated image. Missing primary font uses the packaged companion where covered, then system emergency fallback with a QA failure until actual font loading is restored.

Scene assertions: AC-001/002/006: illustration marker visible at entry; code marks are not navigation; historical product/concentration figures remain narration-only; no implied actual customer or successful-task count. All scenes additionally map to AC-004/007/008/010/011/012/014/022 for fitted stage, clean canvas, keys, 30-second holds, reset, reduced motion, noncolor decoding and pointer. These are required downstream tests, not passed runtime results.

### S05

Content reference: 01_CONTENT.md, stable scene S05. Claim IDs: C02, C12.

Takeaway: Accounting loss contains noncash charges; cash used cannot be computed from these figures alone.

Medium: editable 2D text/vector evidence composition. Depth/camera/lighting: NOT_APPLICABLE. Content arrows: NONE.

Thai rationale draft for future 06_SCENE_RATIONALE: วงเล็บแสดงว่ารายการไม่ใช่เงินสดอยู่ภายในขาดทุนตามข่าว แต่ไม่ใช้พื้นที่สัดส่วนและไม่ลบตัวเลขออกเป็นเงินสด เส้นแยกกับคำถามด้านขวาย้ำว่าขาดหลักฐานเชื่อม

Composition and visual semantics: exact anchors below; one focal group per revealed beat. Existing evidence remains full contrast while the newly revealed group receives attention. Negative space separates distinct evidence, never a measured gap.

| Object | Kind | Entry beat | Geometry / appearance |
|---|---|---:|---|
| question | text | 0 | x=192, y=135, 64px, left, #202722; Loss is not cash used |
| period | text | 0 | x=192, y=285, 40px, left, #576158; FY2025 |
| losslabel | text | 0 | x=192, y=390, 42px, left, #202722; Net loss |
| loss | text | 0 | x=192, y=485, 64px, left, #965038; About US$42,000 million |
| inclusion | path | 1 | d=M 215 560 L 215 765 L 265 765, stroke=#965038 |
| noncashlabel | text | 1 | x=288, y=640, 40px, left, #202722; Includes non-cash charge |
| noncash | text | 1 | x=288, y=735, 56px, left, #965038; About US$34,000 million |
| separation | line | 2 | x1=1170, y1=355, x2=1170, y2=820, stroke=#576158, dash=12 10 |
| cashunknown | text | 2 | x=1475, y=540, 56px, center, #202722; Cash flow ? |

Copy ledger:

| Copy | Segmentation | Count | Class and reason |
|---|---|---:|---|
| Loss is not cash used | Loss / is / not / cash / used | 5 | Ordinary |
| FY2025 | FY2025 | 1 | Essential: Both accounting figures are historical FY2025, not current results. |
| Net loss | Net / loss | 2 | Essential: Net-loss definition distinguishes from operating loss/cash. |
| About US$42,000 million | About / US$42,000 / million | 3 | Essential: Reported approximate net loss and unit. |
| Includes non-cash charge | Includes / non-cash / charge | 3 | Essential: Inclusion and noncash accounting nature, not deduction into cash. |
| About US$34,000 million | About / US$34,000 / million | 3 | Essential: Approximate component amount; typography not proportional area. |
| Cash flow ? | Cash / flow | 2 | Essential: Identifies the unknown cash-flow endpoint; question means data needed, not zero. |

Scene-wide count: 5 ordinary + 14 essential = 19. No extra canvas attribution, titles or labels may be added.

| Beat | Exact spoken cue | Visual job / endpoint | Duration and hold |
|---|---|---|---|
| b0 | ผลขาดทุนสุทธิปี 2025 ราว 42,000 ล้านดอลลาร์ | Show net loss and historical period; top line warns against cash equivalence. All objects with beat ≤ 0 are fully visible and stationary. | Entry 500+200ms; indefinite hold |
| b1 | ตัวเลขนี้รวมค่าใช้จ่ายทางบัญชีที่ไม่ใช่เงินสด | Add subordinate included noncash line and non-quantitative inclusion bracket, with amount unchanged. All objects with beat ≤ 1 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |
| b2 | สิ่งที่ต้องการจริง ๆ คืองบกระแสเงินสด | Reveal separator and open question on cash side. No numeric relation connects the two sides; hold through current-period caution. All objects with beat ≤ 2 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |

Exit: 350ms crossfade to S06 b0; semantic link is the next narrated question. All entry/reveal/settle/hold, cancellation, rapid-input, reduced-motion and optional-back behavior use the universal contract above.

Accessible settled description: Accounting loss contains noncash charges; cash used cannot be computed from these figures alone. No subtraction, $8B residual, waterfall, money disappearance, cash burn result, or current-financial conclusion. Noncash is not irrelevant. Provide the current state’s displayed values/labels as text to assistive technology; do not announce animation frames.

Data/encoding: Exact value/period/metric tuples are the essential-label rows above and references/visual-scenes.json, traced to the claim register. Position is typographic grouping only, not a quantitative axis. No baseline, area, length or growth scale applies. Missing results are unknown, not zero.

Narrated detail remains in the complete unchanged scene: financing revaluation cause, shareholder significance, noncash not irrelevant, unavailable cash-flow reconciliation. Do not fill quiet holds with additional graphics.

Factual boundary: No subtraction, $8B residual, waterfall, money disappearance, cash burn result, or current-financial conclusion. Noncash is not irrelevant.

Assets/fallback: F01/F02 local fonts; all shapes are inline editable vector/DOM. No network media, WebGL or generated image. Missing primary font uses the packaged companion where covered, then system emergency fallback with a QA failure until actual font loading is restored.

Scene assertions: AC-001/002/005/006: FY2025 label applies to both figures; inclusion bracket is unsized; no subtraction result exists in any state; final question does not assert zero cash or insolvency. All scenes additionally map to AC-004/007/008/010/011/012/014/022 for fitted stage, clean canvas, keys, 30-second holds, reset, reduced motion, noncolor decoding and pointer. These are required downstream tests, not passed runtime results.

### S06

Content reference: 01_CONTENT.md, stable scene S06. Claim IDs: C03, C04, C09, C12.

Takeaway: Credit positive preliminary adjusted operating income and keep Q3 outlook separate from cash evidence.

Medium: editable 2D text/vector evidence composition. Depth/camera/lighting: NOT_APPLICABLE. Content arrows: NONE.

Thai rationale draft for future 06_SCENE_RATIONALE: สองงวดใช้ตำแหน่งใกล้กันแต่ขอบเส้นต่างกันและติดสถานะชัด ให้ข่าวกำไรด้านบวกอยู่บนภาพจริง ส่วนกำไรสุทธิกับเงินสดยังเป็นคำถาม ไม่ต่อเป็นสะพานตัวเลขที่ยังไม่มี

Composition and visual semantics: exact anchors below; one focal group per revealed beat. Existing evidence remains full contrast while the newly revealed group receives attention. Negative space separates distinct evidence, never a measured gap.

| Object | Kind | Entry beat | Geometry / appearance |
|---|---|---:|---|
| question | text | 0 | x=192, y=140, 60px, left, #202722; Adjusted profit. Sustainable cash? |
| metric | text | 0 | x=192, y=290, 42px, left, #202722; Adjusted operating income |
| q2-outline | rect | 0 | x=192, y=365, w=700, h=270, stroke=#226B5C |
| q2 | text | 0 | x=235, y=440, 40px, left, #226B5C; Q2 2026 · Preliminary |
| positive | text | 0 | x=235, y=545, 64px, left, #226B5C; Positive |
| q3-outline | rect | 1 | x=1028, y=365, w=700, h=270, stroke=#576158, dash=12 10 |
| q3 | text | 1 | x=1070, y=440, 40px, left, #202722; Q3 2026 · Outlook |
| q3positive | text | 1 | x=1070, y=545, 56px, left, #226B5C; Expected positive |
| unknown | text | 2 | x=960, y=810, 48px, center, #576158; Net income ?   Cash flow ? |

Copy ledger:

| Copy | Segmentation | Count | Class and reason |
|---|---|---:|---|
| Adjusted profit. Sustainable cash? | Adjusted / profit / Sustainable / cash | 4 | Ordinary |
| Adjusted operating income | Adjusted / operating / income | 3 | Essential: Specific profit definition, not generic net profit. |
| Q2 2026 · Preliminary | Q2 / 2026 / Preliminary | 3 | Essential: Quarter and preliminary status attached from entry. |
| Positive | Positive | 1 | Essential: Reported sign only; no amount inferred. |
| Q3 2026 · Outlook | Q3 / 2026 / Outlook | 3 | Essential: Outlook status, not achieved second quarter. |
| Expected positive | Expected / positive | 2 | Essential: Expected sign only; count repeated text instance. |
| Net income ?   Cash flow ? | Net / income / Cash / flow | 4 | Essential: Missing comparable reconciliation endpoints; question marks are not zero. |

Scene-wide count: 4 ordinary + 16 essential = 20. No extra canvas attribution, titles or labels may be added.

| Beat | Exact spoken cue | Visual job / endpoint | Duration and hold |
|---|---|---|---|
| b0 | ไตรมาสสองปี 2026 Anthropic มีกำไร | Show Q2 preliminary positive operating signal and exact adjusted metric. All objects with beat ≤ 0 are fully visible and stationary. | Entry 500+200ms; indefinite hold |
| b1 | คาดว่าจะทำกำไรในนิยามนี้ต่อเนื่องในไตรมาสสาม | Reveal dashed Q3 outlook at equal size, not a growth bar. Hold through adjustments and gross-margin narration; no gross-margin graphic. All objects with beat ≤ 1 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |
| b2 | เชื่อมจากกำไรแบบปรับปรุงแล้ว ไปถึงกำไรสุทธิและเงินสดจริง | Add two explicit unknown reconciliation endpoints below; no arrows or numeric bridge. All objects with beat ≤ 2 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |

Exit: 350ms crossfade to S07 b0; semantic link is the next narrated question. All entry/reveal/settle/hold, cancellation, rapid-input, reduced-motion and optional-back behavior use the universal contract above.

Accessible settled description: Credit positive preliminary adjusted operating income and keep Q3 outlook separate from cash evidence. No numeric profit magnitude, GAAP or cash conclusion. Gross margin >80% and exclusions are narration-only; do not attach them to adjusted operating income. Provide the current state’s displayed values/labels as text to assistive technology; do not announce animation frames.

Data/encoding: Exact value/period/metric tuples are the essential-label rows above and references/visual-scenes.json, traced to the claim register. Position is typographic grouping only, not a quantitative axis. No baseline, area, length or growth scale applies. Missing results are unknown, not zero.

Narrated detail remains in the complete unchanged scene: gross margin >80%, its partner-share/training-cost exclusions, and the prohibition on importing those exclusions into adjusted operating income. Do not fill quiet holds with additional graphics.

Factual boundary: No numeric profit magnitude, GAAP or cash conclusion. Gross margin >80% and exclusions are narration-only; do not attach them to adjusted operating income.

Assets/fallback: F01/F02 local fonts; all shapes are inline editable vector/DOM. No network media, WebGL or generated image. Missing primary font uses the packaged companion where covered, then system emergency fallback with a QA failure until actual font loading is restored.

Scene assertions: AC-001/002/005/006: Q2 qualified positive result receives genuine visibility; Q3 dashed outline and Outlook are attached from first frame; gross-margin >80% and excluded cost categories never appear attached to operating income. All scenes additionally map to AC-004/007/008/010/011/012/014/022 for fitted stage, clean canvas, keys, 30-second holds, reset, reduced motion, noncolor decoding and pointer. These are required downstream tests, not passed runtime results.

### S07

Content reference: 01_CONTENT.md, stable scene S07. Claim IDs: C05, C13.

Takeaway: Reserved capacity can serve demand and creates differently flexible multiyear obligations.

Medium: editable 2D text/vector evidence composition. Depth/camera/lighting: NOT_APPLICABLE. Content arrows: NONE.

Thai rationale draft for future 06_SCENE_RATIONALE: เริ่มจากกำลังผลิตก่อนเผยภาระ เพื่อให้เห็นเหตุผลทางธุรกิจ เส้นยาวหมายถึงสัญญาหลายปีเท่านั้น ไม่มีช่องปีหรือความสูงแทนเงินจ่ายจริง

Composition and visual semantics: exact anchors below; one focal group per revealed beat. Existing evidence remains full contrast while the newly revealed group receives attention. Negative space separates distinct evidence, never a measured gap.

| Object | Kind | Entry beat | Geometry / appearance |
|---|---|---:|---|
| capacity | text | 0 | x=192, y=165, 60px, left, #226B5C; Reserve capacity |
| schematic | text | 0 | x=192, y=280, 36px, left, #576158; Illustrative |
| capacity-outline | rect | 0 | x=315, y=425, w=290, h=250, stroke=#226B5C |
| pin-left0 | line | 0 | x1=265, y1=460, x2=315, y2=460, stroke=#226B5C |
| pin-right0 | line | 0 | x1=605, y1=460, x2=655, y2=460, stroke=#226B5C |
| pin-left1 | line | 0 | x1=265, y1=515, x2=315, y2=515, stroke=#226B5C |
| pin-right1 | line | 0 | x1=605, y1=515, x2=655, y2=515, stroke=#226B5C |
| pin-left2 | line | 0 | x1=265, y1=570, x2=315, y2=570, stroke=#226B5C |
| pin-right2 | line | 0 | x1=605, y1=570, x2=655, y2=570, stroke=#226B5C |
| pin-left3 | line | 0 | x1=265, y1=625, x2=315, y2=625, stroke=#226B5C |
| pin-right3 | line | 0 | x1=605, y1=625, x2=655, y2=625, stroke=#226B5C |
| obligation | text | 1 | x=840, y=165, 60px, left, #965038; Future obligations |
| metric | text | 1 | x=840, y=330, 40px, left, #202722; Commitments |
| amount | text | 1 | x=840, y=435, 56px, left, #965038; At least US$518,000 million |
| period | text | 1 | x=840, y=535, 44px, left, #576158; Roughly a decade |
| span | path | 1 | d=M 840 670 L 840 690 L 1720 690 L 1720 670, stroke=#965038 |

Copy ledger:

| Copy | Segmentation | Count | Class and reason |
|---|---|---:|---|
| Reserve capacity | Reserve / capacity | 2 | Ordinary |
| Illustrative | Illustrative | 1 | Ordinary |
| Future obligations | Future / obligations | 2 | Ordinary |
| Commitments | Commitments | 1 | Essential: Contract commitments, not debt, annual expense or cash used. |
| At least US$518,000 million | At / least / US$518,000 / million | 4 | Essential: At-least cumulative obligation, USD million unit. |
| Roughly a decade | Roughly / a / decade | 3 | Essential: Approximate multiyear horizon; not an annual schedule. |

Scene-wide count: 5 ordinary + 8 essential = 13. No extra canvas attribution, titles or labels may be added.

| Beat | Exact spoken cue | Visual job / endpoint | Duration and hold |
|---|---|---|---|
| b0 | บริษัทก็ต้องมีกำลังประมวลผลเพียงพอ | Establish one abstract capacity outline and reservation wording; silhouette has no rack/unit-count meaning. All objects with beat ≤ 0 are fully visible and stationary. | Entry 500+200ms; indefinite hold |
| b1 | แต่อีกด้านหนึ่งคือภาระที่ต้องรับไว้ก่อน | Reveal future-obligation group with full metric/unit/horizon. Hold through 80%, variable flexibility, xAI 90-day notice and payment timing; no unsupported visual schedule. All objects with beat ≤ 1 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |

Exit: 350ms crossfade to S08 b0; semantic link is the next narrated question. All entry/reveal/settle/hold, cancellation, rapid-input, reduced-motion and optional-back behavior use the universal contract above.

Accessible settled description: Reserved capacity can serve demand and creates differently flexible multiyear obligations. No rack counts, utilization, equal annual payments, total due today, stacked vendor totals or overlap sum. Contract flexibility and 80% detail remain narration-only. Provide the current state’s displayed values/labels as text to assistive technology; do not announce animation frames.

Data/encoding: Exact value/period/metric tuples are the essential-label rows above and references/visual-scenes.json, traced to the claim register. Position is typographic grouping only, not a quantitative axis. No baseline, area, length or growth scale applies. Missing results are unknown, not zero.

Narrated detail remains in the complete unchanged scene: about 80% contract terms, xAI cancellation notice of 90 days and lack of complete annual maturity schedule. Do not fill quiet holds with additional graphics.

Factual boundary: No rack counts, utilization, equal annual payments, total due today, stacked vendor totals or overlap sum. Contract flexibility and 80% detail remain narration-only.

Assets/fallback: F01/F02 local fonts; all shapes are inline editable vector/DOM. No network media, WebGL or generated image. Missing primary font uses the packaged companion where covered, then system emergency fallback with a QA failure until actual font loading is restored.

Scene assertions: AC-001/002/005/006: capacity schematic precedes obligation; cumulative commitments/horizon shown together; no equal year allocation or debt label; 80%/xAI details remain accurate in narration but no invented blocks. All scenes additionally map to AC-004/007/008/010/011/012/014/022 for fitted stage, clean canvas, keys, 30-second holds, reset, reduced motion, noncolor decoding and pointer. These are required downstream tests, not passed runtime results.

### S08

Content reference: 01_CONTENT.md, stable scene S08. Claim IDs: A01.

Takeaway: Three conditional paths are possible, without probability or forecast.

Medium: editable 2D text/vector evidence composition. Depth/camera/lighting: NOT_APPLICABLE. Content arrows: NONE.

Thai rationale draft for future 06_SCENE_RATIONALE: แสดงทีละทางด้วยน้ำหนักเท่ากันและเก็บทั้งสามทางไว้ในตอนท้าย ป้ายสถานการณ์ป้องกันการอ่านเป็นผลที่เกิดแล้ว เส้นขนาดเท่ากันไม่ใช่กราฟหรือโอกาสเกิด

Composition and visual semantics: exact anchors below; one focal group per revealed beat. Existing evidence remains full contrast while the newly revealed group receives attention. Negative space separates distinct evidence, never a measured gap.

| Object | Kind | Entry beat | Geometry / appearance |
|---|---|---:|---|
| scenario | text | 0 | x=192, y=135, 56px, left, #576158; Scenarios |
| condition0 | line | 0 | x1=275, y1=335, x2=675, y2=335, stroke=#226B5C, dash=12 10 |
| path0 | text | 0 | x=795, y=290, 64px, left, #226B5C; Growth outpaces costs |
| condition1 | line | 1 | x1=275, y1=565, x2=675, y2=565, stroke=#965038, dash=12 10 |
| path1 | text | 1 | x=795, y=520, 64px, left, #965038; Cash strained |
| condition2 | line | 2 | x1=275, y1=795, x2=675, y2=795, stroke=#202722, dash=12 10 |
| path2 | text | 2 | x=795, y=750, 64px, left, #202722; More funding |

Copy ledger:

| Copy | Segmentation | Count | Class and reason |
|---|---|---:|---|
| Scenarios | Scenarios | 1 | Ordinary |
| Growth outpaces costs | Growth / outpaces / costs | 3 | Ordinary |
| Cash strained | Cash / strained | 2 | Ordinary |
| More funding | More / funding | 2 | Ordinary |

Scene-wide count: 8 ordinary + 0 essential = 8. No extra canvas attribution, titles or labels may be added.

| Beat | Exact spoken cue | Visual job / endpoint | Duration and hold |
|---|---|---|---|
| b0 | ด้านที่เป็นโอกาสคือ ถ้าลูกค้าใช้ Claude ต่อเนื่อง | Reveal first conditional branch; dashed rule encodes conditionality only, not length or time. All objects with beat ≤ 0 are fully visible and stationary. | Entry 500+200ms; indefinite hold |
| b1 | อีกด้าน ถ้าคู่แข่งกดราคา | Reveal second equal-weight branch; first remains fully readable. All objects with beat ≤ 1 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |
| b2 | ยังมีกรณีที่ธุรกิจโตดี แต่ต้องระดมทุนต่อ | Reveal third equal-weight branch; hold all three while narrator says these are tests, not predictions. All objects with beat ≤ 2 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |

Exit: 350ms crossfade to S09 b0; semantic link is the next narrated question. All entry/reveal/settle/hold, cancellation, rapid-input, reduced-motion and optional-back behavior use the universal contract above.

Accessible settled description: Three conditional paths are possible, without probability or forecast. Equal weight and equal durations; no winner, probabilities, numerical forecasts, directional financial scale or measured outcomes. All three narrated possibilities retained. Provide the current state’s displayed values/labels as text to assistive technology; do not announce animation frames.

Data/encoding: Nonquantitative identity or concept; no scale, axes, baseline or inferred dataset.

Narrated detail remains in the complete unchanged scene: all conditional mechanisms including growth with further financing, no probabilities. Do not fill quiet holds with additional graphics.

Factual boundary: Equal weight and equal durations; no winner, probabilities, numerical forecasts, directional financial scale or measured outcomes. All three narrated possibilities retained.

Assets/fallback: F01/F02 local fonts; all shapes are inline editable vector/DOM. No network media, WebGL or generated image. Missing primary font uses the packaged companion where covered, then system emergency fallback with a QA failure until actual font loading is restored.

Scene assertions: AC-001/002/006/009: three conditional branches retained with identical font size, rule length and reveal timing; scenario label always visible; no probability, winner badge or forecast axis. All scenes additionally map to AC-004/007/008/010/011/012/014/022 for fitted stage, clean canvas, keys, 30-second holds, reset, reduced motion, noncolor decoding and pointer. These are required downstream tests, not passed runtime results.

### S09

Content reference: 01_CONTENT.md, stable scene S09. Claim IDs: C10, C11, C12, A01.

Takeaway: End with three evidence questions, not an investment instruction.

Medium: editable 2D text/vector evidence composition. Depth/camera/lighting: NOT_APPLICABLE. Content arrows: NONE.

Thai rationale draft for future 06_SCENE_RATIONALE: สามกลุ่มคำคือหลักฐานที่ต้องตามต่อ กลุ่มกลางวางกำไรกับเงินสดใกล้กันแต่ไม่ต่อเป็นผลคำนวณ ตอนจบค้างไว้เพื่อให้ผู้เล่าสรุปตามหลักฐาน

Composition and visual semantics: exact anchors below; one focal group per revealed beat. Existing evidence remains full contrast while the newly revealed group receives attention. Negative space separates distinct evidence, never a measured gap.

| Object | Kind | Entry beat | Geometry / appearance |
|---|---|---:|---|
| customers | text | 0 | x=300, y=280, 80px, left, #226B5C; Customers |
| profit | text | 1 | x=770, y=470, 72px, left, #202722; Profit |
| cash | text | 1 | x=1110, y=470, 72px, left, #202722; Cash |
| payment | text | 2 | x=1300, y=710, 46px, left, #965038; Payment obligations |
| question1 | line | 0 | x1=300, y1=405, x2=490, y2=405, stroke=#226B5C, dash=9 10 |
| question2 | line | 1 | x1=770, y1=595, x2=1320, y2=595, stroke=#202722, dash=9 10 |
| question3 | line | 2 | x1=1370, y1=835, x2=1630, y2=835, stroke=#965038, dash=9 10 |

Copy ledger:

| Copy | Segmentation | Count | Class and reason |
|---|---|---:|---|
| Customers | Customers | 1 | Ordinary |
| Profit | Profit | 1 | Ordinary |
| Cash | Cash | 1 | Ordinary |
| Payment obligations | Payment / obligations | 2 | Ordinary |

Scene-wide count: 5 ordinary + 0 essential = 5. No extra canvas attribution, titles or labels may be added.

| Beat | Exact spoken cue | Visual job / endpoint | Duration and hold |
|---|---|---|---|
| b0 | ชุดแรกคือคุณภาพของรายได้ | First evidence question at upper left; dashed underline signals unanswered prompt, not a series. All objects with beat ≤ 0 are fully visible and stationary. | Entry 500+200ms; indefinite hold |
| b1 | ชุดที่สองคือสะพานจากกำไรไปสู่เงินสด | Reveal profit and cash together as one evidence question at center, without a calculated connector. All objects with beat ≤ 1 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |
| b2 | ชุดที่สามคือภาระตามเวลา | Reveal obligations at lower right; retain all three through conclusion and valuation boundary. Final hold does not loop. All objects with beat ≤ 2 are fully visible and stationary. | Space reveal 650+200ms; indefinite hold |

Exit: No automatic exit or loop; final Space no-op, R may restart. All entry/reveal/settle/hold, cancellation, rapid-input, reduced-motion and optional-back behavior use the universal contract above.

Accessible settled description: End with three evidence questions, not an investment instruction. No investment verdict, no invented evidence, no claim profitability impossible, no fourth metric. R restarts cover; final Space does nothing. Provide the current state’s displayed values/labels as text to assistive technology; do not announce animation frames.

Data/encoding: Nonquantitative identity or concept; no scale, axes, baseline or inferred dataset.

Narrated detail remains in the complete unchanged scene: all full narration and source caveats; the canvas is a cue, not a replacement script. Do not fill quiet holds with additional graphics.

Factual boundary: No investment verdict, no invented evidence, no claim profitability impossible, no fourth metric. R restarts cover; final Space does nothing.

Assets/fallback: F01/F02 local fonts; all shapes are inline editable vector/DOM. No network media, WebGL or generated image. Missing primary font uses the packaged companion where covered, then system emergency fallback with a QA failure until actual font loading is restored.

Scene assertions: AC-002/003/008/011: three evidence groups appear at correct cues; final hold remains stable; final Space does nothing; R restores S01; no investment recommendation or fabricated verdict. All scenes additionally map to AC-004/007/008/010/011/012/014/022 for fitted stage, clean canvas, keys, 30-second holds, reset, reduced motion, noncolor decoding and pointer. These are required downstream tests, not passed runtime results.

## Asset and credit handoff

A01 and A01F are the same authentic source bytes at two local package paths, allowing deterministic path-failure recovery without inventing imagery. Runtime path: assets/photos/dario-amodei-techcrunch-2023.jpg; fallback assets/photos/dario-amodei-techcrunch-2023-fallback.jpg. SHA256 is 395a3bc4b0e4ccaae1d3c6cb05e1aa39d10bb235288335551e91a67ab8289a2e for both optimized runtime files; original source SHA256 is 7491726ca688e37f803008cf0010ec126c8fb4da39ee4a54f13b0cd1c749d822. Verified source is 4000×2667 RGB JPEG, 1,545,886 bytes; optimized runtime derivative is 1200×800, 88148 bytes. Display is uncropped contain in x=192,y=220,w=840,h=560, no recoloring/mirroring/generative edits; focal face approx (0.49,0.42). The source’s undecodable background printing is not relabeled or replaced. Required credit names the real 2023 event; imagery does not claim a contemporary IPO event.

CC BY 2.0 full credit and links are in assets/CREDITS.txt and this review directory's README. Builder must copy an easily found CREDITS.txt or CREDITS.html at the package root, link it clearly from README_TH and 06_SCENE_RATIONALE, and retain all copyright/license notices. No visible credits overlay or control is added to the clean recording canvas. This is accompanying-package attribution, not hidden-only metadata. Any standalone export or public recording must travel with the same full credit in its accompanying description/credit document; this delivery does not authorize a new posting. State: verified original retained as provenance; runtime photo proportionally resized to 1200×800 JPEG, no crop. If later crop changes, update credit change notice and re-review image/copy.

F01/F02 are licensed subset Noto Sans Thai 2.002 and Noto Sans 2.015 Unicode-subset WOFF derivatives of variable TTF sources at immutable google/fonts commit 9710da1eacb3be272583c3224dcb70f9da6eadbb. Use width=100 and native weights 400/600, package OFL files; no runtime network requests. See manifest for exact hashes. Official logos and collected full-page/ZIP research evidence are deliberately not committed or packaged. The rights review preserves links and factual verification notes rather than redistributing unlicensed press-kit material.

## Technical brief and exit boundary

Builder reads 01–05, this scene JSON, manifest/credits and Visual review, then owns framework/state/portable-loopback/launchers/ZIP decisions per 04_BUILD.md. Static storyboard code is reference-only proof, not runtime source. Preserve the visual semantics, all-state counts, exact essential labels and cues. Reflowing dense labels, shortening a caveat, changing axes or adding forecast shapes requires upstream review.

Required remaining evidence: actual browser screenshots for every state, normal/reduced-motion complete keyboard run, R mid-reveal, full pointer behavior including over photo, >=30s every-scene hold, console/performance, no external runtime requests, prebuilt clean ZIP extraction/hash/manifest, offline loopback helper and launcher recovery, exact owner folder package upload and rationale. Windows launch/stop/restart and owner rehearsal remain NOT_RUN. Neither static visual review nor content-document review establishes any of these checks.

No owner publication, purchase or new service access is required by this Visual handoff. Existing three owner editions, main, old branches, legacy contents and owner-folder identity remain preserved.

---


## v1.7 language audit contract

All 23 settled states use only English app-authored text. Every entry, reveal, hold, reset and same-source fallback reuses those English objects. Every scene's English semantic description is supplied in references/visual-scenes.json, with English alt text/fallback text and per-scene LANGUAGE_AUDIT. Runtime fallback errors use the exact English fallback text as semantic/accessibility status only, never added visible canvas copy. Existing scene text and same-photo fallback preserve the recorded copy counts. Both image paths failing is a defect requiring repair, not permission to substitute invented imagery. HTML lang=en is required in Build and tested under AC-024. The authentic photo has no legible non-English inscription at the approved no-crop display. Generic Anthropic is a true proper name; there is no recreated wordmark. No non-English source-inscription exception is requested or granted. Thai cue/narration/rationale metadata must never be rendered as app text. Owner PDFs, narration, rationale and quick-start remain Thai.

# Master instructions retained from v1.7

# 03_VISUAL_PLAN.md — Agent 3: Visual Director

Visual planning defines what the audience sees and why. Give Builder enough detail to implement each scene without asking the owner to choose objects or transitions.

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

Read README.md, WORKFLOW_STATUS.md, 01_CONTENT.md, 02_DESIGN_SYSTEM.md, 04_BUILD.md, and 05_QA.md on the active branch.

Output: filled 03_VISUAL_PLAN.md plus asset specifications/provenance in the repo. Reuse the recorded topic Drive folder. Do not place this technical plan in Drive. Do not build the site or substitute a new thesis.

## Planning procedure

1. Select and verify the authentic S01 cover asset before readiness: a real relevant image/official logo/original character asset from a verifiable source, with recorded rights, resolution, crop and offline path. S01 initial state and R reset show it immediately; do not substitute generated imagery. Preserve content scene IDs and claim IDs. S01 is the cover; R must always return to that cover's initial state. Map every narration beat to a visual job. Flag missing or overloaded content and route it to Agent 1 rather than inventing assertions.
2. Choose 2D, chart, real material, 3D, or hybrid based on what improves understanding. Document why depth or complexity is necessary when used.
3. Define one focal subject, composition, scale, safe area, visual hierarchy, and what the audience should notice at each beat.
4. Specify actual data and encodings for charts. Include units, baseline, period, denominator, scale type, missing values, uncertainty, and source links/claim IDs. Schematic sizes cannot masquerade as measurements.
5. Select or specify assets with repo-relative paths, source, license/permission, attribution needs, crop/focal coordinates, resolution, fallback, and generation disclosure. Generated images support illustration; they are not documentary evidence.
6. Keep all scene copy, annotations and essential data labels in English. Audit embedded asset text, including the authentic cover; preserve true wordmarks/names and resolve any indispensable non-English inscription through a recorded owner exception. Validate each scene's ordinary visible copy against the default 0–8-word target across all reveals, including ordinary text baked into media and wordmarks. List excluded essential chart/data labels, units, numbers and legends separately, justify each, and record the total visible count. An explicitly approved Thai-canvas override requires linguistic segmentation. Essential attribution must fit the budget or the asset must change.
7. Build a narration cue map with entry, reveal, settle, hold, and exit. Motion stops at meaningful endpoints. Hold duration is presenter-controlled. Define each state's behavior for Spacebar, R-to-cover, rapid input and reduced motion; specify previous-settled-scene behavior only if optional Left Arrow is implemented, and fullscreen behavior only if optional F is implemented. Spacebar is the main forward control and the complete narration flow never requires clicking visual objects.
8. Prepare the technical brief inputs for Builder in this file, referencing the existing 04_BUILD.md. Do not declare implementation-ready while assets, data, or required decisions are unresolved.

## Fillable scene index

~~~yaml
PROJECT_ID: <from status>
CONTENT_INPUT_COMMIT: <verified SHA>
DESIGN_INPUT_COMMIT: <verified SHA>
VISUAL_PLAN_VERSION: <version>
COVER_ASSET_ID: <verified authentic asset ID>
POINTER_SPEC_REFERENCE: 02_DESIGN_SYSTEM.md#presenter-pointer-and-authentic-first-cover
SCENE_COUNT: <actual>
ASSET_MANIFEST_PATH: assets/manifest.md
~~~

| Scene ID | Narration takeaway | Medium | Focal subject | Ordinary words / excluded data labels / total | Duration estimate | Claim IDs | Asset status |
|---|---|---|---|---|---|---|---|
| S01 | <one idea> | <medium> | <subject> | <ordinary 0–8 / excluded / total> | <seconds> | <IDs> | READY/PENDING |

## Scene specification — repeat for every scene

~~~yaml
SCENE_ID: S01
CONTENT_REFERENCE: "01_CONTENT.md#<section>"
CLAIM_IDS: [<IDs>]
AUDIENCE_TAKEAWAY: <one sentence>
VISUAL_JOB: <why a visual is needed>
MEDIUM: <2D/chart/real/3D/hybrid>
MEDIUM_REASON: <narration-specific reason>
FOCAL_SUBJECT: <object/evidence>
EXPLANATORY_ARROWS: <NONE or minimal arrows with exact relationship/direction, endpoints, semantic job, hierarchy, reveal/hold behavior; never navigation/control styling>
COMPOSITION:
  ANCHOR: <x/y as normalized canvas coordinates>
  BOUNDS: <width/height relative to 16:9 canvas>
  SUPPORTING_OBJECTS: <count, hierarchy, anchors>
  NEGATIVE_SPACE: <where and why>
  SAFE_AREA_CHECK: <no essential clipping>
VISIBLE_COPY: <exact English ordinary copy or empty>
VISIBLE_WORD_COUNT: <ordinary count targeting 0–8 across the entire scene>
ESSENTIAL_DATA_LABELS: <exact English indispensable labels/values/units/legend or NONE>
ESSENTIAL_LABEL_REASON: <why each excluded item is required for truthful reading>
TOTAL_VISIBLE_WORD_COUNT: <ordinary plus excluded items>
COUNT_METHOD: <ordinary versus essential-data distinction; Thai segmentation if needed>
DATA_SPEC: <verified values/encoding, or NOT_APPLICABLE>
ASSETS: [<manifest IDs and repo-relative paths>]
LIGHTING_CAMERA: <3D-only details, or NOT_APPLICABLE>
NARRATION_CUE: <exact phrase that cues entry/reveal>
ENTRY_STATE: <geometry/opacities and what is immediately understandable>
REVEAL_BEATS: <ordered list; expand in timing table>
SETTLE_STATE: <precise endpoint after each reveal>
HOLD_STATE: <stable composition; no decorative continuous motion>
EXIT_STATE: <transition and semantic link to next scene>
REDUCED_MOTION: <same meaning with stable endpoints>
BACK_NAVIGATION: <previous settled scene if optional Left Arrow is implemented; otherwise NOT_APPLICABLE>
RETURN_TO_COVER: <R cancels current motion and selects first scene initial state>
FALLBACK: <asset/WebGL/network failure plan preserving meaning>
FACTUAL_BOUNDARIES: <what this picture must not imply>
IMPLEMENTATION_NOTES: <required behavior, not speculative claims>
LANGUAGE_AUDIT: <English canvas/semantic text and embedded media checked; explicit source-inscription exceptions if any>
POINTER_CONTRAST_CHECK: <dot/outline remains visible over this scene without obstructing the focal subject>
COVER_AUTHENTICITY: <S01 source/asset verification and initial/reset visibility; otherwise NOT_APPLICABLE>
QA_ASSERTIONS: <scene-specific checks and evidence to capture>
~~~

### Timing / cue map — repeat per scene

| Beat | Spoken cue | Presenter action | Visual change | Duration/easing | Settled endpoint | Hold / advance condition |
|---|---|---|---|---|---|---|
| Entry | <cue> | <Space/entry> | <change> | <timing> | <endpoint> | <indefinite hold> |
| Reveal 1 | <cue> | Space | <change> | <timing> | <endpoint> | <next deliberate key> |
| Exit | <cue> | Space at final hold | <change> | <timing> | <next entry> | <condition> |

Normal motion order is Transition → Reveal → Settle → Hold. No timed advance is implied by these estimates. Spacebar is the complete forward route. During a reveal it may first settle the current beat before advancing; R cancels motion and returns to cover. No additional default forward key or object click is required.

### Chart specification — required for data scenes

| Field | Value |
|---|---|
| Claim/source IDs | <verified IDs> |
| Dataset path and exact values | <repo-relative path; preserve source units> |
| Unit / period / denominator | <scope> |
| Encoding and scale | <linear/log, area/length, baseline and justification> |
| Uncertainty / missing data | <how handled> |
| Ordinary copy budget | <exact copy, default target 0–8, and count> |
| Essential data label exclusions | <exact labels/values/units, necessity of each, excluded and total counts> |
| Narrated detail | <detail moved out of canvas without changing meaning> |
| Misinterpretation to prevent | <risk and design response> |

## Asset manifest

Store in assets/manifest.md or as a maintained section here.

| Asset ID | Repo-relative runtime path | Origin/source URL | Rights/license | Type/resolution/size | Crop/focal point | Attribution | Generated? | Fallback | State |
|---|---|---|---|---|---|---|---|---|---|
| A01 | assets/<name> | <actual source> | <permission> | <spec> | <coordinates> | <requirements> | YES/NO | <path/behavior> | READY/PENDING |

Add authenticity (official logo/original character/real photograph/illustration), verification notes and any required credit for the cover. If attribution must appear on the canvas, include it in the copy budget; prefer an asset whose permitted use fits the presentation. An authentic fallback must itself be available in the package.

Reference-only material belongs in references/. Runtime assets must be available from the repo/build's portable asset path; never depend on a local absolute path or an expiring authenticated Drive URL or external CDN. All required presentation assets, including cover and fonts, must be included in the local package.

## Owner rationale draft input

For each scene supply a short Thai plain-language note: what it helps the audience understand, why this medium/composition was chosen, what motion demonstrates, and what remains uncertain. Keep this draft in GitHub. Agent 4 turns it into 06_SCENE_RATIONALE in the existing topic folder after verifying the actual build.

## Exit criteria and handoff

- Every content scene and narration beat has an implementable visual, cue, stable hold, transition, and reduced-motion treatment.
- Ordinary-copy counts target 0–8 with justified essential chart/data label exclusions and total counts; no visible controls, page/scene numbers, progress bars/dots, UI/navigation arrows or persistent UI. Explanatory content arrows are permitted only when minimal, semantically necessary, subordinate to the focal subject and clearly unlike controls.
- Chart data, provenance, rights, and runtime paths are verified; unresolved items are blockers.
- 04_BUILD.md remains available as the implementation brief; 05_QA.md is read and scene assertions are mapped to it.
- Publish artifacts then status: STAGE=READY_FOR_BUILD; NEXT_ACTOR=Agent 4 — Builder.
- NEXT_ACTION: “Read 01–05 and the asset manifest. Fill 04_BUILD.md's implementation choices, build the planned web presentation, record BUILD_NOTES.md and verified package metadata, and create 06_SCENE_RATIONALE in the exact recorded topic folder. Assemble the prebuilt LOCAL_ZIP with launchers, authentic cover and theme-adaptive pointer. Record BUILD_COMMIT, manifest, PACKAGE_SHA256 and observed package download identity. Prepare independent clean-extraction/offline QA and record any real packaging/delivery blocker.”


