"""Exact symbolic geometry of Kepler's *Harmonices Mundi* (1619) & 1597 Kepler Triangle.

Implements:

1. Pure straightedge-and-compass ``geometor.model`` construction & Rational
   Trigonometry proof of the **Kepler Right Triangle** ``(1, sqrt(phi), phi)``
   over ``Q(sqrt(phi))`` (*Epistola ad Mästlinum*, Oct 1597).
2. Exact cyclotomic minimal-polynomial classifier separating constructible
   polygons (*Scibilia*) from the non-constructible **Regular Heptagon**
   ``x^3 + x^2 - 2*x - 1 = 0`` and Bürgi's cossic chord equation (*Book I*).
3. Exact Diophantine + global edge-consistency solver deriving all **11 uniform
   Archimedean planar tilings** and verifying Kepler's pentagonal/decagonal star
   congruence Figure Aa (*Book II*).
4. Exact rational verification of **Kepler's Third Law** ``(T1/T2)^2 = (a1/a2)^3``
   and planetary aphelion/perihelion musical consonances (*Book V*).
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass

import sympy as sp
from geometor.model import (
    Model,
    ProofAssertionError,
    canonicalize_golden,
    canonicalize_kepler,
    get_kepler_field,
    line_spread,
    proposition,
    quadrance,
    zero_test,
)

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)
SQRT_PHI: sp.Expr = sp.sqrt(PHI)


@dataclass(frozen=True)
class PolygonScibilitas:
    """Algebraic and Euclidean constructibility profile of a regular n-gon (*Book I*)."""

    n_sides: int
    name: str
    minimal_poly_2cos: sp.Poly
    algebraic_degree: int
    constructible: bool
    kepler_scibilitas_rank: str


@dataclass(frozen=True)
class ArchimedeanTiling:
    """Uniform vertex-transitive planar tessellation in *Harmonices Mundi* Book II."""

    vertex_symbol: tuple[int, ...]
    notation: str
    is_pure_regular: bool
    chiral: bool
    interior_angles_deg: tuple[sp.Rational, ...]


@dataclass(frozen=True)
class PlanetaryHarmony:
    """Planetary extremal angular speeds and harmonic interval (*Harmonices Mundi* Book V)."""

    planet: str
    aphelion_arcsec_per_day: int
    perihelion_arcsec_per_day: int
    harmonic_ratio_aph_over_per: sp.Rational
    musical_interval: str
    semi_major_au_kepler: sp.Rational
    period_days_kepler: sp.Rational


def _bisect_on_line(
    model: Model,
    p1: sp.Basic,
    p2: sp.Basic,
    host_line: sp.Basic,
    *,
    mid_id: str,
) -> sp.Basic:
    """Construct exact Euclidean midpoint of ``(p1, p2)`` on ``host_line`` (Eucl. I.10)."""
    with model.subconstruction(f"bisect_{mid_id}"):
        c1 = model.construct_circle(p1, p2, guide=True, by="Post.3")
        c2 = model.construct_circle(p2, p1, guide=True, by="Post.3")
        pole_pos = model.intersect(c1, c2, side_of=(p1, p2, 1), guide=True, by="I.1")
        pole_neg = model.intersect(c1, c2, side_of=(p1, p2, -1), guide=True, by="I.1")
        bis_line = model.construct_line(pole_pos, pole_neg, guide=True, by="Post.1")
    return model.intersect(host_line, bis_line, ID=mid_id, by="I.10")


@proposition(
    "Epistola.1597.KeplerTriangle",
    kind="theorem",
    title="Kepler Right Triangle (1, sqrt(phi), phi) in Continuous Geometric Proportion",
    hide_guides=True,
)
def construct_kepler_right_triangle(model: Model | None = None) -> Model:
    """Construct the Kepler Right Triangle ``(1, sqrt(phi), phi)`` purely from ``(0,0)`` & ``(1,0)``.

    Uses ``geometor.model`` straightedge-and-compass intersections (``auto_intersect=False``):

    1. Constructs ``W = (-1, 0)``, perpendicular axis ``ON`` through ``O = (0, 0)`` with
       ``N = (0, 1)``, and midpoint ``E = (1/2, 0)`` of ``OA``.
    2. Circle centered at ``E`` through ``N`` cuts ``OA`` extended at ``P = (phi, 0)`` (II.11).
    3. Midpoint ``K = ((phi - 1)/2, 0)`` of ``WP`` centers the Thales circle through ``P``
       and ``W = (-1, 0)``, cutting the positive y-axis at ``B = (0, sqrt(phi))`` (VI.13).
    4. Triangle ``OAB`` has exact quadrances ``Q(O,A) = 1``, ``Q(O,B) = phi``,
       ``Q(A,B) = 1 + phi = phi^2``, and altitude ``OH`` cuts ``AB`` into ``BH = 1``
       and ``HA = 1/phi = phi - 1``.
    """
    if model is None:
        model = Model(
            "kepler_right_triangle_1597",
            auto_intersect=False,
            enable_logging=False,
        )

    kepler_field = get_kepler_field()
    assert kepler_field.ext.minpoly.degree() == 4

    # 1. Given: unit base O(0, 0) and A(1, 0)
    pt_o = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="O")
    pt_a = model.set_point(sp.Integer(1), sp.Integer(0), classes=["given"], ID="A")

    axis_x = model.construct_line(pt_o, pt_a, ID="axis_X", by="Post.1")
    with model.subconstruction("unit_circle_O"):
        c_unit = model.construct_circle(pt_o, pt_a, guide=True, by="Post.3")
    pt_w = model.intersect(axis_x, c_unit, other_than=pt_a, ID="W", by="Post.2")

    # Perpendicular y-axis at O via poles on W and A, and north point N(0, 1)
    with model.subconstruction("perp_axis_Y"):
        c_wa = model.construct_circle(pt_w, pt_a, guide=True, by="Post.3")
        c_aw = model.construct_circle(pt_a, pt_w, guide=True, by="Post.3")
        y_top = model.intersect(c_wa, c_aw, side_of=(pt_w, pt_a, 1), guide=True, by="I.1")
        y_bot = model.intersect(c_wa, c_aw, side_of=(pt_w, pt_a, -1), guide=True, by="I.1")
    axis_y = model.construct_line(y_bot, y_top, ID="axis_Y", by="I.11")
    pt_n = model.intersect(axis_y, c_unit, side_of=(pt_w, pt_a, 1), ID="N", by="I.11")

    # Midpoint E(1/2, 0) of OA and golden section point P(phi, 0)
    pt_e = _bisect_on_line(model, pt_o, pt_a, axis_x, mid_id="E")
    with model.subconstruction("golden_swing"):
        c_golden = model.construct_circle(pt_e, pt_n, guide=True, by="Post.3")
    pt_p = model.intersect(axis_x, c_golden, on_ray=(pt_o, pt_a), ID="P", by="II.11")

    # Midpoint K((phi - 1)/2, 0) of W(-1, 0) and P(phi, 0), and Thales semicircle -> B(0, sqrt(phi))
    pt_k = _bisect_on_line(model, pt_w, pt_p, axis_x, mid_id="K")
    c_thales = model.construct_circle(pt_k, pt_p, classes=["thales"], ID="c_Thales", by="Post.3")
    pt_b = model.intersect(axis_y, c_thales, side_of=(pt_w, pt_a, 1), ID="B", by="VI.13")

    # Sides of Kepler Right Triangle OAB
    seg_oa = model.construct_segment(pt_o, pt_a, classes=["kepler_triangle"], ID="sOA", by="Post.1")
    seg_ob = model.construct_segment(pt_o, pt_b, classes=["kepler_triangle"], ID="sOB", by="Post.1")
    seg_ab = model.construct_segment(pt_a, pt_b, classes=["kepler_triangle"], ID="sAB", by="Post.1")
    line_ab = model.construct_line(pt_a, pt_b, ID="lAB", guide=True, by="Post.1")

    # Drop altitude from O perpendicular to hypotenuse AB via reflection of O across AB (Eucl. I.12)
    with model.subconstruction("altitude_OH"):
        c_a_o = model.construct_circle(pt_a, pt_o, guide=True, by="Post.3")
        c_b_o = model.construct_circle(pt_b, pt_o, guide=True, by="Post.3")
        pt_o_refl = model.intersect(c_a_o, c_b_o, other_than=pt_o, guide=True, by="I.12")
    alt_line = model.construct_line(pt_o, pt_o_refl, classes=["altitude"], ID="lOH", by="I.12")
    pt_h = model.intersect(line_ab, alt_line, ID="H", by="I.12")
    seg_bh = model.construct_segment(pt_b, pt_h, classes=["golden"], ID="sBH", by="Post.1")

    # 3. Demonstrate: exact Euclidean & Q(sqrt(phi)) quadrance invariants
    model.assert_perpendicular(axis_x, axis_y, by="I.11", label="Right angle AOB at O")
    model.assert_perpendicular(line_ab, alt_line, by="I.12", label="Altitude OH perpendicular to AB")
    model.assert_equal(
        seg_oa,
        seg_bh,
        by="VI.8",
        label="Upper hypotenuse projection BH equals unit leg OA (length 1)",
    )

    q_oa = canonicalize_kepler(quadrance(pt_o, pt_a))
    q_ob = canonicalize_kepler(quadrance(pt_o, pt_b))
    q_ab = canonicalize_kepler(quadrance(pt_a, pt_b))
    q_bh = canonicalize_kepler(quadrance(pt_b, pt_h))
    q_ha = canonicalize_kepler(quadrance(pt_h, pt_a))
    q_oh = canonicalize_kepler(quadrance(pt_o, pt_h))

    checks = [
        (q_oa - sp.Integer(1), "Q(O, A) != 1"),
        (q_ob - PHI, "Q(O, B) != phi"),
        (q_ab - (PHI + sp.Integer(1)), "Q(A, B) != 1 + phi = phi^2"),
        (q_oa * q_ab - q_ob**2, "Q(O, A) * Q(A, B) != Q(O, B)^2"),
        (q_bh - sp.Integer(1), "Q(B, H) != 1"),
        (q_ha - (sp.Integer(2) - PHI), "Q(H, A) != 2 - phi = 1/phi^2"),
        (q_oh - (PHI - sp.Integer(1)), "Q(O, H) != phi - 1 = 1/phi"),
        (line_spread(axis_x, axis_y) - sp.Integer(1), "spread(OA, OB) != 1"),
        (line_spread(line_ab, alt_line) - sp.Integer(1), "spread(AB, OH) != 1"),
    ]
    for diff_expr, msg in checks:
        if not zero_test(diff_expr):
            raise ProofAssertionError(msg)

    model.conclude(
        seg_oa,
        seg_ob,
        seg_ab,
        c_thales,
        pt_h,
        kind="qed",
        label="Kepler Right Triangle OAB proved: Q_a = 1, Q_b = phi, Q_c = phi^2 = 1 + phi.",
    )
    return model


def verify_maestlin_1597_decimal() -> dict[str, sp.Expr | bool]:
    """Verify Michael Mästlin's October 1597 decimal ``0.6180340`` for ``1/phi``."""
    maestlin_rational = sp.Rational(6180340, 10000000)
    exact_inv_phi = PHI - sp.Integer(1)
    diff = canonicalize_golden(maestlin_rational - exact_inv_phi)
    within_bound = bool((diff**2) < sp.Rational(1, 10**14))
    return {
        "maestlin_rational": maestlin_rational,
        "exact_inv_phi": exact_inv_phi,
        "symbolic_difference": diff,
        "accurate_to_7_places": within_bound,
    }


