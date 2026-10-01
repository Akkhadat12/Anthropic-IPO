#!/usr/bin/env python3
"""Builder verification only. Requires already extracted package/helper URL.
Never awards independent QA_PASS. Writes evidence outside the source checkout.
"""
import argparse,json,pathlib,time
from playwright.sync_api import sync_playwright
p=argparse.ArgumentParser();p.add_argument('--url',required=True);p.add_argument('--output',required=True);a=p.parse_args();O=pathlib.Path(a.output);O.mkdir(parents=True,exist_ok=True)
report={'scope':'Builder extracted-package browser check; not independent QA','url':a.url,'checks':[],'errors':[],'requests':[]}
with sync_playwright()as pw:
 b=pw.chromium.launch(headless=True);report['browser']=b.version
 page=b.new_page(viewport={'width':1920,'height':1080});page.on('pageerror',lambda e:report['errors'].append(str(e)));page.on('request',lambda r:report['requests'].append(r.url))
 # Block all external runtime requests. Loopback target is the only permitted origin.
 from urllib.parse import urlsplit
 origin=urlsplit(a.url);allowed=f'{origin.scheme}://{origin.netloc}'
 page.route('**/*',lambda route:route.continue_()if route.request.url.startswith(allowed+'/')else route.abort())
 start=time.perf_counter();page.goto(a.url);page.evaluate('document.fonts.ready');report['ready_ms']=(time.perf_counter()-start)*1000
 assert page.locator('html').get_attribute('lang')=='en';assert page.locator('#stage').get_attribute('data-scene')=='S01'
 assert page.locator('#S01 img').evaluate('(e)=>e.complete&&e.naturalWidth===1200')
 endpoints=[];counts=[1,2,3,3,3,3,2,3,3]
 for i,count in enumerate(counts):
  for beat in range(count):
   expected=f'S{i+1:02}';page.wait_for_function("document.querySelector('#stage').dataset.phase==='hold'")
   actual=page.locator('#stage').evaluate('(e)=>({...e.dataset})');assert actual['scene']==expected and int(actual['beat'])==beat,actual
   assert not page.locator('.scene:not([hidden]) .text').evaluate_all("es=>es.filter(e=>!e.hidden).some(e=>/[\\u0e00-\\u0e7f]/.test(e.textContent))")
   bounds=page.locator('.scene:not([hidden]) .text:not([hidden])').evaluate_all('(es)=>es.map(e=>{const r=e.getBoundingClientRect();return {text:e.textContent,x:r.x,y:r.y,right:r.right,bottom:r.bottom}})')
   assert all(x['x']>=96 and x['y']>=54 and x['right']<=1824 and x['bottom']<=1026 for x in bounds),bounds
   page.screenshot(path=str(O/f'{expected}-b{beat}.png'));endpoints.append(actual)
   if beat==count-1:
    before=page.screenshot();page.wait_for_timeout(30000);assert page.screenshot()==before,'hold changed';assert page.locator('#stage').get_attribute('data-phase')=='hold'
   if i!=8 or beat!=count-1:
    page.keyboard.press('Space');page.keyboard.press('Space') # settle only active transition/reveal
 assert len(endpoints)==23
 page.keyboard.press('Space');assert page.locator('#stage').get_attribute('data-scene')=='S09'
 page.keyboard.press('r');assert page.locator('#stage').get_attribute('data-scene')=='S01'
 page.keyboard.press('Space');page.keyboard.press('r');page.wait_for_timeout(1100);assert page.locator('#stage').get_attribute('data-scene')=='S01'
 for w,h in [(1280,720),(1280,800)]:
  page.set_viewport_size({'width':w,'height':h});page.screenshot(path=str(O/f'cover-{w}x{h}.png'));r=page.locator('#frame').bounding_box();assert abs(r['width']/r['height']-16/9)<0.001
  assert page.evaluate('document.documentElement.scrollWidth===innerWidth&&document.documentElement.scrollHeight===innerHeight')
 page.mouse.move(400,350);assert page.locator('#pointer').is_visible();r=page.locator('#pointer').bounding_box();assert abs(r['x']+7-400)<.1 and abs(r['y']+7-350)<.1 and r['width']==14
 page.keyboard.press('r');assert page.locator('#pointer').is_visible();page.mouse.move(0,0);assert not page.locator('#pointer').is_visible()
 page.emulate_media(reduced_motion='reduce');page.keyboard.press('r')
 for i,count in enumerate(counts):
  for beat in range(count):
   assert page.locator('#stage').get_attribute('data-phase')=='hold'
   assert page.locator('#stage').get_attribute('data-scene')==f'S{i+1:02}'
   if i!=8 or beat!=count-1:page.keyboard.press('Space')
 # Primary failure uses byte-identical fallback; both failure produces semantic status only.
 page.route('**/dario-amodei-techcrunch-2023.jpg',lambda r:r.abort());page.reload();assert page.locator('#S01 img').evaluate('(e)=>e.complete&&e.naturalWidth===1200');assert page.locator('#S01 img').get_attribute('data-fallback-used')=='true'
 page.route('**/dario-amodei-techcrunch-2023-fallback.jpg',lambda r:r.abort());page.reload();page.wait_for_function("document.querySelector('#S01 img').dataset.failed==='true'");assert 'Image unavailable' in page.locator('#status').inner_text()
 assert not report['errors'],report['errors'];assert all(url.startswith(allowed+'/')for url in report['requests'])
 report.update(result='PASS_BUILDER_BROWSER_CHECK',endpoints=endpoints,hold_seconds_per_scene=30,windows='NOT_RUN',performance_target='ready <2000ms on recorded test host; observed separately',performance_target_met=report['ready_ms']<2000)
 b.close()
(O/'browser-check.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
