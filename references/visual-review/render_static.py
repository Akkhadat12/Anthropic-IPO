import json,pathlib,re,math
from PIL import Image,ImageDraw,ImageFont,ImageOps
from fontTools.ttLib import TTFont
from io import BytesIO
R=pathlib.Path(__file__).resolve().parents[2];O=R/'references/visual-review';O.mkdir(exist_ok=True);sc=json.loads((R/'references/visual-scenes.json').read_text());issues=[];bounds=[]
fnt=TTFont(R/'assets/fonts/NotoSans-Subset.woff');fnt.flavor=None;buf=BytesIO();fnt.save(buf);FONT_BYTES=buf.getvalue()
def line(d,pts,fill,width=4,dash=False):
 if not dash:d.line(pts,fill=fill,width=width);return
 for a,b in zip(pts,pts[1:]):
  dx=b[0]-a[0];dy=b[1]-a[1];L=math.hypot(dx,dy)
  for i in range(0,int(L),22):
   p=i/L;q=min(i+12,L)/L;d.line([(a[0]+dx*p,a[1]+dy*p),(a[0]+dx*q,a[1]+dy*q)],fill=fill,width=width)
def path(d,st,col,width=4):
 ts=re.findall(r'[MLCZ]|-?\d+(?:\.\d+)?',st);i=0;cur=(0,0);start=cur
 while i<len(ts):
  cmd=ts[i];i+=1
  if cmd=='M':cur=(float(ts[i]),float(ts[i+1]));start=cur;i+=2
  elif cmd=='L':new=(float(ts[i]),float(ts[i+1]));line(d,[cur,new],col,width);cur=new;i+=2
  elif cmd=='C':
   c1=(float(ts[i]),float(ts[i+1]));c2=(float(ts[i+2]),float(ts[i+3]));new=(float(ts[i+4]),float(ts[i+5]));pts=[]
   for k in range(41):
    t=k/40;u=1-t;pts.append((u**3*cur[0]+3*u*u*t*c1[0]+3*u*t*t*c2[0]+t**3*new[0],u**3*cur[1]+3*u*u*t*c1[1]+3*u*t*t*c2[1]+t**3*new[1]))
   line(d,pts,col,width);cur=new;i+=6
  elif cmd=='Z':line(d,[cur,start],col,width);cur=start
for s in sc:
 for beat in range(len(s['beats'])):
  im=Image.new('RGB',(1920,1080),'#F5F1E8');d=ImageDraw.Draw(im)
  for o in s['objects']:
   if o['beat']>beat:continue
   ty=o['type']
   if ty=='text':
    f=ImageFont.truetype(BytesIO(FONT_BYTES),o['size'],layout_engine=ImageFont.Layout.RAQM)
    w=d.textlength(o['copy'],font=f);x=o['x']-({'center':w/2,'right':w}.get(o['align'],0));y=o['y']
    bb=d.textbbox((x,y),o['copy'],font=f,anchor='lt');d.text((x,y),o['copy'],font=f,fill=o['color'],anchor='lt')
    rec=dict(scene=s['id'],beat=beat,id=o['id'],bbox=bb,linebox=[x,y,x+w,y+o['size']*1.45]);bounds.append(rec)
    if bb[0]<96 or bb[1]<54 or bb[2]>1824 or bb[3]>1026:issues.append(rec)
   elif ty=='asset':
    p=R/'assets/photos/dario-amodei-techcrunch-2023.jpg'
    assert p.exists(), 'Authentic licensed photograph missing; do not substitute a logo'
    a=Image.open(p).convert('RGB')
    a=ImageOps.contain(a,(o['w'],o['h']));x=o['x']+(o['w']-a.width)//2;y=o['y']+(o['h']-a.height)//2;im.paste(a,(x,y),a if a.mode=='RGBA' else None)
   elif ty=='rect':
    x,y,w,h=[o[k] for k in ['x','y','w','h']];line(d,[(x,y),(x+w,y),(x+w,y+h),(x,y+h),(x,y)],o['stroke'],dash=bool(o.get('dash')))
   elif ty=='line':line(d,[(o['x1'],o['y1']),(o['x2'],o['y2'])],o['stroke'],dash=bool(o.get('dash')))
   elif ty=='path':path(d,o['d'],o['stroke'],o.get('width',4))
  im.save(O/f'{s["id"]}-b{beat}.png')
 for wh in [(1280,720),(1280,800)]:
  fit=ImageOps.contain(im,wh);frame=Image.new('RGB',wh,'#F5F1E8');frame.paste(fit,((wh[0]-fit.width)//2,(wh[1]-fit.height)//2));frame.save(O/f'{s["id"]}-final-{wh[0]}x{wh[1]}.png')
 sheet=Image.new('RGB',(1440,900),'white');dr=ImageDraw.Draw(sheet)
for i,s in enumerate(sc):
 a=Image.open(O/f'{s["id"]}-b{len(s["beats"])-1}.png').resize((480,270));sheet.paste(a,((i%3)*480,(i//3)*300));dr.text(((i%3)*480+12,(i//3)*300+277),s['id'],fill='black')
sheet.save(O/'contact-sheet.png');(O/'bounds-check.json').write_text(json.dumps({'renderer':'Pillow RAQM with pinned Noto Sans variable, not browser runtime','bounds':bounds,'out_of_safe_area':issues},ensure_ascii=False,indent=2));print(json.dumps(issues,ensure_ascii=False,indent=2))
