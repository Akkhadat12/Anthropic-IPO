import * as THREE from 'three';
import { DATA, STATUS, SCENARIOS, GATES } from './data.js';

// Each scene is a THREE.Group at x = index * SPACING. Camera poses are local to that group.
export const SPACING = 90;

export function buildScenes(theme, ORDER) {
  const loader = new THREE.TextureLoader();
  const stColor = (s) => theme.status[s];
  const pulses = [];

  function mk(id) {
    const group = new THREE.Group();
    group.position.x = ORDER.indexOf(id) * SPACING;
    return { id, group, labels: [], reveal: [], targets: [], cam: null, aux: null, onEnter: null };
  }

  function mat(color, o = {}) {
    return new THREE.MeshStandardMaterial({ color, roughness: 0.75, metalness: 0.05, ...o });
  }

  function box(w, h, d, color, o = {}) {
    const geo = new THREE.BoxGeometry(w, h, d);
    const m = new THREE.Mesh(geo, mat(color, { transparent: o.op !== undefined, opacity: o.op ?? 1 }));
    if (o.edge !== false) {
      const e = new THREE.LineSegments(
        new THREE.EdgesGeometry(geo),
        new THREE.LineBasicMaterial({ color: o.edgeColor ?? theme.edge, transparent: true, opacity: theme.edgeOpacity }),
      );
      m.add(e);
      m.userData.edges = e;
    }
    return m;
  }

  function wire(w, h, d, color) {
    const geo = new THREE.BoxGeometry(w, h, d);
    const g = new THREE.Group();
    g.add(new THREE.LineSegments(geo && new THREE.EdgesGeometry(geo), new THREE.LineDashedMaterial({ color, dashSize: 0.4, gapSize: 0.3 })));
    g.children[0].computeLineDistances();
    return g;
  }

  function tube(points, r, color, o = {}) {
    const curve = new THREE.CatmullRomCurve3(points.map((p) => new THREE.Vector3(...p)), false, 'centripetal');
    const geo = new THREE.TubeGeometry(curve, 80, r, 10, false);
    return new THREE.Mesh(geo, mat(color, { transparent: o.op !== undefined, opacity: o.op ?? 1, emissive: o.emissive ?? 0x000000, emissiveIntensity: o.ei ?? 0 }));
  }

  function basic(w, h, d, color) {
    return new THREE.Mesh(new THREE.BoxGeometry(w, h, d), new THREE.MeshBasicMaterial({ color, fog: false }));
  }

  function ground(s, y = -0.05, w = 120, d = 120) {
    const g = new THREE.Mesh(new THREE.PlaneGeometry(w, d), new THREE.MeshBasicMaterial({ color: theme.ground }));
    g.rotation.x = -Math.PI / 2;
    g.position.y = y;
    s.group.add(g);
    return g;
  }

  function add(s, obj, x, y, z, delay) {
    obj.position.set(x, y, z);
    s.group.add(obj);
    if (delay !== undefined) s.reveal.push({ obj, delay, s0: obj.scale.clone() });
    return obj;
  }

  // Label with a 3D anchor. The engine projects it on wide layouts and stacks it on narrow ones.
  function label(s, html, x, y, z, cls = '', order = 0) {
    const el = document.createElement('div');
    el.className = 'lbl ' + cls;
    el.innerHTML = html;
    s.labels.push({ el, pos: new THREE.Vector3(x, y, z), order });
    return el;
  }

  const stat = (status, big, desc, period = '') =>
    `<span class="badge" data-st="${status}">${STATUS[status].short}</span><b class="big">${big}</b><span class="desc">${desc}</span>${period ? `<span class="per">${period}</span>` : ''}`;

  function target(s, obj, action, o = {}) {
    obj.userData.action = action;
    s.targets.push(obj);
    if (o.halo) {
      const halo = new THREE.Mesh(
        new THREE.TorusGeometry(o.halo, 0.09, 8, 48),
        new THREE.MeshBasicMaterial({ color: theme.route, transparent: true, opacity: 0.9, fog: false }),
      );
      halo.position.copy(obj.position);
      halo.position.z += o.haloZ ?? 0.3;
      if (o.haloRotY) halo.rotation.y = o.haloRotY;
      s.group.add(halo);
      pulses.push(halo);
    }
  }

  const scenes = {};

  // ---------------------------------------------------------------- cover
  {
    const s = mk('cover');
    s.cam = { pos: [0, 0.5, 15], look: [0, 0, -14] };
    const tex = loader.load(import.meta.env.BASE_URL + 'img/project-rainier-interior.png');
    tex.colorSpace = THREE.SRGBColorSpace;
    const photo = new THREE.Mesh(new THREE.PlaneGeometry(52, 29.25), new THREE.MeshBasicMaterial({ map: tex, fog: false }));
    add(s, photo, 0, 0.5, -16);
    // Doorway frame the camera passes through on entry.
    const door = new THREE.Group();
    const c = theme.route;
    const bars = [
      [12, 0.1, 0.1, 0, 4, 0],
      [12, 0.1, 0.1, 0, -4, 0],
      [0.1, 8.1, 0.1, -6, 0, 0],
      [0.1, 8.1, 0.1, 6, 0, 0],
    ];
    bars.forEach(([w, h, d, x, y, z]) => {
      const b = basic(w, h, d, c);
      b.position.set(x, y, z);
      door.add(b);
    });
    const hit = new THREE.Mesh(new THREE.PlaneGeometry(12, 8), new THREE.MeshBasicMaterial({ color: c, transparent: true, opacity: 0.06, fog: false }));
    door.add(hit);
    add(s, door, 0, 0.6, -1, 0.1);
    target(s, door, 'next');
    door.userData.hit = hit;
    hit.userData.action = 'next';
    s.targets.push(hit);
    // Narrow demand route runs toward a much wider capacity horizon.
    add(s, basic(0.5, 0.12, 20, theme.route), 0, -3.9, 2, 0.2);
    add(s, basic(40, 0.28, 0.4, theme.floor), 0, -6.3, -15.4, 0.35);
    label(s, '<span class="mini">Demand route</span>', 0, -3.4, 8, 'mini-l', 1);
    label(s, '<span class="mini">Capacity horizon</span>', 12, -5.9, -15, 'mini-l', 2);
    label(s, 'Photo: Amazon Web Services, Project Rainier. An AWS compute building used for Anthropic workloads. Not owned by Anthropic.', 0, 0, 0, 'credit', 3);
    s.labels[s.labels.length - 1].fixed = 'br';
    scenes.cover = s;
  }

  // ---------------------------------------------------------------- demand
  {
    const s = mk('demand');
    s.cam = { pos: [0, 6.5, 23], look: [0, 3.6, -2] };
    ground(s);
    const cards = [
      { k: 'fy2025_revenue', x: -11, z: 1, d: 'Revenue recognized', act: null },
      { k: 'q1_2026_revenue', x: -3.7, z: -1, d: 'Quarterly revenue' },
      { k: 'q2_2026_revenue', x: 3.7, z: -3, d: 'Quarterly revenue', act: 'next' },
      { k: 'may_2026_run_rate', x: 11, z: -5, d: 'Annualized run-rate, not booked' },
    ];
    cards.forEach((c, i) => {
      const dt = DATA[c.k];
      const slab = box(5.2, 6, 0.7, stColor(dt.status), { op: dt.status === 'prelim' ? 0.72 : 1 });
      add(s, slab, c.x, 3, c.z, 0.15 + i * 0.16);
      add(s, box(6.2, 0.25, 3.2, theme.floor), c.x, 0.12, c.z, 0.1 + i * 0.16);
      label(s, stat(dt.status, dt.text, c.d, dt.period), c.x, 6.6, c.z, 'tag', i);
      if (c.act) target(s, slab, c.act, { halo: 3.7, haloZ: 0.6 });
    });
    scenes.demand = s;
  }

  // ---------------------------------------------------------------- retained
  {
    const s = mk('retained');
    s.cam = { pos: [1, 13, 20], look: [1, 0, 1] };
    ground(s);
    const rc = theme.status.reported;
    add(s, box(4, 2.4, 4, rc), -11.5, 1.2, 0, 0.1);
    label(s, stat('reported', 'Reported revenue', 'Gross, as recognized', 'FY2025'), -11.5, 4.6, 0, 'tag', 0);
    const lane = (pts, delay, op = 1, color = rc) => add(s, tube(pts, 0.28, color, { op }), 0, 0, 0, delay);
    lane([[-9.5, 0.5, 0], [-7, 0.5, 0], [-4, 0.5, -4.5], [0, 0.5, -4.5], [4, 0.5, -4.5], [7.5, 0.5, 0], [10, 0.5, 0]], 0.3);
    lane([[-9.5, 0.5, 0], [-7, 0.5, 0], [-4, 0.5, 4.5], [0, 0.5, 4.5], [4, 0.5, 4.5], [7.5, 0.5, 0], [10, 0.5, 0]], 0.4);
    label(s, '<span class="mini">Direct</span>', -2, 1.6, -4.5, 'mini-l', 1);
    label(s, '<span class="mini">Via cloud partners</span>', -2, 1.6, 4.5, 'mini-l', 2);
    // Partner share gate on the cloud lane: unnumbered.
    add(s, box(0.4, 2.2, 2, theme.status.unknown, { op: 0.9 }), -1.5, 1.1, 4.5, 0.55);
    label(s, '<span class="badge" data-st="unknown">Not disclosed</span><span class="desc">Partner share</span>', -1.5, 3.6, 4.5, 'tag sm', 3);
    // Retained-value gate: a ring the routes pass through, with a ghost outlet.
    const gate = new THREE.Mesh(new THREE.TorusGeometry(2.2, 0.28, 12, 40), mat(theme.route, { emissive: theme.route, emissiveIntensity: 0.25 }));
    gate.rotation.y = Math.PI / 2;
    add(s, gate, 8.5, 2.2, 0, 0.65);
    target(s, gate, 'next', { halo: 3.2, haloZ: 0, haloRotY: Math.PI / 2 });
    const outlet = tube([[10, 1, 0], [15, 1, 0]], 0.28, theme.status.unknown, { op: 0.4 });
    add(s, outlet, 0, 0, 0, 0.75);
    label(s, '<span class="badge" data-st="unknown">Not disclosed</span><b class="big">Retained value</b><span class="desc">Gross-to-net is unknown</span>', 12, 4.8, 0, 'tag', 4);
    // Two customers near a quarter of FY2025 revenue.
    add(s, box(1.6, 1.6, 1.6, theme.status.reported), -8.5, 0.8, -8.5, 0.5);
    add(s, box(1.6, 1.6, 1.6, theme.status.reported), -6.4, 0.8, -8.5, 0.55);
    label(s, stat('reported', '≈ ¼ of revenue', 'Two customers, combined', 'FY2025'), -7.4, 3.2, -8.5, 'tag sm', 5);
    scenes.retained = s;
  }

  // ---------------------------------------------------------------- models
  {
    const s = mk('models');
    s.cam = { pos: [0, 6, 24], look: [0, 4.4, 0] };
    ground(s);
    const bc = stColor('bench');
    const sc = stColor('stated');
    // Capability axis (left).
    const capG = new THREE.Group();
    const opusBar = box(2.6, 5.8, 2.6, bc);
    const sonBar = box(2.6, 5.6, 2.6, bc);
    add({ group: capG, reveal: [] }, opusBar, -2, 2.9, 0);
    add({ group: capG, reveal: [] }, sonBar, 2, 2.8, 0);
    add({ group: capG, reveal: [] }, box(7, 0.2, 3.4, theme.floor), 0, 0.1, 0);
    add(s, capG, -10, 0, 0, 0.15);
    label(s, '<span class="badge" data-st="bench">Independent benchmark</span><b class="big">Capability</b><span class="desc">Intelligence Index, max effort</span>', -10, -0.3, 3.4, 'tag', 0);
    label(s, '<span class="mini">Opus 5.5 · 58</span>', -12, 6.6, 0, 'mini-l', 1);
    label(s, '<span class="mini">Sonnet 5.5 · 56</span>', -8, 6.4, 0, 'mini-l', 2);
    // Task cost axis (right): same independent test, same basis.
    const costG = new THREE.Group();
    const s5 = box(2.6, 5.09 * 0.75, 2.6, bc);
    const s55 = box(2.6, 7.6 * 0.75, 2.6, bc);
    add({ group: costG, reveal: [] }, s5, -2, (5.09 * 0.75) / 2, 0);
    add({ group: costG, reveal: [] }, s55, 2, (7.6 * 0.75) / 2, 0);
    add({ group: costG, reveal: [] }, box(7, 0.2, 3.4, theme.floor), 0, 0.1, 0);
    add(s, costG, 10, 0, 0, 0.3);
    label(s, '<span class="badge" data-st="bench">Independent benchmark</span><b class="big">Cost per task</b><span class="desc">Same test, max effort, pre-release build</span>', 10, -0.3, 3.4, 'tag', 3);
    label(s, '<span class="mini">Sonnet 5 · $5.09</span>', 8, 4.6, 0, 'mini-l', 4);
    label(s, '<span class="mini">Sonnet 5.5 · $7.60</span>', 12, 6.4, 0, 'mini-l', 5);
    // Anthropic's own typical-task claim sits on a separate translucent layer.
    add(s, box(12, 2.4, 0.12, sc, { op: 0.3 }), 0, 9.6, -6, 0.45);
    label(s, '<span class="badge" data-st="stated">Anthropic stated</span><span class="desc">Own tests: Opus ≈ 40% and Sonnet up to 30% lower cost per typical task. Different basis.</span>', 0, 8.6, -6, 'tag sm', 6);
    // Completed task: the object the presenter clicks.
    const task = box(2.2, 2.2, 2.2, theme.route, { edgeColor: theme.ink });
    add(s, task, 0, 2.4, 0, 0.5);
    target(s, task, 'next', { halo: 2.2, haloZ: 0 });
    label(s, '<span class="mini">Completed task</span>', 0, 4.6, 0, 'mini-l', 7);
    // Opus / Sonnet toggle: changes in-scene details, does not advance.
    const detail = label(s, '', 0, 0.6, 6, 'tag sm detail', 8);
    const modelInfo = {
      opus: '<span class="badge" data-st="stated">Anthropic stated</span><b class="big">Opus 5.5</b><span class="desc">$4 in / $20 out per M tokens · released 22 Sep 2026</span>',
      sonnet: '<span class="badge" data-st="stated">Anthropic stated</span><b class="big">Sonnet 5.5</b><span class="desc">$2 in / $10 out per M tokens · released 28 Sep 2026</span>',
    };
    const setModel = (k) => {
      detail.innerHTML = modelInfo[k];
      const dim = (m, on) => {
        m.material.opacity = on ? 1 : 0.35;
        m.material.transparent = true;
        m.userData.edges.material.opacity = on ? theme.edgeOpacity : 0.15;
      };
      dim(opusBar, k === 'opus');
      dim(sonBar, k === 'sonnet');
      dim(s5, k === 'sonnet');
      dim(s55, k === 'sonnet');
      s.model = k;
    };
    s.onEnter = () => setModel(s.model || 'sonnet');
    s.aux = (host) => {
      const wrap = document.createElement('div');
      wrap.className = 'seg';
      wrap.setAttribute('role', 'group');
      wrap.setAttribute('aria-label', 'Model detail');
      ['opus', 'sonnet'].forEach((k) => {
        const b = document.createElement('button');
        b.type = 'button';
        b.dataset.local = '1';
        b.textContent = k === 'opus' ? 'Opus 5.5' : 'Sonnet 5.5';
        b.setAttribute('aria-pressed', String((s.model || 'sonnet') === k));
        b.addEventListener('click', () => {
          setModel(k);
          wrap.querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
        });
        wrap.appendChild(b);
      });
      host.appendChild(wrap);
      const note = document.createElement('p');
      note.className = 'aux-note';
      note.textContent = 'Basis: Artificial Analysis test. Not Anthropic serving cost or margin.';
      host.appendChild(note);
    };
    scenes.models = s;
  }

  // ---------------------------------------------------------------- statements
  {
    const s = mk('statements');
    s.cam = { pos: [0, 5, 25], look: [0, 4.2, -1] };
    ground(s);
    const items = [
      { st: 'reported', big: DATA.fy2025_revenue.text, desc: 'Revenue', per: 'FY2025', x: -13.5, z: 1 },
      { st: 'reported', big: DATA.fy2025_operating_loss.text, desc: 'Operating loss · accounting, not cash. Compute $7.33B of $12.65B expenses', per: 'FY2025', x: -6.8, z: -0.5 },
      { st: 'reported', big: DATA.fy2025_net_loss.text, desc: 'Net loss · includes ≈ $34B non-cash remeasurement', per: 'FY2025', x: 0, z: -2 },
      { st: 'prelim', big: 'Positive', desc: 'Adjusted operating income · not GAAP', per: 'Q2 2026', x: 6.8, z: -0.5 },
    ];
    items.forEach((it, i) => {
      const p = box(5.4, 5.2, 0.35, stColor(it.st), { op: it.st === 'prelim' ? 0.72 : 1 });
      add(s, p, it.x, 2.8, it.z, 0.15 + i * 0.15);
      label(s, stat(it.st, it.big, it.desc, it.per), it.x, 6.3, it.z, 'tag', i);
    });
    // Cash flow: intentionally empty outline. Clicking it looks ahead.
    const cash = wire(5.4, 5.2, 0.35, theme.ink);
    add(s, cash, 13.5, 2.8, 1, 0.75);
    const hit = new THREE.Mesh(new THREE.BoxGeometry(5.4, 5.2, 0.6), new THREE.MeshBasicMaterial({ transparent: true, opacity: 0.0, depthWrite: false }));
    hit.position.set(13.5, 2.8, 1);
    s.group.add(hit);
    target(s, hit, 'next');
    const halo = new THREE.Mesh(new THREE.TorusGeometry(3.3, 0.09, 8, 48), new THREE.MeshBasicMaterial({ color: theme.route, transparent: true, opacity: 0.9, fog: false }));
    halo.position.set(13.5, 2.8, 1.3);
    s.group.add(halo);
    pulses.push(halo);
    label(s, '<span class="badge" data-st="unknown">Not disclosed here</span><b class="big">Cash flow</b><span class="desc">No operating cash flow, capex, or free cash flow</span>', 13.5, 6.3, 1, 'tag', 4);
    scenes.statements = s;
  }

  // Corridor floor shared by the capacity and scenario scenes.
  function corridor(s, length = 64, z0 = 12) {
    const floor = box(9, 0.9, length, theme.floor, { edge: true });
    add(s, floor, 0, -0.45, z0 - length / 2, 0.1);
    for (let i = 0; i < 9; i++) {
      const z = z0 - 4 - i * 7;
      add(s, basic(9.6, 0.08, 0.14, theme.ink), 0, 0.03, z, 0.15 + i * 0.05);
    }
    return floor;
  }

  // ---------------------------------------------------------------- capacity
  {
    const s = mk('capacity');
    s.cam = { pos: [0, 5.5, 17], look: [0, 3.2, -22] };
    ground(s);
    corridor(s);
    // Demand ribbon above the floor: shown without magnitude beyond "above the floor".
    add(s, tube([[0, 4.6, -6], [0, 5.4, -16], [0, 6.6, -28], [0, 8, -48]], 0.13, theme.route), 0, 0, 0, 0.3);
    label(s, '<span class="mini">Demand</span>', 1.4, 5.6, -10, 'mini-l', 0);
    label(s, stat('reported', '≥ $518B', 'Infrastructure arrangements over ≈ one decade. Not annual spend', 'Floor'), -8.5, 4, -6, 'tag', 1);
    label(s, stat('reported', '≈ 80%', 'Noncancelable or pay even if unused', '≈ one decade'), -8.5, 0.6, -2, 'tag sm', 2);
    label(s, '<span class="mini">≈ 10 years</span>', 0, 1.0, -30, 'mini-l', 3);
    // Optional real anchor: AWS campus, small and off-axis.
    const tex = loader.load(import.meta.env.BASE_URL + 'img/project-rainier-exterior.png');
    tex.colorSpace = THREE.SRGBColorSpace;
    const ph = new THREE.Mesh(new THREE.PlaneGeometry(10, 5.63), new THREE.MeshBasicMaterial({ map: tex, fog: false }));
    ph.rotation.y = -0.35;
    add(s, ph, 15, 8.8, -14, 0.4);
    label(s, 'Photo: Amazon Web Services. AWS Project Rainier campus, one partner site. Not the whole arrangement.', 15, 3.4, -14, 'credit', 4);
    // Utilization threshold gate.
    const gate = new THREE.Group();
    [[-4.8, 3.6], [4.8, 3.6]].forEach(([x, y]) => {
      const p = basic(0.4, 7.2, 0.4, theme.route);
      p.position.set(x, y, 0);
      gate.add(p);
    });
    const top = basic(10, 0.4, 0.4, theme.route);
    top.position.set(0, 7.2, 0);
    gate.add(top);
    const hit = new THREE.Mesh(new THREE.PlaneGeometry(9.6, 7.2), new THREE.MeshBasicMaterial({ color: theme.route, transparent: true, opacity: 0.07, fog: false, side: THREE.DoubleSide }));
    hit.position.set(0, 3.6, 0);
    gate.add(hit);
    hit.userData.action = 'next';
    s.targets.push(hit);
    add(s, gate, 0, 0, -38, 0.5);
    label(s, '<span class="mini">Utilization threshold</span>', 0, 8.2, -38, 'mini-l', 5);
    scenes.capacity = s;
  }

  // ---------------------------------------------------------------- scenarios
  {
    const s = mk('scenarios');
    s.cam = { pos: [0, 8, 26], look: [0, 4, 0] };
    ground(s);
    // Common capacity floor stays visible in every selection.
    add(s, box(34, 0.9, 5, theme.floor), 2, -0.45, 0, 0.05);
    label(s, stat('reported', '≥ $518B floor', 'Common to all paths', '≈ one decade'), 2, -0.9, 6, 'tag sm', 0);
    add(s, box(1.4, 1.4, 1.4, theme.status.scenario), -15, 4, 0, 0.1);
    label(s, '<span class="mini">Same start</span>', -15, 5.4, 0, 'mini-l', 1);
    const paths = {
      upside: tube([[-15, 4, 0], [-8, 5, 0], [0, 7.2, 0], [9, 9.6, 0], [17, 11.6, 0]], 0.3, theme.status.stated),
      base: tube([[-15, 4, 0], [-8, 4.3, 0], [0, 4.6, 0], [9, 4.9, 0], [17, 5.2, 0]], 0.3, theme.status.prelim),
      downside: tube([[-15, 4, 0], [-8, 3.6, 0], [0, 2.6, 0], [9, 1.4, 0], [17, 0.6, 0]], 0.3, theme.status.reported),
    };
    let i = 0;
    for (const k of Object.keys(paths)) {
      add(s, paths[k], 0, 0, 0, 0.25 + i * 0.12);
      paths[k].userData.action = 'pick:' + k;
      s.targets.push(paths[k]);
      i++;
    }
    const ends = { upside: [17.5, 12.6], base: [17.5, 6.2], downside: [17.5, 1.7] };
    const endLabels = {};
    for (const k of Object.keys(ends)) {
      endLabels[k] = label(s, `<span class="badge" data-st="scenario">Scenario</span><b class="big">${SCENARIOS[k].name}</b>`, ends[k][0] - 3, ends[k][1], 0, 'tag sm', 2 + Object.keys(ends).indexOf(k));
    }
    const applySel = (k) => {
      s.sel = k;
      for (const p of Object.keys(paths)) {
        const on = !k || p === k;
        paths[p].material.transparent = true;
        paths[p].material.opacity = on ? 1 : 0.22;
        endLabels[p].classList.toggle('dim', !on);
        endLabels[p].classList.toggle('sel', p === k);
      }
      if (s.note) s.note.textContent = k ? SCENARIOS[k].name + ': ' + SCENARIOS[k].text : 'Select a path to see its condition.';
      if (s.btns) Object.entries(s.btns).forEach(([p, b]) => b.setAttribute('aria-pressed', String(p === k)));
    };
    s.select = applySel;
    s.onEnter = () => applySel(s.sel || null);
    s.aux = (host) => {
      const wrap = document.createElement('div');
      wrap.className = 'seg';
      wrap.setAttribute('role', 'group');
      wrap.setAttribute('aria-label', 'Scenario path');
      s.btns = {};
      Object.keys(SCENARIOS).forEach((k) => {
        const b = document.createElement('button');
        b.type = 'button';
        b.dataset.local = '1';
        b.textContent = SCENARIOS[k].name;
        b.addEventListener('click', () => applySel(k));
        s.btns[k] = b;
        wrap.appendChild(b);
      });
      host.appendChild(wrap);
      s.note = document.createElement('p');
      s.note.className = 'aux-note';
      s.note.setAttribute('aria-live', 'polite');
      host.appendChild(s.note);
      applySel(s.sel || null);
    };
    scenes.scenarios = s;
  }

  // ---------------------------------------------------------------- filing
  {
    const s = mk('filing');
    s.cam = { pos: [0, 5.5, 25], look: [0, 3.2, -2] };
    ground(s);
    const gates = [];
    GATES.forEach((g, i) => {
      const grp = new THREE.Group();
      const c = theme.status.scenario;
      [[-2.2, 3], [2.2, 3]].forEach(([x, y]) => {
        const p = basic(0.34, 6, 0.34, c);
        p.position.set(x, y, 0);
        grp.add(p);
      });
      const t = basic(4.7, 0.34, 0.34, c);
      t.position.set(0, 6, 0);
      grp.add(t);
      const hit = new THREE.Mesh(new THREE.PlaneGeometry(4.4, 6), new THREE.MeshBasicMaterial({ color: c, transparent: true, opacity: 0.08, fog: false, side: THREE.DoubleSide }));
      hit.position.set(0, 3, 0);
      hit.userData.action = 'gate:' + i;
      grp.add(hit);
      s.targets.push(hit);
      add(s, grp, -13 + i * 6.5, 0, 1 - Math.abs(i - 2) * 1.6, 0.15 + i * 0.12);
      gates.push({ grp, hit, t });
      label(s, `<span class="mini">${i + 1} · ${g.title}</span>`, -13 + i * 6.5, 7.4, 1 - Math.abs(i - 2) * 1.6, 'mini-l gate-l', i);
    });
    // Faint route + floor behind the gates to keep the original relationship in view.
    add(s, basic(40, 0.14, 0.3, theme.route), 0, 1, -7, 0.4);
    add(s, box(40, 0.5, 2, theme.floor), 0, -0.25, -7, 0.4);
    const applyGate = (k) => {
      s.sel = k;
      gates.forEach((g, i) => {
        g.hit.material.opacity = i === k ? 0.3 : 0.08;
      });
      if (s.note) s.note.innerHTML = k === null || k === undefined ? 'Select a gate for what it must show.' : `<b>${GATES[k].title}.</b> ${GATES[k].note}`;
      if (s.btns) s.btns.forEach((b, i) => b.setAttribute('aria-pressed', String(i === k)));
    };
    s.select = applyGate;
    s.onEnter = () => applyGate(s.sel ?? null);
    s.aux = (host) => {
      const wrap = document.createElement('div');
      wrap.className = 'seg wrap';
      wrap.setAttribute('role', 'group');
      wrap.setAttribute('aria-label', 'Disclosure gates');
      s.btns = GATES.map((g, i) => {
        const b = document.createElement('button');
        b.type = 'button';
        b.dataset.local = '1';
        b.textContent = String(i + 1) + ' ' + g.title;
        b.addEventListener('click', () => applyGate(i));
        wrap.appendChild(b);
        return b;
      });
      host.appendChild(wrap);
      s.note = document.createElement('p');
      s.note.className = 'aux-note';
      s.note.setAttribute('aria-live', 'polite');
      host.appendChild(s.note);
      applyGate(s.sel ?? null);
    };
    scenes.filing = s;
  }

  // ---------------------------------------------------------------- close
  {
    const s = mk('close');
    s.cam = { pos: [0, 6, 24], look: [0, 4.2, 0] };
    ground(s);
    add(s, tube([[-16, 6.5, 2], [-6, 8, 0], [4, 10.4, -2], [16, 13, -4]], 0.3, theme.route), 0, 0, 0, 0.15);
    add(s, box(36, 0.9, 6, theme.floor), 0, -0.45, -1, 0.25);
    // The gap between demand and floor is held open, not animated closed.
    const gap = wire(1.6, 9.6, 3, theme.ink);
    add(s, gap, 3, 5, -1, 0.5);
    label(s, '<span class="badge" data-st="unknown">Unproven</span><b class="big">Cash conversion</b><span class="desc">Demand above, floor below</span>', 3, 6.6, -1, 'tag', 0);
    label(s, '<span class="mini">Demand route</span>', -13, 8.2, 2, 'mini-l', 1);
    label(s, '<span class="mini">≥ $518B floor · ≈ one decade</span>', -10, 1.6, 2, 'mini-l', 2);
    const restart = box(3, 1.6, 3, theme.route, { edgeColor: theme.ink });
    add(s, restart, -11, 1, 6, 0.6);
    target(s, restart, 'next', { halo: 2.2, haloZ: 1.6 });
    scenes.close = s;
  }

  return { scenes, pulses };
}
