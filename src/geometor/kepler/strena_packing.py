"""Exact symbolic geometry of Kepler's *Strena seu de Nive Sexangula* (1611).

Provides 100% exact SymPy 3D analyses of Kepler's two isohedral rhombic
polyhedra—the space-filling **Rhombic Dodecahedron** (diagonal ratio ``sqrt(2):1``,
dihedral ``120 deg``) and the golden **Rhombic Triacontahedron** (diagonal ratio
``phi:1``, dihedral ``144 deg``)—verifies the cubic/hexagonal sphere close-packing
density ``pi / (3*sqrt(2))`` against simple cubic ``pi / 6``, constructs the
7-circle hexagonal close-packing rosette in ``geometor.model``, and computes
exact rational Fibonacci phyllotaxis convergents to ``phi``.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
from geometor.model import (
    Model,
    ProofAssertionError,
    canonicalize_golden,
    proposition,
    quadrance,
    zero_test,
)

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)


@dataclass(frozen=True)
class RhombicPolyhedronMetrics:
    """Exact 3D metrics of an isohedral Keplerian rhombic zonohedron."""

    name: str
    latin_name: str
    faces: int
    vertices: int
    edges: int
    edge_quadrance: sp.Expr
    long_diag_quadrance: sp.Expr
    short_diag_quadrance: sp.Expr
    diagonal_ratio: sp.Expr
    diagonal_quadrance_ratio: sp.Expr
    dihedral_angle_deg: sp.Rational
    dihedral_cosine: sp.Expr
    space_filling: bool


@dataclass(frozen=True)
class SpherePackingComparison:
    """Exact symbolic sphere-packing fractions in Kepler's *Strena* (1611)."""

    simple_cubic_kissing: int
    simple_cubic_density: sp.Expr
    close_packed_kissing: int
    close_packed_layer_height_over_diameter: sp.Expr
    close_packed_density: sp.Expr
    density_ratio_close_over_cubic: sp.Expr


@dataclass(frozen=True)
class FibonacciConvergent:
    """Exact rational Fibonacci phyllotaxis convergent and Cassini invariant."""

    index: int
    f_prev: int
    f_curr: int
    f_next: int
    ratio_next_over_curr: sp.Rational
    cassini_determinant: int
    error_from_phi: sp.Expr


