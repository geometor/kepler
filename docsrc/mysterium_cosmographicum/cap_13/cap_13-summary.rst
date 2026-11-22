:layout: book
:canonical_id: Cap. XIII
:order: 14
:folio: mysterium_cosmographicum:0054
:tracks: Latin: cap_13-la | English: cap_13-en | Summary: cap_13-summary | Notes: cap_13-notes

.. _mc-cap_13-summary:

Chapter XIII: Summary
=====================

Polar-Duality Insphere & Circumsphere Ratios
--------------------------------------------

Kepler computes the exact insphere-to-circumsphere ratios for all five Platonic solids normalized to a circumradius $R_{\text{out}} = 1000$, using the Pythagorean right triangle $HO^2 - HI^2 = OI^2$ (:just:`I.47`) and Euclidean edge constructions from Book XIII (and Candalla's Book XIV–XV additions). Dual regular solids exchange vertices ($V$) and faces ($F$) while preserving edge count ($E$) and exact insphere-to-circumsphere quadrance ratios:

.. list-table:: Exact Platonic Sphere Ratios (``geometor.kepler.mysterium_spheres``)
   :header-rows: 1
   :widths: 18 12 18 26 26

   * - Solid
     - Schläfli
     - Planetary Pair
     - Exact Quadrance Ratio $Q_{\text{in}} / Q_{\text{out}}$
     - Exact Radius Ratio $r_{\text{in}} / R_{\text{out}}$ (Kepler 1596: $r_{\text{in}}$ for $R=1000$)
   * - **Cube**
     - $\{4, 3\}$
     - Saturn $\to$ Jupiter
     - $\frac{1}{3}$
     - $\frac{\sqrt{3}}{3} \approx 0.57735$ (``577``)
   * - **Tetrahedron**
     - $\{3, 3\}$
     - Jupiter $\to$ Mars
     - $\frac{1}{9}$
     - $\frac{1}{3} \approx 0.33333$ (``333``)
   * - **Dodecahedron**
     - $\{5, 3\}$
     - Mars $\to$ Earth
     - $\frac{5 + 2\sqrt{5}}{15} = \frac{4\phi + 3}{15}$
     - $\sqrt{\frac{5 + 2\sqrt{5}}{15}} \approx 0.79465$ (``795``)
   * - **Icosahedron**
     - $\{3, 5\}$
     - Earth $\to$ Venus
     - $\frac{5 + 2\sqrt{5}}{15} = \frac{4\phi + 3}{15}$
     - $\sqrt{\frac{5 + 2\sqrt{5}}{15}} \approx 0.79465$ (``795``)
   * - **Octahedron**
     - $\{3, 4\}$
     - Venus $\to$ Mercury
     - $\frac{1}{3}$
     - $\frac{\sqrt{3}}{3} \approx 0.57735$ (``577``; ``707`` for square-section circle)
