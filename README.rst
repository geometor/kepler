===============
geometor-kepler
===============

Scholarly **Four-Track Bilingual Book Codex** (Latin / English / Summary / Notes) and **100% Exact Symbolic Geometry Engine** for **Johannes Kepler's (1571–1630)** foundational treatises in the **GEOMETOR** Digital Scriptorium:

1. ***Mysterium Cosmographicum*** (*Prodromus Dissertationum Cosmographicarum*, Tübingen 1596 / Frankfurt 1621; *Frisch Opera Omnia* Vol. I) — The July 19, 1595 Graz Great-Conjunction triangle ($r_{\text{in}} : R_{\text{out}} = 1 : 2$), the five Euclidean regular solids nested between the six Copernican planetary spheres around *Terra* (*Circulus mensor omnium*), and polar-duality insphere/circumsphere invariance over $\mathbb{Q}(\phi)$.
2. ***Strena seu de Nive Sexangula*** (*On the Six-Cornered Snowflake*, Frankfurt 1611; *Frisch Opera Omnia* Vol. VII) — Sixfold snow crystallography, bee honeycomb trihedral bases, discovery of the space-filling **Rhombic Dodecahedron** ($\sqrt{2} : 1$, dihedral $120^\circ$) and **Golden Rhombic Triacontahedron** ($\phi : 1$, dihedral $144^\circ$), cubic/hexagonal close-packing density $\frac{\pi}{3\sqrt{2}} \approx 74.048\%$ (**Kepler Conjecture**), and self-propagating Fibonacci pentamery ($1, 1, 2, 3, 5, 8, 13, 21 \to \phi$).
3. ***Harmonices Mundi Libri I, II & V*** (Linz 1619; *Frisch Opera Omnia* Vol. V) & ***Epistola ad Mästlinum*** (Oct 1597; *Frisch* Vol. I, p. 377) — Euclidean polygon constructibility (*scibilitas*) and the cubic non-constructibility of the regular heptagon ($x^3 + x^2 - 2x - 1 = 0$), complete classification of the **11 uniform Archimedean planar tilings**, `Figure Aa` pentagonal/decagonal star congruence, **Small & Great Stellated Dodecahedra** ($\{5/2, 5\}$ and $\{5/2, 3\}$), the **Kepler Right Triangle** $(1, \sqrt{\phi}, \phi)$ over $\mathbb{Q}(\sqrt{\phi})$, planetary aphelion/perihelion musical consonances, and **Kepler's Harmonic Third Law** $(T_1/T_2)^2 = (a_1/a_2)^3$.

Architecture
------------

* ``src/geometor/kepler/`` — Pure exact symbolic ``SymPy`` + ``geometor.model`` modules (``auto_intersect=False``, ``@proposition`` proofs, Rational Trigonometry quadrance & spread invariants, zero floating-point coordinates in ``Model``):

  * ``mysterium_spheres.py`` — Exact 3D Platonic vertex models, insphere/circumsphere ratios & quadrances over $\mathbb{Q}(\phi)$, polar-duality verifier, 6-planet nested radii, and ``@proposition("Mysterium.Praefatio.Graz1595")`` planar straightedge-and-compass construction.
  * ``strena_packing.py`` — Exact 3D analyzers for the 14-vertex Rhombic Dodecahedron and 32-vertex Golden Rhombic Triacontahedron, FCC/HCP vs. simple-cubic sphere-packing densities, ``@proposition("Strena.HexagonalRosette")`` 7-circle rosette, and Fibonacci/Cassini identity engine.
  * ``harmonices_geometry.py`` — ``@proposition("Epistola.1597.KeplerTriangle")`` pure Euclidean construction of the Kepler Right Triangle $(1, \sqrt{\phi}, \phi)$ over ``get_kepler_field()``, cyclotomic constructibility classifier & Proposition XLV heptagon/Bürgi polynomial verifier, 11-tiling Diophantine + global edge-consistency solver, and Book V Third Law & harmonic consonance verifiers.

* ``docsrc/cosmos_and_harmony/`` — Five-unit, four-track ``:layout: book`` codex (``-en.rst``, ``-la.rst``, ``-summary.rst``, ``-notes.rst``) wired to **9** interactive ``.euclid-graphic`` SVG figures in ``docsrc/_static/figures/`` and scholarly apparatus registries in ``resources/`` (32 persons, 23 citations, 20 glossary entries, 10 cross-corpus concordances).

Provenance & Licensing
----------------------

All Neo-Latin source texts derive strictly from Public Domain early modern editions (1596, 1611, 1619, 1621) and Christian Frisch's *Joannis Kepleri Astronomi Opera Omnia* (1858–1868). Every English translation, executive summary, SVG figure, and commentary note is **100% originally authored for GEOMETOR** without consulting or reproducing copyrighted translations.

Verification & Build
--------------------

.. code-block:: bash

   /home/phi/.local/bin/ruff check src scripts demos tests
   /home/phi/PROJECTS/geometor/.venv/bin/python -m pytest
   /home/phi/PROJECTS/geometor/.venv/bin/python scripts/build_figures.py
   /home/phi/.local/bin/publish build
