#!/usr/bin/env python3
"""Generate the 9 interactive .euclid-graphic SVG plates for GEOMETOR Kepler.

Each SVG strictly obeys the ``photon-platform/publish`` ``.euclid-graphic`` contract:
- ``<defs>`` tick markers (``#geom-tick-1..3``)
- Ordered layer groups: ``#elements``, ``#graphics``, ``#highlights``, ``#points``, ``#labels``
- 3-vertex midpoint ``<path d="M x1 y1 L mx my L x2 y2">`` segments
- Canonical ``data-ref`` attributes wired to ``:g:`` roles in the Book Codex
- ``html.escape`` on all ``<text>`` and ``aria-label`` strings
- Theme-adaptive CSS custom properties for dark and light modes
"""

from __future__ import annotations

import html
import math
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[1] / "docsrc" / "_static" / "figures"

PHI = (1.0 + math.sqrt(5.0)) / 2.0
SQRT_PHI = math.sqrt(PHI)

DEFS_BLOCK = """  <defs>
    <marker id="geom-tick-1" viewBox="-2 -6 4 12" refX="0" refY="0" markerWidth="4" markerHeight="12" orient="auto">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
    </marker>
    <marker id="geom-tick-2" viewBox="-4 -6 8 12" refX="0" refY="0" markerWidth="8" markerHeight="12" orient="auto">
      <line x1="-1.8" y1="-4.5" x2="-1.8" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
      <line x1="1.8" y1="-4.5" x2="1.8" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" orient="auto">
      <line x1="-3.4" y1="-4.5" x2="-3.4" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
      <line x1="3.4" y1="-4.5" x2="3.4" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
    </marker>
  </defs>"""


