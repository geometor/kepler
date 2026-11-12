"""Exact symbolic geometry of Kepler's *Mysterium Cosmographicum* (1596 / 1621).

Derives the insphere-to-circumsphere radius and quadrance ratios of the five
regular Platonic solids directly from exact 3D vertex coordinates over
``Q(phi)``, proves polar-duality ratio equality (Cube = Octahedron,
Dodecahedron = Icosahedron), computes the heliocentric nested planetary sphere
radii from Saturn to Mercury with Earth as *Circulus mensor omnium*, and
constructs Kepler's July 19, 1595 Graz Great-Conjunction planar nesting in
``geometor.model`` with zero floating-point approximations.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
from geometor.model import (
    Model,
    ProofAssertionError,
    canonicalize_golden,
    line_spread,
    proposition,
    quadrance,
    zero_test,
)

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)


@dataclass(frozen=True)
class SolidSphereRatio:
    """Exact insphere/circumsphere metrics for a nested regular polyhedron."""

    name: str
    latin_name: str
    schlafli: tuple[int, int]
    faces: int
    vertices: int
    edges: int
    rank_class: str
    planet_outer: str
    planet_inner: str
    q_in_over_q_out: sp.Expr
    r_in_over_r_out: sp.Expr


@dataclass(frozen=True)
class NestedPlanetOrb:
    """Exact symbolic heliocentric radius in Kepler's five-solid nesting."""

    planet: str
    intervening_solid: str | None
    symbolic_radius: sp.Expr
    symbolic_quadrance: sp.Expr
    copernican_mean_au: sp.Rational


def _centroid(points: list[tuple[sp.Expr, sp.Expr, sp.Expr]]) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    n = sp.Integer(len(points))
    return (
        sp.simplify(sum(p[0] for p in points) / n),
        sp.simplify(sum(p[1] for p in points) / n),
        sp.simplify(sum(p[2] for p in points) / n),
    )


def _norm_sq_3d(vec: tuple[sp.Expr, sp.Expr, sp.Expr]) -> sp.Expr:
    return canonicalize_golden(sp.expand(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2))


def derive_platonic_sphere_ratios() -> tuple[SolidSphereRatio, ...]:
    """Derive exact insphere/circumsphere ratios of all 5 regular solids from 3D vertices.

    Ordered from outermost (Saturn -> Jupiter) to innermost (Venus -> Mercury)
    following *Mysterium Cosmographicum* Cap. II & Cap. XIV.
    """
    one = sp.Integer(1)
    zero = sp.Integer(0)
    inv_phi = PHI - one

    cube_v = (one, one, one)
    cube_face = [(one, one, one), (one, -one, one), (one, -one, -one), (one, one, -one)]
    q_cube = sp.simplify(_norm_sq_3d(_centroid(cube_face)) / _norm_sq_3d(cube_v))

    tetra_v = (one, one, one)
    tetra_face = [(one, one, one), (one, -one, -one), (-one, one, -one)]
    q_tetra = sp.simplify(_norm_sq_3d(_centroid(tetra_face)) / _norm_sq_3d(tetra_v))

    dod_v = (zero, inv_phi, PHI)
    dod_face = [
        (zero, inv_phi, PHI),
        (zero, -inv_phi, PHI),
        (one, -one, one),
        (PHI, zero, inv_phi),
        (one, one, one),
    ]
    q_dod = canonicalize_golden(
        sp.simplify(_norm_sq_3d(_centroid(dod_face)) / _norm_sq_3d(dod_v))
    )

    ico_v = (zero, one, PHI)
    ico_face = [(zero, one, PHI), (zero, -one, PHI), (PHI, zero, one)]
    q_ico = canonicalize_golden(
        sp.simplify(_norm_sq_3d(_centroid(ico_face)) / _norm_sq_3d(ico_v))
    )

    oct_v = (one, zero, zero)
    oct_face = [(one, zero, zero), (zero, one, zero), (zero, zero, one)]
    q_oct = sp.simplify(_norm_sq_3d(_centroid(oct_face)) / _norm_sq_3d(oct_v))

    return (
        SolidSphereRatio(
            name="Cube",
            latin_name="Cubus",
            schlafli=(4, 3),
            faces=6,
            vertices=8,
            edges=12,
            rank_class="primary (outer)",
            planet_outer="Saturn",
            planet_inner="Jupiter",
            q_in_over_q_out=q_cube,
            r_in_over_r_out=sp.sqrt(q_cube),
        ),
        SolidSphereRatio(
            name="Tetrahedron",
            latin_name="Tetraedron (Pyramis)",
            schlafli=(3, 3),
            faces=4,
            vertices=4,
            edges=6,
            rank_class="primary (outer)",
            planet_outer="Jupiter",
            planet_inner="Mars",
            q_in_over_q_out=q_tetra,
            r_in_over_r_out=sp.sqrt(q_tetra),
        ),
        SolidSphereRatio(
            name="Dodecahedron",
            latin_name="Dodecaedron",
            schlafli=(5, 3),
            faces=12,
            vertices=20,
            edges=30,
            rank_class="primary (outer)",
            planet_outer="Mars",
            planet_inner="Earth",
            q_in_over_q_out=q_dod,
            r_in_over_r_out=sp.sqrt(q_dod),
        ),
        SolidSphereRatio(
            name="Icosahedron",
            latin_name="Icosaedron",
            schlafli=(3, 5),
            faces=20,
            vertices=12,
            edges=30,
            rank_class="secondary (inner)",
            planet_outer="Earth",
            planet_inner="Venus",
            q_in_over_q_out=q_ico,
            r_in_over_r_out=sp.sqrt(q_ico),
        ),
        SolidSphereRatio(
            name="Octahedron",
            latin_name="Octaedron",
            schlafli=(3, 4),
            faces=8,
            vertices=6,
            edges=12,
            rank_class="secondary (inner)",
            planet_outer="Venus",
            planet_inner="Mercury",
            q_in_over_q_out=q_oct,
            r_in_over_r_out=sp.sqrt(q_oct),
        ),
    )


