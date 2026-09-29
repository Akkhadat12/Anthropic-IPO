p = 'src/scenes.js'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    if a not in s:
        print('MISSING:', a[:70])
    s = s.replace(a, b)


rep("const g = new THREE.Mesh(new THREE.PlaneGeometry(w, d), mat(theme.ground, { roughness: 1 }));",
    "const g = new THREE.Mesh(new THREE.PlaneGeometry(w, d), new THREE.MeshBasicMaterial({ color: theme.ground }));")
rep("const curve = new THREE.CatmullRomCurve3(points.map((p) => new THREE.Vector3(...p)));",
    "const curve = new THREE.CatmullRomCurve3(points.map((p) => new THREE.Vector3(...p)), false, 'centripetal');")
rep("      halo.position.z += o.haloZ ?? 0.3;\n",
    "      halo.position.z += o.haloZ ?? 0.3;\n      if (o.haloRotY) halo.rotation.y = o.haloRotY;\n")

# cover
rep("new THREE.PlaneGeometry(46, 25.9)", "new THREE.PlaneGeometry(52, 29.25)")
rep("[12, 0.35, 0.35, 0, 4, 0]", "[12, 0.1, 0.1, 0, 4, 0]")
rep("[12, 0.35, 0.35, 0, -4, 0]", "[12, 0.1, 0.1, 0, -4, 0]")
rep("[0.35, 8.35, 0.35, -6, 0, 0]", "[0.1, 8.1, 0.1, -6, 0, 0]")
rep("[0.35, 8.35, 0.35, 6, 0, 0]", "[0.1, 8.1, 0.1, 6, 0, 0]")
rep("add(s, basic(34, 0.5, 0.6, theme.floor), 0, -4.9, -15.4, 0.35);",
    "add(s, basic(40, 0.28, 0.4, theme.floor), 0, -6.3, -15.4, 0.35);")
rep("'Capacity horizon</span>', 11, -3.9, -15,", "'Capacity horizon</span>', 12, -5.9, -15,") if False else None
rep("Capacity horizon</span>', 11, -3.9, -15, 'mini-l', 2);", "Capacity horizon</span>', 12, -5.9, -15, 'mini-l', 2);")

# demand
rep("s.cam = { pos: [0, 5.5, 23], look: [0, 1.5, -2] };", "s.cam = { pos: [0, 6.5, 23], look: [0, 3.6, -2] };")

# retained
rep("s.cam = { pos: [0, 12, 19], look: [0, 0, 0] };", "s.cam = { pos: [1, 13, 20], look: [1, 0, 1] };")
rep("add(s, box(4, 2.4, 4, rc), -13, 1.2, 0, 0.1);", "add(s, box(4, 2.4, 4, rc), -11.5, 1.2, 0, 0.1);")
rep("'Gross, as recognized', 'FY2025'), -13, 4.6, 0,", "'Gross, as recognized', 'FY2025'), -11.5, 4.6, 0,")
rep("target(s, gate, 'next', { halo: 3.2, haloZ: 0 });", "target(s, gate, 'next', { halo: 3.2, haloZ: 0, haloRotY: Math.PI / 2 });")
rep("[[-11, 0.5, 0], [-8, 0.5, 0], [-6, 0.5, -4.5], [0, 0.5, -4.5], [5, 0.5, -4.5], [7, 0.5, 0]]",
    "[[-9.5, 0.5, 0], [-7, 0.5, 0], [-4, 0.5, -4.5], [0, 0.5, -4.5], [4, 0.5, -4.5], [7.5, 0.5, 0], [10, 0.5, 0]]")
rep("[[-11, 0.5, 0], [-8, 0.5, 0], [-6, 0.5, 4.5], [0, 0.5, 4.5], [5, 0.5, 4.5], [7, 0.5, 0]]",
    "[[-9.5, 0.5, 0], [-7, 0.5, 0], [-4, 0.5, 4.5], [0, 0.5, 4.5], [4, 0.5, 4.5], [7.5, 0.5, 0], [10, 0.5, 0]]")
rep("-13, 0.8, -7.5, 0.5);", "-12.5, 0.8, -7.5, 0.5);")
rep("-10.6, 0.8, -7.5, 0.55);", "-10.1, 0.8, -7.5, 0.55);")
rep("-11.8, 3.6, -7.5, 'tag sm', 5);", "-11.3, 3.6, -7.5, 'tag sm', 5);")