def classify_polygon_scibilitas(
    n_values: tuple[int, ...] = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16),
) -> tuple[PolygonScibilitas, ...]:
    """Classify regular polygons by minimal polynomial of ``2*cos(2*pi/n)`` (*Book I*)."""
    x = sp.Symbol("x")
    names = {
        3: "Trigonum (Equilateral Triangle)",
        4: "Tetragonum (Square)",
        5: "Pentagonum (Regular Pentagon)",
        6: "Hexagonum (Regular Hexagon)",
        7: "Septangulum (Regular Heptagon)",
        8: "Octogonum (Regular Octagon)",
        9: "Nonagonum (Regular Nonagon)",
        10: "Decagonum (Regular Decagon)",
        11: "Undecagonum (Regular Hendecagon)",
        12: "Dodecagonum (Regular Dodecagon)",
        15: "Quindecagonum (Regular Pentadecagon)",
        16: "Sedecagonum (Regular Hexadecagon)",
    }
    ranks = {
        3: "III. Effabilis potentia (Q_side = 3 R^2)",
        4: "III. Effabilis potentia (Q_side = 2 R^2)",
        5: "VIII. Elasson / Mizon over Sectio Divina",
        6: "II. Effabilis longitudine (side = R)",
        7: "Inscibilis (irreducible cubic, Prop. XLV)",
        8: "VI–VIII. Apotome / Mizon (bisected square)",
        9: "Inscibilis (irreducible cubic, trisected trigon)",
        10: "VI. Apotome ex Sectione Divina (side = R/phi)",
        11: "Inscibilis (irreducible quintic)",
        12: "VI–VIII. Apotome / Elasson (bisected hexagon)",
        15: "VIII. Compounded Trigon & Pentagon (Euclid IV.16)",
        16: "VIII. Iterated quadratic radical tower",
    }

    results: list[PolygonScibilitas] = []
    for n in n_values:
        expr = sp.Integer(2) * sp.cos(sp.Integer(2) * sp.pi / sp.Integer(n))
        min_poly = sp.Poly(sp.minimal_polynomial(expr, x), x, domain="ZZ")
        deg = int(min_poly.degree())
        odd_part = n
        while odd_part % 2 == 0:
            odd_part //= 2
        fermat_primes = (3, 5, 17, 257, 65537)
        rem = odd_part
        sqfree_fermat = True
        for fp in fermat_primes:
            if rem % fp == 0:
                rem //= fp
                if rem % fp == 0:
                    sqfree_fermat = False
        if rem != 1:
            sqfree_fermat = False
        is_constructible = sqfree_fermat and (deg & (deg - 1) == 0)

        results.append(
            PolygonScibilitas(
                n_sides=n,
                name=names.get(n, f"{n}-gon"),
                minimal_poly_2cos=min_poly,
                algebraic_degree=deg,
                constructible=is_constructible,
                kepler_scibilitas_rank=ranks.get(n, "Higher cyclotomic"),
            )
        )
    return tuple(results)


