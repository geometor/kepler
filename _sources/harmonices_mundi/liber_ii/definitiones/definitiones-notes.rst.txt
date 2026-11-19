:layout: book
:canonical_id: II.Def.
:order: 1
:folio: harmonices_mundi:0065
:tracks: Latin: definitiones-la | English: definitiones-en | Summary: definitiones-summary | Notes: definitiones-notes

.. _unit-4-harmonices-liber-ii-notes:
.. _hm-liber-ii-def-notes:

Definitions: Notes & Provenance
===============================

Why Local Diophantine Solutions Fail Globally
---------------------------------------------

A classic trap in elementary geometry is to assume that any set of regular polygons whose interior angles sum to $360^\circ$ tiles the plane uniformly. Solving $\sum (n_i - 2)/(2n_i) = 1$ yields **17** unordered multisets (and **21** cyclic vertex necklaces), yet **10** of those cyclic necklaces self-destruct after one or two steps!

Consider Kepler's counterexample `5.5.10` ($108^\circ + 108^\circ + 144^\circ = 360^\circ$): around any 5-sided pentagon, the polygons sharing its five edges would have to alternate `5, 10, 5, 10, ?`—an **odd** cycle of length $5$ cannot alternate two distinct symbols! Similarly, `3.7.42`, `3.8.24`, `3.9.18`, `3.10.15`, and `3.4.3.12` force neighbor collisions. In ``geometor.kepler.harmonices_geometry._is_globally_extendable_vertex``, encoding Kepler's exact odd-cycle walk condition eliminates all false local candidates automatically.

Transcription & Provenance
--------------------------

* **Latin Witness**: *Public-domain Neo-Latin text from Ioannis Keppleri Harmonices Mundi Liber II: Architectonicus, seu ex Geometria Figurata, de Figurarum Regularium Congruentia in Plano vel Solido* (:cite:`Linz, 1619, pp. 47–66 <kepler:1619:hm>`; :cite:`ed. Ch. Frisch, Vol. V, pp. 126–144 <frisch:1864:v5>`).
* **English Track**: *Original GEOMETOR English translation from Johannes Kepler's Harmonices Mundi Liber II: Architectonicus, seu ex Geometria Figurata, de Figurarum Regularium Congruentia in Plano vel Solido* (:cite:`Linz: Tampach/Plancus, 1619, pp. 47–66 <kepler:1619:hm>`; :cite:`Frisch V, pp. 126–144 <frisch:1864:v5>`).
* **Folio Scan**: Verified 300-DPI scan ``harmonices_mundi:0065`` (p. 47).
