#!/usr/bin/env python3
"""Pure-symbolic demonstration of Kepler's *Mysterium Cosmographicum* (1596/1621)."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for _p in (_ROOT / "src", _ROOT.parent / "model" / "src"):
    if _p.exists() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import sympy as sp  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.kepler.mysterium_spheres import (  # noqa: E402
    compute_nested_planetary_radii,
    construct_mysterium_planar_nesting,
    derive_platonic_sphere_ratios,
    verify_polar_duality_ratios,
)


def main() -> int:
    console = Console()
    console.print("[bold gold1]Mysterium Cosmographicum (1596 / 1621)[/bold gold1] — Exact Symbolic Verification\n")

    t_solids = Table(title="Five Regular Solids — Exact Insphere / Circumsphere Ratios")
    t_solids.add_column("Solid", style="cyan")
    t_solids.add_column("Rank")
    t_solids.add_column("Planetary Pair")
    t_solids.add_column("Q_in / Q_out", style="green")
    t_solids.add_column("r_in / R_out", style="yellow")

    for s in derive_platonic_sphere_ratios():
        t_solids.add_row(
            f"{s.name} ({s.latin_name})",
            s.rank_class,
            f"{s.planet_outer} -> {s.planet_inner}",
            str(s.q_in_over_q_out),
            str(sp.simplify(s.r_in_over_r_out)),
        )
    console.print(t_solids)

    duality = verify_polar_duality_ratios()
    for check_name, ok in duality.items():
        assert ok, f"Failed check: {check_name}"
    console.print(f"\nPolar-duality invariants proved: {duality}\n")

    t_orbs = Table(title="Heliocentric Nested Orbs (Earth = 1, Circulus mensor omnium)")
    t_orbs.add_column("Planet", style="cyan")
    t_orbs.add_column("Polyhedral Gap")
    t_orbs.add_column("Exact Symbolic Radius", style="green")
    t_orbs.add_column("Polyhedral (evalf 4d)", justify="right")
    t_orbs.add_column("Copernican Mean AU", justify="right")

    for orb in compute_nested_planetary_radii():
        t_orbs.add_row(
            orb.planet,
            orb.intervening_solid or "Circulus mensor omnium",
            str(orb.symbolic_radius),
            f"{float(orb.symbolic_radius.evalf()):.4f}",
            f"{float(orb.copernican_mean_au):.4f}",
        )
    console.print(t_orbs)

    model = construct_mysterium_planar_nesting()
    pts = model.points
    assert all(not p.x.has(sp.Float) and not p.y.has(sp.Float) for p in pts)
    console.print(
        f"\nGraz 1595 planar construction verified: {len(pts)} exact symbolic points, "
        "zero floating-point coordinates."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
