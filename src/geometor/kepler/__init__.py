"""GEOMETOR Kepler — Exact Symbolic Cosmography, Crystallography & Celestial Harmony.

Provides 100% exact SymPy and ``geometor.model`` constructions and proofs for
Johannes Kepler's *Mysterium Cosmographicum* (1596/1621), *Strena seu de Nive
Sexangula* (1611), and *Harmonices Mundi Libri V* (1619).
"""

from __future__ import annotations

from geometor.kepler.harmonices_geometry import (
    ArchimedeanTiling,
    PlanetaryHarmony,
    PolygonScibilitas,
    analyze_planetary_harmonies,
    classify_polygon_scibilitas,
    construct_kepler_right_triangle,
    enumerate_archimedean_planar_tilings,
    verify_heptagon_cubic_obstruction,
    verify_kepler_third_law,
    verify_maestlin_1597_decimal,
    verify_pentagram_star_congruence,
)
from geometor.kepler.music import (
    COSMIC_G2_HZ,
    KeplerNote,
    PlanetaryVoice,
    UniversalChord,
    export_kepler_midi,
    get_folio_0297_scales,
    get_planetary_melodies,
    get_universal_chords,
    synthesize_creation_chords_wav,
    synthesize_planetary_motet_wav,
    verify_kepler_just_intonation,
)
from geometor.kepler.mysterium_spheres import (
    NestedPlanetOrb,
    SolidSphereRatio,
    compute_nested_planetary_radii,
    construct_mysterium_planar_nesting,
    derive_platonic_sphere_ratios,
    verify_polar_duality_ratios,
)
from geometor.kepler.strena_packing import (
    FibonacciConvergent,
    RhombicPolyhedronMetrics,
    SpherePackingComparison,
    analyze_rhombic_dodecahedron,
    analyze_rhombic_triacontahedron,
    compute_fibonacci_phyllotaxis,
    construct_hexagonal_rosette,
    verify_kepler_sphere_packing,
)

__version__ = "0.2.0"

__all__ = [
    "__version__",
    "COSMIC_G2_HZ",
    "ArchimedeanTiling",
    "FibonacciConvergent",
    "KeplerNote",
    "NestedPlanetOrb",
    "PlanetaryHarmony",
    "PlanetaryVoice",
    "PolygonScibilitas",
    "RhombicPolyhedronMetrics",
    "SolidSphereRatio",
    "SpherePackingComparison",
    "UniversalChord",
    "analyze_planetary_harmonies",
    "analyze_rhombic_dodecahedron",
    "analyze_rhombic_triacontahedron",
    "classify_polygon_scibilitas",
    "compute_fibonacci_phyllotaxis",
    "compute_nested_planetary_radii",
    "construct_hexagonal_rosette",
    "construct_kepler_right_triangle",
    "construct_mysterium_planar_nesting",
    "derive_platonic_sphere_ratios",
    "enumerate_archimedean_planar_tilings",
    "export_kepler_midi",
    "get_folio_0297_scales",
    "get_planetary_melodies",
    "get_universal_chords",
    "synthesize_creation_chords_wav",
    "synthesize_planetary_motet_wav",
    "verify_heptagon_cubic_obstruction",
    "verify_kepler_just_intonation",
    "verify_kepler_sphere_packing",
    "verify_kepler_third_law",
    "verify_maestlin_1597_decimal",
    "verify_pentagram_star_congruence",
    "verify_polar_duality_ratios",
]