class EuclidSVGBuilder:
    """Assemble a theme-adaptive ``.euclid-graphic`` SVG figure."""

    def __init__(self, width: int, height: int, aria_label: str) -> None:
        self.width = width
        self.height = height
        self.aria_label = html.escape(aria_label, quote=True)
        self.elements: list[str] = []
        self.graphics: list[str] = []
        self.highlights: list[str] = []
        self.points: list[str] = []
        self.labels: list[str] = []

    def seg(
        self,
        p1: tuple[float, float],
        p2: tuple[float, float],
        ref: str,
        *,
        cls: str = "geom-line",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
        ticks: int = 0,
    ) -> None:
        """Add a 3-vertex midpoint path segment to ``#elements``."""
        x1, y1 = p1
        x2, y2 = p2
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        attrs = [
            f'class="{cls}"',
            f'd="M {x1:.2f} {y1:.2f} L {mx:.2f} {my:.2f} L {x2:.2f} {y2:.2f}"',
            'fill="none"',
            f'data-ref="{html.escape(ref, quote=True)}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        if ticks in (1, 2, 3):
            attrs.append(f'marker-mid="url(#geom-tick-{ticks})"')
        self.elements.append(f"    <path {' '.join(attrs)}/>")

    def circle(
        self,
        center: tuple[float, float],
        radius: float,
        ref: str,
        *,
        cls: str = "geom-circle",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
    ) -> None:
        """Add a circle to ``#elements``."""
        cx, cy = center
        attrs = [
            f'class="{cls}"',
            f'cx="{cx:.2f}"',
            f'cy="{cy:.2f}"',
            f'r="{radius:.2f}"',
            'fill="none"',
            f'data-ref="{html.escape(ref, quote=True)}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        self.elements.append(f"    <circle {' '.join(attrs)}/>")

    def ellipse(
        self,
        center: tuple[float, float],
        rx: float,
        ry: float,
        ref: str,
        *,
        rot_deg: float = 0.0,
        cls: str = "geom-circle",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
    ) -> None:
        """Add an ellipse to ``#elements``."""
        cx, cy = center
        attrs = [
            f'class="{cls}"',
            f'cx="{cx:.2f}"',
            f'cy="{cy:.2f}"',
            f'rx="{rx:.2f}"',
            f'ry="{ry:.2f}"',
            'fill="none"',
            f'data-ref="{html.escape(ref, quote=True)}"',
        ]
        if abs(rot_deg) > 1e-6:
            attrs.append(f'transform="rotate({rot_deg:.2f} {cx:.2f} {cy:.2f})"')
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        self.elements.append(f"    <ellipse {' '.join(attrs)}/>")

    def arc(
        self,
        center: tuple[float, float],
        radius: float,
        deg_start: float,
        deg_end: float,
        ref: str,
        *,
        cls: str = "geom-arc",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
        layer: str = "elements",
    ) -> None:
        """Add a circular arc (math CCW degrees converted to SVG y-down coordinates)."""
        cx, cy = center
        a1 = math.radians(deg_start)
        a2 = math.radians(deg_end)
        x1, y1 = cx + radius * math.cos(a1), cy - radius * math.sin(a1)
        x2, y2 = cx + radius * math.cos(a2), cy - radius * math.sin(a2)
        span = (deg_end - deg_start) % 360.0
        large = 1 if span > 180.0 else 0
        d_str = f"M {x1:.2f} {y1:.2f} A {radius:.2f} {radius:.2f} 0 {large} 0 {x2:.2f} {y2:.2f}"
        attrs = [
            f'class="{cls}"',
            f'd="{d_str}"',
            'fill="none"',
            f'data-ref="{html.escape(ref, quote=True)}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        target = self.graphics if layer == "graphics" else self.elements
        target.append(f"    <path {' '.join(attrs)}/>")

    def right_angle(
        self,
        vertex: tuple[float, float],
        u1: tuple[float, float],
        u2: tuple[float, float],
        ref: str,
        *,
        size: float = 12.0,
    ) -> None:
        """Add a perpendicular right-angle marker in ``#graphics``."""
        vx, vy = vertex
        p1 = (vx + u1[0] * size, vy + u1[1] * size)
        p12 = (vx + (u1[0] + u2[0]) * size, vy + (u1[1] + u2[1]) * size)
        p2 = (vx + u2[0] * size, vy + u2[1] * size)
        self.graphics.append(
            f'    <path class="geom-ang-arc" d="M {p1[0]:.2f} {p1[1]:.2f} '
            f'L {p12[0]:.2f} {p12[1]:.2f} L {p2[0]:.2f} {p2[1]:.2f}" '
            f'fill="none" stroke="var(--geom-muted, #64748b)" stroke-width="1.25" '
            f'data-ref="{html.escape(ref, quote=True)}"/>'
        )

    def polygon(
        self,
        pts: list[tuple[float, float]],
        ref: str,
        *,
        fill: str = "var(--geom-accent, #d97706)",
        fill_opacity: float = 0.12,
    ) -> None:
        """Add a translucent highlight polygon to ``#highlights``."""
        coords = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        self.highlights.append(
            f'    <polygon class="geom-polygon" points="{coords}" '
            f'fill="{fill}" fill-opacity="{fill_opacity:.2f}" stroke="none" '
            f'data-ref="{html.escape(ref, quote=True)}"/>'
        )

    def point(
        self,
        pt: tuple[float, float],
        ref: str,
        *,
        r: float = 3.5,
        fill: str | None = None,
    ) -> None:
        """Add a point dot to ``#points``."""
        px, py = pt
        fill_attr = f' fill="{fill}"' if fill else ""
        self.points.append(
            f'    <circle class="geom-point" cx="{px:.2f}" cy="{py:.2f}" '
            f'r="{r:.2f}"{fill_attr} data-ref="{html.escape(ref, quote=True)}"/>'
        )

    def label(
        self,
        pt: tuple[float, float],
        text: str,
        ref: str,
        *,
        dx: float = 0.0,
        dy: float = 0.0,
        size: int = 14,
        italic: bool = True,
        anchor: str = "middle",
    ) -> None:
        """Add an escaped text label to ``#labels``."""
        lx, ly = pt[0] + dx, pt[1] + dy
        style_italic = "font-style: italic; " if italic else ""
        esc_txt = html.escape(text)
        self.labels.append(
            f'    <text class="geom-label" x="{lx:.2f}" y="{ly:.2f}" '
            f'text-anchor="{anchor}" dominant-baseline="central" '
            f'style="{style_italic}font-size: {size}px;" '
            f'data-ref="{html.escape(ref, quote=True)}">{esc_txt}</text>'
        )

    def caption(self, x: float, y: float, text: str, *, size: int = 13) -> None:
        """Add a structural caption inside multi-panel plates."""
        esc_txt = html.escape(text)
        self.labels.append(
            f'    <text class="geom-label" x="{x:.2f}" y="{y:.2f}" '
            f'text-anchor="middle" style="font-size: {size}px; opacity: 0.85;">{esc_txt}</text>'
        )

    def render(self) -> str:
        """Return complete formatted SVG string."""
        parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
            f'viewBox="0 0 {self.width} {self.height}" role="img" aria-label="{self.aria_label}">',
            DEFS_BLOCK,
            '  <g id="elements">',
            *self.elements,
            "  </g>",
            '  <g id="graphics">',
            *self.graphics,
            "  </g>",
            '  <g id="highlights">',
            *self.highlights,
            "  </g>",
            '  <g id="points">',
            *self.points,
            "  </g>",
            '  <g id="labels">',
            *self.labels,
            "  </g>",
            "</svg>",
            "",
        ]
        return "\n".join(parts)


def _polar(cx: float, cy: float, r: float, deg: float) -> tuple[float, float]:
    rad = math.radians(deg)
    return (cx + r * math.cos(rad), cy - r * math.sin(rad))


def _proj3d(
    v: tuple[float, float, float],
    cx: float,
    cy: float,
    scale: float,
    yaw_deg: float = 28.0,
    pitch_deg: float = 22.0,
) -> tuple[float, float, float]:
    """Orthographic 3D projection returning ``(sx, sy, depth_z)``."""
    x, y, z = v
    yw = math.radians(yaw_deg)
    pt = math.radians(pitch_deg)
    x1 = x * math.cos(yw) - y * math.sin(yw)
    y1 = x * math.sin(yw) + y * math.cos(yw)
    z1 = z
    y2 = y1 * math.cos(pt) - z1 * math.sin(pt)
    z2 = y1 * math.sin(pt) + z1 * math.cos(pt)
    return (cx + scale * x1, cy - scale * z2, y2)


def build_fig01_graz_triangle_conjunction() -> str:
    """Unit 1: July 19, 1595 Graz Great-Conjunction Equilateral Triangle & Circle Envelope."""
    b = EuclidSVGBuilder(560, 440, "Kepler July 19 1595 Graz Great-Conjunction Triangle Diagram")
    cx, cy, r_out = 280.0, 215.0, 165.0
    r_in = r_out / 2.0

    # Outer zodiac / Saturn orb and inner enveloped Jupiter orb
    b.circle((cx, cy), r_out, "cSAT", width=1.9)
    b.circle((cx, cy), r_in, "cJUP", stroke="var(--geom-accent, #d97706)", width=1.9)

    # Background cascade of rotating conjunction chords enveloping cJUP
    for step in range(1, 7):
        base_deg = 90.0 - step * 18.0
        t0 = _polar(cx, cy, r_out, base_deg)
        t1 = _polar(cx, cy, r_out, base_deg - 120.0)
        t2 = _polar(cx, cy, r_out, base_deg - 240.0)
        b.seg(t0, t1, f"conj_{step}a", width=0.8, dash="3 3", stroke="var(--geom-muted, #64748b)")
        b.seg(t1, t2, f"conj_{step}b", width=0.8, dash="3 3", stroke="var(--geom-muted, #64748b)")
        b.seg(t2, t0, f"conj_{step}c", width=0.8, dash="3 3", stroke="var(--geom-muted, #64748b)")

    # Primary equilateral conjunction triangle ABC (r_in / R_out = 1 / 2)
    pt_a = _polar(cx, cy, r_out, 90.0)
    pt_b = _polar(cx, cy, r_out, 330.0)
    pt_c = _polar(cx, cy, r_out, 210.0)
    pt_m = (cx, cy + r_in)

    b.polygon([pt_a, pt_b, pt_c], "ABC", fill_opacity=0.11)
    b.seg(pt_a, pt_b, "AB", width=2.0, ticks=1)
    b.seg(pt_b, pt_c, "BC", width=2.0, ticks=1)
    b.seg(pt_c, pt_a, "CA", width=2.0, ticks=1)

    # Radii OA (R_out = 2) and OM (r_in = 1)
    b.seg((cx, cy), pt_a, "OA", dash="5 4", width=1.3)
    b.seg((cx, cy), pt_m, "OM", stroke="var(--geom-accent, #d97706)", width=1.7)
    b.right_angle(pt_m, (1.0, 0.0), (0.0, -1.0), "angOMB", size=11.0)

    for pt, name, dx, dy in [
        ((cx, cy), "O", -14.0, -6.0),
        (pt_a, "A", 0.0, -15.0),
        (pt_b, "B", 15.0, 10.0),
        (pt_c, "C", -15.0, 10.0),
        (pt_m, "M", 12.0, 14.0),
    ]:
        b.point(pt, name)
        b.label(pt, name, name, dx=dx, dy=dy)

    b.caption(280.0, 418.0, "Graz Conjunction Triangle (19 July 1595): r_in : R_out = OM : OA = 1 : 2 (Q = 1/4)")
    return b.render()


def build_fig02_mysterium_nested_solids() -> str:
    """Unit 1: Concentric Six Planetary Orbs & Five Regular Solids Cross-Section."""
    b = EuclidSVGBuilder(660, 430, "Mysterium Cosmographicum Exact Scale Outer and Inner Planetary Nestings")

    # Left Panel: Saturn (Cube) -> Jupiter (Tetrahedron) -> Mars (Earth core)
    lx, ly = 175.0, 205.0
    r_sat = 152.0
    r_jup = r_sat / math.sqrt(3.0)  # 87.76
    r_mar = r_jup / 3.0  # 29.25
    dod_ratio = math.sqrt((5.0 + 2.0 * math.sqrt(5.0)) / 15.0)
    r_ter_l = r_mar * dod_ratio  # 23.25

    b.circle((lx, ly), r_sat, "cSAT", width=1.8)
    b.circle((lx, ly), r_jup, "cJUP", width=1.6, stroke="var(--geom-accent, #d97706)")
    b.circle((lx, ly), r_mar, "cMAR", width=1.5)
    b.circle((lx, ly), r_ter_l, "cTER", width=1.8, stroke="#10b981")

    # Cube cross-section square inscribed in c_cube_proj (tangent to cJUP: half-side = r_jup, corner = r_jup*sqrt(2))
    # Show cube face projection tangent to cJUP and vertices on cSAT meridian
    sq_pts = [_polar(lx, ly, r_sat, 45.0 + 90.0 * k) for k in range(4)]
    b.polygon(sq_pts, "CUBUS", fill_opacity=0.07)
    for k in range(4):
        b.seg(sq_pts[k], sq_pts[(k + 1) % 4], f"cub_{k}", width=1.4)

    # Tetrahedron cross-section triangle between cJUP and cMAR
    tet_pts = [_polar(lx, ly, r_jup, 90.0 + 120.0 * k) for k in range(3)]
    for k in range(3):
        b.seg(tet_pts[k], tet_pts[(k + 1) % 3], f"tet_{k}", width=1.4, stroke="var(--geom-accent, #d97706)")

    b.point((lx, ly), "S_sun", r=4.0, fill="var(--geom-accent, #d97706)")
    b.label((lx, ly), "Sol", "S_sun", dy=-12.0, size=12)
    b.label((lx, ly - r_sat), "Saturnus", "cSAT", dy=-11.0, size=12)
    b.label((lx, ly - r_jup), "Iupiter", "cJUP", dx=34.0, dy=-6.0, size=12)
    b.label((lx, ly + r_mar), "Mars", "cMAR", dy=13.0, size=11)

    # Right Panel: Magnified Inner System — Mars (Dodecahedron) -> Earth -> Venus (Icosahedron) -> Mercury (Octahedron)
    rx, ry = 490.0, 205.0
    r_mar_r = 148.0
    r_ter_r = r_mar_r * dod_ratio  # 117.61 (Terra: Circulus mensor omnium!)
    r_ven_r = r_ter_r * dod_ratio  # 93.46
    r_mer_r = r_ven_r / math.sqrt(3.0)  # 53.96

    b.circle((rx, ry), r_mar_r, "cMAR_in", width=1.5, dash="5 3")
    b.circle((rx, ry), r_ter_r, "cTER_in", width=2.3, stroke="#10b981")
    b.circle((rx, ry), r_ven_r, "cVEN", width=1.6, stroke="var(--geom-accent, #d97706)")
    b.circle((rx, ry), r_mer_r, "cMER", width=1.6)

    # Dodecahedron decagonal/pentagonal profile between Mars & Earth
    pent_pts = [_polar(rx, ry, r_mar_r, 90.0 + 72.0 * k) for k in range(5)]
    b.polygon(pent_pts, "DODEC", fill="#10b981", fill_opacity=0.07)
    for k in range(5):
        b.seg(pent_pts[k], pent_pts[(k + 1) % 5], f"dod_{k}", width=1.3)

    # Icosahedron hexagonal/triangular profile between Earth & Venus
    ico_pts = [_polar(rx, ry, r_ter_r, 30.0 + 60.0 * k) for k in range(6)]
    for k in range(6):
        b.seg(ico_pts[k], ico_pts[(k + 1) % 6], f"ico_{k}", width=1.2, stroke="var(--geom-accent, #d97706)")

    # Octahedron axial diamond between Venus & Mercury
    oct_pts = [_polar(rx, ry, r_ven_r, 90.0 * k) for k in range(4)]
    for k in range(4):
        b.seg(oct_pts[k], oct_pts[(k + 1) % 4], f"oct_{k}", width=1.3)

    b.point((rx, ry), "S_in", r=4.0, fill="var(--geom-accent, #d97706)")
    b.label((rx, ry - r_mar_r), "Mars (Dodecaedron)", "cMAR_in", dy=-11.0, size=12)
    b.label((rx, ry - r_ter_r), "Terra (Mensor)", "cTER_in", dy=13.0, size=12)
    b.label((rx, ry + r_ven_r), "Venus (Icosaedron)", "cVEN", dy=-12.0, size=11)
    b.label((rx, ry + r_mer_r), "Mercurius", "cMER", dy=-12.0, size=11)

    b.caption(175.0, 398.0, "I. Outer Primary Solids (Saturn -> Mars)")
    b.caption(490.0, 398.0, "II. Inner Secondary Solids around Terra (Mars -> Mercury)")
    return b.render()


def build_fig03_strena_hexagonal_rosette() -> str:
    """Unit 2: Six-Cornered Snowflake & 7-Circle Hexagonal Close-Packing Rosette."""
    b = EuclidSVGBuilder(560, 440, "Strena 1611 Six-Cornered Snowflake and 7-Circle Close-Packing Rosette")
    cx, cy = 280.0, 212.0
    r_sphere = 52.0
    d_center = 2.0 * r_sphere

    # Central sphere O and 6 tangent neighbor spheres P0..P5
    b.circle((cx, cy), r_sphere, "S_center", width=2.0, stroke="var(--geom-accent, #d97706)")
    centers = [_polar(cx, cy, d_center, 60.0 * k) for k in range(6)]
    b.polygon(centers, "HEX", fill_opacity=0.09)

    for k, ctr in enumerate(centers):
        nxt = centers[(k + 1) % 6]
        b.circle(ctr, r_sphere, f"S_{k}", width=1.6)
        b.seg(ctr, nxt, f"P{k}P{(k + 1) % 6}", width=1.5, ticks=1)
        b.seg((cx, cy), ctr, f"OP{k}", width=1.3, dash="4 3")

        # Snowflake feathery barbs along extended sixfold rays
        ray_tip = _polar(cx, cy, d_center + 64.0, 60.0 * k)
        b.seg(ctr, ray_tip, f"ray_{k}", width=1.8, stroke="var(--geom-accent, #d97706)")
        for frac in (0.38, 0.68):
            bx = ctr[0] + frac * (ray_tip[0] - ctr[0])
            by = ctr[1] + frac * (ray_tip[1] - ctr[1])
            b_left = _polar(bx, by, 16.0, 60.0 * k + 60.0)
            b_right = _polar(bx, by, 16.0, 60.0 * k - 60.0)
            b.seg((bx, by), b_left, f"barb_{k}_{frac}_l", width=1.2, stroke="var(--geom-accent, #d97706)")
            b.seg((bx, by), b_right, f"barb_{k}_{frac}_r", width=1.2, stroke="var(--geom-accent, #d97706)")

    # Central compressed Voronoi hexagon cell around O
    voronoi = [_polar(cx, cy, r_sphere / math.cos(math.radians(30.0)), 30.0 + 60.0 * k) for k in range(6)]
    for k in range(6):
        b.seg(voronoi[k], voronoi[(k + 1) % 6], f"vor_{k}", width=1.5, stroke="#10b981")

    b.point((cx, cy), "O", r=3.8)
    b.label((cx, cy), "O", "O", dx=-12.0, dy=-10.0)
    for k, ctr in enumerate(centers):
        lbl = f"P{k}"
        off = _polar(0.0, 0.0, 18.0, 60.0 * k)
        b.point(ctr, lbl)
        b.label(ctr, f"P_{k}", lbl, dx=off[0], dy=off[1], size=13)

    b.caption(280.0, 418.0, "Planar Close-Packing (Kissing Number 6, Q = 4R^2) & Compressed Hexagonal Cell")
    return b.render()


def build_fig04_rhombic_dodecahedron_voronoi() -> str:
    """Unit 2: 3D Orthographic Projection of Kepler's Space-Filling Rhombic Dodecahedron."""
    b = EuclidSVGBuilder(560, 440, "Strena 1611 Rhombic Dodecahedron Space-Filling Voronoi Polyhedron")
    cx, cy, scale = 280.0, 210.0, 74.0

    cubic = [(float(sx), float(sy), float(sz)) for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)]
    octa = [
        (2.0, 0.0, 0.0),
        (-2.0, 0.0, 0.0),
        (0.0, 2.0, 0.0),
        (0.0, -2.0, 0.0),
        (0.0, 0.0, 2.0),
        (0.0, 0.0, -2.0),
    ]
    verts = cubic + octa
    proj = [_proj3d(v, cx, cy, scale, yaw_deg=32.0, pitch_deg=24.0) for v in verts]

    # Edges connect cubic (0..7) to octahedral (8..13) when squared distance == 3
    edges: list[tuple[int, int]] = []
    for i in range(8):
        for j in range(8, 14):
            d2 = sum((verts[i][m] - verts[j][m]) ** 2 for m in range(3))
            if abs(d2 - 3.0) < 1e-6:
                edges.append((i, j))

    # Highlight front rhombus: octa (0, -2, 0) [idx 11? wait: octa indices: 8:(2,0,0), 9:(-2,0,0),
    # 10:(0,2,0), 11:(0,-2,0), 12:(0,0,2), 13:(0,0,-2)]
    # With yaw=32, pitch=24, depth y2 is most negative (closest to viewer? Wait: let's check!)
    # Let's pick rhombus between (2,0,0) [8], (1,1,1) [7], (0,0,2) [12], (1,-1,1) [5]
    idx_a, idx_b, idx_c, idx_d = 8, 7, 12, 5
    pa = (proj[idx_a][0], proj[idx_a][1])
    pb = (proj[idx_b][0], proj[idx_b][1])
    pc = (proj[idx_c][0], proj[idx_c][1])
    pd = (proj[idx_d][0], proj[idx_d][1])
    b.polygon([pa, pb, pc, pd], "ABCD", fill="var(--geom-accent, #d97706)", fill_opacity=0.18)

    for k, (i, j) in enumerate(edges):
        p1 = (proj[i][0], proj[i][1])
        p2 = (proj[j][0], proj[j][1])
        mean_depth = (proj[i][2] + proj[j][2]) / 2.0
        is_back = mean_depth > 0.35
        b.seg(
            p1,
            p2,
            f"rd_e{k}",
            width=1.1 if is_back else 1.85,
            dash="4 4" if is_back else None,
            stroke="var(--geom-muted, #64748b)" if is_back else None,
        )

    # Long (sqrt(2)) and short (1) diagonals on highlighted rhombus ABCD
    b.seg(pa, pc, "AC", stroke="var(--geom-accent, #d97706)", width=1.9, dash="5 3")
    b.seg(pb, pd, "BD", stroke="#10b981", width=1.9, dash="5 3")

    for i, (sx, sy, _depth) in enumerate(proj):
        is_oct = i >= 8
        b.point((sx, sy), f"V{i}", r=4.0 if is_oct else 3.1, fill="var(--geom-accent, #d97706)" if is_oct else None)

    b.label(pa, "A", "A", dx=15.0, dy=4.0)
    b.label(pb, "B", "B", dx=13.0, dy=-10.0)
    b.label(pc, "C", "C", dx=0.0, dy=-15.0)
    b.label(pd, "D", "D", dx=-14.0, dy=6.0)

    b.caption(280.0, 418.0, "Dodecaedron Rhombicum (12 Faces, 14 Vertices, 24 Edges): AC : BD = sqrt(2) : 1, Dihedral 120 deg")
    return b.render()


def build_fig05_fibonacci_golden_phyllotaxis() -> str:
    """Unit 2: Pentamerous Blossom Pentagram & Self-Propagating Fibonacci Golden Spiral."""
    b = EuclidSVGBuilder(640, 410, "Strena 1611 Pentamerous Blossom and Fibonacci Phyllotaxis Convergence")

    # Left Panel: Regular Pentagon ABCDE & Star Pentagram {5/2}
    lx, ly, r_p = 165.0, 198.0, 122.0
    b.circle((lx, ly), r_p, "cPENT", width=1.3, dash="4 4", stroke="var(--geom-muted, #64748b)")
    p_pts = [_polar(lx, ly, r_p, 90.0 + 72.0 * k) for k in range(5)]
    b.polygon(p_pts, "ABCDE", fill_opacity=0.09)
    names = ["A", "B", "C", "D", "E"]
    for k in range(5):
        b.seg(p_pts[k], p_pts[(k + 1) % 5], f"{names[k]}{names[(k + 1) % 5]}", width=1.8)
        b.seg(
            p_pts[k],
            p_pts[(k + 2) % 5],
            f"star_{k}",
            width=1.6,
            stroke="var(--geom-accent, #d97706)",
        )
        off = _polar(0.0, 0.0, 17.0, 90.0 + 72.0 * k)
        b.point(p_pts[k], names[k])
        b.label(p_pts[k], names[k], names[k], dx=off[0], dy=off[1])

    # Right Panel: Exact 13 x 8 Fibonacci Tiling (squares 8, 5, 3, 2, 1, 1)
    u = 18.5
    ox, oy = 345.0, 118.0  # top-left of 13 x 8 rectangle (width=240.5, height=148)
    # Square 8 (left): [0..8, 0..8]
    # Square 5 (top-right): [8..13, 0..5]
    # Square 3 (bottom-right): [10..13, 5..8]
    # Square 2 (bottom-mid-left): [8..10, 6..8]
    # Square 1a: [8..9, 5..6], Square 1b: [9..10, 5..6]
    squares = [
        (0, 0, 8, "sq8", "8"),
        (8, 0, 5, "sq5", "5"),
        (10, 5, 3, "sq3", "3"),
        (8, 6, 2, "sq2", "2"),
        (8, 5, 1, "sq1a", "1"),
        (9, 5, 1, "sq1b", "1"),
    ]
    b.polygon(
        [(ox, oy), (ox + 13 * u, oy), (ox + 13 * u, oy + 8 * u), (ox, oy + 8 * u)],
        "FIB13x8",
        fill="#10b981",
        fill_opacity=0.08,
    )
    for gx, gy, side, ref, lbl in squares:
        x0, y0 = ox + gx * u, oy + gy * u
        w = side * u
        b.seg((x0, y0), (x0 + w, y0), f"{ref}_n", width=1.4)
        b.seg((x0 + w, y0), (x0 + w, y0 + w), f"{ref}_e", width=1.4)
        b.seg((x0 + w, y0 + w), (x0, y0 + w), f"{ref}_s", width=1.4)
        b.seg((x0, y0 + w), (x0, y0), f"{ref}_w", width=1.4)
        b.label((x0 + w / 2.0, y0 + w / 2.0), lbl, ref, italic=False, size=13 if side >= 2 else 10)

    # Quarter-circle Fibonacci spiral arcs
    arcs = [
        ((ox + 8 * u, oy + 8 * u), 8 * u, 90.0, 180.0, "sp8"),
        ((ox + 8 * u, oy + 5 * u), 5 * u, 0.0, 90.0, "sp5"),
        ((ox + 10 * u, oy + 5 * u), 3 * u, 270.0, 360.0, "sp3"),
        ((ox + 10 * u, oy + 6 * u), 2 * u, 180.0, 270.0, "sp2"),
        ((ox + 9 * u, oy + 6 * u), 1 * u, 90.0, 180.0, "sp1a"),
        ((ox + 9 * u, oy + 5 * u), 1 * u, 0.0, 90.0, "sp1b"),
    ]
    for ac, ar, a_s, a_e, aref in arcs:
        b.arc(ac, ar, a_s, a_e, aref, stroke="var(--geom-accent, #d97706)", width=2.2)

    b.caption(165.0, 382.0, "I. Flos Quinquefolius (Pentagram {5/2})")
    b.caption(465.0, 382.0, "II. Propagatio Seminalis: 1, 1, 2, 3, 5, 8, 13 -> phi")
    return b.render()


def build_fig06_scibilia_pentagon_vs_heptagon() -> str:
    """Unit 3: Harmonices Mundi Book I — Scibilis Pentagon/Decagon vs. Inscibilis Heptagon."""
    b = EuclidSVGBuilder(650, 420, "Harmonices Mundi Book I Constructible Pentagon vs Non-Constructible Heptagon")

    # Left Panel: Euclidean / Ptolemaic Golden Construction of Decagon & Pentagon (Scibilis)
    lx, ly, r = 172.0, 200.0, 124.0
    b.circle((lx, ly), r, "cSCIB", width=1.7)
    pt_a = (lx, ly - r)
    pt_w = (lx - r, ly)
    pt_e = (lx + r, ly)
    pt_m = (lx + r / 2.0, ly)
    r_ma = math.hypot(r / 2.0, r)
    pt_g = (lx + r / 2.0 - r_ma, ly)  # OG = r / phi = s_10!

    b.seg(pt_w, pt_e, "WE", width=1.3)
    b.seg((lx, ly - r), (lx, ly + r), "NS", width=1.3, dash="4 3")
    b.seg(pt_m, pt_a, "MA", width=1.5, stroke="var(--geom-accent, #d97706)", dash="4 3")
    b.arc(pt_m, r_ma, 116.5, 180.0, "arcMG", stroke="var(--geom-accent, #d97706)", width=1.5)
    b.seg((lx, ly), pt_g, "OG", width=2.2, stroke="#10b981")
    b.seg(pt_a, pt_g, "AG", width=2.2, stroke="var(--geom-accent, #d97706)")

    # Inscribed regular pentagon for visual clarity
    pent = [_polar(lx, ly, r, 90.0 + 72.0 * k) for k in range(5)]
    b.polygon(pent, "PENT5", fill="#10b981", fill_opacity=0.08)
    for k in range(5):
        b.seg(pent[k], pent[(k + 1) % 5], f"p5_{k}", width=1.5)

    for pt, lbl, dx, dy in [
        ((lx, ly), "O", 11.0, 12.0),
        (pt_a, "A", 0.0, -14.0),
        (pt_m, "M", 0.0, 14.0),
        (pt_g, "G", -4.0, 15.0),
    ]:
        b.point(pt, lbl)
        b.label(pt, lbl, lbl, dx=dx, dy=dy, size=13)

    # Right Panel: Regular Heptagon H1..H7 & Diagonal Triangle (Inscibilis: x^3 + x^2 - 2x - 1 = 0)
    rx, ry = 485.0, 200.0
    b.circle((rx, ry), r, "cHEPT", width=1.7)
    h_pts = [_polar(rx, ry, r, 90.0 + (360.0 / 7.0) * k) for k in range(7)]
    b.polygon(h_pts, "HEPT7", fill="var(--geom-accent, #d97706)", fill_opacity=0.09)
    for k in range(7):
        b.seg(h_pts[k], h_pts[(k + 1) % 7], f"h7_{k}", width=1.8)
        off = _polar(0.0, 0.0, 16.0, 90.0 + (360.0 / 7.0) * k)
        b.point(h_pts[k], f"H{k + 1}")
        b.label(h_pts[k], f"H_{k + 1}", f"H{k + 1}", dx=off[0], dy=off[1], size=12)

    # Heptagonal triangle H1-H2-H4 showing three distinct chord species s_1, s_2, s_3
    b.polygon([h_pts[0], h_pts[1], h_pts[3]], "H1H2H4", fill="#ef4444", fill_opacity=0.14)
    b.seg(h_pts[0], h_pts[2], "diag_s2", width=1.6, stroke="#ef4444", dash="5 3")
    b.seg(h_pts[0], h_pts[3], "diag_s3", width=1.8, stroke="#ef4444")
    b.seg(h_pts[1], h_pts[3], "diag_13", width=1.6, stroke="#ef4444", dash="5 3")

    b.caption(172.0, 392.0, "I. Scibilis: OG = s_10 = R/phi, AG = s_5 (Quadratic)")
    b.caption(485.0, 392.0, "II. Inscibilis (Prop. XLV): Septangulum, x^3 + x^2 - 2x - 1 = 0")
    return b.render()


def _regular_ngon_from_edge(
    p1: tuple[float, float],
    p2: tuple[float, float],
    n: int,
) -> list[tuple[float, float]]:
    """Construct CCW regular n-gon in SVG coords starting with directed edge p1 -> p2."""
    pts = [p1, p2]
    ext = -2.0 * math.pi / n  # CCW in math = negative angle in y-down SVG
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    cx, cy = p2
    for _ in range(n - 2):
        nx = dx * math.cos(ext) - dy * math.sin(ext)
        ny = dx * math.sin(ext) + dy * math.cos(ext)
        dx, dy = nx, ny
        cx += dx
        cy += dy
        pts.append((cx, cy))
    return pts


def _draw_vertex_star(
    b: EuclidSVGBuilder,
    vc: tuple[float, float],
    edge_len: float,
    symbol: tuple[int, ...],
    prefix: str,
    start_deg: float = 0.0,
) -> None:
    """Draw exact polygons meeting edge-to-edge around vertex ``vc``."""
    cur_deg = start_deg
    palette = [
        ("var(--geom-accent, #d97706)", 0.14),
        ("#10b981", 0.13),
        ("#3b82f6", 0.12),
        ("#a855f7", 0.11),
    ]
    for idx, n in enumerate(symbol):
        interior = (n - 2) * 180.0 / n
        p_ray = _polar(vc[0], vc[1], edge_len, cur_deg)
        poly = _regular_ngon_from_edge(vc, p_ray, n)
        col, op = palette[idx % len(palette)]
        b.polygon(poly, f"{prefix}_f{idx}", fill=col, fill_opacity=op)
        for m in range(n):
            b.seg(poly[m], poly[(m + 1) % n], f"{prefix}_f{idx}_e{m}", width=1.45)
        cur_deg += interior
    b.point(vc, prefix, r=4.0, fill="var(--geom-accent, #d97706)")


def build_fig07_archimedean_planar_tilings() -> str:
    """Unit 4: Harmonices Mundi Book II — Four Representative Archimedean Vertex Species."""
    b = EuclidSVGBuilder(660, 460, "Harmonices Mundi Book II Uniform Archimedean Planar Congruences")

    specs = [
        ((170.0, 118.0), 42.0, (3, 6, 3, 6), "V3636", 15.0, "3.6.3.6 (Trihexagonal)"),
        ((490.0, 118.0), 36.0, (4, 8, 8), "V488", 22.5, "4.8.8 (Truncated Square)"),
        ((170.0, 325.0), 38.0, (3, 4, 6, 4), "V3464", 0.0, "3.4.6.4 (Rhombitrihexagonal)"),
        ((490.0, 325.0), 42.0, (3, 3, 3, 3, 6), "V33336", 0.0, "3.3.3.3.6 (Chiral Snub)"),
    ]
    for vc, elen, sym, pref, sdeg, cap in specs:
        _draw_vertex_star(b, vc, elen, sym, pref, start_deg=sdeg)
        b.caption(vc[0], vc[1] + 104.0, cap, size=12)

    return b.render()


def build_fig08_kepler_pentagram_monster_aa() -> str:
    """Unit 4: Kepler's Figure Aa Pentagram–Decagon Star Congruence & Rhombic Triacontahedron."""
    b = EuclidSVGBuilder(660, 440, "Harmonices Mundi Book II Figure Aa Star Tiling and Rhombic Triacontahedron")

    # Left Panel: Central Regular Decagon D0 ringed by 5 Star Pentagrams {5/2} & 5 Pentagons (Fig. Aa motif)
    lx, ly = 180.0, 205.0
    r_dec = 54.0
    edge = 2.0 * r_dec * math.sin(math.pi / 10.0)
    dec_pts = [_polar(lx, ly, r_dec, 18.0 + 36.0 * k) for k in range(10)]
    b.polygon(dec_pts, "DEC0", fill="#10b981", fill_opacity=0.14)
    for k in range(10):
        p1, p2 = dec_pts[k], dec_pts[(k + 1) % 10]
        b.seg(p1, p2, f"dec_e{k}", width=1.7)
        # Alternate outward pentagons on even edges and star pentagram spikes on odd edges!
        out_pent = _regular_ngon_from_edge(p2, p1, 5)
        if k % 2 == 0:
            b.polygon(out_pent, f"pent_{k}", fill="var(--geom-accent, #d97706)", fill_opacity=0.14)
            for m in range(5):
                b.seg(out_pent[m], out_pent[(m + 1) % 5], f"aa_p{k}_{m}", width=1.35)
        else:
            # Draw five-pointed star {5/2} inside/on that outward pentagon!
            for m in range(5):
                b.seg(
                    out_pent[m],
                    out_pent[(m + 2) % 5],
                    f"aa_st{k}_{m}",
                    width=1.35,
                    stroke="#3b82f6",
                )

    _ = edge
    b.point((lx, ly), "D_0", r=3.5)
    b.label((lx, ly), "D_0", "D_0", size=13)

    # Right Panel: 3D Orthographic Projection of Golden Rhombic Triacontahedron (phi : 1)
    rx, ry, scale = 485.0, 205.0, 48.0
    phi2 = PHI * PHI
    icosa_v: list[tuple[float, float, float]] = []
    for s1 in (-1.0, 1.0):
        for s2 in (-1.0, 1.0):
            icosa_v.append((0.0, s1 * PHI, s2 * phi2))
            icosa_v.append((s1 * PHI, s2 * phi2, 0.0))
            icosa_v.append((s2 * phi2, 0.0, s1 * PHI))

    dodeca_v: list[tuple[float, float, float]] = [
        (sx * PHI, sy * PHI, sz * PHI)
        for sx in (-1.0, 1.0)
        for sy in (-1.0, 1.0)
        for sz in (-1.0, 1.0)
    ]
    for s1 in (-1.0, 1.0):
        for s2 in (-1.0, 1.0):
            dodeca_v.append((s1, 0.0, s2 * phi2))
            dodeca_v.append((0.0, s2 * phi2, s1))
            dodeca_v.append((s2 * phi2, s1, 0.0))

    verts = icosa_v + dodeca_v
    proj = [_proj3d(v, rx, ry, scale, yaw_deg=20.0, pitch_deg=18.0) for v in verts]

    target_q = 1.0 + phi2  # 3.6180339...
    for i in range(12):
        for j in range(12, 32):
            d2 = sum((verts[i][m] - verts[j][m]) ** 2 for m in range(3))
            if abs(d2 - target_q) < 1e-4:
                p1 = (proj[i][0], proj[i][1])
                p2 = (proj[j][0], proj[j][1])
                depth = (proj[i][2] + proj[j][2]) / 2.0
                if depth <= 0.45:
                    b.seg(p1, p2, f"rt_{i}_{j}", width=1.55)
                else:
                    b.seg(p1, p2, f"rt_b_{i}_{j}", width=0.8, dash="3 3", stroke="var(--geom-muted, #64748b)")

    # Highlight top/front golden rhombus: (0, phi, phi^2), (1, 0, phi^2), (0, -phi, phi^2), (-1, 0, phi^2)
    # Find indices explicitly
    def _find_v(target: tuple[float, float, float]) -> int:
        return min(range(len(verts)), key=lambda idx: sum((verts[idx][m] - target[m]) ** 2 for m in range(3)))

    iq = _find_v((0.0, -PHI, -phi2))
    ir = _find_v((1.0, 0.0, -phi2))
    is_ = _find_v((0.0, PHI, -phi2))
    it = _find_v((-1.0, 0.0, -phi2))
    # Choose whichever of z = +phi^2 or y = -phi^2 faces the viewer (smaller depth y2)
    i1 = _find_v((0.0, -phi2, 1.0))
    i2 = _find_v((PHI, -phi2, 0.0))
    i3 = _find_v((0.0, -phi2, -1.0))
    i4 = _find_v((-PHI, -phi2, 0.0))
    _ = (iq, ir, is_, it)
    rhomb_pts = [(proj[idx][0], proj[idx][1]) for idx in (i1, i2, i3, i4)]
    b.polygon(rhomb_pts, "PQRS", fill="var(--geom-accent, #d97706)", fill_opacity=0.22)
    b.seg(rhomb_pts[1], rhomb_pts[3], "PR_gold", stroke="var(--geom-accent, #d97706)", width=1.9, dash="4 3")
    b.seg(rhomb_pts[0], rhomb_pts[2], "QS_gold", stroke="#10b981", width=1.9, dash="4 3")

    b.caption(180.0, 412.0, "I. Congruentia Stellata Aa (Decagons, Pentagons & {5/2})")
    b.caption(485.0, 412.0, "II. Triacontaedron Rhombicum (30 Golden Rhombi, phi : 1)")
    return b.render()


def build_fig09_kepler_triangle_and_third_law() -> str:
    """Unit 5: Kepler Right Triangle (1, sqrt(phi), phi) & Book V Elliptic Harmonic Law."""
    b = EuclidSVGBuilder(660, 420, "Kepler Right Triangle 1597 and Harmonices Mundi Book V Third Law")

    # Left Panel: Exact Kepler Right Triangle OAB on Thales Semicircle W(-1,0)..P(phi,0)
    ox, oy = 135.0, 295.0
    u = 92.0
    pt_w = (ox - 1.0 * u, oy)
    pt_o = (ox, oy)
    pt_a = (ox + 1.0 * u, oy)
    pt_p = (ox + PHI * u, oy)
    pt_k = (ox + ((PHI - 1.0) / 2.0) * u, oy)
    r_thales = ((PHI + 1.0) / 2.0) * u
    pt_b = (ox, oy - SQRT_PHI * u)
    # Foot of altitude H on AB: H = (1/phi, 1/(phi*sqrt(phi))) in math coords
    hx_m = 1.0 / PHI
    hy_m = 1.0 / (PHI * SQRT_PHI)
    pt_h = (ox + hx_m * u, oy - hy_m * u)

    b.arc(pt_k, r_thales, 0.0, 180.0, "cThales", dash="5 3", width=1.5, stroke="var(--geom-muted, #64748b)")
    b.seg(pt_w, pt_p, "WP", width=1.4)
    b.polygon([pt_o, pt_a, pt_b], "OAB", fill="var(--geom-accent, #d97706)", fill_opacity=0.14)
    b.seg(pt_o, pt_a, "OA", width=2.2)
    b.seg(pt_o, pt_b, "OB", width=2.2, stroke="#10b981")
    b.seg(pt_a, pt_b, "AB", width=2.3, stroke="var(--geom-accent, #d97706)")
    b.seg(pt_o, pt_h, "OH", width=1.6, dash="4 3")
    b.right_angle(pt_o, (1.0, 0.0), (0.0, -1.0), "angAOB", size=11.0)

    for pt, lbl, dx, dy in [
        (pt_w, "W", 0.0, 15.0),
        (pt_o, "O", 0.0, 15.0),
        (pt_a, "A", 0.0, 15.0),
        (pt_p, "P", 0.0, 15.0),
        (pt_b, "B", -14.0, -4.0),
        (pt_h, "H", 13.0, -8.0),
    ]:
        b.point(pt, lbl)
        b.label(pt, lbl, lbl, dx=dx, dy=dy, size=13)

    b.label(((pt_o[0] + pt_a[0]) / 2.0, oy - 11.0), "1", "OA", italic=False, size=12)
    b.label((ox - 22.0, (oy + pt_b[1]) / 2.0), "sqrt(phi)", "OB", size=12)
    b.label(((pt_a[0] + pt_b[0]) / 2.0 + 18.0, (pt_a[1] + pt_b[1]) / 2.0 - 10.0), "phi", "AB", size=13)

    # Right Panel: Focal Planetary Ellipse (e = 0.45 exaggerated to show perihelion/aphelion sectors)
    ecx, ecy = 495.0, 205.0
    ea = 132.0
    ee = 0.42
    eb = ea * math.sqrt(1.0 - ee * ee)
    c_foc = ea * ee
    pt_sun = (ecx + c_foc, ecy)
    pt_per = (ecx + ea, ecy)
    pt_aph = (ecx - ea, ecy)

    b.ellipse((ecx, ecy), ea, eb, "cORB", width=2.0)
    b.seg(pt_aph, pt_per, "AP_axis", width=1.3, dash="4 3")

    # Equal-time perihelion wide sector vs aphelion narrow sector
    per_u = (ecx + ea * math.cos(math.radians(32.0)), ecy - eb * math.sin(math.radians(32.0)))
    per_l = (ecx + ea * math.cos(math.radians(-32.0)), ecy - eb * math.sin(math.radians(-32.0)))
    aph_u = (ecx + ea * math.cos(math.radians(168.0)), ecy - eb * math.sin(math.radians(168.0)))
    aph_l = (ecx + ea * math.cos(math.radians(192.0)), ecy - eb * math.sin(math.radians(192.0)))

    b.polygon([pt_sun, per_u, pt_per, per_l], "SEC_PER", fill="var(--geom-accent, #d97706)", fill_opacity=0.18)
    b.polygon([pt_sun, aph_u, pt_aph, aph_l], "SEC_APH", fill="#10b981", fill_opacity=0.18)
    for sp_pt, sref in [(per_u, "sp1"), (per_l, "sp2"), (aph_u, "sa1"), (aph_l, "sa2")]:
        b.seg(pt_sun, sp_pt, sref, width=1.3)

    b.point((ecx, ecy), "C_orb", r=3.0)
    b.point(pt_sun, "Sol_f", r=4.8, fill="var(--geom-accent, #d97706)")
    b.point(pt_per, "P_per", r=3.6)
    b.point(pt_aph, "A_aph", r=3.6)
    b.label(pt_sun, "Sol", "Sol_f", dy=16.0, size=13)
    b.label(pt_per, "P", "P_per", dx=13.0, size=13)
    b.label(pt_aph, "A_p", "A_aph", dx=-15.0, size=13)
    b.label(((ecx - ea + ecx) / 2.0, ecy - 12.0), "a", "AP_axis", size=13)

    b.caption(175.0, 392.0, "I. Kepler Triangle (1597): Q = (1, phi, phi^2)")
    b.caption(495.0, 392.0, "II. Lex Tertia & Harmonia Extremorum: T^2 ~ a^3")
    return b.render()


def main() -> int:
    """Generate all 9 .euclid-graphic SVG figures."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    builders = {
        "fig01_graz_triangle_conjunction.svg": build_fig01_graz_triangle_conjunction,
        "fig02_mysterium_nested_solids.svg": build_fig02_mysterium_nested_solids,
        "fig03_strena_hexagonal_rosette.svg": build_fig03_strena_hexagonal_rosette,
        "fig04_rhombic_dodecahedron_voronoi.svg": build_fig04_rhombic_dodecahedron_voronoi,
        "fig05_fibonacci_golden_phyllotaxis.svg": build_fig05_fibonacci_golden_phyllotaxis,
        "fig06_scibilia_pentagon_vs_heptagon.svg": build_fig06_scibilia_pentagon_vs_heptagon,
        "fig07_archimedean_planar_tilings.svg": build_fig07_archimedean_planar_tilings,
        "fig08_kepler_pentagram_monster_aa.svg": build_fig08_kepler_pentagram_monster_aa,
        "fig09_kepler_triangle_and_third_law.svg": build_fig09_kepler_triangle_and_third_law,
    }
    for fname, fn in builders.items():
        svg_text = fn()
        (OUT_DIR / fname).write_text(svg_text, encoding="utf-8")
        print(f"Wrote {OUT_DIR / fname} ({len(svg_text)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
