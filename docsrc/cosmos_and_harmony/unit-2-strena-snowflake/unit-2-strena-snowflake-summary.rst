.. _unit-2-strena-snowflake-summary:

Unit II · Executive Geometric Summary
=====================================

Core Discoveries of *Strena seu de Nive Sexangula* (1611)
---------------------------------------------------------

1. **Birth of Mathematical Crystallography**: Prompted by six-cornered snow crystals falling on his coat on the Prague bridge, :person:`Kepler <kepler>` formulated the foundational principle of structural crystallography—macroscopic symmetry reflects discrete geometric packing of microscopic elementary globules.
2. **Discovery of the Two Isohedral Rhombic Zonohedra**: Extending :person:`Pappus's <pappus>` planar honeycomb analysis into three dimensions via the trihedral rhombic keel of opposing bee cells, Kepler discovered both vertex-dual Catalanesque rhombic polyhedra:

.. list-table:: Kepler's Two Isohedral Rhombic Polyhedra (``geometor.kepler.strena_packing``)
   :header-rows: 1
   :widths: 24 14 18 18 26

   * - Polyhedron
     - $F / V / E$
     - Diagonal Ratio
     - Dihedral Angle
     - Dual / Space-Filling Property
   * - **Rhombic Dodecahedron** (*Dodecaedron Rhombicum*)
     - $12 / 14 / 24$
     - $\sqrt{2} : 1$ ($Q = 2$)
     - $120^\circ$ ($\cos\theta = -\frac{1}{2}$)
     - Dual of Cuboctahedron; **3D Voronoi space-filler** ($3 \times 120^\circ = 360^\circ$)
   * - **Rhombic Triacontahedron** (*Triacontaedron Rhombicum*)
     - $30 / 32 / 60$
     - $\phi : 1$ ($Q = \phi + 1$)
     - $144^\circ$ ($\cos\theta = -\frac{\phi}{2}$)
     - Dual of Icosidodecahedron; golden icosahedral zonohedron

3. **The Kepler Sphere-Packing Conjecture**: Distinguishing simple cubic packing (kissing number $6$, density $\frac{\pi}{6} \approx 0.52360$) from face-centered cubic / hexagonal pyramidal close-packing (kissing number $12$, tetrahedral layer height $\sqrt{2/3}\,d$), Kepler asserted maximal packing density:

   $$\eta_{\text{FCC/HCP}} = \frac{\pi}{3\sqrt{2}} = \frac{\pi}{\sqrt{18}} \approx 0.74048, \qquad \frac{\eta_{\text{FCC/HCP}}}{\eta_{\text{cubic}}} = \sqrt{2},$$

   and showed that uniform isotropic compression transforms close-packed spheres into space-filling **Rhombic Dodecahedra** (the exact Voronoi cell of the $A_3 \cong D_3$ FCC lattice).
4. **Botanical Pentamery & Fibonacci Convergence to $\phi$**: Contrasting inanimate sixfold ice crystals with living five-petaled blossoms, Kepler connected Euclid's self-propagating :term:`Divine Section <sectio-divina>` ($1 : \phi = \phi : (1 + \phi)$) to the integer recurrence $F_{n+1} = F_n + F_{n-1}$ ($1, 1, 2, 3, 5, 8, 13, 21\dots$), observing both monotone rational convergence $F_{n+1}/F_n \to \phi$ and the alternating overshoot/undershoot captured by Cassini's identity $F_{n+1}F_{n-1} - F_n^2 = (-1)^n$.