def verify_polar_duality_ratios() -> dict[str, bool]:
    """Prove exact polar-duality insphere/circumsphere identities (*Mysterium* Cap. XIII)."""
    ratios = {s.name: s for s in derive_platonic_sphere_ratios()}
    golden_target = (sp.Integer(5) + sp.Integer(2) * sp.sqrt(5)) / sp.Integer(15)

    return {
        "cube_quadrance_is_1_over_3": zero_test(
            ratios["Cube"].q_in_over_q_out - sp.Rational(1, 3)
        ),
        "tetrahedron_quadrance_is_1_over_9": zero_test(
            ratios["Tetrahedron"].q_in_over_q_out - sp.Rational(1, 9)
        ),
        "cube_equals_octahedron": zero_test(
            ratios["Cube"].q_in_over_q_out - ratios["Octahedron"].q_in_over_q_out
        ),
        "dodecahedron_equals_icosahedron": zero_test(
            ratios["Dodecahedron"].q_in_over_q_out - ratios["Icosahedron"].q_in_over_q_out
        ),
        "dodecahedron_matches_golden_closed_form": zero_test(
            ratios["Dodecahedron"].q_in_over_q_out - golden_target
        ),
        "euler_characteristic_all_two": all(
            (s.vertices - s.edges + s.faces) == 2 for s in ratios.values()
        ),
    }


