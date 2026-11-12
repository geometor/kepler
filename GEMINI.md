# GEOMETOR · Kepler (`geometor-kepler`)

Multi-treatise Bilingual Book Codex (`:layout: book`) and 100% exact symbolic `SymPy` + `geometor.model` constructive engine for **Johannes Kepler (1571–1630)**:

1. ***Mysterium Cosmographicum*** (1596 / 1621) — Five Platonic solids nested between the six Copernican spheres over $\mathbb{Q}(\phi)$, polar duality, and the 1595 Graz Great-Conjunction triangle.
2. ***Strena seu de Nive Sexangula*** (1611) — Sixfold snow crystallography, Rhombic Dodecahedron ($\sqrt{2}:1$), Golden Rhombic Triacontahedron ($\phi:1$), FCC/HCP sphere close-packing ($\frac{\pi}{3\sqrt{2}}$, Kepler Conjecture), and Fibonacci convergence to $\phi$.
3. ***Harmonices Mundi Libri I, II & V*** (1619) & ***Epistola ad Mästlinum*** (1597) — Polygon constructibility (*scibilitas*) & cubic obstruction of the regular heptagon ($x^3 + x^2 - 2x - 1 = 0$), complete derivation of the **11 uniform Archimedean planar tilings**, `Figure Aa` star-pentagram congruence & stellated dodecahedra, pure Euclidean construction of the **Kepler Right Triangle** $(1, \sqrt{\phi}, \phi)$ over $\mathbb{Q}(\sqrt{\phi})$, and **Kepler's Third Law** $(T_1/T_2)^2 = (a_1/a_2)^3$.

## Key Modules & Layout

- `src/geometor/kepler/mysterium_spheres.py`: Exact 3D Platonic insphere/circumsphere ratios, polar-duality verifier, 6-planet nested radii, and `@proposition("Mysterium.Praefatio.Graz1595")`.
- `src/geometor/kepler/strena_packing.py`: Exact 3D analyzers for Rhombic Dodecahedron and Rhombic Triacontahedron, FCC/HCP sphere-packing density, `@proposition("Strena.HexagonalRosette")`, and Fibonacci/Cassini verifier.
- `src/geometor/kepler/harmonices_geometry.py`: `@proposition("Epistola.1597.KeplerTriangle")` over `get_kepler_field()`, cyclotomic constructibility & Bürgi heptagon polynomials, 11 uniform Archimedean tilings solver, and Book V planetary consonance & Third Law verifiers.
- `src/geometor/kepler/sphinx_ext.py`: Registers `:person:`, `:cite:`, `:term:`, `:g:`, `:just:`, `:eq:` roles and apparatus directives; loads registries from `resources/` (synced identically to `resources/cosmos_and_harmony/`).
- `scripts/build_figures.py`: Generates all **9** `.euclid-graphic` SVG plates into `docsrc/_static/figures/`.
- `docsrc/cosmos_and_harmony/`: 5-unit, 4-track (`-en`, `-la`, `-summary`, `-notes`) Book Codex (zero embedded `py_file` directives inside historical codex tracks; executable demos reside in `demos/` and `docsrc/demos/index.rst`).

## Architectural Invariants

1. **100% Exact Symbolic Coordinates**: Never inject `float` or `sp.Float` into `Model`; always construct with `Model(..., auto_intersect=False)` and explicit `model.intersect(...)` Euclidean selectors.
2. **Strict `.. picture::` Options**: Use only `:alt:` (and `:class:` if needed; never `:width:`, `:name:`, `:align:`, or indented body captions).
3. **100% Public-Domain Latin & Original English**: Never copy copyrighted translations; keep `resources/{persons,citations,glossary}.json` and `resources/cosmos_and_harmony/{persons,citations,glossary}.json` byte-identical.
4. **Clean Git Tree**: Never commit `.pdf` files, PNG/JPG scans, `docs/`, or `docsrc/modules/api/`.

## Offline Sandbox Verification Commands

```bash
/home/phi/.local/bin/ruff check src scripts demos tests
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest
/home/phi/PROJECTS/geometor/.venv/bin/python scripts/build_figures.py
/home/phi/.local/bin/publish build
```
