#!/usr/bin/env python3
"""Cohesive illustrative card art for the projects spotlight (9 cases)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

INK = "#1a1a1a"
MUTED = "#5c5c5c"
BLUE = "#4262ff"
LILAC = "#a78bfa"
PAPER = "#faf9fc"
TEAL = "#2dd4bf"
CORAL = "#f472b6"
AMBER = "#f59e0b"
SLATE = "#94a3b8"
W, H = 480, 640


def write(name, body):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-hidden="true">
{body}
</svg>
'''
    path = ROOT / name
    path.write_text(svg)
    print("wrote", path.name)


def base(uid, accent1, accent2):
    """Shared atmosphere: soft wash + faint grid + corner glow."""
    dots = []
    for y in range(48, H - 40, 36):
        for x in range(36, W - 24, 36):
            dots.append(f'<circle cx="{x}" cy="{y}" r="1.1" fill="{INK}" fill-opacity="0.06"/>')
    return f'''
  <defs>
    <linearGradient id="{uid}-wash" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{PAPER}"/>
      <stop offset="55%" stop-color="#f3f0fc"/>
      <stop offset="100%" stop-color="#ebe6f8"/>
    </linearGradient>
    <radialGradient id="{uid}-glowA" cx="22%" cy="18%" r="55%">
      <stop offset="0%" stop-color="{accent1}" stop-opacity="0.38"/>
      <stop offset="100%" stop-color="{accent1}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="{uid}-glowB" cx="88%" cy="78%" r="50%">
      <stop offset="0%" stop-color="{accent2}" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="{accent2}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#{uid}-wash)"/>
  <rect width="{W}" height="{H}" fill="url(#{uid}-glowA)"/>
  <rect width="{W}" height="{H}" fill="url(#{uid}-glowB)"/>
  {''.join(dots)}
  <rect x="28" y="28" width="{W-56}" height="{H-56}" rx="22" fill="none" stroke="{INK}" stroke-opacity="0.06" stroke-width="1.5"/>
'''


def index_mark(n):
    return f'''
  <text x="52" y="72" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.16em" fill="{BLUE}">{n:02d}</text>
'''


def card_zones():
    # Five soft zone tiles — taxonomy map
    zones = [
        (68, 160, TEAL), (190, 160, LILAC), (312, 160, SLATE),
        (128, 300, CORAL), (250, 300, AMBER),
    ]
    tiles = []
    for i, (x, y, c) in enumerate(zones):
        tiles.append(f'''
  <rect x="{x}" y="{y}" width="100" height="110" rx="18" fill="#fff" fill-opacity="0.72" stroke="{c}" stroke-opacity="0.45" stroke-width="2"/>
  <circle cx="{x+50}" cy="{y+48}" r="22" fill="{c}" fill-opacity="0.18"/>
  <circle cx="{x+50}" cy="{y+48}" r="9" fill="{c}"/>
  <rect x="{x+28}" y="{y+78}" width="44" height="8" rx="4" fill="{INK}" fill-opacity="0.12"/>
''')
    # connector threads
    lines = f'''
  <path d="M168 215 H190 M290 215 H312 M178 270 L178 300 M290 270 L290 300" fill="none" stroke="{BLUE}" stroke-opacity="0.25" stroke-width="2" stroke-dasharray="4 6"/>
'''
    write("card-ai-adoption-zones.svg", base("c1", LILAC, TEAL) + index_mark(1) + lines + "".join(tiles) + f'''
  <text x="52" y="560" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Five zones</text>
  <text x="52" y="588" font-family="Manrope, sans-serif" font-size="14" fill="{MUTED}">One shared taxonomy</text>
''')


def card_signals():
    # Concentric pulse + standing waveform
    rings = []
    for i, r in enumerate([50, 90, 130, 170]):
        op = round(0.45 - i * 0.08, 2)
        rings.append(f'<circle cx="240" cy="300" r="{r}" fill="none" stroke="{BLUE}" stroke-opacity="{op}" stroke-width="2.5"/>')
    wave = "M90 470"
    for i in range(0, 16):
        x = 90 + i * 20
        y = 470 + (18 if i % 2 else -22) * (1 if i % 3 else 0.4)
        wave += f" L{x} {y}"
    write("card-always-on-signals.svg", base("c2", BLUE, LILAC) + index_mark(2) + "".join(rings) + f'''
  <circle cx="240" cy="300" r="22" fill="{LILAC}"/>
  <circle cx="240" cy="300" r="10" fill="#fff" fill-opacity="0.9"/>
  <path d="{wave}" fill="none" stroke="{TEAL}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="52" y="560" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Always on</text>
  <text x="52" y="588" font-family="Manrope, sans-serif" font-size="14" fill="{MUTED}">CSAT × PMF pulse</text>
''')


def card_audiences():
    # Three overlapping audience arcs / soft figures
    figs = [
        (150, 320, LILAC, 0.9),
        (240, 280, BLUE, 1.0),
        (330, 320, TEAL, 0.9),
    ]
    parts = []
    for cx, cy, c, s in figs:
        parts.append(f'''
  <ellipse cx="{cx}" cy="{cy+70}" rx="{58*s}" ry="{78*s}" fill="{c}" fill-opacity="0.22"/>
  <circle cx="{cx}" cy="{cy-20}" r="{32*s}" fill="{c}" fill-opacity="0.55"/>
  <path d="M{cx-40*s} {cy+40} Q{cx} {cy+110} {cx+40*s} {cy+40}" fill="{c}" fill-opacity="0.35"/>
''')
    write("card-new-audiences.svg", base("c3", CORAL, LILAC) + index_mark(3) + "".join(parts) + f'''
  <circle cx="150" cy="200" r="6" fill="{LILAC}"/>
  <circle cx="240" cy="170" r="6" fill="{BLUE}"/>
  <circle cx="330" cy="200" r="6" fill="{TEAL}"/>
  <path d="M156 200 Q240 140 324 200" fill="none" stroke="{INK}" stroke-opacity="0.15" stroke-width="2" stroke-dasharray="3 5"/>
  <text x="52" y="560" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">New audiences</text>
  <text x="52" y="588" font-family="Manrope, sans-serif" font-size="14" fill="{MUTED}">Three designable profiles</text>
''')


def card_lca():
    # Elbow / BIC curve with class nodes
    pts = [(90, 420), (150, 300), (210, 230), (270, 200), (330, 185), (390, 178)]
    path = "M" + " L".join(f"{x},{y}" for x, y in pts)
    nodes = []
    for i, (x, y) in enumerate(pts):
        c = [SLATE, LILAC, BLUE, TEAL, CORAL, AMBER][i]
        r = 8 if i == 3 else 6
        nodes.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>')
    # highlight 5-class
    hx, hy = pts[3]
    write("card-segmentation-lca.svg", base("c4", LILAC, AMBER) + index_mark(4) + f'''
  <line x1="80" y1="160" x2="80" y2="450" stroke="{INK}" stroke-opacity="0.1" stroke-width="2"/>
  <line x1="80" y1="450" x2="410" y2="450" stroke="{INK}" stroke-opacity="0.1" stroke-width="2"/>
  <path d="{path}" fill="none" stroke="{BLUE}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  {''.join(nodes)}
  <circle cx="{hx}" cy="{hy}" r="18" fill="none" stroke="{BLUE}" stroke-width="2" stroke-opacity="0.5"/>
  <text x="{hx}" y="{hy-28}" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="12" font-weight="700" fill="{BLUE}">5-class</text>
  <text x="52" y="560" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Latent classes</text>
  <text x="52" y="588" font-family="Manrope, sans-serif" font-size="14" fill="{MUTED}">Fit over averages</text>
''')


def card_non_adopters():
    # Funnel mouth → many outside, few inside
    outs = []
    import random
    rng = random.Random(7)
    for _ in range(42):
        ang = rng.uniform(0, 6.28)
        dist = rng.uniform(95, 165)
        x = 240 + dist * __import__("math").cos(ang)
        y = 290 + dist * __import__("math").sin(ang) * 0.85
        outs.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rng.choice([3,4,5])}" fill="{SLATE}" fill-opacity="0.35"/>')
    ins = []
    for _ in range(7):
        x = 240 + rng.uniform(-28, 28)
        y = 290 + rng.uniform(-28, 28)
        ins.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{BLUE}" fill-opacity="0.85"/>')
    write("card-ai-canvas-non-adopters.svg", base("c5", SLATE, CORAL) + index_mark(5) + f'''
  <circle cx="240" cy="290" r="78" fill="#fff" fill-opacity="0.55" stroke="{BLUE}" stroke-opacity="0.35" stroke-width="2.5" stroke-dasharray="6 8"/>
  {''.join(outs)}
  {''.join(ins)}
  <text x="52" y="560" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Non-adopters</text>
  <text x="52" y="588" font-family="Manrope, sans-serif" font-size="14" fill="{MUTED}">Access ≠ adoption</text>
''')


def card_data_stories():
    # Story frames + listening bars
    panels = []
    for i, x in enumerate([78, 178, 278]):
        c = [LILAC, BLUE, TEAL][i]
        panels.append(f'''
  <rect x="{x}" y="180" width="88" height="220" rx="16" fill="#fff" fill-opacity="0.75" stroke="{c}" stroke-opacity="0.4" stroke-width="2"/>
  <rect x="{x+16}" y="210" width="56" height="8" rx="4" fill="{c}" fill-opacity="0.35"/>
  <rect x="{x+16}" y="228" width="40" height="6" rx="3" fill="{INK}" fill-opacity="0.1"/>
  <rect x="{x+16}" y="244" width="48" height="6" rx="3" fill="{INK}" fill-opacity="0.08"/>
''')
    bars = ""
    for i in range(12):
        h = [18, 32, 48, 28, 55, 36, 62, 40, 50, 24, 44, 30][i]
        bars += f'<rect x="{90+i*24}" y="{480-h}" width="14" height="{h}" rx="4" fill="{BLUE}" fill-opacity="{0.25 + (i%4)*0.12}"/>'
    write("card-data-stories.svg", base("c6", BLUE, TEAL) + index_mark(6) + "".join(panels) + f'''
  <g transform="translate(0,-20)">{bars}</g>
  <text x="52" y="560" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Data stories</text>
  <text x="52" y="588" font-family="Manrope, sans-serif" font-size="14" fill="{MUTED}">Listening before build</text>
''')


def card_bundles():
    # Core plane + AI enhancer glow stacked
    write("card-purchase-intent-bundles.svg", base("c7", AMBER, LILAC) + index_mark(7) + f'''
  <rect x="90" y="280" width="300" height="160" rx="24" fill="#fff" fill-opacity="0.8" stroke="{INK}" stroke-opacity="0.08" stroke-width="2"/>
  <rect x="110" y="300" width="160" height="14" rx="7" fill="{INK}" fill-opacity="0.12"/>
  <rect x="110" y="328" width="120" height="10" rx="5" fill="{INK}" fill-opacity="0.08"/>
  <rect x="110" y="360" width="100" height="40" rx="12" fill="{BLUE}" fill-opacity="0.9"/>
  <text x="160" y="386" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="12" font-weight="700" fill="#fff">CORE</text>

  <rect x="120" y="170" width="300" height="160" rx="24" fill="{LILAC}" fill-opacity="0.22" stroke="{LILAC}" stroke-opacity="0.55" stroke-width="2"/>
  <circle cx="340" cy="230" r="36" fill="{LILAC}" fill-opacity="0.45"/>
  <circle cx="340" cy="230" r="16" fill="{BLUE}" fill-opacity="0.7"/>
  <text x="170" y="230" font-family="Syne, Manrope, sans-serif" font-size="14" font-weight="700" fill="{BLUE}">AI enhancer</text>
  <text x="170" y="252" font-family="Manrope, sans-serif" font-size="12" fill="{MUTED}">sits on the hook</text>

  <text x="52" y="560" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Bundles</text>
  <text x="52" y="588" font-family="Manrope, sans-serif" font-size="14" fill="{MUTED}">Hook first, AI second</text>
''')


def card_flows():
    # Weekly research rhythm — orbit loop
    checks = []
    import math
    for i in range(7):
        ang = -math.pi / 2 + i * (2 * math.pi / 7)
        x = 240 + 120 * math.cos(ang)
        y = 300 + 120 * math.sin(ang)
        c = TEAL if i < 5 else LILAC
        checks.append(f'''
  <circle cx="{x:.1f}" cy="{y:.1f}" r="18" fill="#fff" fill-opacity="0.85" stroke="{c}" stroke-width="2.5"/>
  <path d="M{x-6:.1f} {y:.1f} l4 5 l8-10" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
''')
    write("card-flows-continuous-research.svg", base("c8", TEAL, BLUE) + index_mark(8) + f'''
  <circle cx="240" cy="300" r="120" fill="none" stroke="{BLUE}" stroke-opacity="0.2" stroke-width="3" stroke-dasharray="8 10"/>
  <circle cx="240" cy="300" r="48" fill="{BLUE}" fill-opacity="0.12"/>
  <text x="240" y="296" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="800" fill="{BLUE}">WEEKLY</text>
  <text x="240" y="316" text-anchor="middle" font-family="Manrope, sans-serif" font-size="11" fill="{MUTED}">rhythm</text>
  {''.join(checks)}
  <text x="52" y="560" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Continuous</text>
  <text x="52" y="588" font-family="Manrope, sans-serif" font-size="14" fill="{MUTED}">Evidence-gated shipping</text>
''')


def card_post_canvas():
    # Ranked friction bars + memory thread
    ranks = [
        (0.92, CORAL, "Memory"),
        (0.74, LILAC, "Context"),
        (0.58, BLUE, "Flow"),
        (0.42, TEAL, "Discover"),
        (0.28, SLATE, "Other"),
    ]
    bars = []
    y0 = 180
    for i, (pct, c, label) in enumerate(ranks):
        y = y0 + i * 52
        w = 60 + pct * 260
        bars.append(f'''
  <text x="70" y="{y+18}" font-family="Syne, Manrope, sans-serif" font-size="12" font-weight="700" fill="{MUTED}">{i+1}</text>
  <rect x="96" y="{y}" width="{w:.0f}" height="28" rx="10" fill="{c}" fill-opacity="0.55"/>
  <text x="{104}" y="{y+19}" font-family="Manrope, sans-serif" font-size="12" font-weight="600" fill="{INK}">{label}</text>
''')
    write("card-post-canvas-rollout.svg", base("c9", CORAL, LILAC) + index_mark(9) + "".join(bars) + f'''
  <path d="M400 170 C430 250, 350 320, 400 420" fill="none" stroke="{BLUE}" stroke-opacity="0.3" stroke-width="2.5" stroke-dasharray="4 6"/>
  <circle cx="400" cy="170" r="7" fill="{BLUE}"/>
  <circle cx="400" cy="420" r="7" fill="{LILAC}"/>
  <text x="52" y="560" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Post-rollout</text>
  <text x="52" y="588" font-family="Manrope, sans-serif" font-size="14" fill="{MUTED}">Ranked, fixable friction</text>
''')


if __name__ == "__main__":
    card_zones()
    card_signals()
    card_audiences()
    card_lca()
    card_non_adopters()
    card_data_stories()
    card_bundles()
    card_flows()
    card_post_canvas()
    print("all 9 card arts ready")
