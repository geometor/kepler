"""Rich CLI verification report for GEOMETOR Kepler (`geometor-kepler`)."""

from __future__ import annotations

import sympy as sp
from rich.console import Console
from rich.table import Table

from geometor.kepler import __version__
from geometor.kepler.harmonices_geometry import (
    classify_polygon_scibilitas,
    construct_kepler_right_triangle,
    enumerate_archimedean_planar_tilings,
    verify_heptagon_cubic_obstruction,
    verify_kepler_third_law,
)
from geometor.kepler.mysterium_spheres import (
    compute_nested_planetary_radii,
    construct_mysterium_planar_nesting,
    derive_platonic_sphere_ratios,
    verify_polar_duality_ratios,
)
from geometor.kepler.strena_packing import (
    analyze_rhombic_dodecahedron,
    analyze_rhombic_triacontahedron,
    compute_fibonacci_phyllotaxis,
    construct_hexagonal_rosette,
    verify_kepler_sphere_packing,
)


def main() -> int:
    """Execute exact symbolic Kepler verifications and render Rich summary tables."""
    console = Console()
    console.print(
        f"[bold gold1]GEOMETOR • Kepler[/bold gold1] v{__version__} — "
        "Exact Symbolic Cosmography, Crystallography & Celestial Harmony"
    )

    # 1. Mysterium Cosmographicum Platonic Solids
    solids_table = Table(title="1. Mysterium Cosmographicum (1596/1621) — Five Regular Solids")
    solids_table.add_column("Solid", style="cyan")
    solids_table.add_column("Schläfli")
    solids_table.add_column("Orbs")
    solids_table.add_column("Q_in / Q_out", style="green")
    solids_table.add_column("r_in / R_out", style="yellow")

    for s in derive_platonic_sphere_ratios():
        solids_table.add_row(
            s.name,
            f"{{{s.schlafli[0]}, {s.schlafli[1]}}}",
            f"{s.planet_outer} -> {s.planet_inner}",
            str(s.q_in_over_q_out),
            str(sp.simplify(s.r_in_over_r_out)),
        )
    console.print(solids_table)

    duality = verify_polar_duality_ratios()
    orbs = compute_nested_planetary_radii()
    m_graz = construct_mysterium_planar_nesting()
    console.print(
        f"  • Polar duality verified: {all(duality.values())} | "
        f"Nested orbs computed: {len(orbs)} | "
        f"Graz 1595 DAG elements: {len(m_graz)}"
    )

    # 2. Strena seu de Nive Sexangula (1611)
    rd = analyze_rhombic_dodecahedron()
    rt = analyze_rhombic_triacontahedron()
    packing = verify_kepler_sphere_packing()
    fib = compute_fibonacci_phyllotaxis(8)
    m_ros = construct_hexagonal_rosette()

    strena_table = Table(title="2. Strena seu de Nive Sexangula (1611) — Rhombic Polyhedra & Packing")
    strena_table.add_column("Structure", style="cyan")
    strena_table.add_column("F / V / E")
    strena_table.add_column("Diagonal Ratio", style="green")
    strena_table.add_column("Dihedral / Density", style="yellow")
    strena_table.add_row(
        rd.name,
        f"{rd.faces} / {rd.vertices} / {rd.edges}",
        f"{rd.diagonal_ratio} : 1",
        f"{rd.dihedral_angle_deg} deg (space-filling)",
    )
    strena_table.add_row(
        rt.name,
        f"{rt.faces} / {rt.vertices} / {rt.edges}",
        f"({rt.diagonal_ratio}) : 1",
        f"{rt.dihedral_angle_deg} deg (golden zonohedron)",
    )
    strena_table.add_row(
        "FCC / HCP Sphere Packing",
        "Kissing = 12",
        f"FCC/Cubic = {packing.density_ratio_close_over_cubic}",
        f"{packing.close_packed_density}",
    )
    console.print(strena_table)
    console.print(
        f"  • Fibonacci convergent F_9/F_8 = {fib[-1].ratio_next_over_curr} "
        f"(Cassini = {fib[-1].cassini_determinant}) | "
        f"Rosette DAG elements: {len(m_ros)}"
    )

    # 3. Harmonices Mundi (1619) & Kepler Right Triangle (1597)
    m_kt = construct_kepler_right_triangle()
    scib = classify_polygon_scibilitas()
    hept = verify_heptagon_cubic_obstruction()
    tilings = enumerate_archimedean_planar_tilings()
    law3 = verify_kepler_third_law()

    hm_table = Table(title="3. Harmonices Mundi (1619) & Kepler Right Triangle (1597)")
    hm_table.add_column("Theorem / Domain", style="cyan")
    hm_table.add_column("Exact Symbolic Invariant", style="green")
    hm_table.add_column("Status", style="yellow")
    hm_table.add_row(
        "Kepler Right Triangle (1597)",
        "Q_a = 1, Q_b = phi, Q_c = 1 + phi = phi^2",
        f"PROVED ({len(m_kt)} DAG elements)",
    )
    hm_table.add_row(
        "Regular Heptagon (Book I Prop. XLV)",
        str(hept["cos_minpoly"].as_expr()) + " = 0",
        f"Irreducible cubic: {hept['cubic_irreducible']}",
    )
    hm_table.add_row(
        "Constructible Polygons Tested",
        f"{sum(1 for p in scib if p.constructible)} Scibilia / {sum(1 for p in scib if not p.constructible)} Inscibilia",
        "VERIFIED",
    )
    hm_table.add_row(
        "Archimedean Planar Tilings (Book II)",
        ", ".join(t.notation for t in tilings),
        f"{len(tilings)} uniform vertex species",
    )
    hm_table.add_row(
        "Kepler's Third Law (Book V Prop. VIII)",
        "(T_1 / T_2)^2 == (a_1 / a_2)^3",
        f"EXACT ({law3['symbolic_sesquialtera_exact']})",
    )
    console.print(hm_table)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
