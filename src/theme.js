// Two distinct visual directions, compared in the prototype (see BUILD_NOTES.md).
// A: "Daylight ledger" — warm paper, ink edges, matte planes.
// B: "Night blueprint" — dark field, luminous edges, glowing status planes.
export const THEMES = {
  a: {
    id: 'a',
    name: 'Daylight ledger',
    bg: 0xe9e3d5,
    ground: 0xd9d1bf,
    ink: 0x1d1b17,
    edge: 0x1d1b17,
    edgeOpacity: 0.55,
    floor: 0x1d1b17,
    route: 0xb5482a,
    fogNear: 60,
    fogFar: 230,
    ambient: 2.4,
    key: 1.9,
    status: { reported: 0xb5482a, prelim: 0xd39a1a, stated: 0x1f7a80, bench: 0x5b4db8, scenario: 0x3a3a3a, unknown: 0x9a9384 },
  },
  b: {
    id: 'b',
    name: 'Night blueprint',
    bg: 0x070b14,
    ground: 0x0d1524,
    ink: 0xe6ecf5,
    edge: 0x9fb4d6,
    edgeOpacity: 0.7,
    floor: 0x2a3c5e,
    route: 0xff7a59,
    fogNear: 50,
    fogFar: 200,
    ambient: 1.6,
    key: 1.6,
    status: { reported: 0xff7a59, prelim: 0xffc24a, stated: 0x37d6c6, bench: 0x9d8cff, scenario: 0xcfd8e6, unknown: 0x5d6b85 },
  },
};

export function pickTheme() {
  const q = new URLSearchParams(location.search).get('dir');
  return THEMES[q] || THEMES.b;
}

export function cssColor(hex) {
  return '#' + hex.toString(16).padStart(6, '0');
}
