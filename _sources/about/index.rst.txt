:navigation: footer
:order: 10
:nav_title: About

.. _kepler-about:

About GEOMETOR Kepler
=====================

Historical, philological, and mathematical provenance for ``geometor-kepler`` in the **GEOMETOR Digital Scriptorium**.

Public-Domain Textual Provenance & Copyright Audit
--------------------------------------------------

All primary Latin texts in this repository derive exclusively from 100% Public Domain early modern imprints and nineteenth-century critical editions:

1. ***Mysterium Cosmographicum* (1596 / 1621)**: *Prodromus Dissertationum Cosmographicarum, continens Mysterium Cosmographicum* (Tübingen: Georg Gruppenbach, 1596; 2nd author-annotated ed., Frankfurt: Erasmus Kempfer / Gottfried Tampach, 1621), together with Kepler's October 1597 letter to Michael Mästlin, edited by :person:`Christian Frisch <frisch>` in *Joannis Kepleri Astronomi Opera Omnia*, Vol. I (Frankfurt & Erlangen: Heyder & Zimmer, 1858, pp. 95–214, 377).
2. ***Strena seu de Nive Sexangula* (1611)**: *Ioannis Kepleri S. Cæs. Maiest. Mathematici Strena seu de Nive Sexangula* (Frankfurt am Main: Gottfried Tampach, 1611, 24 pp.), edited by Christian Frisch in *Opera Omnia*, Vol. VII (1868, pp. 715–730).
3. ***Harmonices Mundi Libri V* (1619)**: *Ioannis Keppleri Harmonices Mundi Libri V* (Linz: Gottfried Tampach / Johannes Planck, 1619), edited by Christian Frisch in *Opera Omnia*, Vol. V (1864, pp. 75–334).

Every English translation (`-en`), executive summary (`-summary`), and historical-mathematical commentary (`-notes`) in this codex is **100% originally translated and authored for GEOMETOR** directly from Kepler's Neo-Latin. Modern copyrighted translations—including C. G. Wallis (1939/1952), Colin Hardie (1966), A. M. Duncan & E. J. Aiton (1981), and E. J. Aiton, A. M. Duncan, & J. V. Field (1997)—were strictly excluded.

Position in the GEOMETOR Canon
------------------------------

Kepler stands at the grand architectural crossroads of the GEOMETOR ecosystem:

* **Euclidean & Neoplatonic Foundations**: Extends ``geometor/euclid``, ``geometor/elements`` (Books II, IV, X, XIII), and ``geometor/proclus`` into physical astronomy and epistemology.
* **Divine Proportion & Kepler Field**: Supplies the canonical :term:`Kepler Right Triangle <kepler-triangle>` $(1, \sqrt{\phi}, \phi)$ formalized in ``geometor.model.get_kepler_field()`` over $\mathbb{Q}(\sqrt{\phi})$ ($x^4 - x^2 - 1 = 0$), bridging ``geometor/pacioli`` and ``geometor/divine``.
* **Morphology & Phyllotaxis**: Connects ``geometor/pappus`` (Book V honeycomb economy & 13 Archimedean solids) to ``geometor/phyllotaxis`` through hexagonal/cubic sphere close-packing, rhombic zonohedra, and Fibonacci convergence.
