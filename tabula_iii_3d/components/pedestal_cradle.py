"""Carved Renaissance Pedestal, S-Scroll Volute Buttresses, Pyramidal Finials &
Four Meridian Cradle Straps supporting Saturn's outer bowl (Tabula III, 1597).

Directly modeled from Christoph Leibfried's engraved base in folio 0034.
"""

from __future__ import annotations

import math
from typing import Any

from .primitives import (
    CENTER_Z,
    R_SATURN_OUT,
    add_box,
    add_extruded_polygon_z,
    add_quad,
    add_revolved_closed_profile,
    add_tri,
    create_scene_group,
    rot_z,
)


def _add_cardinal_prism(
    mesh: Any,
    profile_rz: list[tuple[float, float]],
    half_width: float,
    angle_rad: float,
    mat_key: str,
) -> None:
    """Extrude a 2D (r, z) polygon transversely by ±half_width and rotate by angle_rad around Z."""
    n = len(profile_rz)
    left_pts = [rot_z((r, -half_width, z), angle_rad) for r, z in profile_rz]
    right_pts = [rot_z((r, +half_width, z), angle_rad) for r, z in profile_rz]

    # Centroid for fan-triangulating the ±Y side cheeks cleanly
    cr = sum(r for r, _ in profile_rz) / n
    cz = sum(z for _, z in profile_rz) / n
    c_left = rot_z((cr, -half_width, cz), angle_rad)
    c_right = rot_z((cr, +half_width, cz), angle_rad)

    for i in range(n):
        ni = (i + 1) % n
        # Side cheeks (ensure outward normals along ±Y before rotation)
        add_tri(mesh, c_left, left_pts[i], left_pts[ni], mat_key)
        add_tri(mesh, c_right, right_pts[ni], right_pts[i], mat_key)
        # Perimeter thickness quads
        add_quad(mesh, left_pts[i], right_pts[i], right_pts[ni], left_pts[ni], mat_key)


def _add_pyramid_finial(
    mesh: Any,
    r_base: float,
    z_center: float,
    half_h: float,
    half_w: float,
    tip_len: float,
    angle_rad: float,
    mat_key: str,
) -> None:
    """Add an outward-pointing 4-sided Renaissance pyramidal spike finial along radial angle_rad."""
    p0 = rot_z((r_base, -half_w, z_center - half_h), angle_rad)
    p1 = rot_z((r_base, +half_w, z_center - half_h), angle_rad)
    p2 = rot_z((r_base, +half_w, z_center + half_h), angle_rad)
    p3 = rot_z((r_base, -half_w, z_center + half_h), angle_rad)
    tip = rot_z((r_base + tip_len, 0.0, z_center), angle_rad)

    # 4 triangular faces pointing outward + back cap
    add_tri(mesh, p0, p1, tip, mat_key)
    add_tri(mesh, p1, p2, tip, mat_key)
    add_tri(mesh, p2, p3, tip, mat_key)
    add_tri(mesh, p3, p0, tip, mat_key)
    add_quad(mesh, p0, p3, p2, p1, mat_key)


def _add_meridian_strap(
    mesh: Any,
    angle_rad: float,
    r_inner: float,
    thickness: float,
    half_width: float,
    lat_start_deg: float,
    lat_end_deg: float,
    steps: int,
    mat_key: str,
) -> None:
    """Add a solid curved bronze meridian strap hugging Saturn's lower hemisphere."""
    r_out = r_inner + thickness
    rings: list[tuple[tuple[float, float, float], ...]] = []
    for i in range(steps + 1):
        lat = math.radians(lat_start_deg + (lat_end_deg - lat_start_deg) * i / steps)
        # Meridian point on sphere centered at (0, 0, CENTER_Z)
        ri = r_inner * math.cos(lat)
        zi = CENTER_Z + r_inner * math.sin(lat)
        ro = r_out * math.cos(lat)
        zo = CENTER_Z + r_out * math.sin(lat)
        # 4 corners of rectangular cross section at this latitude
        p_in_l = rot_z((ri, -half_width, zi), angle_rad)
        p_in_r = rot_z((ri, +half_width, zi), angle_rad)
        p_out_r = rot_z((ro, +half_width, zo), angle_rad)
        p_out_l = rot_z((ro, -half_width, zo), angle_rad)
        rings.append((p_in_l, p_in_r, p_out_r, p_out_l))

    for i in range(steps):
        a = rings[i]
        b = rings[i + 1]
        # Outer face, inner face, left cheek, right cheek
        add_quad(mesh, a[3], a[2], b[2], b[3], mat_key)  # outer
        add_quad(mesh, a[1], a[0], b[0], b[1], mat_key)  # inner
        add_quad(mesh, a[0], a[3], b[3], b[0], mat_key)  # left (-Y)
        add_quad(mesh, a[2], a[1], b[1], b[2], mat_key)  # right (+Y)

    # End caps
    a0 = rings[0]
    add_quad(mesh, a0[0], a0[1], a0[2], a0[3], mat_key)
    an = rings[-1]
    add_quad(mesh, an[3], an[2], an[1], an[0], mat_key)


