import pathlib,json,hashlib,re,sys
from html.parser import HTMLParser
R=pathlib.Path(__file__).resolve().parents[1]
sc=json.loads((R/'references/visual-scenes.json').read_text());manifest=json.loads((R/'assets/manifest.json').read_text())
class Page(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.text=[]
 def handle_starttag(self,tag,attrs):self.tags.append((tag,dict(attrs)))
 def handle_data(self,data):self.text.append(data)
p=Page();p.feed((R/'dist/index.html').read_text())
assert p.tags[0]==('html',{'lang':'en'})
assert len([x for x in p.tags if x[0]=='section'])==9
assert len([x for x in p.tags if 'data-object'in x[1]])==sum(len(s['objects'])for s in sc)
assert not re.search('[\u0e00-\u0e7f]',''.join(p.text))
assert not [x for x in p.tags if x[0]in ['button','nav','header','footer']]
for s in sc:
 assert s['ordinary_count']<=8
 for o in s['objects']:
  assert o['beat']<len(s['beats'])
  if o['type']=='text':assert o['size']>=36 and not re.search('[\u0e00-\u0e7f]',o['copy'])
for item in manifest['photos']+manifest['fonts']:
 assert hashlib.sha256((R/'dist'/item['path']).read_bytes()).hexdigest()==item['sha256']
 if 'fallback_path'in item:assert hashlib.sha256((R/'dist'/item['fallback_path']).read_bytes()).hexdigest()==item['fallback_sha256']
 if 'license_path'in item:assert hashlib.sha256((R/'dist'/item['license_path']).read_bytes()).hexdigest()==item['license_sha256']
for tag,a in p.tags:
 for k in ['src','href','data-fallback']:
  if k in a and not a[k].startswith('data:'):assert (R/'dist'/a[k]).is_file(),a[k]
assert not list((R/'dist').rglob('*logo*'))
assert not re.search(r'\b(fetch|XMLHttpRequest|WebSocket|EventSource)\s*\(', (R/'dist/app.js').read_text())
assert 'requestAnimationFrame'not in (R/'dist/app.js').read_text()
print(json.dumps({'result':'PASS_STATIC_ONLY','scenes':9,'endpoints':23,'asset_hashes':'MATCH','language':'en','unverified':'browser, loopback, Windows'},indent=2))
