"""Six Thick-Walled Watertight Cutaway Hemispherical Planetary Shells (alpha..lambda)
and the Central Immobile Sun (mu) of Kepler's Tabula III (folio 0034).

Each planetary bowl has real radial shell thickness representing orbital eccentricity,
a double-beveled gleaming equatorial rim lip, and an engraved planetary medallion
bead seated on its right (+X) equatorial rim matching Christoph Leibfried's 1597 plate.
"""

from __future__ import annotations

import math
from typing import Any

from .primitives import (
    CENTER_Z,
    TabulaIIIRadii,
    add_revolved_closed_profile,
    add_uv_sphere,
    create_scene_group,
)


def _add_cutaway_hemisphere_bowl(
    mesh: Any,
    r_out: float,
    r_in: float,
    cz: float,
    shell_mat: str,
    rim_mat: str,
    lon_segs: int = 64,
    lat_segs: int = 20,
    cut_angle_deg: float = 0.0,
) -> None:
    """Build a watertight thick-walled lower hemispherical bowl with beveled equatorial lip."""
    thickness = max(0.002, r_out - r_in)
    bevel = min(thickness * 0.18, r_out * 0.012)
    lat_max = math.radians(cut_angle_deg)
    lat_min = -0.5 * math.pi

    profile: list[tuple[float, float, str]] = []

    # 1. Outer hemispherical surface: south pole -> just below equatorial rim
    for i in range(lat_segs + 1):
        lat = lat_min + (lat_max - lat_min) * i / lat_segs
        r = 0.0 if i == 0 else r_out * math.cos(lat)
        z = r_out * math.sin(lat)
        if i == lat_segs:
            z -= bevel
        profile.append((r, z, shell_mat))

    # 2. Outer chamfer -> flat equatorial rim lip -> inner chamfer
    r_top_out = r_out * math.cos(lat_max)
    z_top = r_out * math.sin(lat_max)
    r_top_in = r_in * math.cos(lat_max)
    z_top_in = r_in * math.sin(lat_max)

    profile.append((r_top_out - bevel, z_top, rim_mat))
    profile.append((r_top_in + bevel, z_top_in, rim_mat))
    profile.append((r_top_in, z_top_in - bevel, rim_mat))

    # 3. Inner concave hemispherical surface: rim -> inner south pole
    for i in range(1, lat_segs + 1):
        lat = lat_max - (lat_max - lat_min) * i / lat_segs
        r = 0.0 if i == lat_segs else r_in * math.cos(lat)
        z = r_in * math.sin(lat)
        profile.append((r, z, shell_mat))

    add_revolved_closed_profile(mesh, 0.0, 0.0, cz, profile, segs=lon_segs)


def _add_rim_planetary_globe(
    mesh: Any,
    r_mid: float,
    thickness: float,
    cz: float,
    azimuth_deg: float = 0.0,
    with_moon: bool = False,
) -> None:
    """Seat a gleaming planetary medallion globe onto the bowl's flat equatorial rim."""
    ang = math.radians(azimuth_deg)
    bead_r = max(0.005, thickness * 0.56)
    px = r_mid * math.cos(ang)
    py = r_mid * math.sin(ang)
    pz = cz + bead_r * 0.62
    add_uv_sphere(mesh, px, py, pz, bead_r, "planet_bead", lon_segs=16, lat_segs=10)

    if with_moon:
        # Companion Moon beside Earth's Orbis Magnus (Tabula III legend eta: "tellurem cum Luna ferentem")
        m_ang = ang + 0.16
        mx = r_mid * math.cos(m_ang)
        my = r_mid * math.sin(m_ang)
        add_uv_sphere(mesh, mx, my, pz, bead_r * 0.45, "earth_rim", lon_segs=12, lat_segs=8)


def build_planetary_bowls(
    scene: Any,
    radii: TabulaIIIRadii,
    explode: float = 0.0,
) -> dict[str, Any]:
    """Build all six concentric cutaway planetary hemispheres (alpha..lambda) and Sol (mu)."""
    # Optional vertical explode shift per layer (0.0 = exact nested Tabula III!)
    specs = [
        ("02_Alpha_Saturn_Bowl",  radii.saturn_out,  radii.saturn_in,  "saturn_shell",  "saturn_rim",  64, 22, -0.00, 0.0,   False),
        ("04_Gamma_Jupiter_Bowl", radii.jupiter_out, radii.jupiter_in, "jupiter_shell", "jupiter_rim", 56, 18,  0.22, -4.0,  False),
        ("06_Epsilon_Mars_Bowl",  radii.mars_out,    radii.mars_in,    "mars_shell",    "mars_rim",    48, 16,  0.44, -8.0,  False),
        ("08_Eta_Earth_Bowl",     radii.earth_out,   radii.earth_in,   "earth_shell",   "earth_rim",   40, 14,  0.66, -12.0, True),
        ("10_Iota_Venus_Bowl",    radii.venus_out,   radii.venus_in,   "venus_shell",   "venus_rim",   36, 14,  0.86, -15.0, False),
        ("12_Lambda_Mercury_Bowl",radii.mercury_out, radii.mercury_in, "mercury_shell", "mercury_rim", 32, 12,  1.04, -18.0, False),
    ]

    groups: dict[str, Any] = {}
    for name, r_out, r_in, s_mat, r_mat, lon_s, lat_s, exp_step, az_deg, has_moon in specs:
        grp = create_scene_group(scene, name)
        cz = CENTER_Z + explode * exp_step
        _add_cutaway_hemisphere_bowl(
            grp.mesh,
            r_out=r_out,
            r_in=r_in,
            cz=cz,
            shell_mat=s_mat,
            rim_mat=r_mat,
            lon_segs=lon_s,
            lat_segs=lat_s,
        )
        _add_rim_planetary_globe(
            grp.mesh,
            r_mid=0.5 * (r_out + r_in),
            thickness=r_out - r_in,
            cz=cz,
            azimuth_deg=az_deg,
            with_moon=has_moon,
        )
        groups[name] = grp

    # 13. Mu: Sol (Medium sive Centrum Universi immobile)
    sol_grp = create_scene_group(scene, "13_Mu_Sol_Center")
    sol_z = CENTER_Z + explode * 1.18
    add_uv_sphere(sol_grp.mesh, 0.0, 0.0, sol_z, radii.sol_r, "sol_core", lon_segs=28, lat_segs=16)
    groups["13_Mu_Sol_Center"] = sol_grp

    return groups
