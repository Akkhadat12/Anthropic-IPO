# Independent Visual-stage review — final English canvas

Reviewed 2026-10-01 05:27 UTC. **PASS for static storyboard semantics, copy, geometry and inspected asset-use/credit consistency.** No unresolved finding remains in that scope. This is not runtime QA, package/Windows verification, or authorization to advance the workflow before the other required handoff records are aligned.

The parent relayed the owner's explicit choice, “เป็น english แบบเดิม”: English canvas, unchanged Thai narration. This review supersedes the earlier Thai-canvas count/render assessment. Content/Design/Visual document alignment is being handled separately by the parent; it was not assumed complete.

## Evidence and scope

- Current scene data: `references/visual-scenes.json`, SHA-256 `0e4f0d329f4942371c53987e5144316280b75c3571d18606cd0131c4585cb013`
- Visually rechecked all nine final 1280×720 frames; full-size representative reveals S03-b0/b1, S04-b0/b1, S05-b1, S06-b0/b1, S07-b0, S08-b0/b1; and S03 final 1280×800 letterboxing
- Checked the complete 23-state object/cue inventory and existence/dimensions of all 23 endpoint PNGs; recomputed all text counts; inspected the updated bounds report, active renderer and credits
- Compared meaning with all nine Thai narration sections in `inputs/01_CONTENT.md`, the Design financial/geometry contract and applicable visual acceptance criteria in `inputs/05_QA.md`
- These frames are **Pillow RAQM with pinned Noto Sans**, not browser screenshots. The supplied founder-photo CC BY 2.0 rights verification is separate; this review checks its use and credit consistency, not a new legal-rights determination

## Nine-scene result

| Scene | Narration/visual result |
|---|---|
| S01 | Authentic founder photograph and generic Anthropic text introduce an open sustainability question. No endorsement, success/failure verdict or claim that the photograph depicts an IPO |
| S02 | Conceptual document, submission date and unknown offer price are separate; no SEC approval, listing date or fabricated filing contents |
| S03 | FY2025, preliminary Q2 and end-July annualized run-rate keep their definitions and US$ million units. No shared magnitude axis, cross-basis growth ratio or annualized Q2 |
| S04 | Explicitly illustrative work → “Worth paying for?” → “Pay again?” preserves the conditional business argument. Two subordinate content arrows are not controls; no measured retention, task success or current mix |
| S05 | FY2025 loss and included non-cash charge use an inclusion bracket, not subtraction. “Cash flow ?” explicitly identifies the missing evidence; no invented residual or cash-burn result |
| S06 | Positive adjusted operating income is visible. Q2 is preliminary; Q3 is both “Outlook” and “Expected positive.” Net income/cash remain open; gross-margin exclusions are not misapplied |
| S07 | Capacity benefit appears before obligations. At least US$518,000 million retains the roughly-decade horizon; no annual schedule, due-today debt, utilization figure or double-counted partnership total |
| S08 | All three narrated scenarios retain matching text scale and rule length. Explicit scenario label; no probabilities, forecasts or preferred outcome |
| S09 | Customer quality, profit/cash and payment obligations close as evidence questions, without investment instructions |

## Independent all-state copy audit

Counted the union of text objects across all states: persistent objects once, separate repeated instances separately. English words are counted normally; hyphenated compounds are single lexical tokens. Punctuation/question marks and `>` remain visible inventoried marks but are not words. The credit is packaged outside the recording canvas. Essential exclusions are minimal metric, period, amount, unit, status and reconciliation labels, not explanatory paragraphs.

| Scene | Ordinary | Essential excluded | Total |
|---|---:|---:|---:|
| S01 | 5 | 0 | 5 |
| S02 | 5 | 3 | 8 |
| S03 | 4 | 19 | 23 |
| S04 | 8 | 0 | 8 |
| S05 | 5 | 14 | 19 |
| S06 | 4 | 16 | 20 |
| S07 | 5 | 8 | 13 |
| S08 | 8 | 0 | 8 |
| S09 | 5 | 0 | 5 |

All declared counts match independent recomputation. All ordinary totals satisfy 0–8. Currency is explicitly US$ wherever amounts appear. No readable additional photo text was apparent at the inspected display sizes.

## Corrections independently rechecked

- **VR-01 CLOSED:** S04 marker now starts y=290; heading line box ends y=254.4, leaving 35.6 logical px. Revised English labels and reveals have no collision
- **VR-02 CLOSED:** S01 rationale now identifies the authentic 2023 founder photograph and the left-photo/right-question composition
- **VR-03 CLOSED:** `assets/CREDITS.txt` now states proportional fit-contain resizing, no crop/recolor/mirroring/generative edits, with photographer/copyright/source/license retained. No credit controls or panels appear on the canvas
- **VR-04 CLOSED for active rendering:** `render_static.py` fails explicitly when the approved photograph is absent; no logo fallback remains. The obsolete logo renderer still exists in scratch and is excluded from publication per the parent; the eventual published manifest is not tested here
- **VR-05 CLOSED:** both S04 arrows carry `width=3`; the active path renderer uses that per-object width. Rendered arrows are subordinate and legible

## Geometry and downstream limits

The inspected English frames have clear hierarchy, complete labels/numerals, safe margins and no clipping, overlap, distorted imagery or misleading proportional encoding. The bounds report contains no out-of-safe-area glyphs. S03 at 1280×800 preserves a centered 16:9 stage with paper letterboxing. No navigation chrome or exposed controls appears. Thai on-canvas glyph QA no longer applies to this owner-selected English canvas; the Thai narration remains the semantic reference.

Browser font metrics, actual transitions, keyboard/pointer behavior, indefinite holds, reduced motion, performance, offline loading, delivered archive identity, Windows launchers and owner rehearsal remain downstream tests. This report asserts no browser/runtime or QA_PASS result.
