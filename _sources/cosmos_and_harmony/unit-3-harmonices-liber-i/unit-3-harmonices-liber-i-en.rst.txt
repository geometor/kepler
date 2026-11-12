.. _unit-3-harmonices-liber-i-en:

Unit III · Harmonices Mundi Liber I: De Figuris Regularibus (1619)
==================================================================

*Original GEOMETOR English translation from Johannes Kepler's Harmonices Mundi Liber I: De ortu figurarum regularium harmonicarum* (:cite:`Linz: Tampach/Plancus, 1619, pp. 1–46 <kepler:1619:hm>`; :cite:`Frisch V, pp. 75–125 <frisch:1864:v5>`).

1. Prooemium — Vindication of Euclid Book X Against Petrus Ramus
----------------------------------------------------------------

Since antiquity saw that the origins of harmonic proportions arise from the divisions of the circle into equal parts executed geometrically—that is, from **knowable** (*scibiles*) regular plane figures—it was necessary first of all to point out to geometers today those deepest mysteries which :person:`Euclid <euclid>` set forth in his **Tenth Book** concerning incommensurable lines (:cite:`Elements X <euclid:elements>`), corroborated by the commentary of :person:`Proclus Diadochus <proclus>` (:cite:`In Euclidem <proclus:in-euclidem>`).

Why did that great treatise of Euclid's Tenth Book lie almost neglected down to our day? Because :person:`Petrus Ramus <ramus>`, an otherwise sharp and enterprising mind, stumbled upon its subtle distinctions without perceiving **toward what goal** Euclid was steering! Ramus reviled the Tenth Book so fiercely—claiming that among all human sciences no obscurity comparable to that labyrinth had ever appeared—that even my friend :person:`Willebrord Snellius <snellius>`, though republishing the enunciations, hesitated to defend their utility. I confess that I myself stood near Ramus's camp **until I entered upon the investigation of celestial harmonies**: then at sudden daylight I beheld that Euclid had constructed the entire edifice of **commensurable lengths, commensurable squares, medial lines, binomials, apotomes, majors, and minors** for one supreme architectural purpose—to distinguish **knowable and constructible regular figures** (*scibilia*) from **unknowable and non-constructible figures** (*inscibilia*)!

2. Definitions I–XXV — The Eight Degrees of Geometric Scibilitas
----------------------------------------------------------------

* **Definition VII (*To Know in Geometry*)**: **To know** (*scire*) in geometric matters is **to measure by a known measure**; and in our problem of inscribing figures in a circle, that canonical known measure is the **diameter of the circle** ($D = 2R$).
* **Definition VIII (*Knowable / Demonstrable*)**: A line or chord is called **knowable** (:term:`scibilis <scibilitas>`, Greek γνώριμον) when it is either directly measurable by the diameter itself, or at least derived through a **definite and geometrical chain of squares and square-roots** descending from the diameter.

From the diameter $D = 2R$, geometric knowability descends across **eight ordered degrees**:

1. **Degree I (*Identity*)**: Equality with the diameter itself ($s_2 = D = 2R$).
2. **Degree II (*Expressible in Length*)**: Rational commensurability in length (:term:`effabilis longitudine <effabilis-longitudine>`), exemplified by the **Regular Hexagon** whose side equals the radius ($s_6 = R = \frac{1}{2}D$, :just:`IV.15`).
3. **Degree III (*Expressible in Square Only*)**: Incommensurability in length paired with exact rational :term:`quadrance <quadrance>` (:term:`effabilis potentiâ tantùm <effabilis-potentia>`), exemplified by the **Square** ($s_4^2 = 2R^2 = \frac{1}{2}D^2$, :just:`IV.6`) and the **Equilateral Triangle** ($s_3^2 = 3R^2 = \frac{3}{4}D^2$, :just:`XIII.12`).
4. **Degree IV (*Medial / Mese*)**: Geometric mean of two lines commensurable in square only (:term:`mese <mese>`, Euclid X.21), governing areas of the **Regular Octagon** and **Regular Dodecagon**.
5. **Degrees V & VI (*Binomial & Apotome*)**: Sum and difference $a \pm \sqrt{b}$ of lines commensurable in square only (:term:`binominis & apotome <binominis-apotome>`). Here shines forth the **Regular Decagon** (:g:`OG`), whose side $s_{10} = \frac{\sqrt{5}-1}{2}R = \frac{R}{\phi}$ is an **Apotome** cut by the :term:`Divine Section <sectio-divina>` (:just:`XIII.9`)!
6. **Degrees VII & VIII (*Major / Mizon & Minor / Elasson*)**: Compound nested quadratic radicals $\sqrt{a \pm \sqrt{b}}$ (:term:`mizon & elasson <mizon-elasson>`, Euclid X.39, X.76). In the left panel below, the **Regular Pentagon** (:g:`PENT5`) has side :g:`AG` equal to an **Elasson** (*Minor*) line $s_5 = \frac{R}{2}\sqrt{10 - 2\sqrt{5}}$ (:just:`XIII.10`), while the five-pointed star chord (*stella quinquangula*) is its conjugate **Mizon** (*Major*) line $d_5 = \frac{R}{2}\sqrt{10 + 2\sqrt{5}}$, followed by the **Pentadecagon** ($n = 15$, :just:`IV.16`) and iterated bisections ($n = 8, 12, 16, 20, 24\dots$).

