:layout: book
:canonical_id: Cap. XIII
:order: 14
:folio: mysterium_cosmographicum:0054
:tracks: Latin: cap_13-la | English: cap_13-en | Summary: cap_13-summary | Notes: cap_13-notes

.. _mc-cap_13-notes:

Chapter XIII: Notes & Provenance
================================

Transcription & Provenance
--------------------------

* **Primary Witness**: Johannes Kepler, *Prodromus Dissertationum Cosmographicarum, continens Mysterium Cosmographicum* (:cite:`Tübingen, 1596, Caput XIII, p. 44 ff. <kepler:1596:mc>`; *Editio altera cum notis authoris*, :cite:`Frankfurt, 1621 <kepler:1621:mc2>`; :cite:`ed. Ch. Frisch, Vol. I, pp. 141–145 <frisch:1858:v1>`).
* **Folio Scan**: Transcribed directly from 300-DPI scan ``mysterium_cosmographicum:0054`` (p. 44, featuring Kepler's in-text right-triangle sphere diagram ``O-H-I-G-L-M``).
* **English Track**: Original GEOMETOR English translation.

Exact Algebraic Proof of Polar-Duality Sphere Equality
------------------------------------------------------

Why do the **Dodecahedron** ($\{5, 3\}$, 12 pentagonal faces, 20 vertices) and **Icosahedron** ($\{3, 5\}$, 20 triangular faces, 12 vertices) possess the exact same insphere-to-circumsphere ratio? In the right spherical triangle formed by a vertex $V$, an adjacent edge midpoint $E$, and a face center $F$:

$$\frac{r_{\text{in}}}{R_{\text{out}}} = \cos\gamma = \cot\frac{\pi}{p}\,\cot\frac{\pi}{q}.$$

Swapping $p \leftrightarrow q$ leaves the product $\cot(\pi/p)\cot(\pi/q)$ strictly invariant. In ``geometor.kepler.mysterium_spheres.derive_platonic_sphere_ratios``, we verify this without trigonometry directly over $\mathbb{Q}(\phi)$:

* For the **Dodecahedron** on $Q_{\text{out}} = 3$, the pentagonal face in plane $x + \phi z = \phi + 1$ has centroid $G = \frac{1}{5}(\phi + 2,\, 0,\, 3\phi + 1)$ with $Q_{\text{in}} = \frac{4\phi + 3}{5}$, giving $\frac{Q_{\text{in}}}{Q_{\text{out}}} = \frac{4\phi + 3}{15} = \frac{5 + 2\sqrt{5}}{15}$.
* For the **Icosahedron** on $Q_{\text{out}} = \phi + 2$, the triangular face $(0, 1, \phi), (0, -1, \phi), (\phi, 0, 1)$ has centroid $G' = \frac{1}{3}(\phi,\, 0,\, 2\phi + 1)$ with $Q_{\text{in}} = \frac{3\phi + 2}{3}$. Multiplying numerator and denominator of $\frac{3\phi + 2}{3(\phi + 2)}$ by $(3 - \phi)$—using $(\phi + 2)(3 - \phi) = 5$ and $\phi^2 = \phi + 1$—reduces identically to $\frac{4\phi + 3}{15}$.
