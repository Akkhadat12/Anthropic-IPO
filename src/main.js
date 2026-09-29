import * as THREE from 'three';
import { ORDER, SCENES, SRC, STATUS } from './data.js';
import { pickTheme } from './theme.js';
import { buildScenes, SPACING } from './scenes.js';

const theme = pickTheme();
document.documentElement.dataset.dir = theme.id;
document.querySelector('meta[name="theme-color"]').content = '#' + theme.bg.toString(16).padStart(6, '0');

const $ = (id) => document.getElementById(id);
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches || new URLSearchParams(location.search).get('motion') === 'reduced';

// ------------------------------------------------------------------ renderer
const canvas = $('c');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
const scene = new THREE.Scene();
scene.background = new THREE.Color(theme.bg);
scene.fog = new THREE.Fog(theme.bg, theme.fogNear, theme.fogFar);
scene.add(new THREE.HemisphereLight(0xffffff, 0xcfc8b8, theme.ambient));
const key = new THREE.DirectionalLight(0xffffff, theme.key);
key.position.set(-10, 24, 18);
scene.add(key);
const camera = new THREE.PerspectiveCamera(45, 16 / 9, 0.1, 400);

const { scenes, pulses } = buildScenes(theme, ORDER);
ORDER.forEach((id) => scene.add(scenes[id].group));

// ------------------------------------------------------------------ layout
function syncDock() {
  const dock = document.querySelector('.dock');
  document.documentElement.style.setProperty('--dock-h', dock.offsetHeight + 8 + 'px');
}
const labelsEl = $('labels');
let stacked = false;
function layout() {
  const w = innerWidth;
  const h = innerHeight;
  renderer.setSize(w, h, false);
  camera.aspect = w / h;
  stacked = w < 760 || w / h < 0.9;
  labelsEl.classList.toggle('stacked', stacked);
  camera.fov = stacked ? 52 : 45;
  camera.updateProjectionMatrix();
  syncDock();
  if (stacked) camera.setViewOffset(w, h, 0, h * 0.18, w, h);
  else camera.clearViewOffset();
}
addEventListener('resize', layout);

function pose(id) {
  const s = scenes[id];
  const off = s.group.position;
  const a = camera.aspect;
  const k = a >= 1.5 ? 1 : Math.min(3.2, (1.5 / a) * 0.97);
  const look = new THREE.Vector3(...s.cam.look).add(off);
  const pos = new THREE.Vector3(...s.cam.pos).add(off);
  pos.sub(look).multiplyScalar(k).add(look);
  return { pos, look };
}

// ------------------------------------------------------------------ state
let cur = null; // settled scene id
let target = null;
let tr = null;
let revealStart = null;
const camPos = new THREE.Vector3();
const camLook = new THREE.Vector3();
const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
const easeOut = (t) => 1 - Math.pow(1 - t, 3);
const clamp01 = (t) => Math.min(1, Math.max(0, t));

function hideForReveal(s) {
  s.reveal.forEach((r) => {
    if (!r.obj) return;
    r.obj.visible = false;
    r.obj.scale.setScalar(0.001);
  });
}

function showAll(s) {
  s.reveal.forEach((r) => {
    if (!r.obj) return;
    r.obj.visible = true;
    r.obj.scale.copy(r.s0);
  });
}

function setBusy(b) {
  document.body.dataset.busy = String(b);
  $('primary').disabled = b;
}

function goTo(id, opts = {}) {
  if (!ORDER.includes(id)) return;
  unmountUI();
  target = id;
  setBusy(true);
  closeOverlay(true);
  ORDER.forEach((k) => (scenes[k].group.visible = true));
  hideForReveal(scenes[id]);
  pulses.forEach((p) => (p.visible = false));
  revealStart = null;
  const to = pose(id);
  const instant = opts.instant || reduced;
  tr = { t0: performance.now(), dur: instant ? 1 : id === 'cover' ? 2400 : 1900, fromPos: camPos.clone(), fromLook: camLook.clone(), arc: instant ? 0 : Math.min(7, camPos.distanceTo(to.pos) * 0.05) };
  if (instant && cur === null) {
    camPos.copy(to.pos);
    camLook.copy(to.look);
    tr.fromPos.copy(to.pos);
    tr.fromLook.copy(to.look);
  }
  labelsEl.classList.add('hidden');
  document.body.dataset.scene = '';
}

function finish() {
  cur = target;
  tr = null;
  ORDER.forEach((k) => (scenes[k].group.visible = k === cur));
  showAll(scenes[cur]);
  pulses.forEach((p) => (p.visible = p.parent === scenes[cur].group));
  mountUI(cur);
  setBusy(false);
  document.body.dataset.scene = cur;
}

