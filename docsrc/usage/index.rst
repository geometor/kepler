:navigation: header
:order: 20
:nav_title: Usage

.. _kepler-usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the GEOMETOR Interactive Digital Edition

Welcome to the **GEOMETOR Kepler** digital edition. This interactive edition combines primary Latin source texts, scholarly English translations, executive mathematical summaries, critical notes, and exact symbolic Python demonstrations into a unified research workspace.

Synchronized Reading Tracks
---------------------------

Every treatise unit in the **Cosmos & Harmony Codex** (:doc:`/cosmos_and_harmony/index`) is arranged in synchronized parallel tracks:

* **English (`-en`)**: Modern scholarly English translation translated directly from Kepler's original Latin text.
* **Latin (`-la`)**: Primary Neo-Latin text edited from the original seventeenth-century printings and Christian Frisch's critical *Opera Omnia*.
* **Summary (`-summary`)**: Compact geometric and physical synthesis isolating theorems, definitions, and invariant quadrances.
* **Notes (`-notes`)**: Philological, historical, and mathematical commentary situating Kepler's arguments within classical and modern traditions.

Use the track switcher in the book navigation bar at the top of each page to toggle instantly between views while maintaining your reading position.

Primary-Source Folio Milestones
-------------------------------

Kepler's treatises span over two decades of transformative astronomical and geometrical innovation:

* ***Mysterium Cosmographicum* (1596 / 1621)**: First printed in Tübingen (1596) and reissued with author notes in Frankfurt (1621).
* ***Strena seu de Nive Sexangula* (1611)**: Kepler's New Year's gift on hexagonal snow and close-packing printed in Frankfurt.
* ***Harmonices Mundi Libri V* (1619)**: The definitive treatise on geometric scibility, planar and spatial tilings, and harmonic planetary laws printed in Linz.

Marginal citations reference both original signature leaves and Christian Frisch's critical standard pagination (*Joannis Kepleri Astronomi Opera Omnia*, 1858–1871).

Interactive Diagrams & Deductive Links
--------------------------------------

Figures across the edition are rendered as responsive SVG diagrams:

* **Geometric Elements (`:g:`)**: Interactive labels in prose link directly to labeled vertices, arcs, and solids in diagrams.
* **Mathematical Invariants (`:eq:`)**: Equations denote exact rational and radical relationships over cyclotomic and golden fields.
* **Justifications (`:just:`)**: Citations to Euclid's *Elements* or Kepler's own axioms can be inspected in-line.

Full-Text Search with In-Page Highlighting
------------------------------------------

The built-in documentation search engine provides full-text indexing across all units, commentary, and module references.
Search queries append the `?highlight=` parameter to URLs, automatically highlighting queried terms across paragraphs, proofs, and registers.

Categories, Tags & Collection Views
-----------------------------------

The digital scriptorium organizes content along rich faceted taxonomies:

* Browse documents grouped by category, historical milestone, or topic using the sidebar taxonomy panels.
* In the :doc:`/log/index`, toggle between **Cards**, **Banners**, and **List** views using the collection layout switcher.

People, Bibliography & Glossary Tooltips
----------------------------------------

Cross-references throughout the text are linked directly to authoritative registries:

* **People (`:person:`)**: Hover or click on figures such as :person:`Euclid <euclid>`, :person:`Tycho Brahe <brahe>`, or :person:`Michael Mästlin <maestlin>` to view concise biographical context in :doc:`/cosmos_and_harmony/persons`.
* **Citations (`:cite:`)**: Bibliographical references link directly to full bibliographic records in :doc:`/cosmos_and_harmony/bibliography`.
* **Terms (`:term:`)**: Mathematical and philosophical vocabulary links directly to definitions in the :doc:`/cosmos_and_harmony/glossary`.
* **Theme Switching**: Toggle between Light and Dark display modes using the theme control in the navigation header.

Command-Line & Python API
-------------------------

The underlying analytical engine ``geometor.kepler`` provides exact symbolic models using SymPy:

.. code-block:: bash

   # Run CLI help and inspect available modules
   /home/phi/PROJECTS/geometor/.venv/bin/python -m geometor.kepler --help

   # Run test suite
   /home/phi/PROJECTS/geometor/.venv/bin/pytest

Explore the complete API reference in :doc:`/modules/index` and executable scripts in :doc:`/demos/index`.
