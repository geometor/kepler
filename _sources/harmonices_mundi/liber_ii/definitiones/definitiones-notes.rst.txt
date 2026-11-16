:layout: book
:canonical_id: II.Def.
:order: 1
:tracks: Latin: definitiones-la | English: definitiones-en | Summary: definitiones-summary | Notes: definitiones-notes

.. _unit-4-harmonices-liber-ii-notes:
.. _hm-liber-ii-def-notes:

Definitions: Historical & Mathematical Commentary
=================================================

Why Local Diophantine Solutions Fail Globally
---------------------------------------------

A classic trap in elementary geometry is to assume that any set of regular polygons whose interior angles sum to $360^\circ$ tiles the plane uniformly. Solving $\sum (n_i - 2)/(2n_i) = 1$ yields **17** unordered multisets (and **21** cyclic vertex necklaces), yet **10** of those cyclic necklaces self-destruct after one or two steps!

Consider Kepler's counterexample `5.5.10` ($108^\circ + 108^\circ + 144^\circ = 360^\circ$): around any 5-sided pentagon, the polygons sharing its five edges would have to alternate `5, 10, 5, 10, ?`—an **odd** cycle of length $5$ cannot alternate two distinct symbols! Similarly, `3.7.42`, `3.8.24`, `3.9.18`, `3.10.15`, and `3.4.3.12` force neighbor collisions. In ``geometor.kepler.harmonices_geometry._is_globally_extendable_vertex``, encoding Kepler's exact odd-cycle walk condition eliminates all false local candidates automatically.