# models
rep("s.cam = { pos: [0, 5, 24], look: [0, 3, 0] };", "s.cam = { pos: [0, 6, 24], look: [0, 4.4, 0] };")
rep("Intelligence Index, max effort</span>', -10, 8.6, 0, 'tag', 0);", "Intelligence Index, max effort</span>', -10, -0.3, 3.4, 'tag', 0);")
rep("pre-release build</span>', 10, 9.2, 0, 'tag', 3);", "pre-release build</span>', 10, -0.3, 3.4, 'tag', 3);")
rep("Different basis.</span>', 0, 11.6, -6, 'tag sm', 6);", "Different basis.</span>', 0, 8.6, -6, 'tag sm', 6);")
rep("add(s, box(11, 3.2, 0.12, sc, { op: 0.35 }), 0, 9.2, -6, 0.45);", "add(s, box(12, 2.4, 0.12, sc, { op: 0.3 }), 0, 9.6, -6, 0.45);")
rep("add(s, task, 0, 1.6, 3, 0.5);", "add(s, task, 0, 2.4, 0, 0.5);")
rep("Completed task</span>', 0, 3.6, 3, 'mini-l', 7);", "Completed task</span>', 0, 4.6, 0, 'mini-l', 7);")
rep("const detail = label(s, '', 0, -0.4, 5, 'tag sm detail', 8);", "const detail = label(s, '', 0, 0.6, 6, 'tag sm detail', 8);")

# statements
rep("s.cam = { pos: [0, 4, 25], look: [0, 3, -1] };", "s.cam = { pos: [0, 5, 25], look: [0, 4.2, -1] };")
rep("const cash = wire(5.4, 5.2, 0.35, theme.status.unknown);", "const cash = wire(5.4, 5.2, 0.35, theme.ink);")
rep("new THREE.TorusGeometry(3.6, 0.09, 8, 48)", "new THREE.TorusGeometry(3.3, 0.09, 8, 48)")

# capacity
rep("'Infrastructure arrangements over ≈ one decade. Not annual spend', 'Floor'), 0, 3.2, -14, 'tag', 1);",
    "'Infrastructure arrangements over ≈ one decade. Not annual spend', 'Floor'), -8.5, 4, -6, 'tag', 1);")
rep("'Noncancelable or pay even if unused', '≈ one decade'), 0, 3.2, -30, 'tag sm', 2);",
    "'Noncancelable or pay even if unused', '≈ one decade'), 8.5, 4, -14, 'tag sm', 2);")
rep("≈ 10 years</span>', 0, 1.2, -50, 'mini-l', 3);", "≈ 10 years</span>', 0, 1.0, -30, 'mini-l', 3);")
rep("add(s, ph, -13.5, 5.4, -10, 0.4);", "add(s, ph, 15, 8.4, -14, 0.4);")
rep("ph.rotation.y = 0.35;", "ph.rotation.y = -0.35;")
rep("Not the whole arrangement.', -13.5, 1.6, -10, 'credit', 4);", "Not the whole arrangement.', 15, 5.2, -14, 'credit', 4);")
rep("s.cam = { pos: [0, 4.2, 17], look: [0, 2.2, -22] };", "s.cam = { pos: [0, 5.5, 17], look: [0, 3.2, -22] };")
rep("[[0, 4.5, 8], [0, 5.2, -8], [0, 6.2, -24], [0, 7.4, -46]]", "[[0, 4.2, 6], [0, 5, -8], [0, 6.4, -24], [0, 8, -46]]")
open(p, 'w', encoding='utf-8').write(s)

m = 'src/main.js'
t = open(m, encoding='utf-8').read()
a = "scene.add(new THREE.HemisphereLight(0xffffff, theme.ground, theme.ambient));"
assert a in t
t = t.replace(a, "scene.add(new THREE.HemisphereLight(0xffffff, 0xcfc8b8, theme.ambient));")
a = "    l.el.style.visibility = 'visible';\n    l.el.style.transform"
assert a in t
t = t.replace(a, "    if (x - l.w / 2 < headRight && y - l.h < headBottom) y = headBottom + 10 + l.h;\n    l.el.style.visibility = 'visible';\n    l.el.style.transform")
a = "const v = new THREE.Vector3();\nfunction projectLabels() {"
assert a in t
t = t.replace(a, "const v = new THREE.Vector3();\nlet headBottom = 0;\nlet headRight = 0;\nfunction projectLabels() {\n  const hr = document.querySelector('.head').getBoundingClientRect();\n  headBottom = hr.bottom;\n  headRight = hr.right;")
open(m, 'w', encoding='utf-8').write(t)

th = 'src/theme.js'
u = open(th, encoding='utf-8').read()
u = u.replace("ambient: 0.85,\n    key: 1.1,", "ambient: 2.4,\n    key: 1.9,").replace("ambient: 0.55,\n    key: 1.0,", "ambient: 1.6,\n    key: 1.6,")
open(th, 'w', encoding='utf-8').write(u)
print('patched')
