#!/usr/bin/env python3
"""Deterministic static build; only Python standard library; no downloads."""
import pathlib,json,html,shutil,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
def build():
 if OUT.exists():shutil.rmtree(OUT)
 OUT.mkdir()
 scenes=json.loads((ROOT/'references/visual-scenes.json').read_text())
 manifest=json.loads((ROOT/'assets/manifest.json').read_text())
 paths=['assets/CREDITS.txt']
 for item in manifest['photos']+manifest['fonts']:
  path=item['path'];assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==item['sha256'],path
  paths.append(path)
  if 'fallback_path'in item:paths.append(item['fallback_path'])
  if 'license_path'in item:paths.append(item['license_path'])
 for path in paths:
  dst=OUT/path;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/path,dst)
 shutil.copyfile(ROOT/'src/style.css',OUT/'style.css')
 state=(ROOT/'src/state.mjs').read_text().replace('export ','')
 app=(ROOT/'src/app.mjs').read_text().split('\n',1)[1]
 (OUT/'app.js').write_text("'use strict';\n(()=>{\n"+state+'\n'+app+'\n})();\n')
 esc=lambda x:html.escape(str(x),quote=True)
 sections=[]
 for i,s in enumerate(scenes):
  objects=[]
  for o in s['objects']:
   attrs=f'data-object="{esc(o["id"])}" data-beat="{o["beat"]}"'+(' hidden' if o['beat'] else '')
   t=o['type']
   if t=='text':
    transform={'left':'none','center':'translateX(-50%)','right':'translateX(-100%)'}[o['align']]
    objects.append(f'<div class="object text" {attrs} style="left:{o["x"]}px;top:{o["y"]}px;font-size:{o["size"]}px;color:{o["color"]};transform:{transform}">{esc(o["copy"])}</div>')
   elif t=='asset':objects.append(f'<img class="object photo" {attrs} src="./assets/photos/dario-amodei-techcrunch-2023.jpg" data-fallback="./assets/photos/dario-amodei-techcrunch-2023-fallback.jpg" alt="{esc(s["alt_text_en"])}" width="{o["w"]}" height="{o["h"]}" style="left:{o["x"]}px;top:{o["y"]}px">')
   else:
    keys={'rect':['x','y','w','h'],'line':['x1','y1','x2','y2'],'path':['d']}[t]
    geometry=' '.join(f'{dict(w="width",h="height").get(k,k)}="{esc(o[k])}"'for k in keys)
    objects.append(f'<svg class="object shape" aria-hidden="true" {attrs} viewBox="0 0 1920 1080"><{t} {geometry} fill="none" stroke="{o.get("stroke","#202722")}" stroke-width="{o.get("width",4)}" stroke-dasharray="{o.get("dash","")}"/></svg>')
  sections.append(f'<section class="scene" id="{s["id"]}" data-beats="{len(s["beats"])}" data-description="{esc(s["semantic_description_en"])}" aria-label="{esc(s["takeaway"])}"'+(' hidden aria-hidden="true"'if i else ' aria-hidden="false"')+'>'+''.join(objects)+'</section>')
 content='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>Anthropic: Growth and Sustainable Profits</title><link rel="icon" href="data:,"><link rel="preload" href="./assets/fonts/NotoSans-Subset.woff" as="font" type="font/woff" crossorigin><link rel="preload" href="./assets/photos/dario-amodei-techcrunch-2023.jpg" as="image"><link rel="stylesheet" href="./style.css"><style>:root{--scale:min(calc(100vw / 1920px),calc(100vh / 1080px))}</style></head><body><main id="frame"><div id="stage" role="region" aria-label="Anthropic presentation">'+''.join(sections)+'</div></main><div id="pointer" aria-hidden="true" hidden></div><div id="status" class="sr-only" role="status" aria-live="polite" aria-atomic="true"></div><noscript><p class="sr-only">JavaScript is required for presentation controls.</p></noscript><script defer src="./app.js"></script></body></html>'
 (OUT/'index.html').write_text(content,encoding='utf-8')
 print(json.dumps({'output':'dist','scenes':len(scenes),'endpoints':sum(len(s['beats'])for s in scenes),'files':len(list(OUT.rglob('*')))}))
if __name__=='__main__':build()
