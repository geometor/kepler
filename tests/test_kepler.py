"""Comprehensive verification suite for ``geometor-kepler``."""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from pathlib import Path

import sympy as sp
from geometor.model import Model, quadrance, zero_test

from geometor.kepler import (
    __version__,
    analyze_planetary_harmonies,
    analyze_rhombic_dodecahedron,
    analyze_rhombic_triacontahedron,
    classify_polygon_scibilitas,
    compute_fibonacci_phyllotaxis,
    compute_nested_planetary_radii,
    construct_hexagonal_rosette,
    construct_kepler_right_triangle,
    construct_mysterium_planar_nesting,
    derive_platonic_sphere_ratios,
    enumerate_archimedean_planar_tilings,
    verify_heptagon_cubic_obstruction,
    verify_kepler_sphere_packing,
    verify_kepler_third_law,
    verify_maestlin_1597_decimal,
    verify_pentagram_star_congruence,
    verify_polar_duality_ratios,
)
from geometor.kepler.cli import main as cli_main

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PHI = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)


def _assert_zero_floats_in_model(model: Model) -> None:
    pts = model.points
    assert len(pts) >= 4
    for pt in pts:
        assert not pt.x.has(sp.Float), f"Point {model[pt].ID} x-coord contains sp.Float: {pt.x}"
        assert not pt.y.has(sp.Float), f"Point {model[pt].ID} y-coord contains sp.Float: {pt.y}"


def test_version_and_cli() -> None:
    assert __version__ == "0.1.4"
    assert cli_main() == 0


def test_mysterium_platonic_sphere_ratios_and_polar_duality() -> None:
    solids = derive_platonic_sphere_ratios()
    assert [s.name for s in solids] == [
        "Cube",
        "Tetrahedron",
        "Dodecahedron",
        "Icosahedron",
        "Octahedron",
    ]
    duality = verify_polar_duality_ratios()
    assert all(duality.values()), f"Polar duality failed: {duality}"

    orbs = compute_nested_planetary_radii()
    assert len(orbs) == 6
    earth_orb = next(o for o in orbs if o.planet == "Earth")
    assert earth_orb.symbolic_radius == sp.Integer(1)
    radii_float = [float(o.symbolic_radius.evalf()) for o in orbs]
    assert radii_float == sorted(radii_float, reverse=True)


def test_mysterium_graz_planar_construction() -> None:
    model = construct_mysterium_planar_nesting()
    _assert_zero_floats_in_model(model)
    pt_o = model.get_element_by_ID("O")
    pt_a = model.get_element_by_ID("A")
    pt_m = model.get_element_by_ID("M")
    assert zero_test(quadrance(pt_o, pt_m) / quadrance(pt_o, pt_a) - sp.Rational(1, 4))


def test_strena_rhombic_polyhedra_and_packing() -> None:
    rd = analyze_rhombic_dodecahedron()
    assert (rd.faces, rd.vertices, rd.edges) == (12, 14, 24)
    assert zero_test(rd.diagonal_ratio - sp.sqrt(2))
    assert rd.dihedral_angle_deg == sp.Rational(120, 1)
    assert rd.space_filling is True

    rt = analyze_rhombic_triacontahedron()
    assert (rt.faces, rt.vertices, rt.edges) == (30, 32, 60)
    assert zero_test(rt.diagonal_ratio - PHI)
    assert zero_test(rt.diagonal_quadrance_ratio - (PHI + 1))
    assert rt.dihedral_angle_deg == sp.Rational(144, 1)
    assert rt.space_filling is False

    pack = verify_kepler_sphere_packing()
    assert pack.simple_cubic_kissing == 6
    assert pack.close_packed_kissing == 12
    assert zero_test(pack.close_packed_density - sp.pi / (3 * sp.sqrt(2)))
    assert zero_test(pack.density_ratio_close_over_cubic - sp.sqrt(2))


def test_strena_hexagonal_rosette_and_fibonacci() -> None:
    rosette = construct_hexagonal_rosette()
    _assert_zero_floats_in_model(rosette)

    fib = compute_fibonacci_phyllotaxis(12)
    assert [row.f_curr for row in fib[:8]] == [1, 1, 2, 3, 5, 8, 13, 21]
    for row in fib:
        expected = -1 if (row.index % 2 == 1) else 1
        assert row.cassini_determinant == expected


