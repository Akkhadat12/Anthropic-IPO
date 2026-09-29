import { chromium } from 'playwright-core';

const base = 'http://127.0.0.1:4174';
const out = 'qa-evidence/screens';
const browser = await chromium.launch({ channel: 'msedge', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const results = [];

for (const [name, viewport] of Object.entries({ desk: { width: 1920, height: 1080 }, phone: { width: 390, height: 844 } })) {
  const context = await browser.newContext({ viewport, hasTouch: name === 'phone' });
  const page = await context.newPage();
  const settled = async (id) => page.waitForFunction((expected) => document.body.dataset.scene === expected && document.body.dataset.busy === 'false', id);
  await page.goto(`${base}/?scene=demand`);
  await settled('demand');
  await page.locator('#btn-src').click();
  await page.screenshot({ path: `${out}/qa-${name}-overlay.png` });
  results.push(`${name}: overlay links=${await page.locator('#ov-list a').count()}`);
  await page.keyboard.press('Escape');
  await page.goto(`${base}/?scene=scenarios`);
  await settled('scenarios');
  for (const option of ['Upside', 'Base', 'Downside']) {
    await page.getByRole('button', { name: option, exact: true }).click();
    const pressed = await page.getByRole('button', { name: option, exact: true }).getAttribute('aria-pressed');
    results.push(`${name}: ${option} selected=${pressed}, scene=${await page.locator('body').getAttribute('data-scene')}`);
    await page.screenshot({ path: `${out}/qa-${name}-scenario-${option.toLowerCase()}.png` });
  }
  await page.goto(`${base}/?scene=cover`);
  await settled('cover');
  await page.locator('#primary').click();
  await page.waitForTimeout(550);
  await page.screenshot({ path: `${out}/qa-${name}-transition.png` });
  await settled('demand');
  results.push(`${name}: cover click -> ${await page.locator('body').getAttribute('data-scene')}`);
  await context.close();
}

await browser.close();
console.log(results.join('\n'));
