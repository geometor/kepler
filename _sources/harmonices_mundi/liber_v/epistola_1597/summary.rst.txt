:type: summary
:layout: book
:canonical_id: Epistola 1597
:order: 1

.. _unit-5-harmonices-liber-v-summary:
.. _hm-epistola_1597-summary:

Letter to Mästlin: Summary
==========================

The Kepler Right Triangle over :math:`\mathbb{Q}(\sqrt{\phi})`
--------------------------------------------------------------

Constructed purely by straightedge and compass from :math:`O(0,0)` and :math:`A(1,0)` in ``geometor.kepler.harmonices_geometry.construct_kepler_right_triangle`` (``@proposition("Epistola.1597.KeplerTriangle")``, ``auto_intersect=False``) over ``geometor.model.get_kepler_field()`` (quartic minimal polynomial :math:`x^4 - x^2 - 1 = 0`):

.. list-table:: Exact Invariants of the Kepler Right Triangle :math:`\triangle OAB`
   :header-rows: 1
   :widths: 26 24 24 26

   * - Geometric Element
     - Symbolic Length
     - Exact Quadrance :math:`Q`
     - Defining Property
   * - Base leg :math:`OA`
     - :math:`1`
     - :math:`1`
     - Given unit segment
   * - Vertical leg :math:`OB`
     - :math:`\sqrt{\phi}`
     - :math:`\phi = \frac{1 + \sqrt{5}}{2}`
     - Geometric mean :math:`\sqrt{1 \cdot \phi}` (Eucl. VI.13)
   * - Hypotenuse :math:`AB`
     - :math:`\phi`
     - :math:`\phi^2 = \phi + 1 = \frac{3 + \sqrt{5}}{2}`
     - :math:`Q(OA) + Q(OB) = 1 + \phi = \phi^2` (Eucl. I.47 & II.11)
   * - Altitude :math:`OH \perp AB`
     - :math:`\frac{1}{\sqrt{\phi}}`
     - :math:`\phi^{-1} = \phi - 1 = \frac{\sqrt{5} - 1}{2}`
     - Divides :math:`AB` into :math:`BH = 1` and :math:`HA = \phi^{-1}`
