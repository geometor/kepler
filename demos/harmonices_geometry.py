#!/usr/bin/env python3
"""Pure-symbolic demonstration of *Harmonices Mundi* (1619) & 1597 Kepler Triangle."""

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

from geometor.kepler.harmonices_geometry import (  # noqa: E402
    analyze_planetary_harmonies,
    classify_polygon_scibilitas,
    construct_kepler_right_triangle,
    enumerate_archimedean_planar_tilings,
    verify_heptagon_cubic_obstruction,
    verify_kepler_third_law,
    verify_maestlin_1597_decimal,
)


def main() -> int:
    console = Console()
    console.print("[bold gold1]Harmonices Mundi (1619) & Kepler Triangle (1597)[/bold gold1]\n")

    kt_model = construct_kepler_right_triangle()
    pts = kt_model.points
    assert all(not p.x.has(sp.Float) and not p.y.has(sp.Float) for p in pts)
    maestlin = verify_maestlin_1597_decimal()
    console.print(
        f"Kepler Right Triangle proved ({len(pts)} exact symbolic points over Q(sqrt(phi))).\n"
        f"Mästlin 1597 decimal 0.6180340 accurate to 7 places: {maestlin['accurate_to_7_places']}\n"
    )

    t_scib = Table(title="Book I — Scibilitas vs. Inscibilitas of Regular Polygons")
    t_scib.add_column("n", justify="right")
    t_scib.add_column("Polygon", style="cyan")
    t_scib.add_column("MinPoly of 2*cos(2*pi/n)", style="green")
    t_scib.add_column("Deg", justify="right")
    t_scib.add_column("Scibilis?", style="yellow")
    for p in classify_polygon_scibilitas():
        t_scib.add_row(
            str(p.n_sides),
            p.name,
            str(p.minimal_poly_2cos.as_expr()),
            str(p.algebraic_degree),
            "YES" if p.constructible else "NO (Inscibilis)",
        )
    console.print(t_scib)

    hept = verify_heptagon_cubic_obstruction()
    console.print(
        f"\nHeptagon Prop. XLV cubic irreducible: {hept['cubic_irreducible']} | "
        f"Bürgi sextic: {hept['buergi_chord_minpoly'].as_expr()} = 0\n"
    )

    tilings = enumerate_archimedean_planar_tilings()
    console.print(
        f"Book II — Derived all {len(tilings)} uniform Archimedean planar tilings:\n  "
        + ", ".join(t.notation for t in tilings)
        + "\n"
    )

    t_harm = Table(title="Book V — Planetary Extremal Harmonies & Lex Tertia")
    t_harm.add_column("Planet", style="cyan")
    t_harm.add_column("Aphelion / Perihelion (\"/day)", justify="right")
    t_harm.add_column("Ratio", style="green")
    t_harm.add_column("Musical Consonance", style="yellow")
    for h in analyze_planetary_harmonies():
        t_harm.add_row(
            h.planet,
            f"{h.aphelion_arcsec_per_day} / {h.perihelion_arcsec_per_day}",
            str(h.harmonic_ratio_aph_over_per),
            h.musical_interval,
        )
    console.print(t_harm)

    law3 = verify_kepler_third_law()
    console.print(f"\nKepler's Third Law verified: {law3}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