// ------------------------------------------------------------------ UI mount
const primary = $('primary');
function mountUI(id) {
  const s = scenes[id];
  const d = SCENES[id];
  $('kicker').textContent = d.kicker;
  $('line').textContent = d.line;
  primary.textContent = d.primary;
  primary.setAttribute('aria-label', d.primary + (id === 'close' ? '' : '. Goes to ' + SCENES[d.next].kicker));
  labelsEl.replaceChildren();
  const list = [...s.labels].sort((a, b) => a.order - b.order);
  list.forEach((l) => {
    l.el.classList.toggle('fixed-br', l.fixed === 'br');
    labelsEl.appendChild(l.el);
    l.w = 0;
  });
  if (s.aux) s.aux($('aux'));
  if (s.onEnter) s.onEnter();
  labelsEl.classList.remove('hidden');
  syncDock();
  $('live').textContent = d.kicker + '. ' + d.line;
  document.title = 'Anthropic IPO: ' + d.kicker;
  updateRail();
}
function unmountUI() {
  $('aux').replaceChildren();
  labelsEl.classList.add('hidden');
}

// ------------------------------------------------------------------ rail
const rail = $('rail');
ORDER.forEach((id, i) => {
  const b = document.createElement('button');
  b.type = 'button';
  b.dataset.id = id;
  b.setAttribute('aria-label', `Go to stop ${i + 1} of ${ORDER.length}: ${SCENES[id].kicker}`);
  b.title = SCENES[id].kicker;
  b.addEventListener('click', () => {
    goTo(id);
    b.blur();
  });
  rail.appendChild(b);
});
function updateRail() {
  const ci = ORDER.indexOf(cur);
  [...rail.children].forEach((b, i) => {
    if (i === ci) b.setAttribute('aria-current', 'step');
    else b.removeAttribute('aria-current');
    b.classList.toggle('done', i < ci);
  });
}

// ------------------------------------------------------------------ actions
function advance() {
  if (tr || !cur) return;
  if (cur === 'close') return; // no auto loop: restart is explicit
  goTo(SCENES[cur].next);
}
function runAction(a) {
  if (tr || !cur) return;
  const s = scenes[cur];
  if (a === 'next') return cur === 'close' ? goTo('cover') : goTo(SCENES[cur].next);
  if (a.startsWith('pick:')) return s.select(a.slice(5));
  if (a.startsWith('gate:')) return s.select(Number(a.slice(5)));
}
primary.addEventListener('click', () => {
  primary.blur();
  if (!tr && cur) goTo(SCENES[cur].next);
});

// ------------------------------------------------------------------ overlay
const overlay = $('overlay');
let opener = null;
function openOverlay() {
  if (!cur) return;
  const d = SCENES[cur];
  $('ov-title').textContent = 'Sources / caveats · ' + d.kicker;
  const ul = $('ov-list');
  ul.replaceChildren();
  d.sources.forEach((k) => {
    const src = SRC[k];
    const li = document.createElement('li');
    const badge = document.createElement('span');
    badge.className = 'badge';
    badge.dataset.st = src.type;
    badge.textContent = STATUS[src.type].label;
    const a = document.createElement('a');
    a.href = src.url;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    a.textContent = src.title;
    const cav = document.createElement('span');
    cav.className = 'cav';
    cav.textContent = 'Caveat: ' + src.caveat;
    li.append(badge, a, cav);
    ul.appendChild(li);
  });
  $('ov-foot').textContent = `Research cutoff 29 Sep 2026 (Thailand time). No public S-1 was available; Reuters and Bloomberg figures come from documents they saw. Not investment advice. Build ${__BUILD_SHA__} · ${__BUILD_DATE__}.`;
  opener = document.activeElement;
  overlay.hidden = false;
  document.body.dataset.overlay = 'open';
  $('ov-close').focus();
}
function closeOverlay(silent) {
  if (overlay.hidden) return;
  overlay.hidden = true;
  document.body.dataset.overlay = 'closed';
  if (!silent && opener && opener.focus) opener.focus();
}
$('btn-src').addEventListener('click', openOverlay);
$('ov-close').addEventListener('click', () => closeOverlay());
overlay.addEventListener('click', (e) => {
  if (e.target === overlay) closeOverlay();
});
document.body.dataset.overlay = 'closed';

