# Start here — Web Build agent

Build the **new** Anthropic IPO immersive 3D story from branch [`research-ipo-financials-models-2026`](https://github.com/Akkhadat12/Anthropic-IPO/tree/research-ipo-financials-models-2026). First read [WORKFLOW_STATUS.md](WORKFLOW_STATUS.md), then [04_BUILD_WEB.md](04_BUILD_WEB.md), [03_STORY_STRUCTURE.md](03_STORY_STRUCTURE.md), [02_RESEARCH_AND_ANALYSIS.md](02_RESEARCH_AND_ANALYSIS.md), [01_KNOWLEDGE_SUMMARY.md](01_KNOWLEDGE_SUMMARY.md), and [05_QA.md](05_QA.md). The owner approved thesis #1: **revenue is accelerating while minimum compute obligations extend far ahead**. The build must test whether retained cash from Claude demand can cover those obligations, with the uncertainty and contrary evidence intact.

This branch is the research and story handoff. **No website has been built, deployed, or QA-tested for this branch.** The earlier `main` site and QA report are historical; do not present their URL, screenshots, or pass status as the result of this assignment. The later builder must create and verify a distinct public Vercel production build from this branch, then hand its exact URL and commit to independent QA.

## Handoff files

| File | Role |
| --- | --- |
| [01_KNOWLEDGE_SUMMARY.md](01_KNOWLEDGE_SUMMARY.md) / [mobile PDF](01_KNOWLEDGE_SUMMARY.pdf) | Neutral Thai reading pack; source facts and uncertainty. |
| [02_RESEARCH_AND_ANALYSIS.md](02_RESEARCH_AND_ANALYSIS.md) / [mobile PDF](02_RESEARCH_AND_ANALYSIS.pdf) | Thai analysis, approved thesis, scenarios, claim ledger, direct source links. |
| [03_STORY_STRUCTURE.md](03_STORY_STRUCTURE.md) | English 8–12-minute spoken journey; every scene's meaning, evidence, and transition. |
| [04_BUILD_WEB.md](04_BUILD_WEB.md) | English self-contained build brief, interaction map, motion, assets, prototype and deployment conditions. |
| [05_QA.md](05_QA.md) | English independent production QA instructions. |
| [references/chart-data.csv](references/chart-data.csv) | Sourced numeric manifest with periods, status, operators, and caveats. |
| [references/project-rainier-interior.png](references/project-rainier-interior.png), [exterior.png](references/project-rainier-exterior.png) | Exact real AWS Project Rainier image files, source and role documented in 04. |

**Owner reading folder:** [Anthropic IPO — Financials and Claude — 2026-09-29](https://drive.google.com/drive/folders/1hM3luybOC9QNUn4nqEm8g_zNJM3LL4Mz), containing [01 PDF](https://drive.google.com/file/d/1au8HnGrxv30w-R3n8wBehvUUcU9bhHp-/view) and the [current 02 PDF](https://drive.google.com/file/d/1vz5e_y0aSksrV-74gwMSWTPNPbJCVM0J/view). The Markdown files in this branch are authoritative. The 02 PDF was updated in place after Gate 2; do not use a previous downloaded copy.

**Research cutoff:** 29 September 2026, Thailand time. Anthropic announced a confidential S-1, but this team has not read a public filing. Reuters and Bloomberg reports are attributed as such. If a public S-1 appears before build or QA, reopen and update the affected research, PDFs, scene data, and site before claiming current accuracy.

## Later workflow

The builder prototypes two distinct visual directions, builds the entire route, deploys and verifies a public Vercel **production** URL, records exact commit/build notes, and produces one current Thai `06_SCENE_RATIONALE` Google Doc or genuine `.docx` in the owner Drive folder with finished-scene screenshots. The builder updates [WORKFLOW_STATUS.md](WORKFLOW_STATUS.md) to `READY_FOR_QA` only after production verification. Independent QA follows [05_QA.md](05_QA.md) and writes `07_WEB_QA_REPORT.md` on this branch with screenshot evidence, defects, retest, and `QA_PASS` or `QA_FAIL`. No agent should infer these later artifacts from this planning handoff.
