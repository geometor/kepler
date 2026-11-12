.. _unit-4-harmonices-liber-ii-en:

Unit IV · Harmonices Mundi Liber II: De Congruentia Figurarum (1619)
====================================================================

*Original GEOMETOR English translation from Johannes Kepler's Harmonices Mundi Liber II: Architectonicus, seu ex Geometria Figurata, de Figurarum Regularium Congruentia in Plano vel Solido* (:cite:`Linz: Tampach/Plancus, 1619, pp. 47–66 <kepler:1619:hm>`; :cite:`Frisch V, pp. 126–144 <frisch:1864:v5>`).

1. Definitions — Planar and Solid Congruence
--------------------------------------------

In the First Book we contemplated regular plane figures singly, examining which of them are :term:`knowable <scibilitas>` by inscription in a circle; now in the **Second Book**—which may rightly be called **Architectonic**—we consider their **sociability and mutual fitting together** (:term:`congruentia <congruentia>`), inquiring which regular and star polygons join edge-to-edge either to **pave an entire plane continuously without gaps**, or to **close up in three dimensions into a uniform solid body**.

* **Definitions I–III**: Regular polygons exhibit **planar congruence** when the interior angles meeting around every common vertex equal **four right angles** ($360^\circ$), and when the surrounding rings propagate consistently across every edge to infinity. They exhibit **solid congruence** when three or more plane angles (or star-polygon points) meet around a vertex with sum **strictly less than four right angles** ($< 360^\circ$), folding upward into a closed polyhedron.

2. Propositions I–XX — The Eleven Uniform Planar Tilings
--------------------------------------------------------

First, **three and only three** species of **pure regular** plane congruence fill the plane using a single polygon species:

1. **Six Equilateral Triangles** around each vertex (`3.3.3.3.3.3`, $6 \times 60^\circ = 360^\circ$);
2. **Four Squares** around each vertex (`4.4.4.4`, $4 \times 90^\circ = 360^\circ$);
3. **Three Regular Hexagons** around each vertex (`6.6.6`, $3 \times 120^\circ = 360^\circ$).

Next, when **two or three species** of regular polygons meet identically at every vertex, arithmetic alone permits seventeen local angle sums equal to $360^\circ$—including deceptive combinations such as a triangle, heptagon, and forty-two-gon ($60^\circ + 128\frac{4}{7}^\circ + 171\frac{3}{7}^\circ = 360^\circ$) or two pentagons with a decagon ($108^\circ + 108^\circ + 144^\circ = 360^\circ$). **Yet local angle sum does not suffice!** For around any odd-sided polygon—such as a triangle ($n = 3$) or pentagon ($n = 5$)—two distinct neighboring polygon species cannot alternate evenly around an odd number of edges without colliding! Eliminating all self-contradictory vertex figures leaves **eight and strictly eight semi-regular uniform tilings**—making **eleven uniform planar congruences** in all:

* **Three-valent vertices** ($k = 3$): `3.12.12` (triangles and dodecagons), `4.6.12` (square, hexagon, dodecagon), and `4.8.8` (:g:`V488`, squares and octagons).
* **Four-valent vertices** ($k = 4$): `3.6.3.6` (:g:`V3636`, alternating triangles and hexagons), and `3.4.6.4` (:g:`V3464`, triangle, square, hexagon, square).
* **Five-valent vertices** ($k = 5$): `3.3.3.4.4` (adjacent squares), `3.3.4.3.4` (separated squares), and the chiral snub tiling `3.3.3.3.6` (:g:`V33336`, four triangles and one hexagon, existing in left- and right-handed mirror forms).

.. picture:: /_static/figures/fig07_archimedean_planar_tilings.svg
   :alt: Four Representative Uniform Archimedean Planar Congruences in Harmonices Mundi Book II

3. Pentagonal & Star-Pentagram Congruence (`Figure Aa`)
-------------------------------------------------------

Although regular pentagons ($108^\circ$) and regular decagons ($144^\circ$) cannot form a uniform vertex-transitive tiling of convex polygons alone, if we admit the **five-pointed star** (:term:`stella quinquangula <stella-quinquangula>`, $\{5/2\}$, tip angle $36^\circ$, re-entrant pocket $72^\circ$), marvelous **fivefold flower-like congruences** blossom across the plane! Around a central decagon :g:`DEC0` (:g:`D_0` in the left panel below), five regular pentagons and five star pentagrams interlock seamlessly because:

$$144^\circ + 108^\circ + 108^\circ = 360^\circ, \qquad 144^\circ + 144^\circ + 72^\circ = 360^\circ, \qquad 3 \times 108^\circ + 36^\circ = 360^\circ,$$

generating radiating rings of decagons, stars, and twin-pentagon monsters that expand outward indefinitely according to a hidden law of the :term:`Divine Section <sectio-divina>`!

.. picture:: /_static/figures/fig08_kepler_pentagram_monster_aa.svg
   :alt: Kepler's Figure Aa Pentagonal-Decagonal Star Congruence and Golden Rhombic Triacontahedron

4. Propositions XXV–XXVIII — Star Solids, Rhombic Solids & 13 Archimedeans
--------------------------------------------------------------------------

In three-dimensional solid congruence, :person:`Kepler <kepler>` completes the inventory of symmetric polyhedra across four families:

1. **The Five Convex Platonic Solids** (:term:`corpora quinque regularia <corpora-quinque-regularia>`): Cube, Tetrahedron, Dodecahedron, Icosahedron, Octahedron.
2. **Two Regular Non-Convex Star Polyhedra** (:term:`corpora stellata <stella-quinquangula>`): Admitting twelve regular pentagrams $\{5/2\}$ as faces produces **two utterly regular augmented star solids**—the thorny *echinus* or **Small Stellated Dodecahedron** ($\{5/2, 5\}$, twelve 5-pointed vertices) and the **Great Stellated Dodecahedron** ($\{5/2, 3\}$, twenty trihedral vertices)!
3. **Two Isohedral Rhombic Zonohedra**: The 12-faced **Rhombic Dodecahedron** ($\sqrt{2}:1$) and the 30-faced **Golden Rhombic Triacontahedron** (:g:`PQRS` in the right panel above, long diagonal :g:`PR_gold` to short diagonal :g:`QS_gold` in ratio $\phi : 1$).
4. **The Thirteen Convex Archimedean Semi-Regular Solids** (:term:`corpora semiregularia Archimedis <archimedean-solids>`, Prop. XXVIII): Cleanly setting aside the two infinite families of regular **prisms** and **antiprisms**, Kepler reconstructs, names, and proves the completeness of all thirteen semi-regular convex solids recorded by :person:`Pappus <pappus>` (:cite:`Synagoge V.19 <pappus:synagoge:v>`): Truncated Tetrahedron, **Cuboctahedron**, Truncated Cube, Truncated Octahedron, Rhombicuboctahedron, Great Rhombicuboctahedron (Truncated Cuboctahedron), **Snub Cube** (*Cubus simus*), **Icosidodecahedron**, Truncated Dodecahedron, Truncated Icosahedron, Rhombicosidodecahedron, Great Rhombicosidodecahedron (Truncated Icosidodecahedron), and **Snub Dodecahedron** (*Dodecaedron simum*).