// ------------------------------------------------------------------ keyboard
addEventListener('keydown', (e) => {
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  const open = !overlay.hidden;
  if (e.key === 'Escape') {
    if (open) {
      e.preventDefault();
      closeOverlay();
    }
    return;
  }
  if (e.key === 'r' || e.key === 'R') {
    if (e.repeat) return;
    closeOverlay(true);
    goTo('cover');
    return;
  }
  if (open) {
    if (e.key === 'Tab') {
      const f = [...overlay.querySelectorAll('a[href], button')];
      const first = f[0];
      const last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
    return; // Space inside the overlay never advances.
  }
  if (e.code === 'Space') {
    const t = e.target;
    if (t && t.dataset && t.dataset.local) return; // native toggle for in-scene selectors
    e.preventDefault();
    if (e.repeat) return;
    if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
    advance();
  }
});

// ------------------------------------------------------------------ picking
const ray = new THREE.Raycaster();
const ndc = new THREE.Vector2();
let down = null;
function pick(ev) {
  if (!cur || tr || !overlay.hidden) return null;
  ndc.set((ev.clientX / innerWidth) * 2 - 1, -(ev.clientY / innerHeight) * 2 + 1);
  ray.setFromCamera(ndc, camera);
  const hits = ray.intersectObjects(scenes[cur].targets, true);
  for (const h of hits) {
    let o = h.object;
    while (o) {
      if (o.userData && o.userData.action) return o.userData.action;
      o = o.parent;
    }
  }
  return null;
}
canvas.addEventListener('pointerdown', (e) => (down = { x: e.clientX, y: e.clientY }));
canvas.addEventListener('pointerup', (e) => {
  if (!down) return;
  const moved = Math.hypot(e.clientX - down.x, e.clientY - down.y);
  down = null;
  if (moved > 8) return;
  const a = pick(e);
  if (a) runAction(a);
});
canvas.addEventListener('pointermove', (e) => {
  canvas.style.cursor = e.pointerType === 'mouse' && pick(e) ? 'pointer' : 'default';
});

// ------------------------------------------------------------------ frame loop
const v = new THREE.Vector3();
let headBottom = 0;
let headRight = 0;
function projectLabels() {
  const hr = document.querySelector('.head').getBoundingClientRect();
  headBottom = hr.bottom;
  headRight = hr.right;
  if (stacked || !cur || tr) return;
  const s = scenes[cur];
  const W = innerWidth;
  const H = innerHeight;
  for (const l of s.labels) {
    if (l.fixed) continue;
    v.copy(l.pos).add(s.group.position).project(camera);
    if (v.z > 1) {
      l.el.style.visibility = 'hidden';
      continue;
    }
    if (!l.w) {
      l.w = l.el.offsetWidth;
      l.h = l.el.offsetHeight;
    }
    let x = (v.x * 0.5 + 0.5) * W;
    let y = (-v.y * 0.5 + 0.5) * H;
    x = Math.min(W - l.w / 2 - 8, Math.max(l.w / 2 + 8, x));
    y = Math.min(H - 150, Math.max(l.h + 60, y));
    if (x - l.w / 2 < headRight && y - l.h < headBottom) y = headBottom + 10 + l.h;
    l.el.style.visibility = 'visible';
    l.el.style.transform = `translate(${x - l.w / 2}px, ${y - l.h}px)`;
  }
}

function frame(now) {
  requestAnimationFrame(frame);
  if (tr) {
    const p = clamp01((now - tr.t0) / tr.dur);
    const e = ease(p);
    const to = pose(target);
    camPos.lerpVectors(tr.fromPos, to.pos, e);
    camPos.y += Math.sin(Math.PI * e) * tr.arc;
    camLook.lerpVectors(tr.fromLook, to.look, e);
    if (p >= 0.42 && revealStart === null) revealStart = now;
    if (p >= 1) finish();
  } else if (cur) {
    const to = pose(cur);
    camPos.copy(to.pos);
    camLook.copy(to.look);
  }
  camera.position.copy(camPos);
  camera.lookAt(camLook);

  const s = scenes[tr ? target : cur];
  if (s && revealStart !== null && tr) {
    const t = (now - revealStart) / 1000;
    s.reveal.forEach((r) => {
      if (!r.obj) return;
      const k = easeOut(clamp01((t - r.delay) / 0.7));
      r.obj.visible = k > 0.001;
      r.obj.scale.copy(r.s0).multiplyScalar(Math.max(0.001, k));
    });
  }
  if (!reduced && cur && !tr) {
    const k = 0.5 + 0.5 * Math.sin(now / 420);
    pulses.forEach((p) => {
      if (p.visible) p.material.opacity = 0.35 + 0.6 * k;
    });
  }
  projectLabels();
  renderer.render(scene, camera);
}

// ------------------------------------------------------------------ boot
layout();
const initial = new URLSearchParams(location.search).get('scene');
const startId = ORDER.includes(initial) ? initial : 'cover';
const p0 = pose(startId);
camPos.copy(p0.pos);
camLook.copy(p0.look);
goTo(startId, { instant: true });
requestAnimationFrame(frame);
window.__ledger = { goTo, order: ORDER, get scene() { return cur; }, build: __BUILD_SHA__ };
