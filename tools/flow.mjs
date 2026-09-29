// Interaction smoke test. Usage: node tools/flow.mjs <baseUrl>
import { chromium } from 'playwright-core';
const base = process.argv[2] || 'http://localhost:4173';
const ORDER = ['cover', 'demand', 'retained', 'models', 'statements', 'capacity', 'scenarios', 'filing', 'close'];
const browser = await chromium.launch({ channel: 'msedge', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const page = await (await browser.newContext({ viewport: { width: 1600, height: 900 } })).newPage();
const errs = [];
page.on('console', (m) => { if (m.type() === 'error') errs.push(m.text()); });
page.on('pageerror', (e) => errs.push('PAGEERROR ' + e.message));
let fails = 0;
const ok = (c, msg) => { console.log((c ? 'PASS ' : 'FAIL ') + msg); if (!c) fails++; };
const scene = () => page.evaluate(() => document.body.dataset.scene);
const settle = () => page.waitForFunction(() => document.body.dataset.busy === 'false' && document.body.dataset.scene, null, { timeout: 8000 });

await page.goto(base + '/?dir=a');
await settle();
ok((await scene()) === 'cover', 'loads on cover');

// Space walks the whole route, one stop per press.
for (let i = 1; i < ORDER.length; i++) {
  await page.keyboard.press('Space');
  await settle();
  ok((await scene()) === ORDER[i], `Space -> ${ORDER[i]}`);
}
await page.keyboard.press('Space');
await page.waitForTimeout(400);
ok((await scene()) === 'close', 'Space on close does not loop');

// Restart via on-screen target.
await page.click('#primary');
await settle();
ok((await scene()) === 'cover', 'Restart button -> cover');

// Rapid space presses: exactly one advance, no skipped stops.
for (let i = 0; i < 6; i++) await page.keyboard.press('Space');
await settle();
ok((await scene()) === 'demand', 'six rapid Space presses settle on demand (one advance)');

// Primary click destinations.
for (let i = 1; i < ORDER.length - 1; i++) {
  await page.click('#primary');
  await settle();
  ok((await scene()) === ORDER[i + 1], `primary click on ${ORDER[i]} -> ${ORDER[i + 1]}`);
}
await page.keyboard.press('r');
await settle();
ok((await scene()) === 'cover', 'R returns to cover');

// R in the middle of a transition.
await page.keyboard.press('Space');
await page.waitForTimeout(300);
await page.keyboard.press('r');
await settle();
ok((await scene()) === 'cover', 'R mid-transition settles on cover');

// Overlay: open, Space does not advance, Escape closes and stays.
await page.keyboard.press('Space'); await settle();
await page.click('#btn-src');
ok(await page.isVisible('#overlay'), 'sources overlay opens');
ok((await page.locator('#ov-list li').count()) >= 2, 'overlay lists sources');
ok((await page.locator('#ov-list a[href^="https://"]').count()) >= 2, 'overlay has direct source links');
await page.keyboard.press('Space');
await page.waitForTimeout(300);
ok((await scene()) === 'demand', 'Space inside overlay does not advance');
await page.keyboard.press('Escape');
ok(!(await page.isVisible('#overlay')), 'Escape closes overlay');
ok((await scene()) === 'demand', 'still on same scene after overlay');
await page.click('#btn-src');
await page.keyboard.press('r'); await settle();
ok(!(await page.isVisible('#overlay')) && (await scene()) === 'cover', 'R from overlay closes it and returns to cover');

// Scenario selectors keep the scene.
await page.goto(base + '/?scene=scenarios'); await settle();
await page.click('.seg button:has-text("Downside")');
ok((await scene()) === 'scenarios', 'scenario select stays on scenarios');
ok((await page.textContent('.aux-note')).includes('Downside'), 'scenario explanation shown');
ok((await page.getAttribute('.seg button:has-text("Downside")', 'aria-pressed')) === 'true', 'scenario pressed state exposed');
await page.click('#primary'); await settle();
ok((await scene()) === 'filing', 'scenarios gate -> filing');
await page.click('.seg button:has-text("3 Commitments")');
ok((await scene()) === 'filing' && (await page.textContent('.aux-note')).includes('Annual schedule'), 'filing gate note opens and stays');

// Models toggle does not advance.
await page.goto(base + '/?scene=models'); await settle();
await page.click('.seg button:has-text("Opus 5.5")');
ok((await scene()) === 'models', 'model toggle stays on models');
ok((await page.textContent('.lbl.detail')).includes('Opus 5.5'), 'model detail updates');

// Direct 3D click on the door target on cover.
await page.goto(base + '/?scene=cover'); await settle();
await page.mouse.click(800, 450);
await settle();
ok((await scene()) === 'demand', 'clicking the 3D doorway advances to demand');

// Owner feedback: no persistent bottom rail/dots/hint; discreet Scenes menu instead.
await page.goto(base + '/?scene=demand'); await settle();
ok((await page.locator('#rail').count()) === 0 && (await page.locator('.hint').count()) === 0, 'no scene dots or bottom hint in the DOM');
await page.click('#btn-menu');
ok(await page.isVisible('#menu'), 'Scenes menu opens');
ok((await page.locator('#menu-list button').count()) === 9, 'Scenes menu lists nine stops');
await page.keyboard.press('Space');
await page.waitForTimeout(300);
ok((await scene()) === 'demand', 'Space inside menu does not advance');
await page.keyboard.press('Escape');
ok(!(await page.isVisible('#menu')) && (await scene()) === 'demand', 'Escape closes menu, scene unchanged');
await page.click('#btn-menu');
await page.click('#menu-list button:has-text("Statements")'); await settle();
ok((await scene()) === 'statements', 'Scenes menu jumps to statements');

// QA-06: Fable / Mythos availability stated distinctly on models; QA-07: AWS badge.
await page.goto(base + '/?scene=models'); await settle();
const lbls = await page.locator('#labels').innerText();
ok(/Fable 5\.1[^]*generally available/.test(lbls) && /Mythos 5\.1[^]*trusted access/.test(lbls), 'models shows Fable generally available and Mythos trusted access');
await page.click('#btn-src');
ok((await page.locator('#ov-list').innerText()).includes('trusted access'), 'models overlay caveat covers Mythos trusted access');
await page.keyboard.press('Escape');
await page.goto(base + '/?scene=cover'); await settle();
await page.click('#btn-src');
const cov = await page.locator('#ov-list li').first().innerText();
ok(/SOURCE: AWS/i.test(cov) && !/ANTHROPIC STATED/i.test(cov), 'AWS Rainier source has an AWS badge, not Anthropic stated');
await page.keyboard.press('Escape');

// Reduced motion: same destinations.
const rm = await (await browser.newContext({ viewport: { width: 1600, height: 900 }, reducedMotion: 'reduce' })).newPage();
await rm.goto(base + '/?scene=cover');
await rm.waitForFunction(() => document.body.dataset.scene);
for (let i = 1; i < ORDER.length; i++) {
  await rm.keyboard.press('Space');
  await rm.waitForFunction((id) => document.body.dataset.scene === id, ORDER[i], { timeout: 3000 }).catch(() => {});
}
ok((await rm.evaluate(() => document.body.dataset.scene)) === 'close', 'reduced motion reaches close via Space');

ok(errs.length === 0, 'no console errors' + (errs.length ? ': ' + errs.slice(0, 3).join(' | ') : ''));
await browser.close();
console.log(fails ? `\n${fails} FAILED` : '\nALL PASSED');
process.exit(fails ? 1 : 0);
