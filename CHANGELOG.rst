=========
Changelog
=========

0.2.0 (2026-11-19)
------------------

* **added**:

  * **Exact Symbolic Celestial Music Engine (``geometor.kepler.music``)** & **Live Web Audio Studio (``docsrc/_static/harmonices-mundi-studio.html``)**: 100% exact ``sp.Rational`` 5-limit Just-Intonation transcription of Kepler's 1619 *Harmonices Mundi* folios ``0297``–``0302`` and 1596 Monochord (folio ``0050``), featuring all **7 voices** on folio ``0299`` (Saturn, Jupiter, Mars, Earth *MI–FA–MI*, Venus, Mercury's 14-note arpeggio, and the Moon's marginal cradle monody), all **4 Universal Six-Planet Creation Chords** (folios ``0301``–``0302``), live elliptical Keplerian Orbital Orrery Choir with golden Consonance Beam Detector, interactive vibrating brass Monochord & constructible-polygon plucker, pre-rendered stereo Cathedral Organ ``.mp3`` recordings, and a microtonal 14-bit pitch-bend ``.mid`` score.
  * **Tabula III (Folio 0034) 13-Group Parametric 3D CAD Model (``tabula_iii_3d/``)** & **WebGL PBR CAD Studio (``docsrc/_static/tabula-iii-3d.html``)**: Full architectural reconstruction of Christoph Leibfried's 1597 folding copperplate obeying Kepler's exact Caput XIII insphere/circumsphere ratios ($1/\sqrt{3}$, $1/3$, $\sqrt{(5+2\sqrt{5})/15}$)—six thick-walled cutaway planetary bowls ($\alpha$–$\lambda$), five mitered open-frame Platonic scaffolds ($\beta$–$\kappa$), Solar core ($\mu$), and carved 1597 pedestal—exported to IngeTrazo ``.igz``, Binary glTF ``.glb``, Wavefront ``.obj``/``.mtl``, and native Blender ``.blend`` with studio renders, paired with interactive 3D Kepler–Poinsot Star Polyhedra in Book II, Prop. XXVI.
  * **Complete 616-Folio Primary-Source Provenance & Paired Archival Plates**: Ingested 300-DPI scans across *Mysterium Cosmographicum* (1596, 194 folios, complete Chapters I–XXIII), *Strena Sexangula* (1611, 64 folios), and *Harmonices Mundi* (1619, 358 folios), extracting **34** contrast-normalized archival bitmap plates (including Universal Chords ``0301.g1.png`` & ``0302.g1.png``) paired with **14** calibrated five-layer ``.euclid-graphic`` SVG vectorizations (**61/61** ``.. folio::`` directives and **164/164** ``:folio:`` badges resolved; zero orphans).
  * **Illustrated Visual & Symbolic Audit Log (``docsrc/log/26.323-155100/``)**: Preserves headless Chromium WebGL/Canvas audit captures, multimodal scan findings, and the 4-gate verification matrix.

* **changed**:

  * Elevated all three treatises into canonical top-level English-first standalone Book Codices (``mysterium_cosmographicum/``, ``strena_sexangula/``, ``harmonices_mundi/``) with one chapter or proposition per page, synchronized four-track navigation (``English · Latin · Summary · Notes``), native Latin companion title pages (``title-la.rst``), and structured ``People`` and ``Sources`` directories.

0.1.4 (2026-11-15)
------------------

- Rebuilt codex documentation with ``photon-platform/publish`` ``v0.4.6`` so every inline ``.euclid-graphic`` SVG carries explicit ``viewBox`` pixel dimensions, per-diagram scoped ``<style>`` rules, and Nocturnal Codex dark/light theme parity.

0.1.3 (2026-11-15)
------------------

- Ensure canonical GEOMETOR ``logo.png`` and ``favicon.ico`` brand assets are provisioned in ``docsrc/_static/`` and rendered in site headers and browser tabs.

0.1.2 (2026-11-14)
------------------

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.1 (2026-11-14)
------------------

- Standardized Book Title Page, top-level header navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author and Translator profiles in People, and English structural terminology.

0.1.0 (2026-11-12)
------------------

* **Exact Symbolic ``geometor.kepler`` Engine**:

  * ``mysterium_spheres``: Exact 3D vertex derivations of all five Platonic insphere/circumsphere ratios and quadrances over $\mathbb{Q}(\phi)$, polar-duality equality proofs, six-planet nested Copernican radii from *Terra* ($R = 1$), and ``@proposition("Mysterium.Praefatio.Graz1595")`` straightedge-and-compass planar nesting in ``geometor.model``.
  * ``strena_packing``: Exact 3D geometric analyzers for the 14-vertex Rhombic Dodecahedron ($\sqrt{2}:1$, dihedral $120^\circ$, space-filling) and 32-vertex Golden Rhombic Triacontahedron ($\phi:1$, dihedral $144^\circ$), exact FCC/HCP close-packing density $\frac{\pi}{3\sqrt{2}}$ vs. simple cubic $\frac{\pi}{6}$, ``@proposition("Strena.HexagonalRosette")`` 7-circle close-packing rosette, and Fibonacci/Cassini identity verifier.
  * ``harmonices_geometry``: ``@proposition("Epistola.1597.KeplerTriangle")`` pure ruler-and-compass construction of the Kepler Right Triangle $(1, \sqrt{\phi}, \phi)$ over ``get_kepler_field()``, Mästlin's ``0.6180340`` decimal check, cyclotomic minimal-polynomial constructibility classifier ($n = 3 \dots 16$) & Proposition XLV heptagon cubic ($x^3 + x^2 - 2x - 1 = 0$) + Bürgi chord sextic ($y^6 - 7y^4 + 14y^2 - 7 = 0$), exact derivation of all **11 uniform Archimedean planar tilings**, ``Figure Aa`` star-pentagram angle verifier, and Book V **Third Law** $(T_1/T_2)^2 = (a_1/a_2)^3$ + six-planet harmonic consonances.

* **Five-Unit Four-Track Bilingual Book Codex (``docsrc/cosmos_and_harmony/``)**:

  * Complete ``-en.rst``, ``-la.rst``, ``-summary.rst``, and ``-notes.rst`` tracks across Units I–V (*Mysterium Cosmographicum*, *Strena seu de Nive Sexangula*, *Harmonices Mundi* Books I, II, and V + 1597 Kepler Triangle letter).
  * **9** interactive ``.euclid-graphic`` SVG figures with ``data-ref`` ↔ ``:g:`` wiring generated by ``scripts/build_figures.py``.
  * Enriched critical apparatus registries (32 persons, 23 primary & modern citations, 20 Latin/mathematical glossary entries, and 10 cross-corpus GEOMETOR concordances).
