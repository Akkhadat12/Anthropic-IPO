import pathlib,zipfile,json,hashlib,sys,stat,tempfile
archive=pathlib.Path(sys.argv[1]);expect=sys.argv[2]if len(sys.argv)>2 else None
sha=hashlib.sha256(archive.read_bytes()).hexdigest()
if expect:assert sha==expect
with zipfile.ZipFile(archive)as z:
 names=z.namelist();assert len(names)==len(set(names));roots={x.split('/')[0]for x in names};assert len(roots)==1;root=next(iter(roots))
 for info in z.infolist():
  p=pathlib.PurePosixPath(info.filename);assert not p.is_absolute()and '..'not in p.parts and '\\'not in info.filename;assert not stat.S_ISLNK(info.external_attr>>16);assert info.file_size<20_000_000
 manifest=json.loads(z.read(root+'/manifest.json'))
 assert set(names)=={root+'/manifest.json'}|{root+'/'+p for p in manifest['files']}
 for p,h in manifest['files'].items():assert hashlib.sha256(z.read(root+'/'+p)).hexdigest()==h,p
 assert all(not any(q in p.lower()for q in ['.git/','.env','node_modules','legacy','logo','token','credential'])for p in manifest['files'])
 for p in ['START.bat','STOP.bat','serve.py','README_TH.md','app/index.html','CREDITS.txt']:assert p in manifest['files']
 target=pathlib.Path(tempfile.mkdtemp(prefix='anthropic-extracted-'));z.extractall(target)
print(json.dumps({'result':'PASS_ARCHIVE_IDENTITY_STATIC_ONLY','sha256':sha,'BUILD_COMMIT':manifest['BUILD_COMMIT'],'files':len(names),'extracted':str(target/root),'runtime':'NOT_RUN'},indent=2))
