:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:
.. _kepler-about:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor-kepler`` is a bilingual Digital Scriptorium Book Codex, semantic knowledge graph, and exact symbolic modeling environment dedicated to the foundational geometric and cosmological works of :person:`Johannes Kepler <kepler>` (1571–1630). Spanning three seminal treatises—*Mysterium Cosmographicum* (1596 / 1621), *Strena seu de Nive Sexangula* (*On the Six-Cornered Snowflake*, 1611), and *Harmonices Mundi Libri V* (*The Harmony of the World*, 1619)—this edition recovers Kepler's revolutionary vision of geometry as the eternal archetypal blueprint of the physical universe.

The edition structures Kepler's Latin prose into an interactive four-track **Book Codex** powered by ``photon-platform/publish``. Every unit offers synchronized reading across *English* (freshly translated from early modern Latin imprints), *Latin* (verbatim critical text from Christian Frisch's *Opera Omnia*), *Summary* (concise mathematical synopses of propositions and proofs), and *Notes* (in-depth philological, historical, and mathematical commentary). Key geometric concepts—from the Euclidean knowability (:term:`scibilitas`) of regular constructible polygons to the irreducible non-constructibility (:term:`inscibilitas`) of the heptagon, the classification of the 11 uniform Archimedean planar tilings, the discovery of the rhombic dodecahedron and triacontahedron, and Kepler's Third Law—are formalized into machine-addressable semantic elements.

Every construction is grounded symbolically through ``geometor.model`` using exact algebraic fields rather than numerical approximations. Kepler's famous golden right triangle $(1, \sqrt{\phi}, \phi)$ is formalized over the algebraic number field $\mathbb{Q}(\sqrt{\phi})$ defined by $x^4 - x^2 - 1 = 0$, while polyhedral insphere/circumsphere ratios and close-packing densities ($\frac{\pi}{3\sqrt{2}}$) are verified symbolically with SymPy. This positions ``geometor-kepler`` at the vital crossroads of the GEOMETOR ecosystem, directly connecting the axiomatic foundations of ``geometor.elements`` with the harmonic proportions of ``geometor.divine`` and the morphology of ``geometor.pappus``.

The GEOMETOR Mission
--------------------

The **GEOMETOR** initiative, conceived and directed by **phi ARCHITECT**, is dedicated to the systematic recovery, symbolic formalization, and creative re-articulation of humanity's geometric heritage. GEOMETOR unites classical synthesis with modern algebraic rigor across three core pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans, static facsimile bitmaps, and flat optical character recognition (OCR), GEOMETOR recovers the living deductive architecture of 2,300+ years of geometric, axiomatic, and philosophical treatises. Primary sources—spanning Euclid, Apollonius, Archimedes, Pappus, Johannes Kepler, Felix Klein, and Clark Kimberling—are analyzed to elevate enunciations, deductive steps, synthetic justifications, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Geometric constructions must not depend on floating-point approximations or visual artifacts. GEOMETOR anchors geometric entities in 100% exact symbolic algebra via `SymPy <https://www.sympy.org/>`_ and the principles of Rational Trigonometry (quadrance, spread, cross-ratio). Points, lines, circles, and conic loci are evaluated over exact algebraic fields, ensuring that tangencies, incidences, harmonic conjugates, and collinearities represent absolute mathematical truths rather than numerical estimates.

Repurposing Knowledge Across Mediums
    Extracted semantic architectures and exact symbolic models are re-deployed across a unified digital ecosystem: synchronized multi-track **Book Codices** and EPUB 3 editions powered by ``photon-platform/publish``, computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG exploration laboratories (``geometor.explorer``), ultra-high-definition visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

Public-Domain Textual Provenance & Copyright Audit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All primary Latin texts in this repository derive exclusively from 100% Public Domain early modern imprints and nineteenth-century critical editions:

1. ***Mysterium Cosmographicum* (1596 / 1621)**: *Prodromus Dissertationum Cosmographicarum, continens Mysterium Cosmographicum* (Tübingen: Georg Gruppenbach, 1596; 2nd author-annotated ed., Frankfurt: Erasmus Kempfer / Gottfried Tampach, 1621), together with Kepler's October 1597 letter to Michael Mästlin, edited by :person:`Christian Frisch <frisch>` in *Joannis Kepleri Astronomi Opera Omnia*, Vol. I (Frankfurt & Erlangen: Heyder & Zimmer, 1858, pp. 95–214, 377).
2. ***Strena seu de Nive Sexangula* (1611)**: *Ioannis Kepleri S. Cæs. Maiest. Mathematici Strena seu de Nive Sexangula* (Frankfurt am Main: Gottfried Tampach, 1611, 24 pp.), edited by Christian Frisch in *Opera Omnia*, Vol. VII (1868, pp. 715–730).
3. ***Harmonices Mundi Libri V* (1619)**: *Ioannis Keppleri Harmonices Mundi Libri V* (Linz: Gottfried Tampach / Johannes Planck, 1619), edited by Christian Frisch in *Opera Omnia*, Vol. V (1864, pp. 75–334).

Every English translation (`-en`), executive summary (`-summary`), and historical-mathematical commentary (`-notes`) in this codex is **100% originally translated and authored for GEOMETOR** directly from Kepler's Neo-Latin. Modern copyrighted translations—including C. G. Wallis (1939/1952), Colin Hardie (1966), A. M. Duncan & E. J. Aiton (1981), and E. J. Aiton, A. M. Duncan, & J. V. Field (1997)—were strictly excluded.

Position in the GEOMETOR Canon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kepler stands at the grand architectural crossroads of the GEOMETOR ecosystem:

* **Euclidean & Neoplatonic Foundations**: Extends ``geometor/euclid``, ``geometor/elements`` (Books II, IV, X, XIII), and ``geometor/proclus`` into physical astronomy and epistemology.
* **Divine Proportion & Kepler Field**: Supplies the canonical :term:`Kepler Right Triangle <kepler-triangle>` $(1, \sqrt{\phi}, \phi)$ formalized in ``geometor.model.get_kepler_field()`` over $\mathbb{Q}(\sqrt{\phi})$ ($x^4 - x^2 - 1 = 0$), bridging ``geometor/pacioli`` and ``geometor/divine``.
* **Morphology & Phyllotaxis**: Connects ``geometor/pappus`` (Book V honeycomb economy & 13 Archimedean solids) to ``geometor/phyllotaxis`` through hexagonal/cubic sphere close-packing, rhombic zonohedra, and Fibonacci convergence.