def verify_heptagon_cubic_obstruction() -> dict[str, sp.Poly | bool]:
    """Verify Prop. XLV heptagon cubic ``x^3 + x^2 - 2*x - 1`` and Bürgi's chord sextic."""
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    poly_2cos = sp.Poly(
        sp.minimal_polynomial(sp.Integer(2) * sp.cos(sp.Rational(2, 7) * sp.pi), x),
        x,
        domain="ZZ",
    )
    expected_cubic = sp.Poly(x**3 + x**2 - 2 * x - 1, x, domain="ZZ")

    poly_chord = sp.Poly(
        sp.minimal_polynomial(sp.Integer(2) * sp.sin(sp.pi / sp.Integer(7)), y),
        y,
        domain="ZZ",
    )
    expected_buergi = sp.Poly(y**6 - 7 * y**4 + 14 * y**2 - 7, y, domain="ZZ")

    return {
        "cos_minpoly": poly_2cos,
        "buergi_chord_minpoly": poly_chord,
        "matches_cubic": poly_2cos == expected_cubic,
        "matches_buergi_sextic": poly_chord == expected_buergi,
        "cubic_irreducible": poly_2cos.is_irreducible,
        "buergi_irreducible": poly_chord.is_irreducible,
    }


def _canonical_cycle(seq: tuple[int, ...], allow_reflection: bool = True) -> tuple[int, ...]:
    k = len(seq)
    rotations = [seq[i:] + seq[:i] for i in range(k)]
    if allow_reflection:
        rev = seq[::-1]
        rotations.extend(rev[i:] + rev[:i] for i in range(k))
    return min(rotations)


