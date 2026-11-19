:layout: book
:canonical_id: I.Prop. XLV
:order: 4
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

Transcription & Provenance
--------------------------

* **Latin Witness**: *Public-domain Neo-Latin text from Ioannis Keppleri Harmonices Mundi Liber I, Propositio XLV* (:cite:`Linz, 1619, pp. 41–46 <kepler:1619:hm>`; :cite:`ed. Ch. Frisch, Vol. V, pp. 119–125 <frisch:1864:v5>`).
* **English Track**: *Original GEOMETOR English translation from Johannes Kepler's Harmonices Mundi Liber I, Propositio XLV* (:cite:`Linz, 1619, pp. 41–46 <kepler:1619:hm>`; :cite:`Frisch V, pp. 119–125 <frisch:1864:v5>`).
* **Folio Scan**: Verified 300-DPI scan ``harmonices_mundi:0050`` (p. 32).
