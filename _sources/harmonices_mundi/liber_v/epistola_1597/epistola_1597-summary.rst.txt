:layout: book
:canonical_id: Epistola 1597
:order: 1
:tracks: Latin: epistola_1597-la | English: epistola_1597-en | Summary: epistola_1597-summary | Notes: epistola_1597-notes

.. _unit-5-harmonices-liber-v-summary:
.. _hm-epistola_1597-summary:

Epistola 1597: Executive Geometric Summary
==========================================

The Kepler Right Triangle over $\mathbb{Q}(\sqrt{\phi})$
----------------------------------------------------------

Constructed purely by straightedge and compass from $O(0,0)$ and $A(1,0)$ in ``geometor.kepler.harmonices_geometry.construct_kepler_right_triangle`` (``@proposition("Epistola.1597.KeplerTriangle")``, ``auto_intersect=False``) over ``geometor.model.get_kepler_field()`` (quartic minimal polynomial $x^4 - x^2 - 1 = 0$):

.. list-table:: Exact Invariants of the Kepler Right Triangle $\triangle OAB$
   :header-rows: 1
   :widths: 26 24 24 26

   * - Geometric Element
     - Symbolic Length
     - Exact Quadrance $Q$
     - Defining Property
   * - Base leg $OA$
     - $1$
     - $1$
     - Given unit segment
   * - Vertical leg $OB$
     - $\sqrt{\phi}$
     - $\phi = \frac{1 + \sqrt{5}}{2}$
     - Geometric mean $\sqrt{1 \cdot \phi}$ (Eucl. VI.13)
   * - Hypotenuse $AB$
     - $\phi$
     - $\phi^2 = \phi + 1 = \frac{3 + \sqrt{5}}{2}$
     - $Q(OA) + Q(OB) = 1 + \phi = \phi^2$ (Eucl. I.47 & II.11)
   * - Altitude $OH \perp AB$
     - $\frac{1}{\sqrt{\phi}}$
     - $\phi^{-1} = \phi - 1 = \frac{\sqrt{5} - 1}{2}$
     - Divides $AB$ into $BH = 1$ and $HA = \phi^{-1}$
