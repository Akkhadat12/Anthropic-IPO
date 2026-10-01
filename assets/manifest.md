# Runtime asset manifest

Use only the assets listed here. Exact sizes/hashes/source revisions and licensing evidence are in [manifest.json](manifest.json). Local paths are repository-relative and must stay portable in the app package.

| ID | Path | Identity/rights | Display/fallback |
|---|---|---|---|
| A01 | assets/photos/dario-amodei-techcrunch-2023.jpg | Proportionally resized 1200×800 derivative of original 4000×2667 photo, 20 Sep 2023, Kimberly White/Getty Images for TechCrunch, CC BY 2.0 | Uncropped contain in (192,220,840,560), no mirroring/recoloring. Authentic person/event; not IPO-event evidence |
| A01F | assets/photos/dario-amodei-techcrunch-2023-fallback.jpg | Independently packaged, byte-identical licensed photo; same hash/credit | Switch once after primary load failure; preserve same geometry. Both fail = asset error, never generated/logo substitution |
| F01 | assets/fonts/NotoSansThai-Subset.woff | Noto Sans Thai 2.002, OFL1.1 | Native 400/600, width100; retain assets/fonts/NotoSansThai-OFL.txt |
| F02 | assets/fonts/NotoSans-Subset.woff | Noto Sans 2.015, OFL1.1 | Native 400/600, width100; retain assets/fonts/NotoSans-OFL.txt |

## Attribution acceptance condition

Copy [CREDITS.txt](CREDITS.txt) to the package root and link it clearly from README_TH and 06_SCENE_RATIONALE. A separate readable CREDITS.html is allowed, but no credits controls/panel/footer appear on the recording canvas. Any separately exported slide or recording must travel with full credit in an accompanying document/description. Full credit contains title, photographer/provider/copyright, source/license links and the actual no-crop/proportional-resize treatment. Do not imply endorsement. Do not present the 2023 photograph as a 2026 IPO event.

Official company logo files were researched but not cleared, so none are committed or included in the runtime. They are not an emergency fallback. See [RIGHTS_REVIEW.md](RIGHTS_REVIEW.md) for verification and source links. No stock asset purchase, new account permission or public posting is required.
