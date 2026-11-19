"""Modular 3D CAD component library for Kepler's Tabula III (folio 0034)."""

from __future__ import annotations

from typing import Any

from .pedestal_cradle import build_pedestal_cradle
from .planetary_bowls import build_planetary_bowls
from .platonic_scaffolds import build_platonic_scaffolds
from .primitives import (
    CENTER_Z,
    DODEC_ICOSA_RATIO,
    MATERIALS,
    PHI,
    R_SATURN_OUT,
    ShimScene,
    TabulaIIIRadii,
    compute_radii,
)


def build_tabula_iii_scene(
    scene: Any,
    scale_mode: str = "exact",
    explode: float = 0.0,
    include_pedestal: bool = True,
) -> TabulaIIIRadii:
    """Assemble all 13 architectural CAD groups of Tabula III (folio 0034) into ``scene``."""
    radii = compute_radii(scale_mode=scale_mode)

    # Preserve IngeTrazo's Engineer guide billboard if present
    engineer_group = None
    for g in list(getattr(scene, "groups", [])):
        if getattr(g, "is_guide", False) or getattr(g, "name", "") == "Engineer":
            engineer_group = g
            break

    if hasattr(scene, "clear"):
        scene.clear()

    if include_pedestal:
        build_pedestal_cradle(scene, z_offset=-0.12 * explode)
    build_planetary_bowls(scene, radii, explode=explode)
    build_platonic_scaffolds(scene, radii, explode=explode)

    # Sort groups into canonical alpha..mu numeric order (01..13)
    scene.groups.sort(key=lambda g: g.name)

    if engineer_group is not None:
        scene.groups.append(engineer_group)

    if hasattr(scene, "version"):
        scene.version += 1

    return radii


__all__ = [
    "CENTER_Z",
    "DODEC_ICOSA_RATIO",
    "MATERIALS",
    "PHI",
    "R_SATURN_OUT",
    "ShimScene",
    "TabulaIIIRadii",
    "build_pedestal_cradle",
    "build_planetary_bowls",
    "build_platonic_scaffolds",
    "build_tabula_iii_scene",
    "compute_radii",
]
