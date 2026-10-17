#!/usr/bin/env python3
"""Regenerate project case visuals as crisp SVGs matching the portfolio site palette."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

INK = "#1a1a1a"
MUTED = "#5c5c5c"
BLUE = "#4262ff"
LILAC = "#a78bfa"
PAPER = "#faf9fc"
CARD = "#ffffff"
LINE = "rgba(26,26,26,0.10)"
TEAL = "#2dd4bf"
CORAL = "#f472b6"
AMBER = "#f59e0b"
SLATE = "#94a3b8"


def wrap(w, h, body, bg=PAPER):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">
  <rect width="{w}" height="{h}" fill="{bg}" rx="16"/>
  {body}
</svg>
'''


def write(name, svg):
    path = ROOT / name
    path.write_text(svg)
    print("wrote", path.name)


# ── AI Adoption Zones ───────────────────────────────────────────────────────

def ai_zones_cover():
    zones = [
        ("AI Zone 1", TEAL, "18%"),
        ("AI Zone 2", LILAC, "27%"),
        ("AI Zone 3", SLATE, "22%"),
        ("AI Zone 4", CORAL, "14%"),
        ("AI Zone 5", AMBER, "19%"),
    ]
    cards = []
    gap, w = 16, 152
    for i, (name, color, pct) in enumerate(zones):
        x = 40 + i * (w + gap)
        cards.append(f'''
  <rect x="{x}" y="118" width="{w}" height="190" rx="14" fill="{CARD}" stroke="{LINE}"/>
  <circle cx="{x+w/2}" cy="178" r="20" fill="{color}" fill-opacity="0.18"/>
  <circle cx="{x+w/2}" cy="178" r="9" fill="{color}"/>
  <text x="{x+w/2}" y="228" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="14" font-weight="700" fill="{INK}">{name}</text>
  <text x="{x+w/2}" y="258" text-anchor="middle" font-family="Manrope, sans-serif" font-size="26" font-weight="700" fill="{BLUE}">{pct}</text>
  <text x="{x+w/2}" y="282" text-anchor="middle" font-family="Manrope, sans-serif" font-size="12" fill="{MUTED}">of sample</text>''')
    body = f'''
  <text x="40" y="48" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.14em" fill="{BLUE}">FRAMEWORK</text>
  <text x="40" y="86" font-family="Syne, Manrope, sans-serif" font-size="30" font-weight="800" fill="{INK}">AI Adoption Zones</text>
  {''.join(cards)}
'''
    write("ai-adoption-zones-cover.svg", wrap(900, 340, body))


def ai_zones_v1():
    # scatter: plot area well below title; labels outside each cluster
    pts = [
        (TEAL, [(580, 150), (610, 170), (640, 145), (665, 175), (600, 130), (650, 155), (630, 125)]),
        (LILAC, [(360, 250), (395, 275), (380, 300), (420, 265), (350, 285), (405, 315), (385, 240)]),
        (CORAL, [(160, 155), (190, 175), (175, 140), (205, 160), (145, 185), (180, 200)]),
        (AMBER, [(580, 340), (615, 360), (645, 325), (600, 375), (660, 350), (630, 380)]),
        (SLATE, [(165, 350), (195, 370), (150, 385), (180, 335), (210, 360), (170, 395)]),
    ]
    labels = [
        (690, 140, TEAL, "AI Zone 1"),
        (445, 235, LILAC, "AI Zone 2"),
        (215, 135, CORAL, "AI Zone 4"),
        (690, 330, AMBER, "AI Zone 5"),
        (220, 340, SLATE, "AI Zone 3"),
    ]
    circles = []
    for color, group in pts:
        for x, y in group:
            circles.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{color}" fill-opacity="0.9"/>')
            circles.append(f'<circle cx="{x}" cy="{y}" r="12" fill="{color}" fill-opacity="0.12"/>')
    labs = "".join(
        f'<text x="{x}" y="{y}" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" fill="{c}">{t}</text>'
        for x, y, c, t in labels
    )
    body = f'''
  <text x="48" y="40" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">DISTRIBUTION</text>
  <text x="48" y="72" font-family="Syne, Manrope, sans-serif" font-size="24" font-weight="800" fill="{INK}">Capability × readiness</text>
  <line x1="110" y1="430" x2="760" y2="430" stroke="{LINE}" stroke-width="2"/>
  <line x1="110" y1="430" x2="110" y2="110" stroke="{LINE}" stroke-width="2"/>
  <line x1="110" y1="270" x2="760" y2="270" stroke="{LINE}" stroke-dasharray="4 6"/>
  <line x1="435" y1="430" x2="435" y2="110" stroke="{LINE}" stroke-dasharray="4 6"/>
  <text x="435" y="462" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">Organizational readiness →</text>
  <text x="34" y="280" text-anchor="middle" transform="rotate(-90 34 280)" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">Individual capability →</text>
  {''.join(circles)}
  {labs}
'''
    write("ai-adoption-zones-visual-1.svg", wrap(820, 500, body))


def ai_zones_v2():
    # stacked area / line chart over months
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
    # cumulative shares per month for 5 zones (sum ~100)
    series = [
        # zone1..zone5 bottom to top proportions per month
        [14, 15, 16, 17, 18, 18, 19, 18],
        [22, 23, 24, 25, 26, 27, 27, 27],
        [24, 23, 23, 22, 22, 22, 21, 22],
        [18, 17, 16, 15, 15, 14, 14, 14],
        [22, 22, 21, 21, 19, 19, 19, 19],
    ]
    colors = [TEAL, LILAC, SLATE, CORAL, AMBER]
    names = ["AI Zone 1", "AI Zone 2", "AI Zone 3", "AI Zone 4", "AI Zone 5"]
    left, right, top, bottom = 80, 720, 110, 360
    n = len(months)
    xs = [left + i * (right - left) / (n - 1) for i in range(n)]

    def y_at(pct):
        return bottom - (pct / 100) * (bottom - top)

    # build stacked paths bottom-up
    cum = [0] * n
    areas = []
    lines = []
    for si, (row, color) in enumerate(zip(series, colors)):
        lower = cum[:]
        cum = [cum[i] + row[i] for i in range(n)]
        upper = cum[:]
        pts_up = " ".join(f"{xs[i]:.1f},{y_at(upper[i]):.1f}" for i in range(n))
        pts_dn = " ".join(f"{xs[i]:.1f},{y_at(lower[i]):.1f}" for i in range(n - 1, -1, -1))
        areas.append(f'<polygon points="{pts_up} {pts_dn}" fill="{color}" fill-opacity="0.35"/>')
        lines.append(
            f'<polyline points="{" ".join(f"{xs[i]:.1f},{y_at(upper[i]):.1f}" for i in range(n))}" '
            f'fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
        )

    grid = "".join(
        f'<line x1="{left}" y1="{y}" x2="{right}" y2="{y}" stroke="{LINE}"/>'
        for y in (top, (top + bottom) / 2, bottom)
    )
    xlabels = "".join(
        f'<text x="{xs[i]:.1f}" y="{bottom + 28}" text-anchor="middle" '
        f'font-family="Manrope, sans-serif" font-size="12" fill="{MUTED}">{months[i]}</text>'
        for i in range(n)
    )
    legend = "".join(
        f'<circle cx="{80 + i * 130}" cy="400" r="5" fill="{colors[i]}"/>'
        f'<text x="{92 + i * 130}" y="404" font-family="Manrope, sans-serif" font-size="12" fill="{INK}">{names[i]}</text>'
        for i in range(5)
    )
    body = f'''
  <text x="48" y="40" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">SHARE</text>
  <text x="48" y="74" font-family="Syne, Manrope, sans-serif" font-size="24" font-weight="800" fill="{INK}">Zone distribution</text>
  {grid}
  <line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="{LINE}" stroke-width="2"/>
  <line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="{LINE}" stroke-width="2"/>
  {''.join(areas)}
  {''.join(lines)}
  {xlabels}
  {legend}
'''
    write("ai-adoption-zones-visual-2.svg", wrap(800, 440, body))


# ── Always-on Signals ───────────────────────────────────────────────────────

def always_cover():
    # line chart
    body = f'''
  <text x="48" y="48" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">SIGNAL</text>
  <text x="48" y="84" font-family="Syne, Manrope, sans-serif" font-size="28" font-weight="800" fill="{INK}">Monthly performance</text>
  <line x1="60" y1="140" x2="860" y2="140" stroke="{LINE}"/>
  <line x1="60" y1="220" x2="860" y2="220" stroke="{LINE}"/>
  <line x1="60" y1="300" x2="860" y2="300" stroke="{LINE}"/>
  <line x1="60" y1="380" x2="860" y2="380" stroke="{LINE}"/>
  <path d="M80 360 C180 340, 260 300, 340 250 S500 160, 580 140 S740 100, 840 80" fill="none" stroke="{TEAL}" stroke-width="4" stroke-linecap="round"/>
  <path d="M80 360 C180 340, 260 300, 340 250 S500 160, 580 140 S740 100, 840 80 L840 400 L80 400 Z" fill="{TEAL}" fill-opacity="0.12"/>
  <path d="M80 340 C200 320, 300 280, 400 260 S600 220, 720 200 S800 180, 840 170" fill="none" stroke="{LILAC}" stroke-width="3" stroke-linecap="round"/>
  <path d="M80 350 C200 310, 320 270, 420 250 S580 210, 700 180 S800 150, 840 140" fill="none" stroke="{AMBER}" stroke-width="3" stroke-linecap="round"/>
  <circle cx="840" cy="80" r="7" fill="{TEAL}"/>
  <g font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">
    <circle cx="60" cy="440" r="5" fill="{TEAL}"/><text x="72" y="444">CSAT</text>
    <circle cx="160" cy="440" r="5" fill="{LILAC}"/><text x="172" y="444">PMF</text>
    <circle cx="250" cy="440" r="5" fill="{AMBER}"/><text x="262" y="444">Baseline</text>
  </g>
'''
    write("always-on-signals-cover.svg", wrap(900, 480, body))


def always_v1():
    # spaced points + label offsets (dx, dy) so text never stacks
    # x,y,color,label,ldx,ldy
    items = [
        (500, 130, TEAL, "Kanban", 14, 4),
        (620, 145, BLUE, "Tables", 14, 4),
        (540, 195, TEAL, "Miro Engage", 14, 4),
        (480, 230, CORAL, "Sidekicks", 14, 4),
        (660, 210, BLUE, "AI Slides", 14, 4),
        (700, 255, BLUE, "Timeline", 14, 4),
        (230, 135, AMBER, "TalkTrack", 14, 4),
        (200, 185, TEAL, "Flows", 14, 4),
        (190, 330, TEAL, "Presentation", 14, 4),
        (280, 370, BLUE, "Prototyping", 14, 4),
    ]
    dots = []
    for x, y, c, lab, ldx, ldy in items:
        dots.append(
            f'<circle cx="{x}" cy="{y}" r="8" fill="{c}"/>'
            f'<text x="{x+ldx}" y="{y+ldy}" font-family="Manrope, sans-serif" font-size="12" font-weight="600" fill="{INK}">{lab}</text>'
        )
    body = f'''
  <text x="40" y="36" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">QUADRANTS</text>
  <text x="40" y="66" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">CSAT × PMF</text>
  <line x1="90" y1="420" x2="780" y2="420" stroke="{LINE}" stroke-width="2"/>
  <line x1="90" y1="420" x2="90" y2="100" stroke="{LINE}" stroke-width="2"/>
  <line x1="90" y1="260" x2="780" y2="260" stroke="{LINE}" stroke-dasharray="5 6"/>
  <line x1="435" y1="420" x2="435" y2="100" stroke="{LINE}" stroke-dasharray="5 6"/>
  <text x="600" y="118" font-family="Manrope, sans-serif" font-size="12" fill="{MUTED}">loved &amp; needed</text>
  <text x="170" y="400" font-family="Manrope, sans-serif" font-size="12" fill="{MUTED}">neither yet</text>
  <text x="435" y="458" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">CSAT top-2-box (%) →</text>
  <text x="32" y="270" text-anchor="middle" transform="rotate(-90 32 270)" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">PMF top-1-box (%) →</text>
  {''.join(dots)}
'''
    write("always-on-signals-visual-1.svg", wrap(860, 490, body))


def always_v2():
    import math
    # four donut charts
    metrics = [
        ("CSAT", 72, TEAL),
        ("PMF", 41, LILAC),
        ("NPS", 28, BLUE),
        ("Effort", 63, AMBER),
    ]

    def donut(cx, cy, r, pct, color, label):
        # background ring + arc for pct
        circ = 2 * math.pi * r
        dash = circ * pct / 100
        gap = circ - dash
        return f'''
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LINE}" stroke-width="18"/>
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="18"
    stroke-linecap="round" stroke-dasharray="{dash:.1f} {gap:.1f}"
    transform="rotate(-90 {cx} {cy})"/>
  <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">{pct}%</text>
  <text x="{cx}" y="{cy+40+r}" text-anchor="middle" font-family="Manrope, sans-serif" font-size="14" font-weight="600" fill="{MUTED}">{label}</text>'''

    rings = "".join(
        donut(130 + i * 180, 200, 62, pct, color, name)
        for i, (name, pct, color) in enumerate(metrics)
    )
    body = f'''
  <text x="48" y="44" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">SIGNALS</text>
  <text x="48" y="78" font-family="Syne, Manrope, sans-serif" font-size="24" font-weight="800" fill="{INK}">Standing health</text>
  {rings}
'''
    write("always-on-signals-visual-2.svg", wrap(820, 360, body))


# ── New Audiences ───────────────────────────────────────────────────────────

def new_aud_cover():
    body = f'''
  <text x="48" y="48" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">AUDIENCES</text>
  <text x="48" y="86" font-family="Syne, Manrope, sans-serif" font-size="28" font-weight="800" fill="{INK}">Three priority profiles</text>
  <circle cx="170" cy="230" r="70" fill="{CORAL}" fill-opacity="0.92"/>
  <text x="170" y="224" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="14" font-weight="700" fill="#fff">Profile 1</text>
  <text x="170" y="246" text-anchor="middle" font-family="Manrope, sans-serif" font-size="12" fill="#fff" opacity="0.9">Super social</text>
  <circle cx="400" cy="215" r="88" fill="{TEAL}" fill-opacity="0.92"/>
  <text x="400" y="208" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="15" font-weight="700" fill="#fff">Profile 2</text>
  <text x="400" y="232" text-anchor="middle" font-family="Manrope, sans-serif" font-size="12" fill="#fff" opacity="0.9">Super curious</text>
  <circle cx="640" cy="235" r="62" fill="{LILAC}" fill-opacity="0.95"/>
  <text x="640" y="228" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="14" font-weight="700" fill="#fff">Profile 3</text>
  <text x="640" y="250" text-anchor="middle" font-family="Manrope, sans-serif" font-size="12" fill="#fff" opacity="0.9">Super techy</text>
  <line x1="70" y1="360" x2="740" y2="360" stroke="{LINE}" stroke-width="2"/>
  <polygon points="740,360 728,354 728,366" fill="{MUTED}"/>
  <text x="405" y="392" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">monetization potential →</text>
'''
    write("new-audiences-cover.svg", wrap(820, 420, body))


def new_aud_v1():
    # non-overlapping bubbles with labels underneath
    bubbles = [
        (130, 175, 42, "#b45309", "P4", "Heavy listeners"),
        (300, 165, 52, LILAC, "P3", "Super techy"),
        (500, 155, 70, TEAL, "P2", "Super curious"),
        (700, 165, 58, CORAL, "P1", "Super social"),
    ]
    parts = []
    for x, y, r, c, code, name in bubbles:
        parts.append(f'''
  <circle cx="{x}" cy="{y}" r="{r}" fill="{c}" fill-opacity="0.92"/>
  <text x="{x}" y="{y+5}" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="15" font-weight="700" fill="#fff">{code}</text>
  <text x="{x}" y="{y+r+28}" text-anchor="middle" font-family="Manrope, sans-serif" font-size="12" font-weight="600" fill="{INK}">{name}</text>''')
    body = f'''
  <text x="40" y="40" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">PROFILES</text>
  <text x="40" y="72" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Monetization spectrum</text>
  {''.join(parts)}
  <line x1="60" y1="300" x2="780" y2="300" stroke="{LINE}" stroke-width="2"/>
  <polygon points="780,300 768,294 768,306" fill="{MUTED}"/>
  <text x="420" y="332" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">monetization potential →</text>
'''
    write("new-audiences-visual-1.svg", wrap(840, 360, body))


def new_aud_v2():
    rows = [
        ("Willingness to pay", 0.82, 0.71, 0.54),
        ("Tech adoption", 0.61, 0.88, 0.76),
        ("Social density", 0.91, 0.45, 0.38),
        ("Curiosity", 0.55, 0.93, 0.67),
    ]
    colors = [CORAL, TEAL, LILAC]
    cells = []
    for ri, (label, *vals) in enumerate(rows):
        y = 130 + ri * 56
        cells.append(f'<text x="48" y="{y+22}" font-family="Manrope, sans-serif" font-size="14" font-weight="600" fill="{INK}">{label}</text>')
        for ci, v in enumerate(vals):
            x = 240 + ci * 160
            w = 40 + v * 90
            cells.append(f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="10" fill="{colors[ci]}" fill-opacity="{0.35 + v*0.55}"/>')
    body = f'''
  <text x="48" y="48" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">COMPARE</text>
  <text x="48" y="82" font-family="Syne, Manrope, sans-serif" font-size="24" font-weight="800" fill="{INK}">Profile trait map</text>
  <text x="280" y="110" text-anchor="middle" font-family="Manrope, sans-serif" font-size="12" font-weight="700" fill="{MUTED}">P1</text>
  <text x="440" y="110" text-anchor="middle" font-family="Manrope, sans-serif" font-size="12" font-weight="700" fill="{MUTED}">P2</text>
  <text x="600" y="110" text-anchor="middle" font-family="Manrope, sans-serif" font-size="12" font-weight="700" fill="{MUTED}">P3</text>
  {''.join(cells)}
'''
    write("new-audiences-visual-2.svg", wrap(760, 380, body))


# ── Segmentation LCA ────────────────────────────────────────────────────────

def seg_cover():
    # elbow / model-fit style line chart instead of bubbles
    ks = list(range(1, 9))
    aic = [9.2, 7.4, 5.8, 4.9, 4.5, 4.3, 4.2, 4.15]
    bic = [9.6, 7.9, 6.4, 5.6, 5.4, 5.35, 5.4, 5.5]
    left, right, top, bottom = 90, 680, 140, 340

    def xy(i, v, vmin=4, vmax=10):
        x = left + i * (right - left) / (len(ks) - 1)
        y = bottom - (v - vmin) / (vmax - vmin) * (bottom - top)
        return x, y

    def poly(vals, color):
        pts = " ".join(f"{xy(i,v)[0]:.1f},{xy(i,v)[1]:.1f}" for i, v in enumerate(vals))
        return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'

    dots_a = "".join(
        f'<circle cx="{xy(i,v)[0]:.1f}" cy="{xy(i,v)[1]:.1f}" r="5" fill="{BLUE}"/>'
        for i, v in enumerate(aic)
    )
    dots_b = "".join(
        f'<circle cx="{xy(i,v)[0]:.1f}" cy="{xy(i,v)[1]:.1f}" r="5" fill="{LILAC}"/>'
        for i, v in enumerate(bic)
    )
    # highlight chosen k=5
    hx, hy = xy(4, aic[4])
    xlabels = "".join(
        f'<text x="{xy(i,0)[0]:.1f}" y="{bottom+28}" text-anchor="middle" font-family="Manrope, sans-serif" font-size="12" fill="{MUTED}">{k}</text>'
        for i, k in enumerate(ks)
    )
    body = f'''
  <text x="48" y="44" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">METHOD</text>
  <text x="48" y="80" font-family="Syne, Manrope, sans-serif" font-size="28" font-weight="800" fill="{INK}">Latent Class Analysis</text>
  <text x="48" y="112" font-family="Manrope, sans-serif" font-size="14" fill="{MUTED}">Model fit by number of classes (k)</text>
  <line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="{LINE}" stroke-width="2"/>
  <line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="{LINE}" stroke-width="2"/>
  {poly(aic, BLUE)}
  {poly(bic, LILAC)}
  {dots_a}{dots_b}
  <circle cx="{hx:.1f}" cy="{hy:.1f}" r="10" fill="none" stroke="{TEAL}" stroke-width="2.5"/>
  <text x="{hx+14:.1f}" y="{hy-10:.1f}" font-family="Manrope, sans-serif" font-size="12" font-weight="700" fill="{TEAL}">k = 5</text>
  {xlabels}
  <text x="{(left+right)/2:.0f}" y="{bottom+52}" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">Number of classes (k) →</text>
  <circle cx="520" cy="120" r="5" fill="{BLUE}"/><text x="532" y="124" font-family="Manrope, sans-serif" font-size="12" fill="{MUTED}">AIC</text>
  <circle cx="590" cy="120" r="5" fill="{LILAC}"/><text x="602" y="124" font-family="Manrope, sans-serif" font-size="12" fill="{MUTED}">BIC</text>
'''
    write("segmentation-lca-cover.svg", wrap(760, 420, body))


def seg_v1():
    metrics = ["Avg Score", "T2B %", "Enterprise %", "EPD %", "Active %", "LATAM %", "EMEA %", "APAC %", "USA & CA %"]
    # values 0-1 for color intensity per class
    data = [
        [0.8, 0.4, 0.35, 0.3, 0.55],
        [0.7, 0.45, 0.6, 0.35, 0.85],
        [0.55, 0.3, 0.4, 0.5, 0.9],
        [0.4, 0.55, 0.7, 0.45, 0.65],
        [0.5, 0.6, 0.55, 0.7, 0.4],
        [0.35, 0.5, 0.45, 0.2, 0.55],
        [0.85, 0.4, 0.5, 0.55, 0.6],
        [0.75, 0.55, 0.35, 0.5, 0.45],
        [0.6, 0.7, 0.65, 0.55, 0.5],
    ]
    def color(v):
        if v >= 0.75: return TEAL
        if v >= 0.55: return LILAC
        if v >= 0.4: return AMBER
        return CORAL

    cells = []
    for ri, row in enumerate(data):
        y = 110 + ri * 36
        cells.append(f'<text x="40" y="{y+18}" font-family="Manrope, sans-serif" font-size="12" fill="{MUTED}">{metrics[ri]}</text>')
        for ci, v in enumerate(row):
            x = 160 + ci * 110
            cells.append(f'<rect x="{x}" y="{y}" width="96" height="26" rx="8" fill="{color(v)}" fill-opacity="{0.35+v*0.55}"/>')
    headers = "".join(
        f'<text x="{210+i*110}" y="90" text-anchor="middle" font-family="Manrope, sans-serif" font-size="12" font-weight="700" fill="{INK}">Class {i+1}</text>'
        for i in range(5)
    )
    body = f'''
  <text x="40" y="42" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">HEATMAP</text>
  <text x="40" y="72" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Class profiles</text>
  {headers}
  {''.join(cells)}
'''
    write("segmentation-lca-visual-1.svg", wrap(740, 460, body))


def seg_v2():
    sizes = [22, 18, 27, 15, 18]
    colors = [TEAL, LILAC, BLUE, CORAL, AMBER]
    start = -90
    arcs = []
    cx, cy, r = 220, 240, 110
    import math
    total = sum(sizes)
    a0 = math.radians(start)
    for i, (s, c) in enumerate(zip(sizes, colors)):
        sweep = s / total * 360
        a1 = a0 + math.radians(sweep)
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        large = 1 if sweep > 180 else 0
        arcs.append(f'<path d="M {cx} {cy} L {x0:.1f} {y0:.1f} A {r} {r} 0 {large} 1 {x1:.1f} {y1:.1f} Z" fill="{c}" fill-opacity="0.85"/>')
        a0 = a1
    legend = "".join(
        f'<circle cx="420" cy="{120+i*40}" r="7" fill="{colors[i]}"/><text x="440" y="{125+i*40}" font-family="Manrope, sans-serif" font-size="14" fill="{INK}">Class {i+1} · {sizes[i]}%</text>'
        for i in range(5)
    )
    body = f'''
  <text x="40" y="42" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">MIX</text>
  <text x="40" y="72" font-family="Syne, Manrope, sans-serif" font-size="22" font-weight="800" fill="{INK}">Class share</text>
  <circle cx="220" cy="240" r="48" fill="{PAPER}"/>
  {''.join(arcs)}
  <circle cx="220" cy="240" r="48" fill="{PAPER}"/>
  {legend}
'''
    write("segmentation-lca-visual-2.svg", wrap(700, 400, body))


# ── Non-adopters ────────────────────────────────────────────────────────────

def non_adopters():
    import math
    # donut only — no stats %, no "why unaware"
    sizes = [71, 14, 11, 4]
    colors = [LILAC, TEAL, AMBER, CORAL]
    labels = ["One-time", "Weekly", "Monthly", "Daily"]
    cx, cy, r_out, r_in = 280, 210, 110, 68
    wedges = []
    a = -90.0
    for s, c in zip(sizes, colors):
        sweep = s / 100 * 360
        a0, a1 = math.radians(a), math.radians(a + sweep)
        x0, y0 = cx + r_out * math.cos(a0), cy + r_out * math.sin(a0)
        x1, y1 = cx + r_out * math.cos(a1), cy + r_out * math.sin(a1)
        xi0, yi0 = cx + r_in * math.cos(a0), cy + r_in * math.sin(a0)
        xi1, yi1 = cx + r_in * math.cos(a1), cy + r_in * math.sin(a1)
        large = 1 if sweep > 180 else 0
        wedges.append(
            f'<path d="M {x0:.1f} {y0:.1f} A {r_out} {r_out} 0 {large} 1 {x1:.1f} {y1:.1f} '
            f'L {xi1:.1f} {yi1:.1f} A {r_in} {r_in} 0 {large} 0 {xi0:.1f} {yi0:.1f} Z" fill="{c}"/>'
        )
        a += sweep
    legend = "".join(
        f'<circle cx="480" cy="{150+i*42}" r="7" fill="{colors[i]}"/>'
        f'<text x="500" y="{155+i*42}" font-family="Manrope, sans-serif" font-size="15" fill="{INK}">{labels[i]}</text>'
        for i in range(4)
    )
    body = f'''
  <text x="48" y="44" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">FUNNEL</text>
  <text x="48" y="80" font-family="Syne, Manrope, sans-serif" font-size="24" font-weight="800" fill="{INK}">AI activity cohorts</text>
  {''.join(wedges)}
  <text x="{cx}" y="{cy+6}" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="18" font-weight="800" fill="{INK}">AI</text>
  {legend}
'''
    write("ai-canvas-non-adopters-cover.svg", wrap(720, 360, body))


# ── Data stories ────────────────────────────────────────────────────────────

def data_stories():
    body = f'''
  <text x="48" y="56" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">NARRATIVE</text>
  <text x="48" y="96" font-family="Syne, Manrope, sans-serif" font-size="30" font-weight="800" fill="{INK}">Data Stories</text>
  <text x="48" y="130" font-family="Manrope, sans-serif" font-size="15" fill="{MUTED}">From raw tables to executive-ready narratives</text>
  <rect x="80" y="180" width="160" height="100" rx="12" fill="{CARD}" stroke="{LINE}"/>
  <text x="160" y="238" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">Raw signal</text>
  <path d="M250 230 H310" stroke="{LILAC}" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="320" y="170" width="180" height="120" rx="12" fill="{CARD}" stroke="{LILAC}"/>
  <text x="410" y="235" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" font-weight="600" fill="{INK}">Structured insight</text>
  <path d="M510 230 H570" stroke="{BLUE}" stroke-width="2"/>
  <rect x="580" y="155" width="200" height="150" rx="14" fill="{BLUE}"/>
  <text x="680" y="230" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="15" font-weight="700" fill="#fff">Decision story</text>
  <defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{LILAC}"/></marker></defs>
'''
    write("data-stories-cover.svg", wrap(860, 380, body))


# ── Purchase intent ─────────────────────────────────────────────────────────

def purchase_cover():
    prices = ["$11", "$14", "$17", "$20", "$23", "$26", "$29"]
    vals = [52, 58, 65, 61, 70, 78, 67]
    bars = []
    for i, (p, v) in enumerate(zip(prices, vals)):
        x = 430 + i * 50
        h = round(v * 2.0)
        y = 320 - h
        bars.append(f'''
  <rect x="{x}" y="{y}" width="34" height="{h}" rx="6" fill="{CORAL}" fill-opacity="0.85"/>
  <text x="{x+17}" y="{y-8}" text-anchor="middle" font-family="Manrope, sans-serif" font-size="10" font-weight="600" fill="{INK}">{v * 100}</text>
  <text x="{x+17}" y="348" text-anchor="middle" font-family="Manrope, sans-serif" font-size="11" fill="{MUTED}">{p}</text>''')
    body = f'''
  <text x="40" y="40" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">CONJOINT</text>
  <text x="40" y="72" font-family="Syne, Manrope, sans-serif" font-size="24" font-weight="800" fill="{INK}">Preference &amp; revenue</text>
  <text x="40" y="112" font-family="Manrope, sans-serif" font-size="13" font-weight="600" fill="{MUTED}">Unadjusted preference share</text>
  <rect x="40" y="128" width="340" height="200" rx="12" fill="{CARD}" stroke="{LINE}"/>
  <path d="M60 300 L60 155 L360 155 L360 300 Z" fill="{CORAL}" fill-opacity="0.22"/>
  <path d="M60 300 L60 215 C130 195, 210 235, 280 255 L360 265 L360 300 Z" fill="{TEAL}" fill-opacity="0.5"/>
  <path d="M60 300 L60 255 C140 245, 220 275, 360 285 L360 300 Z" fill="{LILAC}"/>
  <circle cx="60" cy="330" r="5" fill="{LILAC}"/><text x="72" y="334" font-family="Manrope, sans-serif" font-size="11" fill="{MUTED}">Core plan</text>
  <circle cx="160" cy="330" r="5" fill="{TEAL}"/><text x="172" y="334" font-family="Manrope, sans-serif" font-size="11" fill="{MUTED}">AI add-on</text>
  <circle cx="260" cy="330" r="5" fill="{CORAL}"/><text x="272" y="334" font-family="Manrope, sans-serif" font-size="11" fill="{MUTED}">Other</text>
  <text x="430" y="112" font-family="Manrope, sans-serif" font-size="13" font-weight="600" fill="{MUTED}">Revenue index</text>
  {''.join(bars)}
'''
    write("purchase-intent-bundles-cover.svg", wrap(820, 380, body))


def purchase_v1():
    # reuse cover style simpler focus chart
    body = f'''
  <text x="48" y="48" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">FINDING</text>
  <text x="48" y="84" font-family="Syne, Manrope, sans-serif" font-size="24" font-weight="800" fill="{INK}">What drives conversion</text>
  <rect x="48" y="130" width="220" height="160" rx="16" fill="{CARD}" stroke="{LINE}"/>
  <text x="158" y="190" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="18" font-weight="700" fill="{BLUE}">Baseline</text>
  <text x="158" y="220" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">Primary hook</text>
  <rect x="300" y="130" width="220" height="160" rx="16" fill="{CARD}" stroke="{LINE}"/>
  <text x="410" y="190" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="18" font-weight="700" fill="{LILAC}">Premium AI</text>
  <text x="410" y="220" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">Secondary enhancer</text>
  <rect x="552" y="130" width="220" height="160" rx="16" fill="{BLUE}"/>
  <text x="662" y="190" text-anchor="middle" font-family="Syne, Manrope, sans-serif" font-size="18" font-weight="700" fill="#fff">Clear story</text>
  <text x="662" y="220" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" fill="#fff" opacity="0.8">Visual-first packaging</text>
'''
    write("purchase-intent-bundles-visual-1.svg", wrap(820, 360, body))


# ── Flows ───────────────────────────────────────────────────────────────────

def flows():
    body = f'''
  <text x="48" y="56" font-family="Syne, Manrope, sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{BLUE}">LOOP</text>
  <text x="48" y="96" font-family="Syne, Manrope, sans-serif" font-size="30" font-weight="800" fill="{INK}">Continuous research</text>
  <g font-family="Syne, Manrope, sans-serif" font-weight="700" font-size="14">
    <rect x="80" y="180" width="140" height="70" rx="14" fill="{CARD}" stroke="{LILAC}" stroke-width="2"/>
    <text x="150" y="222" text-anchor="middle" fill="{INK}">Prototype</text>
    <path d="M230 215 H280" stroke="{BLUE}" stroke-width="2"/>
    <rect x="290" y="180" width="140" height="70" rx="14" fill="{CARD}" stroke="{BLUE}" stroke-width="2"/>
    <text x="360" y="222" text-anchor="middle" fill="{INK}">Test</text>
    <path d="M440 215 H490" stroke="{TEAL}" stroke-width="2"/>
    <rect x="500" y="180" width="140" height="70" rx="14" fill="{CARD}" stroke="{TEAL}" stroke-width="2"/>
    <text x="570" y="222" text-anchor="middle" fill="{INK}">Validate</text>
    <path d="M650 215 H700" stroke="{AMBER}" stroke-width="2"/>
    <rect x="710" y="180" width="140" height="70" rx="14" fill="{BLUE}"/>
    <text x="780" y="222" text-anchor="middle" fill="#fff">Ship</text>
  </g>
  <path d="M780 260 C780 320, 150 320, 150 250" fill="none" stroke="{LILAC}" stroke-width="2" stroke-dasharray="6 6"/>
  <text x="465" y="350" text-anchor="middle" font-family="Manrope, sans-serif" font-size="13" fill="{MUTED}">Evidence-gated backlog rhythm</text>
'''
    write("flows-continuous-research-cover.svg", wrap(900, 400, body))


def main():
    ai_zones_cover()
    ai_zones_v1()
    ai_zones_v2()
    always_cover()
    always_v1()
    always_v2()
    new_aud_cover()
    new_aud_v1()
    new_aud_v2()
    seg_cover()
    seg_v1()
    seg_v2()
    non_adopters()
    data_stories()
    purchase_cover()
    purchase_v1()
    flows()
    print("done")


if __name__ == "__main__":
    main()