def _q3(
    p: tuple[sp.Expr, sp.Expr, sp.Expr],
    q: tuple[sp.Expr, sp.Expr, sp.Expr],
) -> sp.Expr:
    return canonicalize_golden(
        sp.expand((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)
    )


def analyze_rhombic_dodecahedron() -> RhombicPolyhedronMetrics:
    """Analyze the 14-vertex Rhombic Dodecahedron from exact integer 3D coordinates."""
    cubic_vertices = [
        (sp.Integer(sx), sp.Integer(sy), sp.Integer(sz))
        for sx in (-1, 1)
        for sy in (-1, 1)
        for sz in (-1, 1)
    ]
    octahedral_vertices = [
        (sp.Integer(2), sp.Integer(0), sp.Integer(0)),
        (sp.Integer(-2), sp.Integer(0), sp.Integer(0)),
        (sp.Integer(0), sp.Integer(2), sp.Integer(0)),
        (sp.Integer(0), sp.Integer(-2), sp.Integer(0)),
        (sp.Integer(0), sp.Integer(0), sp.Integer(2)),
        (sp.Integer(0), sp.Integer(0), sp.Integer(-2)),
    ]
    all_vertices = cubic_vertices + octahedral_vertices
    assert len(all_vertices) == 14

    u1 = (sp.Integer(2), sp.Integer(0), sp.Integer(0))
    u2 = (sp.Integer(0), sp.Integer(2), sp.Integer(0))
    v1 = (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    v2 = (sp.Integer(1), sp.Integer(1), sp.Integer(-1))

    q_edge = _q3(u1, v1)
    q_long = _q3(u1, u2)
    q_short = _q3(v1, v2)
    diag_q_ratio = sp.simplify(q_long / q_short)
    diag_ratio = sp.sqrt(diag_q_ratio)
    cos_dihedral = sp.Rational(-1, 2)

    return RhombicPolyhedronMetrics(
        name="Rhombic Dodecahedron",
        latin_name="Dodecaedron Rhombicum",
        faces=12,
        vertices=len(all_vertices),
        edges=24,
        edge_quadrance=q_edge,
        long_diag_quadrance=q_long,
        short_diag_quadrance=q_short,
        diagonal_ratio=diag_ratio,
        diagonal_quadrance_ratio=diag_q_ratio,
        dihedral_angle_deg=sp.Rational(120, 1),
        dihedral_cosine=cos_dihedral,
        space_filling=True,
    )


def analyze_rhombic_triacontahedron() -> RhombicPolyhedronMetrics:
    """Analyze the 32-vertex Golden Rhombic Triacontahedron over ``Q(phi)``."""
    zero = sp.Integer(0)
    one = sp.Integer(1)
    phi2 = canonicalize_golden(PHI**2)

    icosa_vertices: list[tuple[sp.Expr, sp.Expr, sp.Expr]] = []
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            icosa_vertices.append((zero, s1 * PHI, s2 * phi2))
            icosa_vertices.append((s1 * PHI, s2 * phi2, zero))
            icosa_vertices.append((s2 * phi2, zero, s1 * PHI))

    dodeca_vertices: list[tuple[sp.Expr, sp.Expr, sp.Expr]] = [
        (sx * PHI, sy * PHI, sz * PHI)
        for sx in (-1, 1)
        for sy in (-1, 1)
        for sz in (-1, 1)
    ]
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            dodeca_vertices.append((s1 * one, zero, s2 * phi2))
            dodeca_vertices.append((zero, s2 * phi2, s1 * one))
            dodeca_vertices.append((s2 * phi2, s1 * one, zero))

    all_vertices = icosa_vertices + dodeca_vertices
    assert len(all_vertices) == 32

    u1 = (zero, PHI, phi2)
    u2 = (zero, -PHI, phi2)
    v1 = (one, zero, phi2)
    v2 = (-one, zero, phi2)

    q_edge = _q3(u1, v1)
    q_long = _q3(u1, u2)
    q_short = _q3(v1, v2)
    diag_q_ratio = canonicalize_golden(sp.simplify(q_long / q_short))
    diag_ratio = canonicalize_golden(sp.sqrt(diag_q_ratio))
    cos_dihedral = canonicalize_golden(-PHI / sp.Integer(2))

    return RhombicPolyhedronMetrics(
        name="Rhombic Triacontahedron",
        latin_name="Triacontaedron Rhombicum",
        faces=30,
        vertices=len(all_vertices),
        edges=60,
        edge_quadrance=q_edge,
        long_diag_quadrance=q_long,
        short_diag_quadrance=q_short,
        diagonal_ratio=diag_ratio,
        diagonal_quadrance_ratio=diag_q_ratio,
        dihedral_angle_deg=sp.Rational(144, 1),
        dihedral_cosine=cos_dihedral,
        space_filling=False,
    )


def verify_kepler_sphere_packing() -> SpherePackingComparison:
    """Derive exact simple-cubic vs. FCC/HCP close-packing densities (*Strena* §§10–14)."""
    r_fcc = sp.sqrt(2)
    v_sphere_fcc = sp.Rational(4, 3) * sp.pi * r_fcc**3
    v_voronoi_rhombic = sp.Integer(16)
    fcc_density = sp.simplify(v_sphere_fcc / v_voronoi_rhombic)

    cubic_density = sp.pi / sp.Integer(6)
    ratio = sp.simplify(fcc_density / cubic_density)
    assert zero_test(fcc_density - sp.pi / (sp.Integer(3) * sp.sqrt(2)))
    assert zero_test(ratio - sp.sqrt(2))

    layer_h_over_d = sp.sqrt(sp.Rational(2, 3))

    return SpherePackingComparison(
        simple_cubic_kissing=6,
        simple_cubic_density=cubic_density,
        close_packed_kissing=12,
        close_packed_layer_height_over_diameter=layer_h_over_d,
        close_packed_density=fcc_density,
        density_ratio_close_over_cubic=ratio,
    )


def compute_fibonacci_phyllotaxis(n_terms: int = 10) -> tuple[FibonacciConvergent, ...]:
    """Compute Kepler's self-propagating Fibonacci sequence ``1, 1, 2, 3, 5, 8, 13, 21...``."""
    if n_terms < 1:
        raise ValueError("n_terms must be >= 1")

    seq = [0, 1]
    while len(seq) < n_terms + 2:
        seq.append(seq[-1] + seq[-2])

    results: list[FibonacciConvergent] = []
    for idx in range(1, n_terms + 1):
        f_prev = seq[idx - 1]
        f_curr = seq[idx]
        f_next = seq[idx + 1]
        ratio = sp.Rational(f_next, f_curr)
        cassini = f_next * f_prev - f_curr * f_curr
        expected_sign = -1 if (idx % 2 == 1) else 1
        assert cassini == expected_sign
        results.append(
            FibonacciConvergent(
                index=idx,
                f_prev=f_prev,
                f_curr=f_curr,
                f_next=f_next,
                ratio_next_over_curr=ratio,
                cassini_determinant=cassini,
                error_from_phi=canonicalize_golden(ratio - PHI),
            )
        )
    return tuple(results)


@proposition(
    "Strena.HexagonalRosette",
    kind="theorem",
    title="Six Congruent Unit Circles Surround a Central Unit Circle in Mutual Tangency",
    hide_guides=True,
)
def construct_hexagonal_rosette(model: Model | None = None) -> Model:
    """Construct Kepler's planar 7-circle hexagonal close-packing / snowflake rosette.

    Starting purely from ``O = (0, 0)`` and ``P_0 = (2, 0)`` (center spacing ``2R = 2``
    for unit circles ``R = 1``), constructs the 6 surrounding centers around a regular
    hexagon and all 7 mutually tangent unit circles with zero floating-point values.
    """
    if model is None:
        model = Model(
            "strena_hexagonal_7_circle_rosette",
            auto_intersect=False,
            enable_logging=False,
        )

    pt_o = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="O")
    pt_p0 = model.set_point(sp.Integer(2), sp.Integer(0), classes=["given"], ID="P_0")

    axis_x = model.construct_line(pt_o, pt_p0, ID="axis_X", by="Post.1")
    c_ring = model.construct_circle(pt_o, pt_p0, classes=["lattice"], ID="c_ring", by="Post.3")

    pt_p3 = model.intersect(axis_x, c_ring, other_than=pt_p0, ID="P_3", by="Post.2")

    with model.subconstruction("hexagon_stepping"):
        c_step0 = model.construct_circle(pt_p0, pt_o, guide=True, by="Post.3")
        c_step3 = model.construct_circle(pt_p3, pt_o, guide=True, by="Post.3")
        pt_p1 = model.intersect(c_ring, c_step0, side_of=(pt_o, pt_p0, 1), ID="P_1", by="IV.15")
        pt_p5 = model.intersect(c_ring, c_step0, side_of=(pt_o, pt_p0, -1), ID="P_5", by="IV.15")
        pt_p2 = model.intersect(c_ring, c_step3, side_of=(pt_o, pt_p0, 1), ID="P_2", by="IV.15")
        pt_p4 = model.intersect(c_ring, c_step3, side_of=(pt_o, pt_p0, -1), ID="P_4", by="IV.15")
        chord_15 = model.construct_line(pt_p1, pt_p5, guide=True, by="Post.1")

    pt_t0 = model.intersect(axis_x, chord_15, ID="T_0", by="I.10")
    c_center = model.construct_circle(pt_o, pt_t0, classes=["sphere"], ID="S_center", by="Post.3")

    ring_centers = [pt_p0, pt_p1, pt_p2, pt_p3, pt_p4, pt_p5]
    outer_spheres = []
    radial_pairs = []
    perimeter_pairs = []

    for idx, ctr in enumerate(ring_centers):
        nxt = ring_centers[(idx + 1) % 6]
        model.construct_segment(ctr, nxt, classes=["hexagon"], ID=f"hex_{idx}", by="Post.1")
        rad_line = model.construct_line(pt_o, ctr, guide=True, ID=f"rad_{idx}", by="Post.1")
        pt_tang = model.intersect(
            rad_line,
            c_center,
            between=(pt_o, ctr),
            ID=f"t_{idx}",
            by="III.11",
        )
        sph = model.construct_circle(ctr, pt_tang, classes=["sphere"], ID=f"S_{idx}", by="Post.3")
        outer_spheres.append(sph)
        radial_pairs.append((pt_o, ctr))
        perimeter_pairs.append((ctr, nxt))

    # Demonstrate: all 6 radial center-quadrances and all 6 perimeter center-quadrances equal 4
    model.assert_equal(
        *radial_pairs,
        *perimeter_pairs,
        by="IV.15",
        label="All 12 radial and hexagonal center-to-center quadrances equal 4R^2 = 4",
    )
    if not zero_test(quadrance(pt_o, pt_p0) - sp.Integer(4)):
        raise ProofAssertionError("Center-to-center quadrance != 4")

    model.conclude(
        c_center,
        *outer_spheres,
        kind="qed",
        label="Six congruent unit circles kiss central unit circle S_center simultaneously.",
    )
    return model
