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
    assert __version__ == "0.2.0"
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
        assert len(root_data) >= 20
    concordance = json.loads((PROJECT_ROOT / "resources" / "concordance.json").read_text(encoding="utf-8"))
    assert len(concordance["entries"]) >= 5



def test_bilingual_codex_tracks_and_picture_directives() -> None:
    docsrc_dir = PROJECT_ROOT / "docsrc"
    books = {
        docsrc_dir / "mysterium_cosmographicum": (
            "praefatio",
            *(f"cap_{i:02d}" for i in range(1, 24)),
        ),
        docsrc_dir / "strena_sexangula": (
            "sec_01",
            "sec_02",
            "sec_03",
            "sec_04",
        ),
        docsrc_dir / "harmonices_mundi" / "liber_i": (
            "prooemium",
            "def_01_25",
            "prop_29",
            "prop_45",
        ),
        docsrc_dir / "harmonices_mundi" / "liber_ii": (
            "definitiones",
            "prop_01_20",
            "figura_aa",
            "prop_25",
            "prop_26",
            "prop_27",
            "prop_28",
        ),
        docsrc_dir / "harmonices_mundi" / "liber_v": (
            "epistola_1597",
            "cap_03_prop_08",
            "cap_04_09",
        ),
    }
    tracks = ("en", "la", "summary", "notes")
    for parent_dir, units in books.items():
        for unit in units:
            for track in tracks:
                rst_path = parent_dir / unit / f"{unit}-{track}.rst"
                assert rst_path.is_file(), f"Missing track file: {rst_path}"
                txt = rst_path.read_text(encoding="utf-8")
                assert len(txt.strip()) > 200
                assert ".. py_file::" not in txt
                assert ":align:" not in txt
                assert ":width:" not in txt


def test_archival_bitmaps_vectorizations_and_3d_studios() -> None:
    docsrc_dir = PROJECT_ROOT / "docsrc"
    png_plates = sorted(docsrc_dir.rglob("*.g*.png"))
    svg_plates = sorted(docsrc_dir.rglob("*.g*.svg"))

    assert len(png_plates) == 34, f"Expected 34 extracted archival bitmap plates, found {len(png_plates)}"
    assert len(svg_plates) == 14, f"Expected 14 calibrated folio SVG vectorizations, found {len(svg_plates)}"

    for png_path in png_plates:
        header = png_path.read_bytes()[:8]
        assert header == b"\x89PNG\r\n\x1a\n", f"Invalid PNG header: {png_path}"

    ns = "{http://www.w3.org/2000/svg}"
    for svg_path in svg_plates:
        root = ET.fromstring(svg_path.read_text(encoding="utf-8"))
        assert "euclid-graphic" in root.attrib.get("class", ""), f"Missing euclid-graphic class: {svg_path}"
        layer_ids = [
            child.attrib.get("id")
            for child in root
            if child.tag == f"{ns}g" and "id" in child.attrib
        ]
        assert layer_ids == ["elements", "graphics", "highlights", "points", "labels"], (
            f"Unexpected SVG layers in {svg_path}: {layer_ids}"
        )

    # Confirm zero orphaned plates: every extracted PNG and SVG must be referenced in its sibling RSTs
    for plate_path in [*png_plates, *svg_plates]:
        sibling_text = "\n".join(
            p.read_text(encoding="utf-8") for p in plate_path.parent.glob("*.rst")
        )
        assert plate_path.name in sibling_text, f"Orphaned plate not embedded in RST: {plate_path}"

    # Confirm Interactive 3D CAD Studio & Star Polyhedra mounts are surfaced
    for rel_path in (
        "mysterium_cosmographicum/index.rst",
        "mysterium_cosmographicum/cap_02/cap_02-en.rst",
        "mysterium_cosmographicum/cap_14/cap_14-en.rst",
    ):
        txt = (docsrc_dir / rel_path).read_text(encoding="utf-8")
        assert 'data-scene="tabula_iii_cad"' in txt, f"Missing Tabula III 3D CAD mount in {rel_path}"
        assert "tabula-iii-3d.html" in txt

    prop26_txt = (docsrc_dir / "harmonices_mundi/liber_ii/prop_26/prop_26-en.rst").read_text(encoding="utf-8")
    assert 'data-scene="harmonices_stellated"' in prop26_txt


