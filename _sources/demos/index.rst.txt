:order: 25
:nav_title: Demos

Symbolic Demonstrations
=======================

Executable pure-symbolic Python demonstrations (`Model(..., auto_intersect=False)`) verifying every geometric construction, polyhedral invariant, sphere-packing density, cyclotomic minimal polynomial, uniform planar tessellation, and harmonic orbital law in ``geometor.kepler`` with **zero floating-point coordinates**.

.. contents:: On this page
   :local:
   :depth: 2

1. Mysterium Cosmographicum — Five Regular Solids & Graz 1595 Nesting
---------------------------------------------------------------------

Derives the insphere/circumsphere radius and quadrance ratios of the five Platonic solids directly from exact 3D vertex sets over :math:`\mathbb{Q}(\phi)`, proves polar-duality equality (:math:`\text{Cube} = \text{Octahedron}` with :math:`Q_{\text{in}}/Q_{\text{out}} = \frac{1}{3}`; :math:`\text{Dodecahedron} = \text{Icosahedron}` with :math:`Q_{\text{in}}/Q_{\text{out}} = \frac{5 + 2\sqrt{5}}{15}`), propagates the six heliocentric planetary orbs from *Terra* (:math:`R = 1`), and constructs Kepler's July 19, 1595 Graz Great-Conjunction planar diagram.

.. literalinclude:: ../../demos/mysterium_spheres.py
   :language: python
   :linenos:

Run locally:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python demos/mysterium_spheres.py

2. Strena seu de Nive Sexangula — Rhombic Zonohedra, Close-Packing & Fibonacci
------------------------------------------------------------------------------

Verifies the exact 3D geometry of the space-filling **Rhombic Dodecahedron** (12 faces, 14 vertices, 24 edges, diagonal ratio :math:`\sqrt{2}:1`, dihedral :math:`120^\circ`) and the **Golden Rhombic Triacontahedron** (30 faces, 32 vertices, 60 edges, diagonal ratio :math:`\phi:1`, dihedral :math:`144^\circ`), proves FCC/HCP sphere close-packing density :math:`\frac{\pi}{3\sqrt{2}}` (:math:`\sqrt{2}` times denser than simple cubic :math:`\frac{\pi}{6}`), constructs the 7-circle hexagonal close-packing rosette, and checks Cassini's determinant across Kepler's Fibonacci ratios converging to :math:`\phi`.

.. literalinclude:: ../../demos/strena_packing.py
   :language: python
   :linenos:

Run locally:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python demos/strena_packing.py

3. Harmonices Mundi & 1597 Kepler Right Triangle
------------------------------------------------

Constructs the **Kepler Right Triangle** :math:`(1, \sqrt{\phi}, \phi)` over :math:`\mathbb{Q}(\sqrt{\phi})` purely from :math:`(0,0)` and :math:`(1,0)` by Euclidean ruler-and-compass intersections, classifies constructible polygons (*Scibilia*) against the irreducible cubic of the regular heptagon (:math:`x^3 + x^2 - 2x - 1 = 0`) and Jost Bürgi's cossic chord sextic (:math:`y^6 - 7y^4 + 14y^2 - 7 = 0`), derives all **11 uniform Archimedean planar tilings** from scratch, and verifies Kepler's Harmonic Third Law :math:`(T_1/T_2)^2 = (a_1/a_2)^3`.

.. literalinclude:: ../../demos/harmonices_geometry.py
   :language: python
   :linenos:

Run locally:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python demos/harmonices_geometry.py
