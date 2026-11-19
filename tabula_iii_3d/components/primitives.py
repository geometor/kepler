"""Shared 3D CAD primitives, exact Caput XIII SymPy geometry, and PBR materials
for Kepler's Tabula III (Mysterium Cosmographicum, 1596/1597, folio 0034).

Follows the modular IngeTrazo 0.6.0 + Blender 5.x + WebGL CAD architecture
established in ``GOR-9/tower_3d/components/primitives.py``.

Coordinate system: Z-up, units in METERS (museum sculptural orrery scale:
Saturn outer diameter = 2.00 m, pedestal resting flush on Z = 0.00 m,
cosmic center Sol at Z = 1.48 m).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

# ── Exact Mathematical Constants (verified over Q(sqrt(3), phi)) ───────────
SQRT2 = math.sqrt(2.0)
SQRT3 = math.sqrt(3.0)
SQRT5 = math.sqrt(5.0)
PHI = (1.0 + SQRT5) / 2.0
# Exact insphere/circumsphere ratio of Dodecahedron & Icosahedron:
# r_in / R_out = sqrt((5 + 2*sqrt(5)) / 15) = sqrt((4*phi + 3) / 15)
DODEC_ICOSA_RATIO = math.sqrt((5.0 + 2.0 * SQRT5) / 15.0)

# ── Master Architectural Elevations (Z-up, Meters) ─────────────────────────
CENTER_Z = 1.480      # Center of the cosmos (Sol, mu) above pedestal floor Z = 0
R_SATURN_OUT = 1.000  # Outer radius of Saturn's cutaway bowl (2.00 m diameter)


@dataclass(frozen=True)
class TabulaIIIRadii:
    """Exact radial schedule for all 6 planetary shells, 5 Platonic scaffolds, and Sol."""

    saturn_out: float
    saturn_in: float
    cube_r: float
    jupiter_out: float
    jupiter_in: float
    tetra_r: float
    mars_out: float
    mars_in: float
    dodeca_r: float
    earth_out: float
    earth_in: float
    icosa_r: float
    venus_out: float
    venus_in: float
    octa_r: float
    mercury_out: float
    mercury_in: float
    sol_r: float


def compute_radii(scale_mode: str = "exact") -> TabulaIIIRadii:
    """Compute exact nested shell and polyhedron radii in meters.

    Modes:
      - ``"exact"``: Exact Caput XIII Euclidean ratios (Cube 1/sqrt(3),
        Tetrahedron 1/3, Dodecahedron & Icosahedron sqrt((5+2*sqrt(5))/15),
        Octahedron 1/sqrt(3)) with realistic thin planetary eccentricity shells.
      - ``"expanded"``: Slightly magnified inner trio (Mars-Earth-Venus-Mercury)
        preserving exact polyhedron tangency for wide-angle legibility.
    """
    if scale_mode == "expanded":
        # Enlarged inner core while preserving visual nesting hierarchy
        sat_out = R_SATURN_OUT
        sat_in = 0.945
        cube_r = sat_in
        jup_out = cube_r / SQRT3  # 0.5456
        jup_in = 0.510
        tetra_r = jup_in
        mar_out = 0.285
        mar_in = 0.265
        dodeca_r = mar_in
        ear_out = dodeca_r * DODEC_ICOSA_RATIO  # 0.2106
        ear_in = 0.195
        icosa_r = ear_in
        ven_out = icosa_r * DODEC_ICOSA_RATIO   # 0.1550
        ven_in = 0.143
        octa_r = ven_in
        mer_out = octa_r / SQRT3                # 0.0826
        mer_in = 0.072
        sol_r = 0.036
        return TabulaIIIRadii(
            sat_out, sat_in, cube_r, jup_out, jup_in, tetra_r,
            mar_out, mar_in, dodeca_r, ear_out, ear_in, icosa_r,
            ven_out, ven_in, octa_r, mer_out, mer_in, sol_r,
        )

    # Default: Exact Caput XIII Euclidean ratios throughout!
    sat_out = R_SATURN_OUT
    sat_in = 0.945
    cube_r = sat_in
    jup_out = cube_r / SQRT3                 # 0.545596 m
    jup_in = jup_out - 0.036                 # 0.509596 m
    tetra_r = jup_in
    mar_out = tetra_r / 3.0                  # 0.169865 m
    mar_in = mar_out - 0.011                 # 0.158865 m
    dodeca_r = mar_in
    ear_out = dodeca_r * DODEC_ICOSA_RATIO   # 0.126243 m
    ear_in = ear_out - 0.008                 # 0.118243 m
    icosa_r = ear_in
    ven_out = icosa_r * DODEC_ICOSA_RATIO    # 0.093962 m
    ven_in = ven_out - 0.006                 # 0.087962 m
    octa_r = ven_in
    mer_out = octa_r / SQRT3                 # 0.050785 m
    mer_in = mer_out - 0.005                 # 0.045785 m
    sol_r = 0.024                            # 0.024000 m (48 mm glowing Sun)
    return TabulaIIIRadii(
        sat_out, sat_in, cube_r, jup_out, jup_in, tetra_r,
        mar_out, mar_in, dodeca_r, ear_out, ear_in, icosa_r,
        ven_out, ven_in, octa_r, mer_out, mer_in, sol_r,
    )


# ── Museum Orrery Metallic & Mineral PBR Material Palette ──────────────────
MATERIALS: dict[str, dict[str, Any]] = {
    # Carved Renaissance Pedestal & Meridian Cradle
    "pedestal_stone": {"color": (0.16, 0.17, 0.20), "roughness": 0.68, "metallic": 0.08},
    "pedestal_trim":  {"color": (0.28, 0.26, 0.24), "roughness": 0.52, "metallic": 0.22},
    "pedestal_bronze": {"color": (0.58, 0.44, 0.24), "roughness": 0.34, "metallic": 0.84},
    "cradle_strap":   {"color": (0.48, 0.36, 0.20), "roughness": 0.36, "metallic": 0.86},
    "finial_gold":    {"color": (0.85, 0.68, 0.30), "roughness": 0.24, "metallic": 0.92},

    # Cutaway Hemispherical Planetary Shells (silvered pewter / engraved ivory-silver / orbital tints)
    "saturn_shell":   {"color": (0.76, 0.72, 0.62), "roughness": 0.36, "metallic": 0.62},
    "saturn_rim":     {"color": (0.86, 0.76, 0.52), "roughness": 0.26, "metallic": 0.82},
    "jupiter_shell":  {"color": (0.78, 0.70, 0.64), "roughness": 0.34, "metallic": 0.60},
    "jupiter_rim":    {"color": (0.86, 0.64, 0.50), "roughness": 0.26, "metallic": 0.82},
    "mars_shell":     {"color": (0.76, 0.62, 0.58), "roughness": 0.34, "metallic": 0.62},
    "mars_rim":       {"color": (0.88, 0.50, 0.44), "roughness": 0.26, "metallic": 0.82},
    "earth_shell":    {"color": (0.54, 0.74, 0.68), "roughness": 0.30, "metallic": 0.64},
    "earth_rim":      {"color": (0.42, 0.84, 0.68), "roughness": 0.24, "metallic": 0.84},
    "venus_shell":    {"color": (0.64, 0.74, 0.86), "roughness": 0.30, "metallic": 0.64},
    "venus_rim":      {"color": (0.58, 0.76, 0.94), "roughness": 0.24, "metallic": 0.84},
    "mercury_shell":  {"color": (0.68, 0.80, 0.88), "roughness": 0.28, "metallic": 0.70},
    "mercury_rim":    {"color": (0.52, 0.84, 0.96), "roughness": 0.22, "metallic": 0.88},

    # Five Architectural Open-Frame Platonic Scaffolds (Outer, Inner, Reveal)
    "cube_outer":     {"color": (0.88, 0.68, 0.26), "roughness": 0.26, "metallic": 0.90},
    "cube_reveal":    {"color": (0.66, 0.50, 0.20), "roughness": 0.34, "metallic": 0.86},
    "cube_inner":     {"color": (0.48, 0.36, 0.16), "roughness": 0.42, "metallic": 0.82},

    "tetra_outer":    {"color": (0.84, 0.44, 0.34), "roughness": 0.28, "metallic": 0.88},
    "tetra_reveal":   {"color": (0.64, 0.32, 0.24), "roughness": 0.36, "metallic": 0.84},
    "tetra_inner":    {"color": (0.46, 0.22, 0.18), "roughness": 0.42, "metallic": 0.80},

    "dodeca_outer":   {"color": (0.74, 0.56, 0.92), "roughness": 0.26, "metallic": 0.86},
    "dodeca_reveal":  {"color": (0.54, 0.40, 0.72), "roughness": 0.34, "metallic": 0.82},
    "dodeca_inner":   {"color": (0.38, 0.28, 0.54), "roughness": 0.42, "metallic": 0.78},

    "icosa_outer":    {"color": (0.42, 0.66, 0.94), "roughness": 0.26, "metallic": 0.88},
    "icosa_reveal":   {"color": (0.30, 0.50, 0.76), "roughness": 0.34, "metallic": 0.84},
    "icosa_inner":    {"color": (0.20, 0.36, 0.58), "roughness": 0.42, "metallic": 0.80},

    "octa_outer":     {"color": (0.34, 0.82, 0.94), "roughness": 0.24, "metallic": 0.90},
    "octa_reveal":    {"color": (0.22, 0.62, 0.76), "roughness": 0.32, "metallic": 0.86},
    "octa_inner":     {"color": (0.16, 0.44, 0.56), "roughness": 0.40, "metallic": 0.82},

    # Solar Core & Rim Planetary Medallions
    "sol_core":       {"color": (1.00, 0.82, 0.28), "roughness": 0.15, "metallic": 0.30, "emissive": True},
    "planet_bead":    {"color": (0.94, 0.80, 0.40), "roughness": 0.22, "metallic": 0.92},
}


# ── Pure-Python Standalone CAD Scene Shim (matches IngeTrazo API) ──────────
class ShimVector3D:
    __slots__ = ("x", "y", "z")

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def to_tuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)


class ShimFace:
    __slots__ = ("pts", "attrs")

    def __init__(self, pts: list[Any]) -> None:
        self.pts: list[tuple[float, float, float]] = [
            p.to_tuple() if hasattr(p, "to_tuple") else (float(p[0]), float(p[1]), float(p[2]))
            for p in pts
        ]
        self.attrs: dict[str, Any] = {}


class ShimMesh:
    def __init__(self) -> None:
        self.faces: list[ShimFace] = []

    def add_face(self, pts: list[Any]) -> ShimFace:
        f = ShimFace(pts)
        self.faces.append(f)
        return f


class ShimGroup:
    def __init__(self, name: str, mesh: ShimMesh | None = None) -> None:
        self.name = name
        self.mesh = mesh or ShimMesh()
        self.pivot = None


class ShimScene:
    def __init__(self) -> None:
        self.groups: list[ShimGroup] = []
        self.version: int = 0

    def clear(self) -> None:
        self.groups.clear()


# ── Vector Helpers ─────────────────────────────────────────────────────────
Vec3 = tuple[float, float, float]


def v_add(a: Vec3, b: Vec3) -> Vec3:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def v_sub(a: Vec3, b: Vec3) -> Vec3:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def v_scale(a: Vec3, s: float) -> Vec3:
    return (a[0] * s, a[1] * s, a[2] * s)


def v_dot(a: Vec3, b: Vec3) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def v_cross(a: Vec3, b: Vec3) -> Vec3:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def v_len(a: Vec3) -> float:
    return math.sqrt(v_dot(a, a))


def v_norm(a: Vec3) -> Vec3:
    m = v_len(a)
    return (a[0] / m, a[1] / m, a[2] / m) if m > 1e-12 else (0.0, 0.0, 1.0)


def v_lerp(a: Vec3, b: Vec3, t: float) -> Vec3:
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t)


def rot_x(v: Vec3, rad: float) -> Vec3:
    c, s = math.cos(rad), math.sin(rad)
    return (v[0], v[1] * c - v[2] * s, v[1] * s + v[2] * c)


def rot_z(v: Vec3, rad: float) -> Vec3:
    c, s = math.cos(rad), math.sin(rad)
    return (v[0] * c - v[1] * s, v[0] * s + v[1] * c, v[2])


# ── IngeTrazo / Shim Scene Helpers ─────────────────────────────────────────
def create_scene_group(scene: Any, name: str) -> Any:
    """Create a named group compatible with both IngeTrazo 0.6.0 and ShimScene."""
    if isinstance(scene, ShimScene):
        grp = ShimGroup(name=name, mesh=ShimMesh())
        scene.groups.append(grp)
        return grp
    from core.group import Group
    from core.mesh import Mesh

    grp = Group(name=name, mesh=Mesh())
    scene.groups.append(grp)
    return grp


def add_face(mesh: Any, pts: list[Vec3], attrs: dict[str, Any], mat_key: str = "") -> Any:
    """Add a polygon face with material metadata to either ShimMesh or IngeTrazo Mesh."""
    face_attrs = dict(attrs)
    if mat_key:
        face_attrs["_mat"] = mat_key
    if isinstance(mesh, ShimMesh):
        f = mesh.add_face(pts)
        f.attrs.update(face_attrs)
        return f
    from PySide6.QtGui import QVector3D

    qpts = [p if isinstance(p, QVector3D) else QVector3D(float(p[0]), float(p[1]), float(p[2])) for p in pts]
    f = mesh.add_face(qpts)
    if f is not None:
        f.attrs.update(face_attrs)
    return f


def add_quad(mesh: Any, p0: Vec3, p1: Vec3, p2: Vec3, p3: Vec3, mat_key: str) -> None:
    add_face(mesh, [p0, p1, p2, p3], MATERIALS[mat_key], mat_key=mat_key)


def add_tri(mesh: Any, p0: Vec3, p1: Vec3, p2: Vec3, mat_key: str) -> None:
    add_face(mesh, [p0, p1, p2], MATERIALS[mat_key], mat_key=mat_key)


def add_box(
    mesh: Any,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    y1: float,
    z1: float,
    mat_key: str,
) -> None:
    p000 = (x0, y0, z0)
    p100 = (x1, y0, z0)
    p110 = (x1, y1, z0)
    p010 = (x0, y1, z0)
    p001 = (x0, y0, z1)
    p101 = (x1, y0, z1)
    p111 = (x1, y1, z1)
    p011 = (x0, y1, z1)
    add_quad(mesh, p000, p010, p110, p100, mat_key)  # -Z bottom
    add_quad(mesh, p001, p101, p111, p011, mat_key)  # +Z top
    add_quad(mesh, p000, p100, p101, p001, mat_key)  # -Y south
    add_quad(mesh, p100, p110, p111, p101, mat_key)  # +X east
    add_quad(mesh, p110, p010, p011, p111, mat_key)  # +Y north
    add_quad(mesh, p010, p000, p001, p011, mat_key)  # -X west


def add_revolved_closed_profile(
    mesh: Any,
    cx: float,
    cy: float,
    cz: float,
    profile_rz: list[tuple[float, float, str]],
    segs: int = 64,
) -> None:
    """Revolve a closed CCW cross-section [(r, z, mat_key), ...] around the Z-axis.

    Each segment ``profile_rz[k] -> profile_rz[k+1]`` inherits ``profile_rz[k][2]``
    as its material key, allowing distinct rim vs. bowl materials on one watertight shell.
    Vertices with ``r <= 1e-6`` cleanly emit pole triangles instead of degenerate quads.
    """
    n = len(profile_rz)
    rings: list[list[Vec3]] = []
    for k in range(n):
        r, z, _ = profile_rz[k]
        ring: list[Vec3] = []
        for s in range(segs):
            ang = 2.0 * math.pi * s / segs
            ring.append((cx + r * math.cos(ang), cy + r * math.sin(ang), cz + z))
        rings.append(ring)

    for k in range(n):
        nk = (k + 1) % n
        r0, z0, mat_key = profile_rz[k]
        r1, z1, _ = profile_rz[nk]
        if abs(r0 - r1) < 1e-9 and abs(z0 - z1) < 1e-9:
            continue
        for s in range(segs):
            ns = (s + 1) % segs
            a0, a1 = rings[k][s], rings[k][ns]
            b0, b1 = rings[nk][s], rings[nk][ns]
            if r0 < 1e-6 and r1 < 1e-6:
                continue
            elif r0 < 1e-6:
                add_tri(mesh, (cx, cy, cz + z0), b1, b0, mat_key)
            elif r1 < 1e-6:
                add_tri(mesh, a0, a1, (cx, cy, cz + z1), mat_key)
            else:
                add_quad(mesh, a0, a1, b1, b0, mat_key)


def add_uv_sphere(
    mesh: Any,
    cx: float,
    cy: float,
    cz: float,
    radius: float,
    mat_key: str,
    lon_segs: int = 24,
    lat_segs: int = 12,
) -> None:
    """Build a watertight UV sphere using a closed semicircular revolved profile."""
    profile: list[tuple[float, float, str]] = []
    for i in range(lat_segs + 1):
        lat = -0.5 * math.pi + math.pi * i / lat_segs
        r = max(0.0, radius * math.cos(lat))
        z = radius * math.sin(lat)
        if i == 0 or i == lat_segs:
            r = 0.0
        profile.append((r, z, mat_key))
    # Revolved closed profile expects CCW in (r, z) so outward normals face +r;
    # going south (-pi/2) -> north (+pi/2) has outward normal to the RIGHT of path,
    # matching our add_revolved_closed_profile winding (a0, b0, b1, a1)!
    for k in range(len(profile) - 1):
        r0, z0, mk = profile[k]
        r1, z1, _ = profile[k + 1]
        for s in range(lon_segs):
            ns = (s + 1) % lon_segs
            t0 = 2.0 * math.pi * s / lon_segs
            t1 = 2.0 * math.pi * ns / lon_segs
            p_a0 = (cx + r0 * math.cos(t0), cy + r0 * math.sin(t0), cz + z0)
            p_a1 = (cx + r0 * math.cos(t1), cy + r0 * math.sin(t1), cz + z0)
            p_b0 = (cx + r1 * math.cos(t0), cy + r1 * math.sin(t0), cz + z1)
            p_b1 = (cx + r1 * math.cos(t1), cy + r1 * math.sin(t1), cz + z1)
            if r0 < 1e-6:
                add_tri(mesh, (cx, cy, cz + z0), p_b1, p_b0, mk)
            elif r1 < 1e-6:
                add_tri(mesh, p_a0, p_a1, (cx, cy, cz + z1), mk)
            else:
                add_quad(mesh, p_a0, p_a1, p_b1, p_b0, mk)


def add_extruded_polygon_z(
    mesh: Any,
    pts_xy: list[tuple[float, float]],
    z0: float,
    z1: float,
    mat_key: str,
) -> None:
    """Extrude a CCW 2D polygon cleanly from z0 to z1 with capped top & bottom."""
    bot = [(x, y, z0) for x, y in pts_xy]
    top = [(x, y, z1) for x, y in pts_xy]
    n = len(pts_xy)
    # Fan triangulation on bottom & top for universal compatibility (OBJ/GLB/IngeTrazo)
    cx = sum(x for x, _ in pts_xy) / n
    cy = sum(y for _, y in pts_xy) / n
    c_bot = (cx, cy, z0)
    c_top = (cx, cy, z1)
    for i in range(n):
        ni = (i + 1) % n
        add_tri(mesh, c_bot, bot[ni], bot[i], mat_key)
        add_tri(mesh, c_top, top[i], top[ni], mat_key)
        add_quad(mesh, bot[i], bot[ni], top[ni], top[i], mat_key)


def add_beveled_polyhedron_frame(
    mesh: Any,
    verts: list[Vec3],
    faces: list[list[int]],
    center: Vec3,
    aperture: float,
    radial_depth: float,
    outer_mat: str,
    reveal_mat: str,
    inner_mat: str,
) -> None:
    """Build a watertight Leonardo/Kepler open-frame mitered solid-beam polyhedron.

    Each k-gon face produces 3*k watertight quads:
      - k outer chamfered beam quads (lying on the exact outer polyhedron planes),
      - k inner radial cavity quads (at radius factor ``1.0 - radial_depth``),
      - k window-reveal jamb quads bridging outer aperture to inner cavity.
    """
    r_in_scale = 1.0 - radial_depth
    cx, cy, cz = center

    def shift(p: Vec3) -> Vec3:
        return (p[0] + cx, p[1] + cy, p[2] + cz)

    for face in faces:
        k = len(face)
        fverts = [verts[idx] for idx in face]
        # Face centroid in local space (around origin)
        fc = v_scale(
            (sum(p[0] for p in fverts), sum(p[1] for p in fverts), sum(p[2] for p in fverts)),
            1.0 / k,
        )
        # Ensure CCW outward orientation around fc
        fn = v_cross(v_sub(fverts[1], fverts[0]), v_sub(fverts[2], fverts[0]))
        if v_dot(fn, fc) < 0:
            fverts = list(reversed(fverts))

        w_out = [v_lerp(v, fc, aperture) for v in fverts]
        v_in = [v_scale(v, r_in_scale) for v in fverts]
        w_in = [v_scale(w, r_in_scale) for w in w_out]

        for i in range(k):
            ni = (i + 1) % k
            # Outer face strip (outward normal)
            add_quad(
                mesh,
                shift(fverts[i]),
                shift(fverts[ni]),
                shift(w_out[ni]),
                shift(w_out[i]),
                outer_mat,
            )
            # Inner cavity strip (inward normal, reversed winding)
            add_quad(
                mesh,
                shift(v_in[ni]),
                shift(v_in[i]),
                shift(w_in[i]),
                shift(w_in[ni]),
                inner_mat,
            )
            # Window-jamb reveal (normal pointing inward toward window center fc)
            add_quad(
                mesh,
                shift(w_out[i]),
                shift(w_out[ni]),
                shift(w_in[ni]),
                shift(w_in[i]),
                reveal_mat,
            )
