import pathlib,json,hashlib,re
from fontTools.ttLib import TTFont
from PIL import Image,ImageOps,ImageDraw
R=pathlib.Path(__file__).resolve().parents[2];S=json.loads((R/'references/visual-scenes.json').read_text());M=json.loads((R/'assets/manifest.json').read_text());C={}
C['scope']='Static specification, licensed asset identity and Pillow RAQM endpoint concepts; not browser/runtime/package QA'
C['on_canvas_language']='English by explicit owner decision';C['narration_language']='Thai unchanged'
C['scene_ids']=[s['id'] for s in S];C['beats']=sum(len(s['beats']) for s in S);C['editorial_seconds']=sum(s['seconds'] for s in S)
C['copy_counts']={s['id']:[s['ordinary_count'],s['excluded_count'],s['total_count']] for s in S};C['all_ordinary_le_8']=all(s['ordinary_count']<=8 for s in S)
C['no_Thai_canvas']=all(not re.search('[\u0e00-\u0e7f]',o['copy']) for s in S for o in s['objects'] if o['type']=='text')
C['sequential_beats']=all([b['index'] for b in s['beats']]==list(range(len(s['beats']))) for s in S)
fonts={}
for f in M['fonts']:
 C[f['id']+'_hash']=hashlib.sha256((R/f['path']).read_bytes()).hexdigest()==f['sha256'];fonts[f['id']]=TTFont(R/f['path']).getBestCmap();C[f['id']+'_OFL_hash']=hashlib.sha256((R/f['license_path']).read_bytes()).hexdigest()==f['license_sha256']
chars=set(''.join(o['copy'] for s in S for o in s['objects'] if o['type']=='text'));C['missing_English_glyphs']=[x for x in chars if ord(x) not in fonts['F02'] and not x.isspace()]
for a in M['photos']:C[a['id']+'_hash']=hashlib.sha256((R/a['path']).read_bytes()).hexdigest()==a['sha256'];C[a['fallback_id']+'_hash']=hashlib.sha256((R/a['fallback_path']).read_bytes()).hexdigest()==a['fallback_sha256']
C['bounds_violations']=json.loads((R/'references/visual-review/bounds-check.json').read_text())['out_of_safe_area'];C['browser']='NOT_RUN: Chromium launch failed before page creation with executor socket restriction';C['package_Windows']='NOT_RUN: Build has not started'
O=R/'references/visual-review';(O/'static-checks.json').write_text(json.dumps(C,ensure_ascii=False,indent=2));ImageOps.grayscale(Image.open(O/'contact-sheet.png')).save(O/'contact-sheet-grayscale.png')
im=Image.open(O/'S01-b0.png');d=ImageDraw.Draw(im);x,y=620,360
d.ellipse((x-10,y-10,x+10,y+10),fill='#202722');d.ellipse((x-9,y-9,x+9,y+9),fill='#F5F1E8');d.ellipse((x-7,y-7,x+7,y+7),fill='#354F91');im.save(O/'S01-pointer-static.png')
print(json.dumps(C,ensure_ascii=False,indent=2))
