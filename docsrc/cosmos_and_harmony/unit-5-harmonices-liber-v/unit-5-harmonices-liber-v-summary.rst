.. _unit-5-harmonices-liber-v-summary:

Unit V · Executive Geometric Summary
====================================

Core Symbolic Constructions & Laws (*Epistola* 1597 & *Harmonices Mundi* Book V, 1619)
--------------------------------------------------------------------------------------

1. **The Kepler Right Triangle over** $\mathbb{Q}(\sqrt{\phi})$: Constructed purely by straightedge and compass from $O(0,0)$ and $A(1,0)$ in ``geometor.kepler.harmonices_geometry.construct_kepler_right_triangle`` (``@proposition("Epistola.1597.KeplerTriangle")``, ``auto_intersect=False``) over ``geometor.model.get_kepler_field()`` (quartic minimal polynomial $x^4 - x^2 - 1 = 0$):

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

2. **Planetary Extremal Consonances & Kepler's Third Law**: Verified symbolically and against Kepler's Book V tables in ``analyze_planetary_harmonies`` and ``verify_kepler_third_law`` (every naked-eye Tychonic orbit satisfies $(T/T_\oplus)^2 = (a/a_\oplus)^3$ to better than $0.89\%$):

.. list-table:: Six-Planet Consonances & Sesquialterate Ratio (*Harmonices Mundi* Book V)
   :header-rows: 1
   :widths: 15 18 18 23 13 13

   * - Planet
     - $\omega_{\text{aph}}$ ($''/\text{day}$)
     - $\omega_{\text{per}}$ ($''/\text{day}$)
     - Harmonic Consonance
     - $a$ (AU, Kepler)
     - $T$ (days, Kepler)
   * - **Saturn**
     - $106''$ ($1'46''$)
     - $135''$ ($2'15''$)
     - $4 : 5$ (Major Third)
     - $9.510$
     - $10759.2$
   * - **Jupiter**
     - $270''$ ($4'30''$)
     - $330''$ ($5'30''$)
     - $5 : 6$ (Minor Third)
     - $5.200$
     - $4332.6$
   * - **Mars**
     - $1574''$ ($26'14''$)
     - $2281''$ ($38'01''$)
     - $2 : 3$ (Perfect Fifth)
     - $1.524$
     - $686.98$
   * - **Earth**
     - $3433''$ ($57'03''$)
     - $3673''$ ($61'13''$)
     - $15 : 16$ (Semitone *mi–fa*)
     - $1.000$
     - $365.25$
   * - **Venus**
     - $5690''$ ($94'50''$)
     - $5867''$ ($97'47''$)
     - $24 : 25$ (Chromatic Diesis)
     - $0.724$
     - $224.70$
   * - **Mercury**
     - $9840''$ ($164'00''$)
     - $23040''$ ($384'00''$)
     - $5 : 12$ (Octave + Minor Third)
     - $0.388$
     - $87.97$