def test_kepler_right_triangle_1597() -> None:
    model = construct_kepler_right_triangle()
    _assert_zero_floats_in_model(model)
    pt_o = model.get_element_by_ID("O")
    pt_a = model.get_element_by_ID("A")
    pt_b = model.get_element_by_ID("B")
    assert zero_test(quadrance(pt_o, pt_a) - 1)
    assert zero_test(quadrance(pt_o, pt_b) - PHI)
    assert zero_test(quadrance(pt_a, pt_b) - (PHI + 1))

    maestlin = verify_maestlin_1597_decimal()
    assert maestlin["accurate_to_7_places"] is True


def test_harmonices_polygon_scibilitas_and_heptagon() -> None:
    profiles = {p.n_sides: p for p in classify_polygon_scibilitas()}
    for n_scib in (3, 4, 5, 6, 8, 10, 12, 15, 16):
        assert profiles[n_scib].constructible is True
    for n_inscib in (7, 9, 11):
        assert profiles[n_inscib].constructible is False

    hept = verify_heptagon_cubic_obstruction()
    assert hept["matches_cubic"] is True
    assert hept["matches_buergi_sextic"] is True
    assert hept["cubic_irreducible"] is True
    assert hept["buergi_irreducible"] is True


def test_harmonices_11_archimedean_tilings_and_star_congruence() -> None:
    tilings = enumerate_archimedean_planar_tilings()
    assert len(tilings) == 11
    notations = {t.notation for t in tilings}
    assert notations == {
        "3.3.3.3.3.3",
        "4.4.4.4",
        "6.6.6",
        "3.3.3.3.6",
        "3.3.3.4.4",
        "3.3.4.3.4",
        "3.4.6.4",
        "3.6.3.6",
        "3.12.12",
        "4.6.12",
        "4.8.8",
    }
    star = verify_pentagram_star_congruence()
    assert all(star.values())


def test_harmonices_book_v_third_law_and_consonances() -> None:
    harmonies = analyze_planetary_harmonies()
    assert len(harmonies) == 6
    law3 = verify_kepler_third_law()
    assert law3["symbolic_sesquialtera_exact"] is True
    assert law3["kepler_exemplar_a4_t8"] is True
    assert law3["kepler_exemplar_a9_t27"] is True
    assert law3["all_planets_within_one_percent"] is True


def test_euclid_graphic_svg_plates_and_apparatus_registries() -> None:
    fig_dir = PROJECT_ROOT / "docsrc" / "_static" / "figures"
    svgs = sorted(fig_dir.glob("fig*.svg"))
    assert len(svgs) == 9
    ns = "{http://www.w3.org/2000/svg}"
    for svg_path in svgs:
        root = ET.fromstring(svg_path.read_text(encoding="utf-8"))
        assert "euclid-graphic" in root.attrib.get("class", "")
        layer_ids = [
            child.attrib.get("id")
            for child in root
            if child.tag == f"{ns}g" and "id" in child.attrib
        ]
        assert layer_ids == ["elements", "graphics", "highlights", "points", "labels"]

    for fname in ("persons.json", "citations.json", "glossary.json"):
        root_data = json.loads((PROJECT_ROOT / "resources" / fname).read_text(encoding="utf-8"))
        codex_data = json.loads(
            (PROJECT_ROOT / "resources" / "cosmos_and_harmony" / fname).read_text(encoding="utf-8")
        )
        assert len(root_data) >= 20
        assert root_data == codex_data


def test_bilingual_codex_tracks_and_picture_directives() -> None:
    codex_dir = PROJECT_ROOT / "docsrc" / "cosmos_and_harmony"
    unit_slugs = (
        "unit-1-mysterium-cosmographicum",
        "unit-2-strena-snowflake",
        "unit-3-harmonices-liber-i",
        "unit-4-harmonices-liber-ii",
        "unit-5-harmonices-liber-v",
    )
    tracks = ("en", "la", "summary", "notes")
    for slug in unit_slugs:
        for track in tracks:
            rst_path = codex_dir / slug / f"{slug}-{track}.rst"
            assert rst_path.is_file(), f"Missing track file: {rst_path}"
            txt = rst_path.read_text(encoding="utf-8")
            assert len(txt.strip()) > 200
            assert ".. py_file::" not in txt
            assert ":align:" not in txt
            assert ":width:" not in txt

