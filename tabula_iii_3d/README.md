# Kepler's Tabula III (Folio 0034) — Parametric 3D CAD Model

Parametric 3D CAD reconstruction of Christoph Leibfried's famous 1597 folding copperplate **Tabula III** (*Mysterium Cosmographicum*, Tübingen 1596/1597, ad p. 25, folio `0034`), engineered following the modular **IngeTrazo 0.6.0 + Blender 5.x + Local Three.js WebGL** CAD pipeline from `phiarchitect/GOR-9/tower_3d/`.

---

## 1. Architectural Assemblies (`01`–`13`, Exact Caput XIII Ratios)

Built in **Z-up meters** at museum architectural orrery scale ($R_{\text{Saturn,out}} = 1.000\text{ m}$, cosmic center $\mu$ at $Z = 1.480\text{ m}$):

1. `01_Pedestal_Cradle` — Stepped Renaissance plinth (`1.28 m × 1.28 m`), 4 cardinal semicircular bastion lobes, central bronze turntable calyx, 4 cruciform S-scroll volute buttress legs with **8 outward-pointing pyramidal spike finials**, and **4 curved bronze meridian cradle straps** embracing Saturn's outer bowl.
2. `02_Alpha_Saturn_Bowl` ($\alpha$, *Sphaera ♄*) — Thick-walled double-beveled cutaway hemisphere ($R = 1.000 \to 0.945\text{ m}$) + rim planetary globe.
3. `03_Beta_Cube_Frame` ($\beta$, *Cubus*) — Watertight mitered solid-beam open-frame Cube ($r/R = 1/\sqrt{3} \approx 0.5774$).
4. `04_Gamma_Jupiter_Bowl` ($\gamma$, *Sphaera ♃*) — Cutaway hemisphere ($R = 0.546 \to 0.510\text{ m}$) + rim globe.
5. `05_Delta_Tetrahedron_Frame` ($\delta$, *Tetraedron*) — Apex-up watertight open-frame Tetrahedron ($r/R = 1/3 \approx 0.3333$).
6. `06_Epsilon_Mars_Bowl` ($\epsilon$, *Sphaera ♂*) — Cutaway hemisphere ($R = 0.170 \to 0.159\text{ m}$) + rim globe.
7. `07_Zeta_Dodecahedron_Frame` ($\zeta$, *Dodecaedron*) — Flat-pentagon-top open-frame Dodecahedron ($r/R = \sqrt{(5+2\sqrt{5})/15} \approx 0.7947$).
8. `08_Eta_Earth_Bowl` ($\eta$, *Orbis Magnus ⊕*) — Cutaway hemisphere ($R = 0.126 \to 0.118\text{ m}$) + Earth & companion Moon rim globes.
9. `09_Theta_Icosahedron_Frame` ($\theta$, *Icosaedron*) — Polar-dual vertex-up open-frame Icosahedron ($r/R \approx 0.7947$).
10. `10_Iota_Venus_Bowl` ($\iota$, *Sphaera ♀*) — Cutaway hemisphere ($R = 0.094 \to 0.088\text{ m}$) + rim globe.
11. `11_Kappa_Octahedron_Frame` ($\kappa$, *Octaedron*) — Vertex-up open-frame Octahedron with horizontal equatorial square ($r/R = 1/\sqrt{3}$).
12. `12_Lambda_Mercury_Bowl` ($\lambda$, *Sphaera ☿*) — Cutaway hemisphere ($R = 0.051 \to 0.046\text{ m}$) + rim globe.
13. `13_Mu_Sol_Center` ($\mu$, *Sol*) — Immobile glowing golden Solar sphere ($r = 0.024\text{ m}$) at `(0, 0, 1.480)`.

---

## 2. Building & Exporting CAD Formats

- **Export `.obj`, `.mtl`, `.glb` (and `.igz` under IngeTrazo Python)**:
  ```bash
  /home/phi/PROJECTS/phi-WORKS/ingetrazo/.venv/bin/python tabula_iii_3d/build_ingetrazo_tabula_iii.py
  # Add --live with IngeTrazo 0.6.0 AI Bridge active on 127.0.0.1:4763 to push live into the viewport!
  ```
- **Generate Native Blender 5.x `.blend` & Studio Renders**:
  ```bash
  blender --background --python tabula_iii_3d/blender_tabula_iii.py
  ```
- **Interactive WebGL 3D CAD Studio**:
  - Open [`docsrc/_static/tabula-iii-3d.html`](../docsrc/_static/tabula-iii-3d.html) (or embedded inside *Mysterium Cosmographicum* Index, Chapter II, and Chapter XIV).
