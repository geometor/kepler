:layout: book
:canonical_id: § 3
:order: 3
:tracks: Latin: sec_03-la | English: sec_03-en | Summary: sec_03-summary | Notes: sec_03-notes

.. _strena-sec_03-notes:

Section 3: Historical & Mathematical Commentary
===============================================

Equivalence of Kepler's Square-Pyramidal and Hexagonal Packings
---------------------------------------------------------------

A remarkable geometric subtlety appears in *Strena* §§11–12: Kepler describes **two** ways of stacking horizontal sphere layers so that each interior sphere touches twelve neighbors:

1. Start with a **square** grid in the horizontal $(x, y)$ plane and seat each sphere of the next layer into the fourfold hollow of four touching spheres below (cannonball pyramid).
2. Start with a **triangular-hexagonal** grid (`fig03`) and seat each sphere of the next layer into a threefold hollow ($A \to B \to C \to A\dots$ or $A \to B \to A\dots$).

In fact, the square-based cannonball pyramid **is** the **face-centered cubic (FCC)** lattice viewed along its `[001]` fourfold axis, whose `[111]` diagonal planes are hexagonal layers in `ABCABC` stacking! Both `ABCABC` (FCC, Voronoi cell = **Rhombic Dodecahedron**) and `ABAB` (HCP, Voronoi cell = **Trapezo-Rhombic Dodecahedron**) achieve the exact same packing fraction $\frac{\pi}{3\sqrt{2}}$. After standing open for **387 years**, Kepler's optimality claim was proved by :person:`Thomas C. Hales <hales>` in 1998 (:cite:`published 2005 <hales:2005>`) and formally verified by machine in the Flyspeck theorem-proving project (2014).