def compute_nested_planetary_radii(
    earth_radius: sp.Expr | int = 1,
) -> tuple[NestedPlanetOrb, ...]:
    """Compute exact symbolic radii from Saturn to Mercury (*Mysterium* Cap. XIV).

    Takes the Telluric orb (*Terra est Circulus mensor omnium*) as ``earth_radius``
    and propagates outward via circumscribed Dodecahedron, Tetrahedron, and Cube,
    and inward via inscribed Icosahedron and Octahedron.
    """
    by_name = {s.name: s for s in derive_platonic_sphere_ratios()}
    r_earth = sp.sympify(earth_radius)
    r_mars = sp.simplify(r_earth / by_name["Dodecahedron"].r_in_over_r_out)
    r_jupiter = sp.simplify(r_mars / by_name["Tetrahedron"].r_in_over_r_out)
    r_saturn = sp.simplify(r_jupiter / by_name["Cube"].r_in_over_r_out)
    r_venus = sp.simplify(r_earth * by_name["Icosahedron"].r_in_over_r_out)
    r_mercury = sp.simplify(r_venus * by_name["Octahedron"].r_in_over_r_out)

    return (
        NestedPlanetOrb(
            planet="Saturn",
            intervening_solid="Cube (outside Jupiter)",
            symbolic_radius=r_saturn,
            symbolic_quadrance=canonicalize_golden(sp.simplify(r_saturn**2)),
            copernican_mean_au=sp.Rational(9174, 1000),
        ),
        NestedPlanetOrb(
            planet="Jupiter",
            intervening_solid="Tetrahedron (outside Mars)",
            symbolic_radius=r_jupiter,
            symbolic_quadrance=canonicalize_golden(sp.simplify(r_jupiter**2)),
            copernican_mean_au=sp.Rational(5219, 1000),
        ),
        NestedPlanetOrb(
            planet="Mars",
            intervening_solid="Dodecahedron (outside Earth)",
            symbolic_radius=r_mars,
            symbolic_quadrance=canonicalize_golden(sp.simplify(r_mars**2)),
            copernican_mean_au=sp.Rational(1520, 1000),
        ),
        NestedPlanetOrb(
            planet="Earth",
            intervening_solid=None,
            symbolic_radius=r_earth,
            symbolic_quadrance=canonicalize_golden(sp.simplify(r_earth**2)),
            copernican_mean_au=sp.Rational(1, 1),
        ),
        NestedPlanetOrb(
            planet="Venus",
            intervening_solid="Icosahedron (inside Earth)",
            symbolic_radius=r_venus,
            symbolic_quadrance=canonicalize_golden(sp.simplify(r_venus**2)),
            copernican_mean_au=sp.Rational(719, 1000),
        ),
        NestedPlanetOrb(
            planet="Mercury",
            intervening_solid="Octahedron (inside Venus)",
            symbolic_radius=r_mercury,
            symbolic_quadrance=canonicalize_golden(sp.simplify(r_mercury**2)),
            copernican_mean_au=sp.Rational(360, 1000),
        ),
    )


