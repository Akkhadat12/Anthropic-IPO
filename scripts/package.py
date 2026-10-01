#!/usr/bin/env python3
"""Reproducible ZIP from an exact clean committed source. Python standard library."""
import pathlib,json,hashlib,zipfile,subprocess,sys,shutil
from build import build,ROOT
version=sys.argv[1]if len(sys.argv)>1 else '0.1.0-provisional'
if not all(c.isalnum()or c in '.-'for c in version):raise SystemExit('Invalid package version')
commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
if subprocess.check_output(['git','status','--porcelain','--untracked-files=no'],cwd=ROOT,text=True).strip():raise SystemExit('Tracked source must be clean')
build();payload={}
for f in sorted((ROOT/'dist').rglob('*')):
 if f.is_file():payload['app/'+f.relative_to(ROOT/'dist').as_posix()]=f.read_bytes()
for p in ['serve.py','START.bat','STOP.bat','README_TH.md']:
 payload[p]=(ROOT/'delivery'/p).read_bytes()
payload['CREDITS.txt']=(ROOT/'assets/CREDITS.txt').read_bytes()
manifest={'PROJECT_ID':'anthropic-ipo-20261001-0426','PACKAGE_VERSION':version,'BUILD_COMMIT':commit,'LOCAL_RUNTIME':'Python >=3.10 standard library','STATUS':'PROVISIONAL_RUNTIME_NOT_VERIFIED','files':{p:hashlib.sha256(b).hexdigest()for p,b in sorted(payload.items())}}
payload['manifest.json']=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode()
root='anthropic-ipo-'+version
out=ROOT/'delivery'/f'anthropic-ipo-20261001-0426-{version}-local.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
 for p,data in sorted(payload.items()):
  info=zipfile.ZipInfo(root+'/'+p,(2026,10,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;z.writestr(info,data,compresslevel=9)
sha=hashlib.sha256(out.read_bytes()).hexdigest()
evidence={'path':out.name,'root_folder':root,'bytes':out.stat().st_size,'sha256':sha,'BUILD_COMMIT':commit,'PACKAGE_VERSION':version,'manifest':manifest,'windows':'NOT_RUN','browser':'NOT_RUN_BY_ASSEMBLY','loopback':'NOT_RUN_BY_ASSEMBLY'}
(ROOT/'delivery/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(ROOT/'delivery/package-identity.json').write_text(json.dumps(evidence,indent=2)+'\n')
print(json.dumps({k:v for k,v in evidence.items()if k!='manifest'},indent=2))
