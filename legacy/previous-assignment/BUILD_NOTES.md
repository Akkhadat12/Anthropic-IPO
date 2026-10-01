# Build notes — Anthropic IPO presenter

**Date:** 29 September 2026  
**Branch:** `main`  
**Production URL:** https://anthropic-ipo-two-clocks.vercel.app

After the 29 September 2026 QA pass, the clickable Reuters source is the readable StreetInsider syndication of the same 28 September report. The KELO page returned 403 in that review. Scene 3 labels the Sonnet 5.5 “30%” figure as customer API cost in company tests, not Anthropic’s internal compute cost.  
**Site root:** `web/`  
**Evidence recheck:** No public Anthropic, PBC S-1 was returned as the filer in an EDGAR full-text search for “Anthropic, PBC” on Form S-1 / S-1/A from 1 January 2026 through 29 September 2026. Hits were other issuers that mention the phrase. Company browse results were investment funds, not a public Anthropic prospectus. The site therefore keeps the confidential-draft status and the Reuters / Bloomberg / company-statement labels. It does not show a priced or listed IPO.

## Palette comparison

Two directions were rendered in a real browser on Scene 1, which already carried the FY2025 and May 2026 labels, units, and basis lines. Screenshots from that comparison are not shipped inside the site.

| Role | Hall (chosen) | Paper (rejected) |
|---|---|---|
| Stage | `#141816` | `#e7e1d6` |
| Type | `#f3eee6` | `#1b1915` |
| Accent | `#e3a15a` | `#c4622d` |
| Number plate | `#f4efe6` with ink `#1c1915` | `#fffdf8` with ink `#1b1915` |

Hall was chosen because the cream plates and copper accent stay readable against a quiet stage, and the same dark field sits naturally beside the Project Rainier photographs. The paper stage was also legible, but the plates nearly matched the background, so the figures had less separation in a 16:9 recording frame. The alternate rules remain in `web/styles.css` under `html[data-palette="paper"]` and are not applied on the published site.

Loss and the adjusted signal are also distinguished by the words “operating loss”, “Positive”, “adjusted”, and “not GAAP”, not by color alone.

## Images

| File | Scene | Original |
|---|---|---|
| `web/images/project-rainier-interior.png` | Cover | https://assets.aboutamazon.com/7d/36/614bf5354a3a9d570976a3db3a6e/interior-rainier.png via the [AWS Project Rainier article](https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster) |
| `web/images/project-rainier-exterior.png` | Scene 5 | https://assets.aboutamazon.com/50/19/309b104648e1b00c5c7dec3fdc54/projectrainier-exterior.png via the same article |

Both files are the copies stored in `references/`. The exterior uses `object-fit: contain` so the campus is not cropped into a strip or stretched. The cover uses a deliberate cover crop that keeps the aisle, racks, and a person. On-screen text says the hall is an AWS site, not an Anthropic-owned facility.

Chart inputs in `web/chart-data.csv` match `references/chart-data.csv`. Visible figures use only the rows the story compares: FY2025 revenue and operating loss, May 2026 run-rate, Q2 2026 preliminary revenue, the AWS agreement, and the multiyear obligations. February and April run-rates are in the file and are not drawn, so the page does not invent a trend line.

## Material changes from the plan

- Scene 2 uses three different path shapes (straight, stepped, curved), all ending at Paid use. Route buttons change the highlighted path and replay one trip. They do not advance the story and do not encode a share.
- Scene 4 shows the adjusted signal as the word “Positive” with the amount undisclosed. The `>$11.5B` figure is labeled preliminary quarterly revenue, not adjusted income.
- Scene 5 places the work/capacity clocks beside the commitments, not as proportional bars on the dollar amounts. The two amounts are not added.
- Focus rings sit on the individual plates in Scenes 1 and 4 so a keyboard outline does not draw a bridge between unlike bases.
- Sources sits at the top right, outside the cover question. There is no slide rail, timer, or auto-advance.

## Interaction

Space advances one beat from the cover through Scene 6 and does nothing on the closing scene. R returns to the cover. Repeated keys during a transition are ignored. Route and early proof-gate clicks do not advance. The last proof gate, Commitment schedule, opens the closing scene. The closing clocks return to the cover.