@proposition(
    "Mysterium.Praefatio.Graz1595",
    kind="theorem",
    title="Graz 1595 Equilateral Conjunction Triangle and Inscribed Square Nestings",
    hide_guides=True,
)
def construct_mysterium_planar_nesting(model: Model | None = None) -> Model:
    """Construct Kepler's July 19, 1595 Graz Great-Conjunction planar diagram.

    Starting purely from rational points ``O = (0, 0)`` and ``A = (0, 1)``,
    constructs the circumscribed circle ``c_out``, the inscribed equilateral
    triangle ``ABC`` with incircle ``c_in_tri`` (``Q_in / Q_out = 1/4``,
    ``r_in / R_out = 1/2``), and the inscribed square ``AESW`` with incircle
    ``c_in_sq`` (``Q_in / Q_out = 1/2``).
    """
    if model is None:
        model = Model(
            "mysterium_graz_1595_planar_nesting",
            auto_intersect=False,
            enable_logging=False,
        )

    # 1. Given: center O(0, 0) and north apex A(0, 1)
    pt_o = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="O")
    pt_a = model.set_point(sp.Integer(0), sp.Integer(1), classes=["given"], ID="A")

    # 2. Construct: outer planetary circle c_out and vertical axis OA
    c_out = model.construct_circle(pt_o, pt_a, classes=["given"], ID="c_out", by="Post.3")
    axis_ns = model.construct_line(pt_o, pt_a, ID="axis_NS", by="Post.1")
    pt_s = model.intersect(axis_ns, c_out, other_than=pt_a, ID="S", by="Post.2")

    # Auxiliary circle centered at S through O cuts c_out at B and C (Elements IV.2 / XIII.12)
    with model.subconstruction("equilateral_base"):
        c_aux_s = model.construct_circle(pt_s, pt_o, guide=True, by="Post.3")
        pt_b = model.intersect(c_out, c_aux_s, side_of=(pt_s, pt_a, -1), ID="B", by="IV.2")
        pt_c = model.intersect(c_out, c_aux_s, side_of=(pt_s, pt_a, 1), ID="C", by="IV.2")

    seg_ab = model.construct_segment(pt_a, pt_b, classes=["triangle"], ID="sAB", by="Post.1")
    seg_bc = model.construct_segment(pt_b, pt_c, classes=["triangle"], ID="sBC", by="Post.1")
    seg_ca = model.construct_segment(pt_c, pt_a, classes=["triangle"], ID="sCA", by="Post.1")
    line_bc = model.construct_line(pt_b, pt_c, guide=True, ID="lBC", by="Post.1")
    pt_m = model.intersect(line_bc, axis_ns, ID="M", by="I.12")
    c_in_tri = model.construct_circle(pt_o, pt_m, classes=["incircle"], ID="c_in_tri", by="Post.3")

    # Construct equatorial diameter EW perpendicular to NS via radical axis of poles A and S
    with model.subconstruction("perp_EW"):
        c_a_s = model.construct_circle(pt_a, pt_s, guide=True, by="Post.3")
        c_s_a = model.construct_circle(pt_s, pt_a, guide=True, by="Post.3")
        pole_e = model.intersect(c_a_s, c_s_a, side_of=(pt_s, pt_a, -1), guide=True, by="I.1")
        pole_w = model.intersect(c_a_s, c_s_a, side_of=(pt_s, pt_a, 1), guide=True, by="I.1")
    axis_ew = model.construct_line(pole_w, pole_e, ID="axis_EW", by="I.11")
    pt_e = model.intersect(axis_ew, c_out, side_of=(pt_s, pt_a, -1), ID="E", by="Post.2")
    pt_w = model.intersect(axis_ew, c_out, side_of=(pt_s, pt_a, 1), ID="W", by="Post.2")

    line_ae = model.construct_line(pt_a, pt_e, classes=["square"], ID="lAE", by="Post.1")
    with model.subconstruction("mid_AE"):
        c_ae_1 = model.construct_circle(pt_a, pt_e, guide=True, by="Post.3")
        c_ae_2 = model.construct_circle(pt_e, pt_a, guide=True, by="Post.3")
        p_ae_1 = model.intersect(c_ae_1, c_ae_2, side_of=(pt_a, pt_e, 1), guide=True, by="I.1")
        p_ae_2 = model.intersect(c_ae_1, c_ae_2, side_of=(pt_a, pt_e, -1), guide=True, by="I.1")
        bis_ae = model.construct_line(p_ae_1, p_ae_2, guide=True, by="I.10")
    pt_n_sq = model.intersect(line_ae, bis_ae, ID="N_sq", by="I.10")
    c_in_sq = model.construct_circle(pt_o, pt_n_sq, classes=["incircle"], ID="c_in_sq", by="Post.3")

    _ = pt_w

    # 3. Demonstrate: equilateral triangle sides Q = 3, Q_in_tri/Q_out = 1/4, Q_in_sq/Q_out = 1/2
    model.assert_equal(seg_ab, seg_bc, seg_ca, by="XIII.12", label="Triangle ABC is equilateral")
    model.assert_perpendicular(axis_ns, axis_ew, by="I.11", label="Diameter EW perpendicular to NS")

    if not zero_test(quadrance(pt_a, pt_b) - sp.Integer(3)):
        raise ProofAssertionError("Equilateral side quadrance Q(A, B) != 3")
    if not zero_test(quadrance(pt_o, pt_m) / quadrance(pt_o, pt_a) - sp.Rational(1, 4)):
        raise ProofAssertionError("Triangle incircle/circumcircle quadrance ratio != 1/4")
    if not zero_test(quadrance(pt_o, pt_n_sq) / quadrance(pt_o, pt_a) - sp.Rational(1, 2)):
        raise ProofAssertionError("Square incircle/circumcircle quadrance ratio != 1/2")
    if not zero_test(line_spread(axis_ns, axis_ew) - sp.Integer(1)):
        raise ProofAssertionError("Axes spread != 1")

    model.conclude(
        c_out,
        seg_ab,
        seg_bc,
        seg_ca,
        c_in_tri,
        c_in_sq,
        kind="qed",
        label="Graz 1595 triangle Q_in/Q_out = 1/4 and square Q_in/Q_out = 1/2.",
    )
    return model
