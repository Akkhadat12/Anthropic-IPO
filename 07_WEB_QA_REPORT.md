# Independent web QA report — Anthropic IPO two-clock story

**Current status after owner clarification: FAIL — only F5 evidence capture remains an acceptance gap.**  
Test date: 29 September 2026 (Asia/Bangkok).  
Final URL tested: https://anthropic-ipo-two-clocks.vercel.app/  
Browser: Chrome, live public URL. Desktop viewports tested at 1920 × 900 and 1600 × 900 (16:9); narrow viewport tested at 390 × 844. The page opened without an application login prompt. The scene table and findings below record the first pass; the dated retest at the end gives the current finding status.

## Evidence and limits

- The owner-facing [Thai scene rationale](https://docs.google.com/document/d/1grcgF9jbovWbEG0_ASc12Te_xeT81PlGqjhEyiG6nik/edit) contains embedded settled desktop images for Cover, Scenes 1–6, and Closing. I compared those scenes with the live published page and inspected settled desktop (including 1600 × 900) and phone states in Chrome.
- Precise observations below record actual visible text, controls, and state changes. Separate durable 16:9, phone, and transition screenshot files are **not yet linked**. This falls short of the stable evidence requirement in [05_QA.md](https://github.com/Akkhadat12/Anthropic-IPO/blob/main/05_QA.md). Capture and link those files after corrections; do not convert this report into a blanket PASS without them.
- I did not run the production build, a clean unauthenticated browser profile, a reduced-motion emulation, or a long-duration memory test. The live page showed no site-origin console errors during this pass; warnings observed came from a Chrome extension.

## Scene-by-scene results

| Scope | Expected / observed at settled 1600 × 900 and 390 × 844 | Result |
| --- | --- | --- |
| Cover | Project Rainier aisle, racks, person, question, and entry region appeared at both widths. The AWS ownership caption is difficult to read over the bright photo on phone. Clicking the cover entered Scene 1. | PARTIAL — F4 |
| Scene 1 | FY2025 Reuters-reported revenue ~$4.6B and operating loss >$8B stayed on one plate. Company-stated May 2026 annualized pace >$47B stayed on a separate plate; phone stacked them without dropping periods or inequality signs. No continuous trend was drawn. | PASS |
| Scene 2 | Customer work reached Paid use through Direct, API, or Cloud. Selecting API then Cloud changed the selected route and remained on Scene 2; Paid use advanced. The route mix was labeled unknown. | PASS |
| Scene 3 | Price per task and compute per task were both visible; frontier training was separate. No measured split or exact task cost was drawn. The Sonnet 5.5 footnote needs a more exact cost definition. | PARTIAL — F3 |
| Scene 4 | FY2025 operating loss >$8B and preliminary Q2 2026 positive adjusted operating income were separated and labeled NOT COMPARABLE. Q2 revenue >$11.5B was identified as preliminary revenue, not adjusted income. Phone preserved both bases. | PASS |
| Scene 5 | A recognizable Project Rainier campus rendered at both widths. AWS >$100B over 10 years and Reuters ~$518B in future years were separate, with overlap and non-2027-cash caveats. Phone caveat text is very small. | PARTIAL — F4 |
| Scene 6 | Claude, GPT-6 Astra, and Gemini appeared as options without a ranking. Four gates remained visible on phone. Early gate clicks highlighted without advancing; Commitment schedule opened Closing. | PASS |
| Closing | Two clocks remained apart with NOT YET and “Two clocks. One cash test.” Clicking the focal region returned to Cover. Space at the settled Closing state did nothing; R from Closing returned to Cover. | PASS |
| Sources overlay | Desktop and phone overlay opened, phone contents scrolled, and Escape closed it. The Reuters link failed in the QA browser. | FAIL — F2 |

## Findings requiring correction

**F1 — HIGH — Word deliverable is not a Word file.** The Drive item named `06_SCENE_RATIONALE.docx` has MIME type `application/vnd.google-apps.document` (file ID `1grcgF9jbovWbEG0_ASc12Te_xeT81PlGqjhEyiG6nik`). Its Thai content and embedded images are present, but the .docx suffix does not change its native Google Docs format. Export to a real DOCX, place that file in the specified Drive folder, and verify MIME type `application/vnd.openxmlformats-officedocument.wordprocessingml.document` and its returned file link. Retest pending.

**F2 — MEDIUM — Reuters source link fails.** The Sources overlay and the Thai rationale point to `https://kelo.com/2026/09/28/exclusive-anthropics-ipo-prospectus-shows-sweeping-ai-vision-surging-costs/`. Direct opening in the QA Chrome session returned “403 Forbidden — Request forbidden by administrative rules.” A [Reuters bylined syndication](https://www.streetinsider.com/Reuters/Exclusive-Anthropics%2BIPO%2Bprospectus%2Bshows%2Bsweeping%2BAI%2Bvision%2C%2Bsurging%2Bcosts/27115819.html) was readable and supports the 2025 figures and “coming years” qualifier. Replace or supplement the failing link in the site and rationale, then click-test it. Retest pending.

**F3 — MEDIUM — Scene 3 blurs customer cost and provider compute cost.** The site puts “Sonnet 5.5 · company test · up to 30% less per task” beneath a price-versus-compute diagram. [Anthropic's product page](https://www.anthropic.com/claude-sonnet-5-5) says this is the API customer's per-task cost in its own tests, mainly because fewer tokens were needed at unchanged token prices. It does not disclose Anthropic's internal compute cost or gross margin. Label the claim “customer API cost per task in company tests; provider compute cost unknown” and keep it out of any proof that serving cost or operating leverage has already improved. Update the Thai rationale if it uses the test as internal cost evidence. Retest pending.

**F4 — MEDIUM — Small-screen evidence labels need stronger legibility.** At 390 × 844 the white “AWS Project Rainier · not Anthropic-owned” caption sits on a bright image and is hard to read. In Scene 5 the overlap/2027 cash caveat is tiny despite carrying essential meaning. Put the cover caption on a solid or darker backing and enlarge/reflow the Scene 5 caveat without hiding the photo or obligations. Retest at phone width and recording scale pending.

**F5 — MEDIUM — Durable QA captures remain missing.** The [acceptance plan](https://github.com/Akkhadat12/Anthropic-IPO/blob/main/05_QA.md) calls for settled 16:9 and phone captures for every beat plus representative transitions and interactive states. The rationale supplies embedded desktop stills, and I observed all scenes live at 1600 × 900, but no stable phone/transition links are in this report or repository. Add the final-version captures and links; retest changed and adjacent states. Pending.

**F6 — LOW — Repository handoff text is stale.** [README.md](https://github.com/Akkhadat12/Anthropic-IPO/blob/main/README.md) still says no website or deployment exists, although [BUILD_NOTES.md](https://github.com/Akkhadat12/Anthropic-IPO/blob/main/BUILD_NOTES.md) lists the production URL. Update README after fixes so a new reviewer is not sent back to the pre-build assignment. Pending.

## Source and interaction checks

The [Series H announcement](https://www.anthropic.com/news/series-h) supports the >$47B May run-rate; the [Anthropic–AWS announcement](https://www.anthropic.com/news/anthropic-amazon-compute) supports >$100B over ten years; [Bloomberg](https://news.bloomberglaw.com/artificial-intelligence/anthropic-revenue-surges-to-over-11-5-billion-in-second-quarter) reports preliminary Q2 revenue >$11.5B and positive adjusted operating income; the readable Reuters syndication above supports FY2025 revenue near $4.6B, operating loss >$8B, and ~$518B over coming years. The site kept these bases distinct in the inspected states. The [Anthropic confidential S-1 announcement](https://www.anthropic.com/news/confidential-draft-s1-sec) does not establish a priced listing.

Cover-to-Closing clicks, route selection, early proof-gate feedback, Spacebar advancement, R return, Sources open/close, and Escape were exercised. No skipped scene was observed in the tested sequence. Rapid repetition, refresh during navigation, reduced motion, and clean-profile access still require the acceptance plan's separate retest.

## First-pass acceptance decision

**FAIL / return for correction.** F1 and F2 block the specified deliverables or source access. F3–F5 require correction or durable verification before final sign-off. After changes, recheck the exact production URL and actual DOCX, capture final desktop/phone/transition evidence, and record a dated post-fix result for each finding here.

## Retest after correction commit 94ea643 — 29 September 2026

This retest supersedes the first-pass finding statuses above. I reopened the public production URL in Chrome, inspected the corrected phone states at 390 × 844 and Scene 5 at 1600 × 900, clicked the replacement Reuters link, checked the Thai rationale text, inspected the commit, and listed the specified Drive folder.

| Finding | Current result | Retest evidence |
| --- | --- | --- |
| F1 — document format | **ACCEPTED BY OWNER** | The file is a native Google Doc, despite its .docx filename. On 29 September 2026 the owner clarified that this Google Docs file is the intended deliverable. A separate Word export is no longer required for acceptance. |
| F2 — Reuters link | **PASS** | The live Sources overlay now links to the Reuters article on StreetInsider. Clicking it opened the full bylined article, including FY2025 revenue, operating loss, and future obligations. The Thai rationale and both chart-data CSVs use the same reachable URL. |
| F3 — customer vs provider cost | **PASS** | Live Scene 3 now says “up to 30% less customer API cost per task · provider compute cost unknown.” The Thai rationale explicitly says this is not Anthropic internal compute cost or proof of serving margin. |
| F4 — phone labels | **PASS at tested size** | At 390 × 844, the Cover ownership label has a dark backing and Scene 5’s overlap/not-2027-cash caveat is larger and wraps legibly. Scene 5 also remained intact at 1600 × 900. |
| F5 — durable visual evidence | **OPEN** | The repository still has no linked final-version settled desktop/phone and representative transition/interaction capture set required by 05_QA.md. The specified Drive folder contains the rationale and two reading PDFs plus the link text file, not that capture set. Browser observations are recorded here but are not stable screenshot artifacts. |
| F6 — README handoff | **PARTIAL / LOW** | The opening now names the live site and QA report. Later paragraphs still instruct the next agent to build and publish the already-existing website and upload the rationale; those should be revised for a clean handoff. |

**Current acceptance decision after owner clarification: FAIL on evidence only.** The product corrections F2–F4 passed. The owner accepts the native Google Doc, so F1 is closed by clarified scope. F5 remains required by the QA acceptance plan: link final-version settled desktop/phone and representative transition/interaction captures, then verify those artifacts before final sign-off. F6 is a low-priority documentation cleanup.

## Owner clarification — 29 September 2026

The owner confirmed that the Google Docs file in the specified Drive folder is the intended document deliverable. This overrides the earlier DOCX-format requirement for this delivery. The first-pass F1 observation about MIME type remains factually correct as a historical check, but it is **not an open defect or acceptance blocker**. The remaining acceptance gap is F5, the durable visual QA evidence specified in 05_QA.md.
