"""Five Watertight Architectural Open-Frame Platonic Polyhedra Scaffolds
(beta Cube, delta Tetrahedron, zeta Dodecahedron, theta Icosahedron, kappa Octahedron)
in exact Tabula III (folio 0034) orientation and exact Caput XIII Euclidean proportions.
"""

from __future__ import annotations

import math
from typing import Any

from .primitives import (
    CENTER_Z,
    PHI,
    TabulaIIIRadii,
    Vec3,
    add_beveled_polyhedron_frame,
    create_scene_group,
    rot_x,
    rot_z,
    v_add,
    v_cross,
    v_dot,
    v_norm,
    v_scale,
    v_sub,
)


def _norm_verts(raw: list[Vec3], radius: float) -> list[Vec3]:
    return [v_scale(v_norm(v), radius) for v in raw]


def _make_cube(r: float) -> tuple[list[Vec3], list[list[int]]]:
    """Face-horizontal Cube matching Tabula III beta (square top & bottom faces)."""
    raw: list[Vec3] = [
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1,  1), (1, -1,  1), (1, 1,  1), (-1, 1,  1),
    ]
    verts = _norm_verts(raw, r)
    faces = [
        [0, 3, 2, 1],  # -Z bottom
        [4, 5, 6, 7],  # +Z top
        [0, 1, 5, 4],  # -Y south
        [1, 2, 6, 5],  # +X east
        [2, 3, 7, 6],  # +Y north
        [3, 0, 4, 7],  # -X west
    ]
    return verts, faces


def _make_tetrahedron_apex_up(r: float, yaw_deg: float = -22.0) -> tuple[list[Vec3], list[list[int]]]:
    """Apex-up Tetrahedron matching Tabula III delta (horizontal triangle base at z = -R/3)."""
    z_base = -r / 3.0
    r_base = r * (2.0 * math.sqrt(2.0) / 3.0)
    yaw = math.radians(yaw_deg)
    verts: list[Vec3] = [(0.0, 0.0, r)]
    for k in range(3):
        ang = yaw + 2.0 * math.pi * k / 3.0
        verts.append((r_base * math.cos(ang), r_base * math.sin(ang), z_base))
    faces = [
        [1, 3, 2],  # bottom horizontal base (-Z normal)
        [0, 1, 2],  # side 1
        [0, 2, 3],  # side 2
        [0, 3, 1],  # side 3
    ]
    return verts, faces


def _make_icosahedron_vertex_up(r: float, yaw_deg: float = 18.0) -> tuple[list[Vec3], list[list[int]]]:
    """Vertex-up Icosahedron matching Tabula III theta (polar dual to flat-top Dodecahedron)."""
    raw: list[Vec3] = [
        (0, 1, PHI), (0, -1, PHI), (0, 1, -PHI), (0, -1, -PHI),
        (1, PHI, 0), (-1, PHI, 0), (1, -PHI, 0), (-1, -PHI, 0),
        (PHI, 0, 1), (-PHI, 0, 1), (PHI, 0, -1), (-PHI, 0, -1),
    ]
    # Rotate around X by atan2(1, PHI) so vertex (0, 1, PHI) points straight along +Z
    tilt = math.atan2(1.0, PHI)
    yaw = math.radians(yaw_deg)
    verts = [rot_z(rot_x(v, tilt), yaw) for v in _norm_verts(raw, r)]
    faces = [
        [0, 1, 8], [0, 8, 4], [0, 4, 5], [0, 5, 9], [0, 9, 1],
        [1, 6, 8], [8, 6, 10], [8, 10, 4], [4, 10, 2], [4, 2, 5],
        [5, 2, 11], [5, 11, 9], [9, 11, 7], [9, 7, 1], [1, 7, 6],
        [3, 6, 7], [3, 10, 6], [3, 2, 10], [3, 11, 2], [3, 7, 11],
    ]
    return verts, faces


def _make_dodecahedron_face_up(r: float, yaw_deg: float = 18.0) -> tuple[list[Vec3], list[list[int]]]:
    """Flat-pentagon-top Dodecahedron matching Tabula III zeta (dual of vertex-up Icosahedron)."""
    ico_v, ico_f = _make_icosahedron_vertex_up(1.0, yaw_deg=yaw_deg)
    raw_verts: list[Vec3] = []
    for f in ico_f:
        c = v_add(v_add(ico_v[f[0]], ico_v[f[1]]), ico_v[f[2]])
        raw_verts.append(v_norm(c))
    verts = _norm_verts(raw_verts, r)

    faces: list[list[int]] = []
    for vi in range(12):
        adj = [fi for fi, f in enumerate(ico_f) if vi in f]
        axis = ico_v[vi]
        ref = v_norm(v_sub(verts[adj[0]], v_scale(axis, v_dot(verts[adj[0]], axis))))
        tan = v_cross(axis, ref)
        adj.sort(key=lambda idx: math.atan2(v_dot(verts[idx], tan), v_dot(verts[idx], ref)))
        faces.append(adj)
    return verts, faces


def _make_octahedron_vertex_up(r: float, yaw_deg: float = 15.0) -> tuple[list[Vec3], list[list[int]]]:
    """Vertex-up Octahedron matching Tabula III kappa & Ch. XVII horizontal equatorial square."""
    yaw = math.radians(yaw_deg)
    raw: list[Vec3] = [
        (r, 0, 0), (-r, 0, 0),
        (0, r, 0), (0, -r, 0),
        (0, 0, r), (0, 0, -r),
    ]
    verts = [rot_z(v, yaw) for v in raw]
    faces = [
        [4, 0, 2], [4, 2, 1], [4, 1, 3], [4, 3, 0],
        [5, 2, 0], [5, 1, 2], [5, 3, 1], [5, 0, 3],
    ]
    return verts, faces


def build_platonic_scaffolds(
    scene: Any,
    radii: TabulaIIIRadii,
    explode: float = 0.0,
) -> dict[str, Any]:
    """Build all five watertight beveled open-frame Platonic polyhedra (beta..kappa)."""
    # (group_name, builder, circumradius, aperture, depth, mat_prefix, explode_step)
    specs = [
        ("03_Beta_Cube_Frame",         _make_cube(radii.cube_r),                      0.17, 0.056, "cube",   0.11),
        ("05_Delta_Tetrahedron_Frame", _make_tetrahedron_apex_up(radii.tetra_r),      0.16, 0.056, "tetra",  0.33),
        ("07_Zeta_Dodecahedron_Frame", _make_dodecahedron_face_up(radii.dodeca_r),    0.22, 0.052, "dodeca", 0.55),
        ("09_Theta_Icosahedron_Frame", _make_icosahedron_vertex_up(radii.icosa_r),    0.24, 0.044, "icosa",  0.76),
        ("11_Kappa_Octahedron_Frame",  _make_octahedron_vertex_up(radii.octa_r),      0.22, 0.052, "octa",   0.95),
    ]

    groups: dict[str, Any] = {}
    for name, (verts, faces), aperture, depth, prefix, exp_step in specs:
        grp = create_scene_group(scene, name)
        cz = CENTER_Z + explode * exp_step
        add_beveled_polyhedron_frame(
            grp.mesh,
            verts=verts,
            faces=faces,
            center=(0.0, 0.0, cz),
            aperture=aperture,
            radial_depth=depth,
            outer_mat=f"{prefix}_outer",
            reveal_mat=f"{prefix}_reveal",
            inner_mat=f"{prefix}_inner",
        )
        groups[name] = grp

    return groups