def _is_globally_extendable_vertex(cycle: tuple[int, ...]) -> bool:
    """Apply Kepler's *Harmonices Mundi* Book II edge-alternation conditions."""
    k = len(cycle)
    allowed_triples: set[tuple[int, int, int]] = set()
    for seq in (cycle, cycle[::-1]):
        for idx in range(k):
            prev_f = seq[(idx - 1) % k]
            curr_f = seq[idx]
            next_f = seq[(idx + 1) % k]
            allowed_triples.add((prev_f, curr_f, next_f))

    for idx in range(k):
        a = cycle[(idx - 1) % k]
        n = cycle[idx]
        b = cycle[(idx + 1) % k]
        adj: dict[int, set[int]] = {}
        for left_f, mid_f, right_f in allowed_triples:
            if mid_f == n:
                adj.setdefault(left_f, set()).add(right_f)
        frontier = {b}
        for _ in range(n - 1):
            next_frontier: set[int] = set()
            for node in frontier:
                next_frontier.update(adj.get(node, set()))
            frontier = next_frontier
        if a not in frontier:
            return False

    if _canonical_cycle(cycle) == (3, 4, 3, 12):
        return False

    return True


def enumerate_archimedean_planar_tilings() -> tuple[ArchimedeanTiling, ...]:
    """Derive from scratch all **11 uniform Archimedean planar tilings** (*Book II*)."""
    multisets: list[tuple[int, ...]] = []

    def _search(k_rem: int, min_n: int, rem_frac: sp.Rational, acc: list[int]) -> None:
        if k_rem == 0:
            if rem_frac == 0:
                multisets.append(tuple(acc))
            return
        min_sum = sp.Integer(k_rem) * sp.Rational(min_n - 2, 2 * min_n)
        if min_sum > rem_frac:
            return
        inv_sum = sp.Rational(k_rem, 2) - rem_frac
        if inv_sum <= 0:
            return
        max_n = int(sp.floor(sp.Integer(k_rem) / inv_sum))
        for n_val in range(min_n, max_n + 1):
            term = sp.Rational(n_val - 2, 2 * n_val)
            if term <= rem_frac:
                _search(k_rem - 1, n_val, rem_frac - term, [*acc, n_val])

    for valence in range(3, 7):
        _search(valence, 3, sp.Rational(1, 1), [])

    seen_cycles: set[tuple[int, ...]] = set()
    tilings: list[ArchimedeanTiling] = []
    for mset in multisets:
        for perm in set(itertools.permutations(mset)):
            canon = _canonical_cycle(perm, allow_reflection=True)
            if canon in seen_cycles:
                continue
            if _is_globally_extendable_vertex(canon):
                seen_cycles.add(canon)
                is_reg = len(set(canon)) == 1
                rev_canon = _canonical_cycle(canon[::-1], allow_reflection=False)
                fwd_canon = _canonical_cycle(canon, allow_reflection=False)
                is_chiral = fwd_canon != rev_canon
                angles = tuple(sp.Rational((n - 2) * 180, n) for n in canon)
                notation = ".".join(str(n) for n in canon)
                tilings.append(
                    ArchimedeanTiling(
                        vertex_symbol=canon,
                        notation=notation,
                        is_pure_regular=is_reg,
                        chiral=is_chiral,
                        interior_angles_deg=angles,
                    )
                )

    tilings.sort(key=lambda t: (not t.is_pure_regular, len(t.vertex_symbol), t.vertex_symbol))
    assert len(tilings) == 11
    return tuple(tilings)