.. picture:: /_static/figures/fig06_scibilia_pentagon_vs_heptagon.svg
   :alt: Constructible Euclidean Pentagon and Decagon versus Non-Constructible Regular Heptagon

3. Proposition XXIX — Self-Propagation of the Divine Section
------------------------------------------------------------

* **Definition XXVI & Proposition XXIX**: A line is cut in **Proportio Divina** (Euclid's *extreme and mean ratio*) when as the whole is to the greater segment, so is the greater segment to the lesser ($1 + \phi : \phi = \phi : 1$). Uniquely among all divisions of magnitude, **once established it propagates itself forever**: if the greater segment is laid off upon the whole, or if the whole is added to the greater segment (:just:`XIII.5`), a new Divine Section springs forth immediately without fresh construction—just as :person:`Ptolemy's <ptolemy>` swing arc from midpoint :g:`M` through apex :g:`A` cuts off both the decagon side :g:`OG` ($R/\phi$) and the pentagon chord :g:`AG` ($\sqrt{R^2 + s_{10}^2}$) in a single stroke.

4. Proposition XLV — Non-Constructibility (*Inscibilitas*) of the Heptagon
--------------------------------------------------------------------------

* **Proposition XLV (*Enunciation*)**: **The side of the Regular Heptagon (*Septangulum*, :g:`HEPT7`), and every figure whose number of sides is a prime number beyond five (such as 7, 11, 13, 17?, 19) or a multiple of nine, lacks geometric knowability and cannot be constructed from the diameter by Euclidean plane geometry.**

For consider the heptagonal triangle :g:`H1H2H4` inscribed in :g:`cHEPT` (right panel above), bounded by three unequal chords: the heptagon side $s_1 = H_1 H_2$, the short diagonal $s_2 = H_1 H_3$ (:g:`diag_s2`), and the long diagonal $s_3 = H_1 H_4$ (:g:`diag_s3`). Unlike the pentagon—where only **two** chord species exist ($s_5$ and $d_5$), locking their ratio immediately into a quadratic equation $x^2 - x - 1 = 0$ solvable by a circle and straight line—the heptagon entangles **three** chord species simultaneously!

My ingenious friend :person:`Jost Bürgi <buergi>` (*Justus Byrgius*) has indeed exhibited an algebraic (*Cossic*) equation relating the chord of one-seventh of the circumference to the radius:

$$y^6 - 7y^4 + 14y^2 - 7 = 0 \qquad \Longleftrightarrow \qquad x^3 + x^2 - 2x - 1 = 0 \quad \left(x = 2\cos\frac{2\pi}{7}\right).$$

Yet I reply that **algebraic root-reckoning is not Euclidean geometric determination**! First, this equation climbs to the **cubic** (third) solid degree in $x$ (or sixth in $y$), which no intersection of straight lines and circles in a plane can cut off; second, the very same algebraic equation admits **three distinct real roots** simultaneously—answering indifferently to the convex heptagon chord $\frac{1}{7}$, the first star heptagram $\frac{2}{7}$, and the second star heptagram $\frac{3}{7}$—without singling out one magnitude from the diameter by finite geometric necessity:

   *"Therefore no Regular Heptagon has ever been constructed by anyone knowingly, willingly, and acting from deliberate geometrical purpose; nor **can** it be constructed from deliberate purpose—though by blind chance its length might be stumbled upon, without anyone ever knowing whether it has been!"*

Thus the Creator excluded the heptagon, enneagon ($n = 9$), hendecagon ($n = 11$), and their kin from the archetypal council of cosmic harmonies.
