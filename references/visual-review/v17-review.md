# Independent v1.7 migration supplement

Reviewed 2026-10-01 06:08 UTC. **PASS — bounded language, exact-master and optimized-asset metadata consistency review.** This supplements `independent-review.md`; it does not repeat or expand the original static geometry review and is not browser/runtime/package QA.

## Scope and identity

Reviewed the actual root-level `01_CONTENT.md` through `05_QA.md`, their live project sections and retained master suffixes, current scene language fields, current asset manifest/credits/rights summary/CSS and local derivative binaries.

- `references/visual-scenes.json` SHA-256: `2a6fbd71caaa910cbfcfec6934c48018f4b984bee27a5156ac22e3d356cdd45d`
- `assets/manifest.json` SHA-256: `451a6fed8b7a704286c36941624f89c6dcb0c77d0b57853d1af6f0b74112b60f`
- `assets/fonts/fonts.css` SHA-256: `2fa0c66dc8df7bc9afe6b94cd7b42abccb34e8b51bfac0491cb8b5e93ba0435f`

## Checks passed

1. **Exact masters:** all five files end with the exact corresponding current v1.7 master text supplied for comparison. No suffix edits or silent requirement weakening were found. AC-024 remains a required future package test.
2. **Language:** live specs consistently select English for audience-facing canvas, semantic descriptions, alternative text and app-authored fallback/error text, with document `lang=en`. Thai remains appropriate for narration, presenter cues, owner reading editions/rationale and quick-start. Every scene supplies English semantic/alt/fallback fields and a LANGUAGE_AUDIT; no Thai characters or missing fields were found in these audience-facing fields or rendered copy.
3. **Fallback/count separation:** fallback messages are explicitly semantic/accessibility status only, not new visible canvas copy. Normal visual fallback reuses the existing text and same-source photo. A double image failure remains a defect. Thus the previously reviewed visible-copy ledger is unchanged; the new accessibility strings are language-audited without being silently added to the canvas.
4. **Current counts:** S01–S09 ordinary/excluded/total remain respectively 5/0/5, 5/3/8, 4/19/23, 8/0/8, 5/14/19, 4/16/20, 5/8/13, 8/0/8, 5/0/5. These are the approved English normal-state inventories.
5. **Optimized photo:** actual runtime image is 1200×800 RGB JPEG, 88,148 bytes. SHA-256 `395a3bc4b0e4ccaae1d3c6cb05e1aa39d10bb235288335551e91a67ab8289a2e` matches the current manifest. Runtime SHA-1 is separately recorded from original-source SHA-1. Credits/rights summary now distinguish the derivative from the original 4000×2667 source and describe proportional resize with no crop. This was metadata/binary verification, not a repeat license determination.
6. **Font derivatives:** both WOFF byte sizes/hashes, source-TTF hashes and bundled OFL hashes match the manifest. Both subsets cover every current canvas character. Retained Unicode glyph advances, units-per-em and horizontal/vertical line metrics agree with the originals. Instantiated weight 400 and 600 at width 100 also have zero decomposed glyph-outline or advance differences for all retained characters. Variable axes remain present. These checks do not establish browser font loading or shaping behavior.
7. **Font routing:** current CSS references the subset WOFF files; current manifest and Visual prose describe WOFF derivatives of immutable-source variable TTFs. No runtime network font dependency is introduced.

## Corrections found and closed during this review

- Replaced the residual Design examples of Thai on-canvas approximation words with “Nearly” and “About”
- Corrected CSS references from stale TTF/old-manifest paths to the current WOFF derivatives/manifest
- Corrected the rights summary's stale original-image dimensions and obsolete optional 4:5 crop statement
- Separated original-photo checksum evidence from runtime-derivative checksums
- Corrected the Visual asset paragraph's stale “variable TTFs” description
- Made the English fallback display policy explicit so its accessibility strings are not uncounted visible scene text

No remaining contradictory Thai-on-canvas instruction was identified in the reviewed live specifications. Thai working prose and narrator/owner-document content are not violations. The obsolete research assets, stale alternative manifests and unused generators are outside the current canonical manifest and must remain excluded from the eventual publication/package.

## Limits

No redesign, nine-scene geometry re-review, new source-fact audit, rendered-browser test, asset-failure exercise, screen-reader test, reduced-motion/input/pointer/hold check, ZIP identity test or Windows execution was performed. Final runtime must independently verify the shipped WOFFs/photo, exact language separation and all AC-024 states. This supplement does not assert QA_PASS or COMPLETE.