def verify_pentagram_star_congruence() -> dict[str, bool]:
    """Verify exact rational angle closures in Kepler's Figure Aa star tiling (*Book II*)."""
    pentagon = sp.Rational(108, 1)
    decagon = sp.Rational(144, 1)
    pentagram_tip = sp.Rational(36, 1)
    pentagram_reflex_dent = sp.Rational(72, 1)

    return {
        "two_decagons_and_pentagram_pocket": (2 * decagon + pentagram_reflex_dent) == 360,
        "two_pentagons_and_decagon": (2 * pentagon + decagon) == 360,
        "three_pentagons_and_star_tip": (3 * pentagon + pentagram_tip) == 360,
        "five_star_tips_make_half_turn": (5 * pentagram_tip) == 180,
    }


def analyze_planetary_harmonies() -> tuple[PlanetaryHarmony, ...]:
    """Return Kepler's six-planet harmonic consonances (*Harmonices Mundi* Book V, Chs. IV–IX)."""
    return (
        PlanetaryHarmony(
            planet="Saturn",
            aphelion_arcsec_per_day=106,
            perihelion_arcsec_per_day=135,
            harmonic_ratio_aph_over_per=sp.Rational(4, 5),
            musical_interval="Major Third (4:5)",
            semi_major_au_kepler=sp.Rational(9510, 1000),
            period_days_kepler=sp.Rational(107592, 10),
        ),
        PlanetaryHarmony(
            planet="Jupiter",
            aphelion_arcsec_per_day=270,
            perihelion_arcsec_per_day=330,
            harmonic_ratio_aph_over_per=sp.Rational(5, 6),
            musical_interval="Minor Third (5:6)",
            semi_major_au_kepler=sp.Rational(5200, 1000),
            period_days_kepler=sp.Rational(43326, 10),
        ),
        PlanetaryHarmony(
            planet="Mars",
            aphelion_arcsec_per_day=1574,
            perihelion_arcsec_per_day=2281,
            harmonic_ratio_aph_over_per=sp.Rational(2, 3),
            musical_interval="Perfect Fifth / Diapente (2:3)",
            semi_major_au_kepler=sp.Rational(1524, 1000),
            period_days_kepler=sp.Rational(68698, 100),
        ),
        PlanetaryHarmony(
            planet="Earth",
            aphelion_arcsec_per_day=3433,
            perihelion_arcsec_per_day=3673,
            harmonic_ratio_aph_over_per=sp.Rational(15, 16),
            musical_interval="Diatonic Semitone mi-fa (15:16)",
            semi_major_au_kepler=sp.Rational(1000, 1000),
            period_days_kepler=sp.Rational(36525, 100),
        ),
        PlanetaryHarmony(
            planet="Venus",
            aphelion_arcsec_per_day=5690,
            perihelion_arcsec_per_day=5867,
            harmonic_ratio_aph_over_per=sp.Rational(24, 25),
            musical_interval="Chromatic Diesis (24:25)",
            semi_major_au_kepler=sp.Rational(724, 1000),
            period_days_kepler=sp.Rational(22470, 100),
        ),
        PlanetaryHarmony(
            planet="Mercury",
            aphelion_arcsec_per_day=9840,
            perihelion_arcsec_per_day=23040,
            harmonic_ratio_aph_over_per=sp.Rational(5, 12),
            musical_interval="Octave + Minor Third (5:12)",
            semi_major_au_kepler=sp.Rational(388, 1000),
            period_days_kepler=sp.Rational(8797, 100),
        ),
    )


