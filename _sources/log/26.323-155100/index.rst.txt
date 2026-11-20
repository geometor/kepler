:date: 26.323-155100
:author: phi ARCHITECT
:type: log
:categories: visual-audit, 3d-cad, celestial-music, scriptorium
:tags: kepler, tabula-iii, harmonices-mundi, just-intonation, web-audio, webgl, chromium-qa
:excerpt: Closed-loop multimodal visual & symbolic audits bringing Kepler's Tabula III (1597) 3D CAD Studio and Harmonices Mundi (1619) Live Celestial Music Studio to life—verified pixel-by-pixel via headless Chromium, Blender renders, folio provenance, and exact SymPy rationals.

========================================================================================
Visual & Symbolic Audits: Bringing Kepler's 3D Polyhedra & Celestial Music to Life
========================================================================================

*November 19, 2026* — Across three coordinated milestones (``2b5a0a4``, ``bfcee1b``, and ``fadc2d9``), ``geometor-kepler`` evolved from a static bilingual edition into a **living 3D CAD and Just-Intonation acoustic instrument**—audited at every layer by direct multimodal scan inspection, headless Chromium WebGL/Canvas captures, and exact symbolic algebra.

Rather than treating visual QA as an invisible scratch step, this log preserves the actual **audit captures, edge-case catches, and four-gate verification matrix** that validated both interactive studios before publication.

1. Multimodal Primary-Source Scan Audits (Vision Over OCR)
----------------------------------------------------------

Every geometric figure, polyhedral frame, and musical notehead was verified by directly inspecting Kepler's 300-DPI *editio princeps* scans rather than relying on embedded OCR layers:

* **Folio 0034 (Tabula III, Tübingen 1597)** — Confirmed Leibfried's cutaway hemispherical planetary bowls ($\alpha$–$\lambda$), mitered open-frame Platonic struts ($\beta$–$\kappa$), eccentric Solar core ($\mu$), and turned Renaissance pedestal, grounding the 13-group parametric CAD model in ``tabula_iii_3d/``.
* **Folio 0299 (Harmonices Mundi Book V, Linz 1619, p. 207)** — Direct visual reading caught two details frequently omitted in secondary transcriptions:

  1. Kepler's **seventh marginal voice** (*"Hic locum habet etiam ☽"*) assigning the Moon a Perfect-4th cradle monody ($G_4$–$A_4$–$B_4$–$C_5$–$B_4$–$A_4$–$G_4$, exact ratio $3:4$); and
  2. All **14 diamond mensural lozenges** of Mercury's melody—ten stepwise ascending pitches ($C_4 \to E_5$) followed by a four-note descending major-triad arpeggio ($C_5 \to G_4 \to E_4 \to C_4$).

* **Folios 0297, 0301 & 0302 (Linz 1619, pp. 205, 209–210)** — Verified Kepler's exact integer string-length divisions (``2160`` down to ``864`` for *Cantus Durus* and *Cantus Mollis*) and visually crop-audited both **Universal Six-Planet Creation Chord** engravings (``0301.g1.png`` *Genus Durum* and ``0302.g1.png`` *Genus Molle*), extending ``0301``'s lower margin to ``0.905`` and trimming ``0302``'s bottom to ``0.685`` so every staff border sits cleanly balanced.

2. Headless WebGL Audit: Tabula III 3D Parametric CAD Studio
------------------------------------------------------------

Using headless Chromium with offline-vendored Three.js (``docsrc/_static/vendor/``), we rendered and inspected both the **assembled 1597 engraving angle** and the **85% exploded vertical CAD stack** of :ref:`Tabula III <mysterium-3d-studio>` (`Launch Full-Screen CAD Studio <../../_static/tabula-iii-3d.html>`_):

.. container:: kepler-plate-pair

   .. picture:: tabula_iii_studio_audit.png
      :alt: Headless Chromium WebGL audit capture of Kepler Tabula III 3D CAD Studio at the 1597 copperplate viewing angle
      :caption: WebGL Studio Audit (Assembled 0% Explode): Verifies concentric cutaway bowls (α–λ), mitered Cube/Tetrahedron/Dodecahedron/Icosahedron/Octahedron frames, 1597 pedestal, and α–μ toggle legend.

   .. picture:: tabula_iii_exploded_audit.png
      :alt: Headless Chromium WebGL audit capture of Kepler Tabula III 3D CAD Studio at 85% exploded vertical assembly
      :caption: WebGL Studio Audit (85% Exploded Assembly): Confirms clean separation of all 13 parametric CAD groups from the carved pedestal through Mercury's Octahedron and Sol (μ).

Each CAD shell obeys Kepler's exact **Caput XIII** insphere/circumsphere schedule to $< 10^{-9}$ tolerance: Cube & Octahedron $1/\sqrt{3}$, Tetrahedron $1/3$, and Dodecahedron & Icosahedron $\sqrt{(5 + 2\sqrt{5})/15}$, exported simultaneously as IngeTrazo ``.igz``, Binary glTF ``.glb``, Wavefront ``.obj``/``.mtl``, and native Blender ``.blend``.

3. Headless Canvas & Layout Audits: Live Celestial Music Studio
---------------------------------------------------------------

Every one of the four instruments inside the :ref:`Interactive Celestial Music Studio <harmonices-audio-studio>` (`Launch Full-Screen Music Studio <../../_static/harmonices-mundi-studio.html>`_) was rendered and inspected via headless Chromium before commit.

**Real UI Catches Fixed During the Audit:**

