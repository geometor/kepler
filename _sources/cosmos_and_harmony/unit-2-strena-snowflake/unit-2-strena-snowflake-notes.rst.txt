.. _unit-2-strena-snowflake-notes:

Unit II · Historical & Mathematical Commentary
==============================================

1. Literary Paradox (*Nix* / *Nihil*) and Morphological Method
--------------------------------------------------------------

Composed at Imperial Prague in late 1610 as a playful humanist gift for Privy Councillor :person:`J. M. Wackher von Wackenfels <wackher>`, *Strena* stands in the Renaissance tradition of paradoxical encomia (*Praise of Nothing*). Yet within twenty-four quarto pages Kepler inaugurated **three** modern disciplines simultaneously:

* **Geometric Crystallography & Lattice Theory** (later developed by Steno, Hooke, Huygens, Haüy, and Bravais);
* **Discrete & Computational Geometry** (sphere packing, kissing numbers, and 3D Voronoi/Dirichlet tessellations, :cite:`Thompson 1942 <thompson:1942>`);
* **Mathematical Phyllotaxis** (linking Fibonacci parastichy numbers to the golden section, developed across ``geometor/phyllotaxis``).

2. Equivalence of Kepler's Square-Pyramidal and Hexagonal Packings
------------------------------------------------------------------

A remarkable geometric subtlety appears in *Strena* §§11–12: Kepler describes **two** ways of stacking horizontal sphere layers so that each interior sphere touches twelve neighbors:

1. Start with a **square** grid in the horizontal $(x, y)$ plane and seat each sphere of the next layer into the fourfold hollow of four touching spheres below (cannonball pyramid).
2. Start with a **triangular-hexagonal** grid (`fig03`) and seat each sphere of the next layer into a threefold hollow ($A \to B \to C \to A\dots$ or $A \to B \to A\dots$).

In fact, the square-based cannonball pyramid **is** the **face-centered cubic (FCC)** lattice viewed along its `[001]` fourfold axis, whose `[111]` diagonal planes are hexagonal layers in `ABCABC` stacking! Both `ABCABC` (FCC, Voronoi cell = **Rhombic Dodecahedron**) and `ABAB` (HCP, Voronoi cell = **Trapezo-Rhombic Dodecahedron**) achieve the exact same packing fraction $\frac{\pi}{3\sqrt{2}}$. After standing open for **387 years**, Kepler's optimality claim was proved by :person:`Thomas C. Hales <hales>` in 1998 (:cite:`published 2005 <hales:2005>`) and formally verified by machine in the Flyspeck theorem-proving project (2014).

3. The Maraldi Angle of the Honeycomb Rhombus
---------------------------------------------

In `geometor.kepler.strena_packing.analyze_rhombic_dodecahedron`, each face of the Rhombic Dodecahedron has half-diagonals $\sqrt{2}$ and $1$ and edge length $\sqrt{3}$. By the law of cosines on the rhombus triangles:

$$\cos\alpha_{\text{obtuse}} = \frac{3 + 3 - 8}{2 \cdot 3} = -\frac{1}{3} \implies \alpha_{\text{obtuse}} = \arccos\!\left(-\frac{1}{3}\right) \approx 109^\circ 28' 16'',$$

the celebrated **Maraldi tetrahedral angle** (rediscovered experimentally in beehives by Giacomo Filippo Maraldi in 1712), minimizing wax surface area for a given hexagonal cell volume!
