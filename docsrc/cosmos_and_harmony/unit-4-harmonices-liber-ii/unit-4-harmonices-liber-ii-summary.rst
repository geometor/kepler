.. _unit-4-harmonices-liber-ii-summary:

Unit IV · Executive Geometric Summary
=====================================

Core Architectonic Theorems (*Harmonices Mundi* Book II, 1619)
--------------------------------------------------------------

1. **First Complete Classification of the 11 Uniform Planar Tilings**: Solving the rational interior-angle equation

   $$\sum_{i=1}^{k} \frac{n_i - 2}{2 n_i} = 1 \qquad (3 \le k \le 6,\; n_i \ge 3)$$

   and filtering local solutions by global edge-alternation consistency around odd-sided faces, ``geometor.kepler.harmonices_geometry.enumerate_archimedean_planar_tilings`` reproduces :person:`Kepler's <kepler>` exact **11 uniform vertex-transitive planar tessellations**:

.. list-table:: The 11 Uniform Archimedean Planar Tilings (*Book II*)
   :header-rows: 1
   :widths: 18 14 34 34

   * - Vertex Symbol
     - Valence $k$
     - Interior Angles ($= 360^\circ$)
     - Symmetry & Classification
   * - ``3.3.3.3.3.3``
     - $6$
     - $60^\circ \times 6$
     - Pure regular triangular lattice ($p6m$)
   * - ``4.4.4.4``
     - $4$
     - $90^\circ \times 4$
     - Pure regular square lattice ($p4m$)
   * - ``6.6.6``
     - $3$
     - $120^\circ \times 3$
     - Pure regular hexagonal honeycomb ($p6m$)
   * - ``3.12.12``
     - $3$
     - $60^\circ + 150^\circ + 150^\circ$
     - Truncated hexagonal ($p6m$)
   * - ``4.6.12``
     - $3$
     - $90^\circ + 120^\circ + 150^\circ$
     - Great rhombitrihexagonal ($p6m$)
   * - ``4.8.8``
     - $3$
     - $90^\circ + 135^\circ + 135^\circ$
     - Truncated square ($p4m$)
   * - ``3.4.6.4``
     - $4$
     - $60^\circ + 90^\circ + 120^\circ + 90^\circ$
     - Small rhombitrihexagonal ($p6m$)
   * - ``3.6.3.6``
     - $4$
     - $60^\circ + 120^\circ + 60^\circ + 120^\circ$
     - Trihexagonal / Kagome ($p6m$)
   * - ``3.3.3.3.6``
     - $5$
     - $60^\circ \times 4 + 120^\circ$
     - **Chiral** snub hexagonal ($p6$, enantiomorphic)
   * - ``3.3.3.4.4``
     - $5$
     - $60^\circ \times 3 + 90^\circ \times 2$
     - Elongated triangular ($cmm$)
   * - ``3.3.4.3.4``
     - $5$
     - $60^\circ + 60^\circ + 90^\circ + 60^\circ + 90^\circ$
     - Snub square ($p4g$)

2. **Kepler–Poinsot Star Polyhedra & Non-Periodic Tiling Precursor**: Book II introduces the **Small Stellated Dodecahedron** $\{5/2, 5\}$ and **Great Stellated Dodecahedron** $\{5/2, 3\}$ (:cite:`Poinsot 1810 <poinsot:1810>`) alongside the **Figure Aa** pentagram–decagon tiling that directly inspired :person:`Roger Penrose's <penrose>` aperiodic P1 tiling (:cite:`1974 <penrose:1974>`).
3. **Completeness of the 13 Archimedean Convex Solids**: By separating prisms ($4.4.n$) and antiprisms ($3.3.3.n$) into infinite families, Kepler gave the first complete modern proof that exactly **13** convex vertex-transitive semi-regular solids exist.