def test_tabula_iii_3d_cad_model_and_exports() -> None:
    import sys

    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))

    from tabula_iii_3d.components import ShimScene, build_tabula_iii_scene, compute_radii

    # Verify exact Caput XIII ratios in CAD radial schedule
    r = compute_radii("exact")
    assert abs(r.jupiter_out / r.cube_r - 1.0 / float(sp.sqrt(3))) < 1e-9
    assert abs(r.mars_out / r.tetra_r - 1.0 / 3.0) < 1e-9
    dodec_ratio = float(sp.sqrt((5 + 2 * sp.sqrt(5)) / 15))
    assert abs(r.earth_out / r.dodeca_r - dodec_ratio) < 1e-9
    assert abs(r.venus_out / r.icosa_r - dodec_ratio) < 1e-9
    assert abs(r.mercury_out / r.octa_r - 1.0 / float(sp.sqrt(3))) < 1e-9

    # Verify clean 13-group assembly build
    scene = ShimScene()
    build_tabula_iii_scene(scene, scale_mode="exact", explode=0.0)
    assert len(scene.groups) == 13
    assert scene.groups[0].name == "01_Pedestal_Cradle"
    assert scene.groups[-1].name == "13_Mu_Sol_Center"

    # Verify CAD files exist and have valid binary magic headers
    cad_dir = PROJECT_ROOT / "tabula_iii_3d"
    for fname in ("tabula_iii.igz", "tabula_iii.glb", "tabula_iii.obj", "tabula_iii.mtl", "tabula_iii.blend"):
        fpath = cad_dir / fname
        assert fpath.is_file() and fpath.stat().st_size > 1000, f"Missing/empty CAD artifact: {fpath}"

    assert (cad_dir / "tabula_iii.glb").read_bytes()[:4] == b"glTF"
    assert (cad_dir / "tabula_iii.igz").read_bytes()[:2] == b"PK"

    # Verify web-served Three.js studio & downloadable CAD copies
    static_dir = PROJECT_ROOT / "docsrc" / "_static"
    for rel in (
        "tabula-iii-3d.html",
        "vendor/three.module.js",
        "vendor/OrbitControls.js",
        "models/tabula_iii.glb",
        "models/tabula_iii.igz",
        "models/tabula_iii.obj",
        "models/tabula_iii.mtl",
    ):
        assert (static_dir / rel).is_file(), f"Missing static 3D CAD asset: {rel}"


def test_harmonices_music_engine_and_studio() -> None:
    from geometor.kepler import (
        get_folio_0297_scales,
        get_planetary_melodies,
        get_universal_chords,
        verify_kepler_just_intonation,
    )

    checks = verify_kepler_just_intonation()
    assert len(checks) >= 10
    assert all(checks.values()), f"Kepler Just-Intonation check failed: {checks}"

    melodies = get_planetary_melodies()
    assert len(melodies) == 7
    assert [m.key for m in melodies] == [
        "saturn",
        "jupiter",
        "mars",
        "earth",
        "venus",
        "mercury",
        "moon",
    ]
    mercury = next(m for m in melodies if m.key == "mercury")
    assert len(mercury.notes) == 14
    for melody in melodies:
        for note in melody.notes:
            assert isinstance(note.ratio_from_g2, sp.Rational)
            assert isinstance(note.freq_hz, sp.Rational)
            assert not note.freq_hz.has(sp.Float)

    chords = get_universal_chords()
    assert len(chords) == 4
    scales = get_folio_0297_scales()
    assert set(scales.keys()) == {"cantus_durus", "cantus_mollis"}

    # Verify static Web Audio studio, microtonal MIDI, and stereo MP3s
    static_dir = PROJECT_ROOT / "docsrc" / "_static"
    studio_html = static_dir / "harmonices-mundi-studio.html"
    assert studio_html.is_file() and studio_html.stat().st_size > 20_000
    studio_txt = studio_html.read_text(encoding="utf-8")
    assert "AudioContext" in studio_txt
    assert "harmonices_mundi" in studio_txt or "Harmonices Mundi" in studio_txt

    midi_path = static_dir / "audio" / "kepler_harmonices_1619.mid"
    assert midi_path.is_file() and midi_path.read_bytes()[:4] == b"MThd"

    for mp3_name in ("kepler_planetary_motet.mp3", "kepler_creation_chords.mp3"):
        mp3_path = static_dir / "audio" / mp3_name
        assert mp3_path.is_file() and mp3_path.stat().st_size > 100_000

    # Confirm studio & audio embeds in Book Codex RSTs
    docsrc_dir = PROJECT_ROOT / "docsrc"
    for rel_path in (
        "harmonices_mundi/index.rst",
        "harmonices_mundi/liber_v/cap_04_09/cap_04_09-en.rst",
        "harmonices_mundi/liber_v/cap_04_09/cap_04_09-la.rst",
        "mysterium_cosmographicum/cap_12/cap_12-en.rst",
        "mysterium_cosmographicum/cap_12/cap_12-la.rst",
    ):
        txt = (docsrc_dir / rel_path).read_text(encoding="utf-8")
        assert "harmonices-mundi-studio.html" in txt, f"Missing live music studio embed in {rel_path}"





