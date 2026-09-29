# Workflow status — Anthropic IPO, new assignment

- **Repository:** [Akkhadat12/Anthropic-IPO](https://github.com/Akkhadat12/Anthropic-IPO)
- **Working branch:** [research-ipo-financials-models-2026](https://github.com/Akkhadat12/Anthropic-IPO/tree/research-ipo-financials-models-2026); `main` is preserved as the historical assignment.
- **Approved scope:** Financial statements and quality of figures; model/compute economics; Claude's current standing; competition, risks, and conditional future outcomes.
- **Owner Gate 2 decision:** Thesis #1 — revenue acceleration versus long-lived minimum compute obligations. The analytical question is whether retained cash from Claude can carry serving, training, partner shares, and contracted capacity.
- **Stage:** `QA_FAIL` — independent QA found four open major findings and one minor finding on the production build source (commit `349c3cd`). See [07_WEB_QA_REPORT.md](07_WEB_QA_REPORT.md).
- **Last verified handoff content commit:** [`bf42c6c`](https://github.com/Akkhadat12/Anthropic-IPO/commit/bf42c6cdce196900c2269be953df9994684732bc), 29 September 2026. Status is recorded in a later commit.
- **Owner reading folder:** [Google Drive](https://drive.google.com/drive/folders/1hM3luybOC9QNUn4nqEm8g_zNJM3LL4Mz); [01 PDF](https://drive.google.com/file/d/1au8HnGrxv30w-R3n8wBehvUUcU9bhHp-/view) and [02 PDF](https://drive.google.com/file/d/1vz5e_y0aSksrV-74gwMSWTPNPbJCVM0J/view). The 02 PDF was replaced in place after Gate 2; Drive reports 227,259 bytes and the same file ID.
- **Required handoff files:** [01 MD/PDF](01_KNOWLEDGE_SUMMARY.md), [02 MD/PDF](02_RESEARCH_AND_ANALYSIS.md), [03 story](03_STORY_STRUCTURE.md), [04 build brief](04_BUILD_WEB.md), [05 QA brief](05_QA.md), and [source assets/data](references/chart-data.csv). Their local links were checked on 29 September 2026.
- **Public build URL / build commit:** https://anthropic-ipo-capacity-ledger.vercel.app / `349c3cd67d4217496d3dae1b0ac7338647af1e85`
- **Post-build rationale / QA report:** `06_SCENE_RATIONALE` remains missing; [07_WEB_QA_REPORT.md](07_WEB_QA_REPORT.md) records the independent `QA_FAIL` and evidence.
- **Open findings/blockers:** QA-01–04 major; QA-05 minor. The public S-1 was not confirmed at QA time; refresh research if one appears.
- **Next actor and exact action:** Web Build agent — fix findings in 07, create and link the current Thai `06_SCENE_RATIONALE` with finished-scene screenshots, deploy a new production commit, and hand its exact URL/SHA back to independent QA for retest.

**Reused-repository boundary:** The prior Anthropic IPO site, deployment, build notes, source, and QA record on `main` must never be counted as this branch's build or pass status.
