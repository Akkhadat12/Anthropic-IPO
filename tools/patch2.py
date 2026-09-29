p = 'src/scenes.js'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    if a not in s:
        print('MISSING:', a[:80])
    s = s.replace(a, b)


# capacity
rep("[[0, 4.2, 6], [0, 5, -8], [0, 6.4, -24], [0, 8, -46]]", "[[0, 4.6, -6], [0, 5.4, -16], [0, 6.6, -28], [0, 8, -48]]")
rep("Demand</span>', 1.2, 5.6, -2, 'mini-l', 0);", "Demand</span>', 1.4, 5.6, -10, 'mini-l', 0);")
rep("'Noncancelable or pay even if unused', '≈ one decade'), 8.5, 4, -14, 'tag sm', 2);",
    "'Noncancelable or pay even if unused', '≈ one decade'), -8.5, 0.6, -2, 'tag sm', 2);")
rep("Not the whole arrangement.', 15, 5.2, -14, 'credit', 4);", "Not the whole arrangement.', 15, 3.4, -14, 'credit', 4);")
rep("add(s, ph, 15, 8.4, -14, 0.4);", "add(s, ph, 15, 8.8, -14, 0.4);")

# retained: customers further back, separate label
rep("-12.5, 0.8, -7.5, 0.5);", "-8.5, 0.8, -8.5, 0.5);")
rep("-10.1, 0.8, -7.5, 0.55);", "-6.4, 0.8, -8.5, 0.55);")
rep("-11.3, 3.6, -7.5, 'tag sm', 5);", "-7.4, 3.2, -8.5, 'tag sm', 5);")
open(p, 'w', encoding='utf-8').write(s)
print('ok')
