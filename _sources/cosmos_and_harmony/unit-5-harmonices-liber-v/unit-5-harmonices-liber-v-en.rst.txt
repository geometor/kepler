.. _unit-5-harmonices-liber-v-en:

Unit V · Epistola 1597 & Harmonices Mundi Liber V: Harmonia Coelestis (1619)
============================================================================

*Original GEOMETOR English translation from Johannes Kepler's Epistola ad Michaelem Mästlinum (Graz, October 1597)* (:cite:`Frisch I, p. 377 <kepler:1597:maestlin>`) *and Harmonices Mundi Liber V: De Harmonia Perfectissima Motuum Coelestium* (:cite:`Linz: Tampach/Plancus, 1619, pp. 177–255 <kepler:1619:hm>`; :cite:`Frisch V, pp. 269–329 <frisch:1864:v5>`).

1. Epistola ad Mästlinum (October 1597) — The Kepler Right Triangle
-------------------------------------------------------------------

*"If upon a straight line cut in :term:`extreme and mean ratio <sectio-divina>` one constructs a right-angled triangle out of the segments and the whole—in such a way that the hypotenuse subtending the right angle is the greater segment (or the whole), and the base is the lesser segment (or the greater)—then the square on one leg together with the square on the other composes the square on the hypotenuse, while the **three sides themselves stand in continuous geometric proportion**!"* (:person:`Kepler <kepler>` to :person:`Michael Mästlin <maestlin>`, :cite:`Graz, October 1597 <kepler:1597:maestlin>`).

Here the **Two Great Treasures of Geometry** (:person:`Pythagoras's <pythagoras>` right-triangle theorem, :cite:`Euclid I.47 <euclid:elements>`, and the :term:`Divine Section <sectio-divina>`, :cite:`Euclid II.11 & VI.30 <euclid:elements>`) fuse into a single unique figure—the :term:`Kepler Right Triangle <kepler-triangle>` :g:`OAB` (left panel below):

* **Pure Euclidean Construction over** $\mathbb{Q}(\sqrt{\phi})$: Taking the unit segment :g:`OA` ($= 1$) from :g:`O` to :g:`A`, extend the baseline leftward to :g:`W` ($-1, 0$) and rightward by the golden-section arc (:cite:`Euclid II.11 <euclid:elements>`) to :g:`P` ($\phi, 0$). Erect the Thales semicircle :g:`cThales` upon diameter :g:`WP` of length $1 + \phi = \phi^2$; by :cite:`Euclid VI.13 <euclid:elements>`, it cuts the perpendicular through :g:`O` (at right angle :g:`angAOB`) in :g:`B` at height :g:`OB` $= \sqrt{1 \cdot \phi} = \sqrt{\phi}$.
* **Geometric Progression of Sides & Quadrances**: Joining :g:`AB` completes the right triangle :g:`OAB` whose sides stand in continuous geometric proportion $1 : \sqrt{\phi} : \phi$, while their :term:`quadrances <quadrance>` satisfy

  $$Q(\text{OA}) = 1, \qquad Q(\text{OB}) = \phi, \qquad Q(\text{AB}) = 1 + \phi = \phi^2.$$

* **Self-Similar Golden Altitude**: Dropping the perpendicular altitude :g:`OH` from the right angle :g:`O` onto the hypotenuse :g:`AB` at :g:`H` divides the hypotenuse into extreme and mean ratio once again: $BH = 1$ and $HA = \phi - 1 = \phi^{-1}$—upon which :person:`Mästlin <maestlin>` computed on the margin of Kepler's letter the celebrated first decimal approximation $6180340$ for a base of $10000000$ ($1/\phi \approx 0.6180340$).

.. picture:: /_static/figures/fig09_kepler_triangle_and_third_law.svg
   :alt: Kepler Right Triangle 1597 and Harmonices Mundi Book V Planetary Ellipse and Third Law

2. Liber V, Caput I & III (Prop. VIII) — The Harmonic Third Law
---------------------------------------------------------------

In the **Fifth Book** of *Harmonices Mundi* (completed May 27, 1618; printed 1619), :person:`Kepler <kepler>` returns after twenty-two years to the **five regular solids** of *Mysterium Cosmographicum* (:cite:`1596 <kepler:1596:mc>`), armed now with :person:`Tycho Brahe's <brahe>` exact observations and his own discovery in *Astronomia Nova* (:cite:`1609 <kepler:1609:an>`) that each planetary orbit is a focal ellipse :g:`cORB` with the Sun :g:`Sol_f` at one focus, sweeping equal areas in equal times between :g:`P_per` (perihelion) and :g:`A_aph` (aphelion) along the major axis :g:`AP_axis` (semi-major axis $a$ around orbital center :g:`C_orb`).

