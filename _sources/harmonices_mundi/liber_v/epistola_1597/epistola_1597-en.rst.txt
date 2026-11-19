:layout: book
:canonical_id: Epistola 1597
:order: 1
:tracks: Latin: epistola_1597-la | English: epistola_1597-en | Summary: epistola_1597-summary | Notes: epistola_1597-notes

.. _unit-5-harmonices-liber-v-en:
.. _hm-epistola_1597-en:
.. _hm-epistola_1597:

Letter to Mästlin (1597): The Kepler Right Triangle
===================================================

*"If upon a straight line cut in :term:`extreme and mean ratio <sectio-divina>` one constructs a right-angled triangle out of the segments and the whole—in such a way that the hypotenuse subtending the right angle is the greater segment (or the whole), and the base is the lesser segment (or the greater)—then the square on one leg together with the square on the other composes the square on the hypotenuse, while the **three sides themselves stand in continuous geometric proportion**!"* (:person:`Kepler <kepler>` to :person:`Michael Mästlin <maestlin>`, :cite:`Graz, October 1597 <kepler:1597:maestlin>`).

Here the **Two Great Treasures of Geometry** (:person:`Pythagoras's <pythagoras>` right-triangle theorem, :cite:`Euclid I.47 <euclid:elements>`, and the :term:`Divine Section <sectio-divina>`, :cite:`Euclid II.11 & VI.30 <euclid:elements>`) fuse into a single unique figure—the :term:`Kepler Right Triangle <kepler-triangle>` :g:`OAB` (left panel below):

* **Pure Euclidean Construction over** $\mathbb{Q}(\sqrt{\phi})$: Taking the unit segment :g:`OA` ($= 1$) from :g:`O` to :g:`A`, extend the baseline leftward to :g:`W` ($-1, 0$) and rightward by the golden-section arc (:cite:`Euclid II.11 <euclid:elements>`) to :g:`P` ($\phi, 0$). Erect the Thales semicircle :g:`cThales` upon diameter :g:`WP` of length $1 + \phi = \phi^2$; by :cite:`Euclid VI.13 <euclid:elements>`, it cuts the perpendicular through :g:`O` (at right angle :g:`angAOB`) in :g:`B` at height :g:`OB` $= \sqrt{1 \cdot \phi} = \sqrt{\phi}$.
* **Geometric Progression of Sides & Quadrances**: Joining :g:`AB` completes the right triangle :g:`OAB` whose sides stand in continuous geometric proportion $1 : \sqrt{\phi} : \phi$, while their :term:`quadrances <quadrance>` satisfy

  $$Q(\text{OA}) = 1, \qquad Q(\text{OB}) = \phi, \qquad Q(\text{AB}) = 1 + \phi = \phi^2.$$

* **Self-Similar Golden Altitude**: Dropping the perpendicular altitude :g:`OH` from the right angle :g:`O` onto the hypotenuse :g:`AB` at :g:`H` divides the hypotenuse into extreme and mean ratio once again: $BH = 1$ and $HA = \phi - 1 = \phi^{-1}$—upon which :person:`Mästlin <maestlin>` computed on the margin of Kepler's letter the celebrated first decimal approximation $6180340$ for a base of $10000000$ ($1/\phi \approx 0.6180340$).

.. picture:: /_static/figures/fig09_kepler_triangle_and_third_law.svg
   :alt: Kepler Right Triangle 1597 and Harmonices Mundi Book V Planetary Ellipse and Third Law
