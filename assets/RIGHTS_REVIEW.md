# Anthropic visual asset verification

Status: READY FOR BUILD using the licensed Dario photograph plus OFL fonts. Logos are NOT CLEARED.

## Chosen cover photograph

`photos/dario-amodei-techcrunch-2023.jpg` is the 1200 × 800 optimized JPEG derivative of the verified original 4000 × 2667 Wikimedia Commons image. Commons identifies Dario Amodei at TechCrunch Disrupt 2023 on 20 September 2023. The original downloaded source SHA-1 matched Commons. Runtime derivative SHA-1/SHA-256 are distinct and separately recorded. The originating TechCrunch Flickr page still links CC BY 2.0; Commons records a successful historical license review. The actual photographer and copyright parties are retained in `CREDITS.txt` and the manifest, including Kimberly White, Getty Images for TechCrunch, and © 2023 Getty Images.

CC BY 2.0 permits reproduction and adaptation with attribution. Supply title, creator/provider, copyright notice, source link, license link, and a statement of changes. Keep credits with the complete delivered package and in an accessible accompanying credits view. Section 4(c) permits reasonable credit placement and requires comparable authorship credits to have comparable prominence. This permits a full accompanying credits panel rather than insisting on the complete credit inside an eight-word slide; a standalone slide/image must travel with the credit. Do not rely on a hidden manifest that recipients cannot find. Use an explicit credits link in README_TH and the owner rationale, plus an easily found package-root CREDITS file. Do not add a credits control or panel to the recording canvas. Attribution availability is a build acceptance condition.

Use for accurate independent editorial coverage only. Do not imply Anthropic, the subject, or TechCrunch endorses the presentation. CC licenses do not grant publicity or privacy rights. Local internal preview is covered by the copyright grant if attribution is retained. The image shows a real 2023 event; do not present it as depicting a later IPO announcement.

Cropping/resizing is allowed; describe crop/resize in final credit. The supplied runtime image is proportionally resized, uncropped and in original color. No 4:5 crop is currently approved. Fallback: render the independently packaged byte-identical optimized image uncropped, contained within the same frame.

Sources:
- https://commons.wikimedia.org/wiki/File:Dario_Amodei_at_TechCrunch_Disrupt_2023_01.jpg
- https://www.flickr.com/photos/techcrunch/53202070940/
- https://creativecommons.org/licenses/by/2.0/
- https://creativecommons.org/licenses/by/2.0/legalcode.en

## Logo rights blocker

The official newsroom redirects its press-kit download to an Anthropic CDN ZIP. Extracted logos match archive bytes, and SVG dimensions/PNG resolutions and SHA-256 hashes are recorded in `manifest.json`. No license or permission grant was found in the archive. The official Trademark Guidelines require specific permission and prior approval of materials, forbid alterations, require clear/readable placement and reasonable spacing, and prohibit adding trademark symbols. They do not specify numerical clear space or a general private-preview exception. Therefore neither public use nor an internal-use waiver is verified from these terms. Download availability alone is insufficient. Do not embed these logo files into a preview or final artifact under this verification standard. They were inspected locally as provenance research only; they are not included in this repository handoff or runtime package.

If logo use later becomes mandatory, seek specific written permission covering the material and use. The official contact listed is marketing@anthropic.com. Independent legal exceptions may exist; none was assumed or adjudicated here. The Commons/Brandfetch CC0-marked logo was rejected as a substitute because the uploader's authority was not established and trademark issues remain.

Sources:
- https://www.anthropic.com/news
- https://www.anthropic.com/press-kit
- https://www.anthropic.com/legal/trademark-guidelines

## Fonts

Noto Sans 2.015 and Noto Sans Thai 2.002 are OFL-permitted Unicode-subset WOFF derivatives of variable TTFs from the immutable Google Fonts commit recorded in the manifest. Both include native 400 Regular and 600 SemiBold instances at width 100, and both are under SIL OFL 1.1. The bundled OFL files include the required copyright notices. Use local files, width 100, weights 400 or 600, and disable synthetic font styles. No font credit is required on the slide; keep license and copyright notices with redistributed binaries. No online font request is required.

## Checks

- Original and proportionally resized photo inspected visually: true photographic event portrait, no invented logo or reconstruction.
- Binary identity checked against Commons checksum.
- Font axis ranges and 400/600 named instances verified with fontTools.
- Official logo extraction verified byte-for-byte against official ZIP, but permission unresolved.
- Source HTML and license snapshots were checked locally; only source links and verification summaries are handed off, not collected whole-page/archive copies.
