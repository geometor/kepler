.. _unit-1-mysterium-cosmographicum-notes:

Unit I · Historical & Mathematical Commentary
=============================================

1. From Metaphysical Archetype to Physical Astronomy (1596 $\to$ 1621)
----------------------------------------------------------------------

Published at Tübingen in 1596 under the editorial care of :person:`Michael Mästlin <maestlin>`—who appended :person:`Georg Joachim Rheticus's <rheticus>` *Narratio Prima* (:cite:`1540 <rheticus:1540>`) and computed independent Copernican orbital tables—*Mysterium Cosmographicum* was the **first avowedly Copernican treatise published since 1543**. More profoundly, Chapter XX introduced a revolutionary physical hypothesis: because planetary periods lengthen more rapidly than circumference alone as distance from the Sun increases, a **motivating soul or physical force (*anima motrix* / *virtus*)** emanates from the central Sun and weakens with distance. Sending copies to :person:`Galileo Galilei <galileo>` and :person:`Tycho Brahe <brahe>` in 1597 brought Kepler to Prague in 1600, where Tycho's Mars observations forced him from eccentric circles to focal ellipses (*Astronomia Nova*, :cite:`1609 <kepler:1609:an>`).

When Kepler issued the second edition at Frankfurt in 1621 (*cum notis authoris*, :cite:`1621 <kepler:1621:mc2>`), he kept every word of the 1596 text intact while adding dense scholarly endnotes showing where youthful approximations had matured into exact physical and harmonic laws.

2. Exact Algebraic Proof of Polar-Duality Sphere Equality
---------------------------------------------------------

Why do the **Dodecahedron** ($\{5, 3\}$, 12 pentagonal faces, 20 vertices) and **Icosahedron** ($\{3, 5\}$, 20 triangular faces, 12 vertices) possess the exact same insphere-to-circumsphere ratio? Let any regular polyhedron $\{p, q\}$ have edge half-angle $\alpha$, face-center-to-edge-midpoint angle $\beta$, and vertex-to-face-center angle $\gamma$ on the unit sphere. In the right spherical triangle formed by a vertex $V$, an adjacent edge midpoint $E$, and a face center $F$:

$$\frac{r_{\text{in}}}{R_{\text{out}}} = \cos\gamma = \cot\frac{\pi}{p}\,\cot\frac{\pi}{q}.$$

Swapping $p \leftrightarrow q$ leaves the product $\cot(\pi/p)\cot(\pi/q)$ strictly invariant! In ``geometor.kepler.mysterium_spheres.derive_platonic_sphere_ratios``, we verify this without trigonometry directly over $\mathbb{Q}(\phi)$:

* For the **Dodecahedron** on $Q_{\text{out}} = 3$, the pentagonal face in plane $x + \phi z = \phi + 1$ has centroid $G = \frac{1}{5}(\phi + 2,\, 0,\, 3\phi + 1)$ with $Q_{\text{in}} = \frac{4\phi + 3}{5}$, giving $\frac{Q_{\text{in}}}{Q_{\text{out}}} = \frac{4\phi + 3}{15} = \frac{5 + 2\sqrt{5}}{15}$.
* For the **Icosahedron** on $Q_{\text{out}} = \phi + 2$, the triangular face $(0, 1, \phi), (0, -1, \phi), (\phi, 0, 1)$ has centroid $G' = \frac{1}{3}(\phi,\, 0,\, 2\phi + 1)$ with $Q_{\text{in}} = \frac{3\phi + 2}{3}$. Multiplying numerator and denominator of $\frac{3\phi + 2}{3(\phi + 2)}$ by $(3 - \phi)$—using $(\phi + 2)(3 - \phi) = 5$ and $\phi^2 = \phi + 1$—reduces identically to $\frac{4\phi + 3}{15}$!

3. Kepler's Octahedral Square Variant for Mercury
-------------------------------------------------

In *Mysterium* Cap. XIV, Kepler noticed that while the Octahedron's insphere gives $r_{\text{in}}/R_{\text{out}} = 1/\sqrt{3} \approx 0.5774$, the circle inscribed in the **equatorial square** of four octahedron vertices gives $r_{\text{eq}}/R_{\text{out}} = 1/\sqrt{2} \approx 0.7071$, closer to Mercury's *aphelion* sphere when Venus's eccentric shell thickness is included—an early clue that polyhedral geometry alone required harmonic tuning of orbital eccentricities.