def build_pedestal_cradle(scene: Any, z_offset: float = 0.0) -> Any:
    """Build the Renaissance carved plinth, 4 scrolled volute legs, finials & cradle straps."""
    grp = create_scene_group(scene, "01_Pedestal_Cradle")
    m = grp.mesh

    # 1. Lower Base Plinth Slab (1.28 m x 1.28 m, Z = 0.000 -> 0.055 m)
    add_box(m, -0.64, -0.64, 0.000 + z_offset, 0.64, 0.64, 0.055 + z_offset, "pedestal_stone")

    # 2. Stepped Upper Plinth (1.06 m x 1.06 m, Z = 0.055 -> 0.105 m)
    add_box(m, -0.53, -0.53, 0.055 + z_offset, 0.53, 0.53, 0.105 + z_offset, "pedestal_trim")

    # 3. Four Cardinal Semicircular Bastion Lobes projecting from the stepped plinth
    for k in range(4):
        ang = k * math.pi / 2.0
        lobe_pts: list[tuple[float, float]] = []
        r_lobe = 0.145
        cx_lobe = 0.51
        for i in range(13):
            t = -math.pi / 2.0 + math.pi * i / 12.0
            px = cx_lobe + r_lobe * math.cos(t)
            py = r_lobe * math.sin(t)
            rx, ry, _ = rot_z((px, py, 0.0), ang)
            lobe_pts.append((rx, ry))
        add_extruded_polygon_z(m, lobe_pts, 0.055 + z_offset, 0.108 + z_offset, "pedestal_trim")

    # 4. Central Circular Turntable Medallion & Lower Calyx Collar
    turntable_prof = [
        (0.0, 0.105, "pedestal_bronze"),
        (0.35, 0.105, "pedestal_bronze"),
        (0.35, 0.132, "pedestal_bronze"),
        (0.32, 0.142, "pedestal_trim"),
        (0.18, 0.142, "pedestal_bronze"),
        (0.16, 0.210, "pedestal_bronze"),
        (0.21, 0.455, "pedestal_bronze"),
        (0.30, 0.525, "cradle_strap"),
        (0.23, 0.525, "cradle_strap"),
        (0.12, 0.482, "pedestal_bronze"),
        (0.0, 0.482, "pedestal_bronze"),
    ]
    add_revolved_closed_profile(m, 0.0, 0.0, z_offset, turntable_prof, segs=40)

    # 5. Four Cardinal Cruciform Scrolled Volute Buttress Legs + 8 Pyramidal Spike Finials
    for k in range(4):
        ang = k * math.pi / 2.0

        # Outer vertical architectural leg + curved foot resting on the bastion lobe
        leg_profile = [
            (0.45, 0.108 + z_offset),
            (0.56, 0.108 + z_offset),
            (0.56, 0.185 + z_offset),
            (0.51, 0.205 + z_offset),
            (0.51, 0.365 + z_offset),
            (0.57, 0.375 + z_offset),
            (0.57, 0.455 + z_offset),
            (0.43, 0.455 + z_offset),
            (0.43, 0.190 + z_offset),
            (0.45, 0.108 + z_offset),
        ]
        _add_cardinal_prism(m, leg_profile[:-1], half_width=0.052, angle_rad=ang, mat_key="pedestal_bronze")

        # Horizontal yoke arm connecting vertical leg to central S-scroll calyx
        yoke_profile = [
            (0.15, 0.370 + z_offset),
            (0.45, 0.370 + z_offset),
            (0.45, 0.445 + z_offset),
            (0.15, 0.445 + z_offset),
        ]
        _add_cardinal_prism(m, yoke_profile, half_width=0.044, angle_rad=ang, mat_key="pedestal_bronze")

        # Upper S-Scroll Volute Arch curving up under Saturn's bowl
        upper_scroll = [
            (0.17, 0.445 + z_offset),
            (0.36, 0.445 + z_offset),
            (0.41, 0.510 + z_offset),
            (0.37, 0.575 + z_offset),
            (0.28, 0.590 + z_offset),
            (0.20, 0.545 + z_offset),
            (0.16, 0.490 + z_offset),
        ]
        _add_cardinal_prism(m, upper_scroll, half_width=0.040, angle_rad=ang, mat_key="cradle_strap")

        # Lower S-Scroll Volute Curl resting on the central turntable
        lower_scroll = [
            (0.15, 0.142 + z_offset),
            (0.33, 0.142 + z_offset),
            (0.36, 0.215 + z_offset),
            (0.31, 0.295 + z_offset),
            (0.23, 0.310 + z_offset),
            (0.16, 0.255 + z_offset),
        ]
        _add_cardinal_prism(m, lower_scroll, half_width=0.036, angle_rad=ang, mat_key="pedestal_bronze")

        # Lower & Upper Iconic Pyramidal Spike Finials (matching 1597 copperplate!)
        _add_pyramid_finial(
            m, r_base=0.56, z_center=0.146 + z_offset,
            half_h=0.038, half_w=0.042, tip_len=0.165,
            angle_rad=ang, mat_key="finial_gold",
        )
        _add_pyramid_finial(
            m, r_base=0.57, z_center=0.415 + z_offset,
            half_h=0.040, half_w=0.044, tip_len=0.175,
            angle_rad=ang, mat_key="finial_gold",
        )

        # Curved Bronze Meridian Cradle Strap hugging Saturn's outer bowl up to equator
        _add_meridian_strap(
            m,
            angle_rad=ang,
            r_inner=R_SATURN_OUT - 0.002,
            thickness=0.024,
            half_width=0.042,
            lat_start_deg=-80.0,
            lat_end_deg=-0.5,
            steps=24,
            mat_key="cradle_strap",
        )

    return grp
