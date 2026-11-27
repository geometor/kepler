:type: notes
:layout: book
:canonical_id: Cap. XIII
:order: 14
:folio: mysterium_cosmographicum:0054

.. _mc-cap_13-notes:

Chapter XIII: Notes & Provenance
================================

Transcription & Provenance
--------------------------

* **Primary Witness**: Johannes Kepler, *Prodromus Dissertationum Cosmographicarum, continens Mysterium Cosmographicum* (:cite:`Tübingen, 1596, Caput XIII, pp. 44–47 <kepler:1596:mc>`; *Editio altera cum notis authoris*, :cite:`Frankfurt, 1621 <kepler:1621:mc2>`; :cite:`ed. Ch. Frisch, Vol. I, pp. 143–146 <frisch:1858:v1>`).
* **Folio Scans**: Transcribed directly from 300-DPI scans ``mysterium_cosmographicum:0054`` (p. 44, right-triangle diagram ``O-H-I-G-L-M``), ``0055`` (p. 45), ``0056`` (p. 46), and ``0057`` (p. 47, Tetrahedron diagram ``N-G-O-I-H-M`` and 1000-part ratio table).
* **English Track**: Fresh first-person translation directly from the 1596 Latin text.
* **Key Figures**: On p. 47, Kepler adds the parenthetical note ``707. quadrato Octaedri inscripti circuli`` (:math:`1000/\sqrt{2} \approx 707.11`), which becomes crucial in Chapter XV for Mercury's eccentric orb inscribed in the equatorial square of the Octahedron rather than its triangular face-insphere.

Exact Algebraic Proof of Polar-Duality Sphere Equality
------------------------------------------------------

Why do the **Dodecahedron** (:math:`\{5, 3\}`, 12 pentagonal faces, 20 vertices) and **Icosahedron** (:math:`\{3, 5\}`, 20 triangular faces, 12 vertices) possess the exact same insphere-to-circumsphere ratio? In the right spherical triangle formed by a vertex :math:`V`, an adjacent edge midpoint :math:`E`, and a face center :math:`F`:

.. math::

   \frac{r_{\text{in}}}{R_{\text{out}}} = \cos\gamma = \cot\frac{\pi}{p}\,\cot\frac{\pi}{q}.

Swapping :math:`p \leftrightarrow q` leaves the product :math:`\cot(\pi/p)\cot(\pi/q)` strictly invariant. In ``geometor.kepler.mysterium_spheres.derive_platonic_sphere_ratios``, we verify this without trigonometry directly over :math:`\mathbb{Q}(\phi)`:

* For the **Dodecahedron** on :math:`Q_{\text{out}} = 3`, the pentagonal face in plane :math:`x + \phi z = \phi + 1` has centroid :math:`G = \frac{1}{5}(\phi + 2,\, 0,\, 3\phi + 1)` with :math:`Q_{\text{in}} = \frac{4\phi + 3}{5}`, giving :math:`\frac{Q_{\text{in}}}{Q_{\text{out}}} = \frac{4\phi + 3}{15} = \frac{5 + 2\sqrt{5}}{15}`.
* For the **Icosahedron** on :math:`Q_{\text{out}} = \phi + 2`, the triangular face :math:`(0, 1, \phi), (0, -1, \phi), (\phi, 0, 1)` has centroid :math:`G' = \frac{1}{3}(\phi,\, 0,\, 2\phi + 1)` with :math:`Q_{\text{in}} = \frac{3\phi + 2}{3}`. Multiplying numerator and denominator of :math:`\frac{3\phi + 2}{3(\phi + 2)}` by :math:`(3 - \phi)`—using :math:`(\phi + 2)(3 - \phi) = 5` and :math:`\phi^2 = \phi + 1`—reduces identically to :math:`\frac{4\phi + 3}{15}`.