In **Chapter III, Proposition VIII**—conceived on March 8, 1618, lost through an arithmetic slip, and recovered triumphantly on **May 15, 1618**—Kepler announces the universal law governing all orbital periods and distances (:term:`Lex Tertia <lex-tertia>`):

   *"Yet the thing is most certain and altogether exact: **the proportion that holds between the periodic times of any two planets whatsoever is precisely the sesquialterate** ($3/2$ power) **of the proportion of their mean distances**, that is, of the spheres themselves—keeping in mind, however, that the arithmetic mean between the two diameters of the elliptical oval is slightly less than the longer diameter. And therefore, if from the period of Earth, for instance, which is one year, and from the period of Saturn, which is thirty years, you take the third part of the proportion—that is, the cube roots—and double that proportion by squaring the roots, you will obtain in the resulting numbers the most exact proportion of the mean distances of Earth and Saturn from the Sun."*

Expressed in exact algebraic ratio:

$$\left(\frac{T_1}{T_2}\right)^2 = \left(\frac{a_1}{a_2}\right)^3, \qquad \text{or} \qquad T \propto a^{3/2}.$$

Thus if one planet were four times farther from the Sun than another ($a_1 : a_2 = 4 : 1$), its periodic time would be eightfold ($T_1 : T_2 = 8 : 1$, since $8^2 = 4^3 = 64$); if nine times farther ($9 : 1$), twenty-sevenfold ($27 : 1$, since $27^2 = 9^3 = 729$).

3. Liber V, Capita IV–IX — Consonances of Extremal Motions & Polyhedral Synthesis
---------------------------------------------------------------------------------

Why then did the :term:`five regular solids <corpora-quinque-regularia>` of *Mysterium Cosmographicum* leave small discrepancies when compared with :person:`Copernicus's <copernicus>` and :person:`Brahe's <brahe>` eccentricities? Because—Kepler demonstrates in Chapters IV–IX—the Supreme Geometer wedded **two distinct archetypes** in a single cosmos:

1. **Spatial Polyhedral Scaffolding**: The five Euclidean regular solids (together with the :term:`Golden Rhombic Triacontahedron <triacontaedron-rhombicum>`) prescribe the *rough spacing* of the six planetary shells around *Terra* (:term:`Circulus mensor <circulus-mensor>`).
2. **Dynamic Musical Tuning of Eccentricities** (:term:`harmonia motuum extremorum <harmonia-extremorum>`): Because a planet sweeps equal focal sector areas in equal times—compare the short, wide perihelion sector :g:`SEC_PER` around :g:`P_per` with the long, narrow aphelion sector :g:`SEC_APH` around :g:`A_aph`—its apparent daily heliocentric angular speed $\omega$ varies inversely as the square of its solar distance:

   $$\frac{\omega_{\text{per}}}{\omega_{\text{aph}}} = \left(\frac{r_{\text{aph}}}{r_{\text{per}}}\right)^2 = \left(\frac{1 + e}{1 - e}\right)^2.$$

   Tuning these extremal daily angular motions to the **just-intonation musical consonances** derived from constructible polygons in Books I and III fixes the precise orbital eccentricities $e$ of all six planets:

   * **Saturn** ($1'46'' : 2'15''$ per day $\approx 4 : 5$) — **Major Third** (*ditonus*);
   * **Jupiter** ($4'30'' : 5'30''$ per day $= 5 : 6$) — **Minor Third** (*sesquiquinta*);
   * **Mars** ($26'14'' : 38'1''$ per day $\approx 2 : 3$) — **Perfect Fifth** (*diapente*);
   * **Earth** ($57'3'' : 61'18''$ per day $\approx 15 : 16$) — **Diatonic Semitone** (*mi–fa*, prompting Kepler's wry lament: *"Earth sings MI–FA–MI, so that even from the syllable you may guess that in this home of ours MIsery and FAmine hold sway"*);
   * **Venus** ($94'50'' : 97'37''$ per day $\approx 24 : 25$) — **Chromatic Diesis** (nearly circular orbit inside the icosahedron);
   * **Mercury** ($164'0'' : 384'0''$ per day $= 5 : 12$) — **Octave plus Minor Third** (*diapason cum semiditono*, matching Mercury's dramatic eccentricity inside the octahedron).
