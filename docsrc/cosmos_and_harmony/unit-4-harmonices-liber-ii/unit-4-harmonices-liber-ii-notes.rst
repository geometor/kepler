.. _unit-4-harmonices-liber-ii-notes:

Unit IV · Historical & Mathematical Commentary
==============================================

1. Why Local Diophantine Solutions Fail Globally
------------------------------------------------

A classic trap in elementary geometry is to assume that any set of regular polygons whose interior angles sum to $360^\circ$ tiles the plane uniformly. Solving $\sum (n_i - 2)/(2n_i) = 1$ yields **17** unordered multisets (and **21** cyclic vertex necklaces), yet **10** of those cyclic necklaces self-destruct after one or two steps!

Consider Kepler's counterexample `5.5.10` ($108^\circ + 108^\circ + 144^\circ = 360^\circ$): around any 5-sided pentagon, the polygons sharing its five edges would have to alternate `5, 10, 5, 10, ?`—an **odd** cycle of length $5$ cannot alternate two distinct symbols! Similarly, `3.7.42`, `3.8.24`, `3.9.18`, `3.10.15`, and `3.4.3.12` force neighbor collisions. In ``geometor.kepler.harmonices_geometry._is_globally_extendable_vertex``, encoding Kepler's exact odd-cycle walk condition eliminates all false local candidates automatically.

2. From Kepler's `Figure Aa` (1619) to Penrose Tilings (1974) & Quasicrystals
-----------------------------------------------------------------------------

In *Harmonices Mundi* Book II (pp. 59–61, engraved `Figura Aa`), after noting that `5.5.10` fails as a uniform tiling, :person:`Kepler <kepler>` refused to abandon fivefold symmetry. Allowing decagons, fused twin-pentagons, regular pentagons, and star pentagrams $\{5/2\}$, he drew an extraordinary patch with concentric fivefold inflation symmetry and remarked cryptically that *"if you truly wish to continue it outward, certain irregularities must be mixed in, with two decagons joined together..."*

In 1974, :person:`Sir Roger Penrose <penrose>` (:cite:`1974 <penrose:1974>`) proved that Kepler's exact `Aa` prototiles—a regular pentagon, a five-pointed star, a three-pointed "boat" (partial star), and a "diamond" rhomb, together with decagons—tile the entire infinite Euclidean plane **aperiodically** through golden-ratio deflation ($\phi : 1$)! Eight years later (1982), Dan Shechtman observed sharp tenfold electron-diffraction Bragg peaks in rapidly cooled Al–Mn alloys—physical **icosahedral quasicrystals** built on the three-dimensional cousin of Kepler's `Figure Aa`, the **Golden Rhombic Triacontahedron**!

3. Kepler's Enduring Polyhedral Nomenclature
--------------------------------------------

Every modern student of geometry speaks Kepler's Latin daily: *cuboctahedron*, *icosidodecahedron*, *rhombic dodecahedron*, *rhombic triacontahedron*, *truncation*, and *snub* (*simus*—"snub-nosed", for the chiral `3.3.3.3.4` and `3.3.3.3.5` solids) were all coined or standardized in *Harmonices Mundi* Book II (:cite:`Coxeter 1973 <coxeter:1973>`).
