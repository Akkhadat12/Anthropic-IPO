# Visual 1.0 gate review

Date: 2026-10-01 UTC. Incoming Design handoff: 12623fdb09076fec741aa368897923dd9f90eab3; Design artifact aa74da74a0103a59ca7f2d53b2bc180191b55ed2. Scope is Visual planning, verified source assets, and rendered still-state concepts. This is not an application build or an independent runtime/package QA result.

## Result

PASS_VISUAL_SPEC_AND_STATIC_REVIEW. Nine English-canvas scenes / 23 controlled beat endpoints are fully specified. Thai narration is unchanged, confirmed by extraction/hash comparison in upstream-alignment.json. The explicit owner language choice supersedes the earlier Thai copy draft. No financial claim or period changed.

## What was actually checked

- All nine scene plans compared to full narration, claim/source registers and current 02/03/05 requirements
- All nine final stills viewed; full-size representative S01/S03/S04/S05/S06/S07/S08/S09 frames inspected. Independent review checked all nine finals and representative reveals; report is independent-review.md
- All 23 endpoints rendered at 1920×1080 from exact JSON, plus all final states scaled to 1280×720 and 1280×800 paper-letterboxed frames
- Programmatic full glyph-bounds check over all 23 states returned no safe-area violations; complete label tuples appear at their initial data reveal
- Ordinary/excluded/total counts independently recomputed; all ordinary counts 4–8. English-only canvas verified, no Thai string in runtime-copy JSON
- Actual local Noto font/notice hashes checked; no missing glyphs for the final English strings; native 400/600 and width100 source axes verified
- Actual original 4000×2667 photograph inspected, downloaded identity verified against Commons, original Flickr license checked, rights/credit/crop metadata pinned; same-source fallback is byte-identical
- Color contact sheet and grayscale proof inspected: preliminary/outlook and conditional/unanswered distinctions retain explicit labels/line treatment; no color-only fact encoding
- Static pointer-over-photo sample inspected; contrast edges remain visible. This is not a tracking/latency/fullscreen test
- Scoped upstream field alignment: English canvas / Thai narration, authentic founder-photo substitute, actual copy counts. Existing three owner editions, claim register, main/old branches and owner-folder identity preserved

## Corrections made before handoff

1. Rejected official logo because authentic download did not establish a usable permission grant; selected and verified CC BY 2.0 real 2023 founder photo instead
2. Enlarged/relocated cover for left-photo/right-question hierarchy; generic company text, no reconstructed wordmark
3. Replaced abstract S04 lone question mark with explicitly illustrative Work → Worth paying for? → Pay again? dependency sequence, within eight ordinary words
4. Labeled S05 unknown endpoint Cash flow ?, preserving noncash inclusion without a numeric residual
5. Increased S04 label clearance, set its content arrows to 3 px, corrected photo rationale/credit text, and made renderer fail if licensed photo is missing
6. Owner chose English: regenerated all nine scenes/23 states with Noto Sans, recomputed exact counts and retained explicit US$ units, preliminary/outlook distinctions, and no cross-basis scale

Independent review's VR-01..VR-05 are local Visual-review notes, all closed after reinspection. They are not project runtime QA findings and do not pre-allocate QA-001 IDs.

## Evidence and reproducibility

- references/visual-scenes.json: exact objects, English copy tokens, claims, cue beats, rationales and boundaries
- S01-b0.png..S09-b2.png as applicable: individual still endpoints; filenames absent for nonexistent beats are intentional
- contact-sheet.png and contact-sheet-grayscale.png: nine final states; scene IDs are outside each proof panel, never runtime UI
- S01-pointer-static.png: static attention-dot specimen only
- *-final-1280x720.png and *-final-1280x800.png: fitted/letterboxed final proofs
- bounds-check.json, static-checks.json and upstream-alignment.json: measured inventory/hash/geometry results
- render_static.py and check_static.py: reference-only Pillow RAQM proof generator/checker, no presentation app
- assets/manifest.json, assets/RIGHTS_REVIEW.md and assets/CREDITS.txt: source/rights/binary identities

From repository root, with Pillow including RAQM and fontTools available: python references/visual-review/render_static.py; python references/visual-review/check_static.py. These are authoring tools, not end-user prerequisites. Runtime must not depend on Python imaging packages, online fonts or source URLs.

## Explicitly not run

Browser page creation was attempted through local Chromium but failed before launch due to executor socket() restriction; no browser rendering result is claimed. Pillow still proofs do not establish browser font metrics or implemented layout. Actual motion/reduced motion, keyboard/rapid-input/reset, >=30s holds, exact pointer tracking, fullscreen, performance, console/network, asset load-failure, clean-extraction/offline/package/launcher/Windows and owner rehearsal checks are NOT_RUN. Builder and independent QA must perform these against the actual package, not reuse this report as their pass.

## Handoff

Proceed to Agent 4 Builder only after artifact/status publication/readback. Read 01–05, scene JSON, asset manifest/credits and this review. Build the specified local presentation and prebuilt Windows-oriented ZIP, write BUILD_NOTES, verify actual source/archive/Drive identity and create the Thai scene rationale in the existing owner folder. The 9:20 duration remains an editorial estimate until an actual Thai read-through is measured. Public hosting is not requested.

## v1.7 and transport-size amendment

Exact v1.7 master suffixes replace v1.6 in all five files, adding AC-024 and English semantic/alt/fallback rules. No scene geometry or visible text changed. Per-scene LANGUAGE_AUDIT/semantic/alt/fallback metadata is now explicit; diagnostic fallback strings are semantic-only, not additional visible scene copy. The exact original-photo source hash is retained, while the shipped photo is a disclosed uncropped 1200×800 JPEG derivative. OFL-compliant WOFF subsets retain source glyph metrics and are independently hashed. Static proofs were regenerated with those shipped derivatives; no missing glyphs or safe-area violations were found. See v17-review.md and v17-migration.json.

To avoid unnecessarily large evidence uploads, the repository retains contact-sheet.jpg and representative S01/S03/S06 final JPEG proofs, exact all-23 endpoint hashes, and the reproducible static renderer. The large PNG/viewport/grayscale/pointer proofs described above were actually generated and inspected locally; they are regenerated by the committed script and are not all stored as Git blobs. This does not represent them as browser output.