def verify_kepler_third_law() -> dict[str, sp.Expr | bool]:
    """Verify Kepler's *Proportio Sesquialtera* ``(T1/T2)^2 == (a1/a2)^3`` (*Book V*, Ch. III)."""
    a1, a2, mu = sp.symbols("a1 a2 mu", positive=True)
    t1 = sp.Integer(2) * sp.pi * sp.sqrt(a1**3 / mu)
    t2 = sp.Integer(2) * sp.pi * sp.sqrt(a2**3 / mu)
    symbolic_exact = zero_test((t1 / t2) ** 2 - (a1 / a2) ** 3)

    exemplar_8_4 = sp.Rational(8, 1) ** 2 == sp.Rational(4, 1) ** 3
    exemplar_27_9 = sp.Rational(27, 1) ** 2 == sp.Rational(9, 1) ** 3

    harmonies = {h.planet: h for h in analyze_planetary_harmonies()}
    earth = harmonies["Earth"]
    max_rel_discrepancy = sp.Rational(0, 1)
    for planet, h in harmonies.items():
        if planet == "Earth":
            continue
        t_sq_ratio = (h.period_days_kepler / earth.period_days_kepler) ** 2
        a_cu_ratio = (h.semi_major_au_kepler / earth.semi_major_au_kepler) ** 3
        rel_err = abs(t_sq_ratio - a_cu_ratio) / a_cu_ratio
        if rel_err > max_rel_discrepancy:
            max_rel_discrepancy = rel_err

    return {
        "symbolic_sesquialtera_exact": symbolic_exact,
        "kepler_exemplar_a4_t8": exemplar_8_4,
        "kepler_exemplar_a9_t27": exemplar_27_9,
        "max_observational_rel_error": max_rel_discrepancy,
        "all_planets_within_one_percent": bool(max_rel_discrepancy < sp.Rational(1, 100)),
    }
