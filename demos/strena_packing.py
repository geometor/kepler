#!/usr/bin/env python3
"""Pure-symbolic demonstration of Kepler's *Strena seu de Nive Sexangula* (1611)."""

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

from geometor.kepler.strena_packing import (  # noqa: E402
    analyze_rhombic_dodecahedron,
    analyze_rhombic_triacontahedron,
    compute_fibonacci_phyllotaxis,
    construct_hexagonal_rosette,
    verify_kepler_sphere_packing,
)


def main() -> int:
    console = Console()
    console.print("[bold gold1]Strena seu de Nive Sexangula (1611)[/bold gold1] — Exact Symbolic Verification\n")

    rd = analyze_rhombic_dodecahedron()
    rt = analyze_rhombic_triacontahedron()
    t_poly = Table(title="Kepler's Two Isohedral Rhombic Polyhedra")
    t_poly.add_column("Polyhedron", style="cyan")
    t_poly.add_column("F / V / E")
    t_poly.add_column("Edge Q")
    t_poly.add_column("Diagonal Ratio", style="green")
    t_poly.add_column("Dihedral Angle", style="yellow")
    t_poly.add_column("Space-Filling")
    for m in (rd, rt):
        t_poly.add_row(
            f"{m.name} ({m.latin_name})",
            f"{m.faces} / {m.vertices} / {m.edges}",
            str(m.edge_quadrance),
            f"({m.diagonal_ratio}) : 1",
            f"{m.dihedral_angle_deg} deg (cos = {m.dihedral_cosine})",
            str(m.space_filling),
        )
    console.print(t_poly)

    pack = verify_kepler_sphere_packing()
    console.print(
        f"\nSphere Close-Packing (Kepler Conjecture):\n"
        f"  • Simple Cubic (kissing {pack.simple_cubic_kissing}): {pack.simple_cubic_density}\n"
        f"  • FCC / HCP Close-Packed (kissing {pack.close_packed_kissing}): {pack.close_packed_density}\n"
        f"  • Exact Density Ratio (Close / Cubic): {pack.density_ratio_close_over_cubic}\n"
    )

    t_fib = Table(title="Botanical Pentamery & Fibonacci Convergence to phi")
    t_fib.add_column("n", justify="right")
    t_fib.add_column("F_{n+1} / F_n", style="green")
    t_fib.add_column("Cassini F_{n+1}F_{n-1} - F_n^2", justify="right", style="yellow")
    for row in compute_fibonacci_phyllotaxis(9):
        t_fib.add_row(str(row.index), str(row.ratio_next_over_curr), str(row.cassini_determinant))
    console.print(t_fib)

    rosette = construct_hexagonal_rosette()
    pts = rosette.points
    assert all(not p.x.has(sp.Float) and not p.y.has(sp.Float) for p in pts)
    console.print(
        f"\n7-Circle Hexagonal Rosette verified: {len(pts)} exact symbolic points, "
        "zero floating-point coordinates."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
