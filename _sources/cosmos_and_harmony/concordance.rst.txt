.. _kepler-concordance:

Cross-Corpus Geometric Concordance
==================================

Bidirectional concordance mapping propositions and constructions in :person:`Johannes Kepler's <kepler>` *Mysterium Cosmographicum* (1596/1621), *Strena seu de Nive Sexangula* (1611), and *Harmonices Mundi* (1619) to sister repositories across the **GEOMETOR** canon and exact symbolic verifiers in ``geometor.kepler``.

.. list-table:: Kepler Cross-Corpus Concordance
   :header-rows: 1
   :widths: 22 30 24 24

   * - Kepler Locus
     - Geometric Proposition / Invariant
     - Sister GEOMETOR Canon
     - Symbolic Verifier (``geometor.kepler``)
   * - *Mysterium* Praefatio (1596, pp. 6–10)
     - July 19, 1595 Graz Great-Conjunction equilateral triangle ($r_{\text{in}} / R_{\text{out}} = 1/2$, $Q = 1/4$) & square ($Q = 1/2$)
     - ``euclid`` / ``elements`` IV.2–5, XIII.12
     - ``mysterium_spheres.construct_mysterium_planar_nesting``
   * - *Mysterium* Cap. II & XIV (1596, pp. 22–26, 46–49)
     - Curved vs. Straight (:person:`Cusanus <cusanus>`); 5 Platonic solids nested between 6 Copernican orbs (*Terra* = 1)
     - ``euclid`` / ``elements`` XIII.13–18; ``proclus`` Prologue
     - ``mysterium_spheres.compute_nested_planetary_radii``
   * - *Mysterium* Cap. XII–XIII (1596, pp. 41–45)
     - Two Great Treasures (:just:`I.47` & :just:`II.11`); polar-duality equality ($Q_{\text{Cube}} = Q_{\text{Oct}} = \frac{1}{3}$, $Q_{\text{Dod}} = Q_{\text{Ico}} = \frac{5+2\sqrt{5}}{15}$)
     - ``divine`` / ``pacioli`` / ``wildberger`` quadrance
     - ``mysterium_spheres.verify_polar_duality_ratios``
   * - *Epistola ad Mästlinum* (Oct 1597; Frisch I, p. 377)
     - **Kepler Right Triangle** $(1, \sqrt{\phi}, \phi)$ with $Q_a : Q_b : Q_c = 1 : \phi : \phi^2$ and Mästlin's $1/\phi \approx 0.6180340$
     - ``model`` ``get_kepler_field`` ($\mathbb{Q}(\sqrt{\phi})$); ``elements`` II.11, VI.13
     - ``harmonices_geometry.construct_kepler_right_triangle``
   * - *Strena* §§1–9 (1611, pp. 3–11)
     - Sixfold snow crystals, bee honeycomb trihedra, **Rhombic Dodecahedron** ($\sqrt{2}:1$, $120^\circ$) & **Rhombic Triacontahedron** ($\phi:1$, $144^\circ$)
     - ``pappus`` *Synagoge* V.1–3; ``pacioli`` rhombic solids
     - ``strena_packing.analyze_rhombic_dodecahedron`` & ``analyze_rhombic_triacontahedron``
   * - *Strena* §§10–14 (1611, pp. 11–15)
     - Planar 7-circle rosette (kissing 6) & 3D FCC/HCP **Kepler Sphere-Packing Conjecture** (kissing 12, $\frac{\pi}{3\sqrt{2}}$)
     - ``fundamentals`` 6-circle rosette; ``phyllotaxis`` packing
     - ``strena_packing.verify_kepler_sphere_packing`` & ``construct_hexagonal_rosette``
   * - *Strena* §§15–19 (1611, pp. 15–19)
     - Pentamerous blossoms & self-propagating Fibonacci recurrence $1, 1, 2, 3, 5, 8, 13, 21 \to \phi$ (Cassini $(-1)^n$)
     - ``phyllotaxis`` parastichy lattices; ``divine``
     - ``strena_packing.compute_fibonacci_phyllotaxis``
   * - *Harmonices Mundi* I, Defs./Props. I–XLIV
     - Refutation of :person:`Ramus <ramus>` on Book X; eight degrees of :term:`scibilitas <scibilitas>` for constructible $n$-gons ($3,4,5,6,8,10,12,15,16$)
     - ``euclid`` IV.10–16, X, XIII.1–11; ``proclus``; ``hoenen``
     - ``harmonices_geometry.classify_polygon_scibilitas``
   * - *Harmonices Mundi* I, Props. XLV–L
     - :term:`Inscibilitas <inscibilitas>` of the **Regular Heptagon** ($x^3 + x^2 - 2x - 1 = 0$) & :person:`Bürgi's <buergi>` cossic sextic ($y^6 - 7y^4 + 14y^2 - 7 = 0$)
     - ``hilbert`` quadratic field towers
     - ``harmonices_geometry.verify_heptagon_cubic_obstruction``
   * - *Harmonices Mundi* II, Props. I–XXVIII
     - Complete **11 uniform Archimedean planar tilings**, star congruence `Figure Aa`, **13 Archimedean solids**, & stellated dodecahedra
     - ``pappus`` *Synagoge* V.19; ``divine`` star pentagram
     - ``harmonices_geometry.enumerate_archimedean_planar_tilings``
   * - *Harmonices Mundi* V, Cap. I, III–IX
     - Aphelion/perihelion consonances ($4:5, 5:6, 2:3, 15:16, 24:25, 5:12$) & **Kepler's Third Law** $(T_1/T_2)^2 = (a_1/a_2)^3$
     - ``ptolemy`` *Harmonics*; ``wildberger`` rational laws
     - ``harmonices_geometry.verify_kepler_third_law``
