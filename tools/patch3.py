p = 'src/scenes.js'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    if a not in s:
        print('MISSING:', a[:80])
    s = s.replace(a, b)


# scenarios: floor label below the slab, out of the path area
rep("'Common to all paths', '≈ one decade'), 2, 1.6, 2.6, 'tag sm', 0);", "'Common to all paths', '≈ one decade'), 2, -0.9, 6, 'tag sm', 0);")

# close: tall dashed gap between route and floor, label inside it, restart inside the frame
rep("const gap = wire(1.2, 5.4, 3, theme.status.unknown);\n    add(s, gap, 3, 3.4, -1, 0.5);",
    "const gap = wire(1.6, 9.6, 3, theme.ink);\n    add(s, gap, 3, 5, -1, 0.5);")
rep("Demand above, floor below</span>', 3, 8.2, -1, 'tag', 0);", "Demand above, floor below</span>', 3, 6.6, -1, 'tag', 0);")
rep("add(s, restart, -15, 1, 6, 0.6);", "add(s, restart, -11, 1, 6, 0.6);")
open(p, 'w', encoding='utf-8').write(s)

m = 'src/main.js'
t = open(m, encoding='utf-8').read()
a = "  const k = a >= 1.5 ? 1 : 1 + (1.5 - a) * 1.05;"
assert a in t
t = t.replace(a, "  const k = a >= 1.5 ? 1 : Math.min(3.2, (1.5 / a) * 0.97);")
a = "  const dock = document.querySelector('.dock');\n  document.documentElement.style.setProperty('--dock-h', dock.offsetHeight + 8 + 'px');\n"
assert a in t
t = t.replace(a, "  syncDock();\n")
a = "// ------------------------------------------------------------------ layout\n"
t = t.replace(a, a + "function syncDock() {\n  const dock = document.querySelector('.dock');\n  document.documentElement.style.setProperty('--dock-h', dock.offsetHeight + 8 + 'px');\n}\n")
a = "  labelsEl.classList.remove('hidden');\n  $('live')"
assert a in t
t = t.replace(a, "  labelsEl.classList.remove('hidden');\n  syncDock();\n  $('live')")
open(m, 'w', encoding='utf-8').write(t)
print('ok')
