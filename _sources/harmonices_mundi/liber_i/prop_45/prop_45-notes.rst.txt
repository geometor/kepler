:layout: book
:canonical_id: I.Prop. XLV
:order: 28
:folio: harmonices_mundi:0050
:tracks: Latin: prop_45-la | English: prop_45-en | Summary: prop_45-summary | Notes: prop_45-notes

.. _hm-liber-i-prop_45-notes:

Proposition XLV: Notes & Provenance
===================================

Derivation of Bürgi's Chord Equation in SymPy
---------------------------------------------

Let $\zeta = e^{2\pi i / 7}$ satisfy $1 + \zeta + \zeta^2 + \zeta^3 + \zeta^4 + \zeta^5 + \zeta^6 = 0$. Dividing by $\zeta^3$ and setting $x = \zeta + \zeta^{-1} = 2\cos(2\pi/7)$:

$$\left(x^3 - 3x\right) + \left(x^2 - 2\right) + x + 1 = 0 \implies x^3 + x^2 - 2x - 1 = 0.$$

Since the heptagon side in a unit circle is $y = 2\sin(\pi/7)$ with $x = 2\cos(2\pi/7) = 2 - y^2$? Wait: $2\cos(2\pi/7) = 2\left(1 - 2\sin^2\frac{\pi}{7}\right) = 2 - y^2$? Almost: $y = 2\sin(\pi/7) \implies y^2 = 4\sin^2(\pi/7) = 2 - 2\cos(2\pi/7) = 2 - x \implies x = 2 - y^2$! Substitute $x = 2 - u$ ($u = y^2$) into $x^3 + x^2 - 2x - 1 = 0$:

$$(2 - u)^3 + (2 - u)^2 - 2(2 - u) - 1 = -u^3 + 7u^2 - 14u + 7 = 0 \implies y^6 - 7y^4 + 14y^2 - 7 = 0,$$

recovering **Jost Bürgi's exact Cossic sextic** verified in ``geometor.kepler.harmonices_geometry.verify_heptagon_cubic_obstruction``!

Modern Algebraic & Constructibility Commentary
----------------------------------------------

* **Prime Polygons Beyond Five**: Kepler groups together all prime-sided regular polygons beyond the pentagon (7, 11, 13, 17, 19, …) and multiples of nine as non-constructible by Euclidean compass and straightedge. Two centuries later, Gauss (1796) discovered that Fermat primes such as $17$ ($2^{2^2}+1$) *are* constructible, while Wantzel (1837) proved that primes not of Fermat form—beginning with $7$, $11$, $13$, and $19$, as well as $9$—cannot be constructed, confirming Kepler's thesis for the heptagon and nonagon.
* **Pentagon vs. Heptagon**: In the pentagon only two chord species exist ($s_5$ and $d_5$), locking their ratio into the quadratic $x^2 - x - 1 = 0$ solvable by circle and straight line; in the heptagon three chord species ($s_7$, $d_7$, and the long diagonal) are governed by the irreducible cubic $x^3 + x^2 - 2x - 1 = 0$ with $x = 2\cos(2\pi/7)$, whose three real roots are Galois conjugates corresponding to the $\frac{1}{7}$, $\frac{2}{7}$, and $\frac{3}{7}$ chords.

Transcription & Provenance
--------------------------

* **Latin Witness**: *Public-domain Neo-Latin text from Ioannis Keppleri Harmonices Mundi Liber I, Propositio XLV* (:cite:`Linz, 1619, pp. 32–36 <kepler:1619:hm>`; :cite:`ed. Ch. Frisch, Vol. V <frisch:1864:v5>`).
* **English Track**: *Original GEOMETOR English translation from Johannes Kepler's Harmonices Mundi Liber I, Propositio XLV* (:cite:`Linz, 1619, pp. 32–36 <kepler:1619:hm>`; :cite:`Frisch V <frisch:1864:v5>`).
* **Folio Scan**: Verified 300-DPI scans ``harmonices_mundi:0050``–``0054`` (pp. 32–36).