* **Card Baseline Alignment (Tab 1)**: The first render of the seven planetary staves revealed that ``Luna (Cradle Monody)`` wrapped its ``▶ Play`` button and frequency span onto two lines, making the seventh card 18 px taller than Saturn through Mercury. Adding ``white-space: nowrap`` on ``.btn`` and tightening the title to ``Luna`` restored a razor-sharp horizontal grid across all 7 voices.
* **Narrow Book-Column Embed Mode**: Capturing the compiled Sphinx chapter page :ref:`Book V, Chapters IV–IX <hm-cap_04_09-en>` showed header chrome crowding inside the 680 px reading column when mounted via ``?embed=1``. Introducing ``body.is-embed`` compact spacing immediately surfaced Saturn, Jupiter, and Mars staves directly on first paint without scroll clutter.

.. container:: kepler-plate-pair

   .. picture:: music_01_melodies_audit.png
      :alt: Headless Chromium audit of Harmonices Mundi Studio Tab 1 showing all 7 planetary diamond-note mensural staves
      :caption: Studio Audit — Tab 1 (Planetary Melodies, Fol. 0299): Post-polish alignment of all 7 voices (Saturnus through Luna) with clickable diamond mensural noteheads and Discrete/Glissando mode switch.

   .. picture:: music_02_orrery_audit.png
      :alt: Headless Chromium audit of Harmonices Mundi Studio Tab 2 showing the live 6-planet Keplerian elliptical orrery with a golden Fifth (2:3) consonance beam between Venus and Mercury
      :caption: Studio Audit — Tab 2 (Live Orbital Orrery Choir): Real-time Keplerian ellipses singing ω(ν) ∝ 1/r²—caught live flashing a golden Just Fifth (2:3) consonance beam between Venus (672.8 Hz) and Mercury (505.9 Hz).

.. container:: kepler-plate-pair

   .. picture:: music_03_chords_audit.png
      :alt: Headless Chromium audit of Harmonices Mundi Studio Tab 3 showing Kepler's four 6-planet Universal Creation Chords beside the live oscilloscope
      :caption: Studio Audit — Tab 3 (Four Universal Creation Chords, Fols. 0301–0302): Both Genus Durum (Major) and Genus Molle (Minor) 6-planet alignments wired to a live Web Audio AnalyserNode oscilloscope.

   .. picture:: music_04_monochord_audit.png
      :alt: Headless Chromium audit of Harmonices Mundi Studio Tab 4 showing the equilateral triangle, brass vibrating monochord string, constructible vs non-constructible polygons, and folio 0297 string-length keys
      :caption: Studio Audit — Tab 4 (1596/1619 Monochord & Polygons, Fols. 0050 & 0297): Interactive brass bridge, Scibilia (gold) vs. Inscibilia 7/9 (rose) polygons, and Kepler's exact 2160–864 string-length keys.

.. picture:: music_05_book_v_page_audit.png
   :class: archival-plate
   :alt: Full-page headless Chromium audit of compiled Sphinx Book Codex page harmonices_mundi/liber_v/cap_04_09/cap_04_09-en.html
   :caption: Full Book Codex Page Audit (Book V, Chapters IV–IX): Compact ?embed=1 music studio iframe, side-by-side stereo Cathedral Organ HTML5 audio players (Planetary Motet 0:26 & Universal Creation Chords 0:24), and original 1619 Linz woodcuts below.

Direct synthesized recordings and microtonal scores produced by ``geometor.kepler.music``:

* `Seven-Voice Planetary Motet (Stereo Cathedral Organ .MP3) <../../_static/audio/kepler_planetary_motet.mp3>`_
* `Four Universal Creation Chords (Stereo Cathedral Organ .MP3) <../../_static/audio/kepler_creation_chords.mp3>`_
* `Kepler 1619 Multi-Track Microtonal Just-Intonation Score (.MIDI) <../../_static/audio/kepler_harmonices_1619.mid>`_

4. Four-Gate Symbolic & Archival Verification Matrix
----------------------------------------------------

Every commit in this campaign cleared four independent automated verification gates inside the offline Python 3.13 sandbox:

.. list-table:: Automated Verification Summary (``geometor-kepler`` @ ``fadc2d9``)
   :header-rows: 1
   :widths: 24 22 54

   * - Verification Gate
     - Result
     - Key Audited Invariants
   * - ``uv run --no-sync pytest``
     - **14 / 14 passed**
     - Zero ``sp.Float`` coordinates in ``geometor.model``; 10/10 exact ``sp.Rational`` Just-Intonation identities (including syntonic comma $81/80$ and Earth's $15:16$ *MI–FA–MI*); exact Caput XIII CAD shell ratios ($< 10^{-9}$); valid ``glTF``, ``PK`` (``.igz``), ``MThd`` (``.mid``), and ``.mp3`` headers.
   * - Archival Plates & SVGs
     - **34 PNG + 14 SVG**
     - 34 cropped 300-DPI archival plates and 14 five-layer ``.euclid-graphic`` vectorizations (``elements`` → ``labels``); **0** orphaned files.
   * - ``publish folio-links``
     - **616 scans · 0 unresolved**
     - **61 / 61** ``.. folio::`` directives and **164 / 164** ``:folio:`` track badges resolved across *Mysterium*, *Strena*, and *Harmonices Mundi*.
   * - ``ruff check`` & ``publish build``
     - **0 lint · 0 warnings**
     - Clean lint across ``src``, ``tests``, and ``tabula_iii_3d``; clean full Sphinx Book Codex build (``"ok": true``, ``warnings_count: 0``).
