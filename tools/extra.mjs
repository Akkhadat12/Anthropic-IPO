// Extra retest captures: scenario states, sources overlay, a mid-transition frame, model toggle.
// Usage: node tools/extra.mjs <baseUrl> <outDir>
import { chromium } from 'playwright-core';
const [base, out] = process.argv.slice(2);
const browser = await chromium.launch({ channel: 'msedge', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const vps = { desk: { width: 1920, height: 1080 }, phone: { width: 390, height: 844 } };
for (const [vn, vp] of Object.entries(vps)) {
  const ctx = await browser.newContext({ viewport: vp, hasTouch: vn === 'phone' });
  const page = await ctx.newPage();
  const ready = () => page.waitForFunction(() => document.body.dataset.busy === 'false' && document.body.dataset.scene, null, { timeout: 15000 });
  await page.goto(base + '/?scene=scenarios'); await ready();
  for (const k of ['Upside', 'Base', 'Downside']) {
    await page.click(`.seg button:has-text("${k}")`);
    await page.waitForTimeout(300);
    await page.screenshot({ path: `${out}/qa-${vn}-scenario-${k.toLowerCase()}.png` });
  }
  await page.goto(base + '/?scene=demand'); await ready();
  await page.click('#btn-src'); await page.waitForTimeout(300);
  await page.screenshot({ path: `${out}/qa-${vn}-overlay.png` });
  await page.keyboard.press('Escape');
  await page.goto(base + '/?scene=cover'); await ready();
  await page.keyboard.press('Space'); await page.waitForTimeout(900);
  await page.screenshot({ path: `${out}/qa-${vn}-transition.png` });
  await page.goto(base + '/?scene=models'); await ready();
  await page.click('.seg button:has-text("Opus 5.5")'); await page.waitForTimeout(300);
  await page.screenshot({ path: `${out}/qa-${vn}-models-opus.png` });
  await ctx.close();
}
await browser.close();
console.log('done');
