// Usage: node tools/shot.mjs <baseUrl> <outDir> [dirs=a,b] [scenes=all]
import { chromium } from 'playwright-core';
const [base, out = 'qa-shots', dirs = 'a', scenesArg = 'all'] = process.argv.slice(2);
const ORDER = ['cover','demand','retained','models','statements','capacity','scenarios','filing','close'];
const scenes = scenesArg === 'all' ? ORDER : scenesArg.split(',');
const vps = { desk: { width: 1920, height: 1080 }, phone: { width: 390, height: 844 } };
const browser = await chromium.launch({ channel: 'msedge', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
for (const dir of dirs.split(',')) for (const [vn, vp] of Object.entries(vps)) {
  const ctx = await browser.newContext({ viewport: vp, deviceScaleFactor: 1, hasTouch: vn === 'phone' });
  const page = await ctx.newPage();
  const errs = [];
  page.on('console', m => { if (['error','warning'].includes(m.type())) errs.push(m.text()); });
  page.on('pageerror', e => errs.push('PAGEERROR ' + e.message));
  for (const s of scenes) {
    await page.goto(`${base}/?dir=${dir}&scene=${s}`);
    await page.waitForFunction(() => document.body.dataset.scene, null, { timeout: 15000 });
    await page.waitForTimeout(600);
    await page.screenshot({ path: `${out}/${dir}-${vn}-${s}.png` });
  }
  if (errs.length) console.log(dir, vn, 'console:', [...new Set(errs)].slice(0, 6));
  await ctx.close();
}
await browser.close();
console.log('done');
