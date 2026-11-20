# GEOMETOR · Kepler (`geometor-kepler`)

Multi-treatise Bilingual Book Codex (`:layout: book`) and 100% exact symbolic `SymPy` + `geometor.model` constructive engine for **Johannes Kepler (1571–1630)**:

1. ***Mysterium Cosmographicum*** (1596 / 1621) — Five Platonic solids nested between the six Copernican spheres over $\mathbb{Q}(\phi)$, polar duality, and the 1595 Graz Great-Conjunction triangle.
2. ***Strena seu de Nive Sexangula*** (1611) — Sixfold snow crystallography, Rhombic Dodecahedron ($\sqrt{2}:1$), Golden Rhombic Triacontahedron ($\phi:1$), FCC/HCP sphere close-packing ($\frac{\pi}{3\sqrt{2}}$, Kepler Conjecture), and Fibonacci convergence to $\phi$.
3. ***Harmonices Mundi Libri I, II & V*** (1619) & ***Epistola ad Mästlinum*** (1597) — Polygon constructibility (*scibilitas*) & cubic obstruction of the regular heptagon ($x^3 + x^2 - 2x - 1 = 0$), complete derivation of the **11 uniform Archimedean planar tilings**, `Figure Aa` star-pentagram congruence & stellated dodecahedra, pure Euclidean construction of the **Kepler Right Triangle** $(1, \sqrt{\phi}, \phi)$ over $\mathbb{Q}(\sqrt{\phi})$, and **Kepler's Third Law** $(T_1/T_2)^2 = (a_1/a_2)^3$.

## Key Modules & Layout

- `src/geometor/kepler/mysterium_spheres.py`: Exact 3D Platonic insphere/circumsphere ratios, polar-duality verifier, 6-planet nested radii, and `@proposition("Mysterium.Praefatio.Graz1595")`.
- `src/geometor/kepler/strena_packing.py`: Exact 3D analyzers for Rhombic Dodecahedron and Rhombic Triacontahedron, FCC/HCP sphere-packing density, `@proposition("Strena.HexagonalRosette")`, and Fibonacci/Cassini verifier.
- `src/geometor/kepler/harmonices_geometry.py`: `@proposition("Epistola.1597.KeplerTriangle")` over `get_kepler_field()`, cyclotomic constructibility & Bürgi heptagon polynomials, 11 uniform Archimedean tilings solver, and Book V planetary consonance & Third Law verifiers.
- `src/geometor/kepler/music.py`: 100% exact `sp.Rational` 5-limit Just-Intonation engine transcribing all 7 planetary voices on folio `0299` (including Mercury's 14-note arpeggio and Luna), all 4 Universal Creation Chords (folios `0301`–`0302`), folio `0297` string-length scales (`2160–864`), microtonal 14-bit pitch-bend `.mid` export, and stereo Cathedral Organ WAV synthesis.
- `tabula_iii_3d/`: 13-group parametric 3D CAD assembly of Tabula III (1597, folio `0034`) obeying exact Caput XIII radial ratios, exported as IngeTrazo `.igz`, Binary glTF `.glb`, Wavefront `.obj`/`.mtl`, and native Blender `.blend`.
- `docsrc/_static/tabula-iii-3d.html` & `docsrc/_static/harmonices-mundi-studio.html`: Zero-CDN offline WebGL PBR CAD Studio (vendored Three.js) and Live Web Audio Celestial Music & Monochord Studio, plus stereo `.mp3` & microtonal `.mid` assets in `docsrc/_static/audio/`.
- `docsrc/{mysterium_cosmographicum,strena_sexangula,harmonices_mundi}/`: Three standalone four-track (`-en`, `-la`, `-summary`, `-notes`) English-first Book Codices backed by **616** tracked 300-DPI folio scans (`resources/*/folios/`), **34** cropped archival bitmap plates, and **14** calibrated five-layer `.euclid-graphic` SVG vectorizations (plus **9** symbolic SVG plates in `docsrc/_static/figures/`).

## Architectural Invariants

1. **100% Exact Symbolic Coordinates & Ratios**: Never inject `float` or `sp.Float` into `Model` or `KeplerNote`; construct with `Model(..., auto_intersect=False)` and explicit `model.intersect(...)` Euclidean selectors.
2. **Strict `.. picture::` Options**: Use only `:alt:`, `:caption:`, and `:class:` (never `:width:`, `:name:`, `:align:`, or `.. py_file::` inside historical codex tracks).
3. **100% Public-Domain Latin & Original English**: Never copy copyrighted translations; keep primary-source folio provenance in `*-notes.rst` and `:folio:` / `.. folio::` directives with zero unresolved links (`publish folio-links`).
4. **Clean Git Tree**: Never commit raw `.pdf` files, `docs/`, or `docsrc/modules/api/`.

## Offline Sandbox Verification Commands

```bash
ruff check src scripts demos tests tabula_iii_3d
uv run --no-sync pytest -q
publish folio-links --repo /home/phi/PROJECTS/geometor/kepler --json
publish build --clean --repo /home/phi/PROJECTS/geometor/kepler --json
```
