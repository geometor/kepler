.. _unit-3-harmonices-liber-i-notes:

Unit III · Historical & Mathematical Commentary
===============================================

1. Why Harmonic Consonances Stop at the Number Five (*Senarius*)
----------------------------------------------------------------

Renaissance music theorists led by Gioseffo Zarlino (*Le Istitutioni Harmoniche*, 1558) had observed empirically that pure just-intonation musical consonances employ only ratios built from the integers $\{1, 2, 3, 4, 5, 6\}$ (octave $1:2$, fifth $2:3$, fourth $3:4$, major third $4:5$, minor third $5:6$, major sixth $3:5$, minor sixth $5:8$), whereas **seven** ($6:7, 7:8$) sounds harsh and dissonant—yet Zarlino offered only numerological excuses (*senarius*).

In *Harmonices Mundi* Books I and III, :person:`Kepler <kepler>` replaced numerology with **constructive Euclidean geometry**: the soul judges harmonic proportions by comparing circular arcs against the whole circle through innate geometric archetypes (*scibilitas*). Because polygons of $3, 4, 5, 6, 8, 10, 12, 15, 16\dots$ sides are constructible by straightedge and compass (*Scibilia*), their arc divisions generate musical consonances; because the **regular heptagon** ($n = 7$), **enneagon** ($n = 9$? wait: $1/3$ is constructible while $1/9$ requires angle trisection, though $9$ enters secondary ratios only via $3 \times 3$), **hendecagon** ($n = 11$), and **tridecagon** ($n = 13$) are non-constructible (*Inscibilia*), the prime $7$ is barred from primary harmonic division!

2. Gauss (1801), the 17-gon, and Wantzel (1837)
-----------------------------------------------

Kepler's two central mathematical claims in Book I fared extraordinarily well under nineteenth-century algebra:

* **Exclusion of $n = 7, 9, 11, 13$**: Completely **vindicated** by :person:`Pierre Laurent Wantzel <wantzel>` (:cite:`1837 <wantzel:1837>`), who proved that straightedge-and-compass constructions reach solely algebraic numbers whose minimal polynomial over $\mathbb{Q}$ has degree $2^k$ (and lies in a $2$-tower of normal closures). Since $\deg(2\cos(2\pi/7)) = 3$, $\deg(2\cos(2\pi/9)) = 3$, and $\deg(2\cos(2\pi/11)) = 5$, none is constructible.
* **What about $n = 17$?** Having seen degree $\frac{p-1}{2}$ fail for $p = 7$ (degree $3$), $p = 11$ (degree $5$), and $p = 13$ (degree $6$, containing an odd factor $3$), Kepler naturally assumed all primes $p > 5$ were non-constructible. On March 30, 1796, nineteen-year-old :person:`Carl Friedrich Gauss <gauss>` (:cite:`1801, §365 <gauss:1801>`) discovered that for $p = 17$, $\frac{p-1}{2} = 8 = 2^3$ decomposes into a pure chain of **three nested quadratic equations** because $17 = 2^{2^2} + 1$ is a **Fermat prime**! Even so, for musical acoustics $17$-fold division lies far beyond primary consonance, leaving Kepler's geometric demarcation of $\{2, 3, 5\}$ intact across the small integers.

3. Derivation of Bürgi's Chord Equation in SymPy
------------------------------------------------

Let $\zeta = e^{2\pi i / 7}$ satisfy $1 + \zeta + \zeta^2 + \zeta^3 + \zeta^4 + \zeta^5 + \zeta^6 = 0$. Dividing by $\zeta^3$ and setting $x = \zeta + \zeta^{-1} = 2\cos(2\pi/7)$:

$$\left(x^3 - 3x\right) + \left(x^2 - 2\right) + x + 1 = 0 \implies x^3 + x^2 - 2x - 1 = 0.$$

Since the heptagon side in a unit circle is $y = 2\sin(\pi/7)$ with $x = 2\cos(2\pi/7) = 2 - y^2$? Wait: $2\cos(2\pi/7) = 2\left(1 - 2\sin^2\frac{\pi}{7}\right) = 2 - y^2$? Almost: $y = 2\sin(\pi/7) \implies y^2 = 4\sin^2(\pi/7) = 2 - 2\cos(2\pi/7) = 2 - x \implies x = 2 - y^2$! Substitute $x = 2 - u$ ($u = y^2$) into $x^3 + x^2 - 2x - 1 = 0$:

$$(2 - u)^3 + (2 - u)^2 - 2(2 - u) - 1 = -u^3 + 7u^2 - 14u + 7 = 0 \implies y^6 - 7y^4 + 14y^2 - 7 = 0,$$

recovering **Jost Bürgi's exact Cossic sextic** verified in ``geometor.kepler.harmonices_geometry.verify_heptagon_cubic_obstruction``!
