:type: notes
:layout: book
:canonical_id: II.Def.
:order: 1
:folio: harmonices_mundi:0065

.. _unit-4-harmonices-liber-ii-notes:
.. _hm-liber-ii-def-notes:

Definitions: Notes & Provenance
===============================

Editorial & Geometric Apparatus
-------------------------------

* **Prooemium (p. 47–48)**: Connects Latin *congruere* / *congruentia* directly to Greek *ἁρμόττειν* / *ἁρμονία* ("fitting together"), grounding Book II's geometric combinatorics in Kepler's metaphysical architecture of Creation.
* **Space-Filling Solids & Honeycomb Cells (Def. V Nota, pp. 48–49)**: Kepler notes that among polyhedra filling 3D space around a point, only the cube and his newly described *rhombus dodecahedricus* (rhombic dodecahedron, which he links to the 3-rhombus base of bee honeycomb cells) achieve pure one-species space-filling—anticipating crystallography and Fedorov's parallelohedra.
* **Infinite Prisms and Antiprisms (Def. X, p. 49)**: Classes *A* and *B* on the plate at fol. 53 refer respectively to regular :math:`n`-gonal prisms (starting at :math:`n=3`, where :math:`n=4` is the cube—a *most perfect* regular solid) and :math:`n`-gonal antiprisms (starting at :math:`n=3`, the regular octahedron—another *most perfect* regular solid).
* **Why Local Diophantine Solutions Fail Globally (Def. XIII)**: A classic trap in elementary geometry is to assume that any set of regular polygons whose interior angles sum to :math:`360^\circ` tiles the plane uniformly. Solving :math:`\sum (n_i - 2)/(2n_i) = 1` yields **17** unordered multisets (and **21** cyclic vertex necklaces), yet **10** of those cyclic necklaces self-destruct after one or two steps! Consider Kepler's counterexample `5.5.10` (:math:`108^\circ + 108^\circ + 144^\circ = 360^\circ`): around any 5-sided pentagon, the polygons sharing its five edges would have to alternate `5, 10, 5, 10, ?`—an **odd** cycle of length :math:`5` cannot alternate two distinct symbols. Similarly, `3.7.42`, `3.8.24`, `3.9.18`, `3.10.15`, and `3.4.3.12` force neighbor collisions. In ``geometor.kepler.harmonices_geometry._is_globally_extendable_vertex``, encoding Kepler's exact odd-cycle walk condition eliminates all false local candidates automatically.
* **Print Erratum**: In Def. VII (p. 49), the 1619 Linz edition prints *regulatia* for *regularia*. In Def. XI (p. 50), *tueans* is printed for *tueatur* (or *tuens*).

Transcription & Provenance
--------------------------

* **Latin Witness**: *Public-domain Neo-Latin text from Ioannis Keppleri Harmonices Mundi Liber II: Architectonicus, seu ex Geometria Figurata, de Figurarum Regularium Congruentia in Plano vel Solido* (:cite:`Linz, 1619, pp. 47–50 <kepler:1619:hm>`; :cite:`ed. Ch. Frisch, Vol. V, pp. 126–129 <frisch:1864:v5>`).
* **English Track**: *Original GEOMETOR English translation from Johannes Kepler's Harmonices Mundi Liber II* (:cite:`Linz: Tampach/Plancus, 1619, pp. 47–50 <kepler:1619:hm>`; :cite:`Frisch V, pp. 126–129 <frisch:1864:v5>`).
* **Folio Scans**: Verified 300-DPI scans ``harmonices_mundi:0065``–``0068`` (pp. 47–50).
