#!/usr/bin/env python3
"""Kepler Tabula III (Mysterium Cosmographicum, 1596/1597, folio 0034)
======================================================================
Parametric 3D CAD assembly builder mirroring ``GOR-9/tower_3d/build_ingetrazo_tower.py``.

Exports:
  - ``tabula_iii_3d/tabula_iii.obj`` & ``tabula_iii.mtl`` (standard Wavefront CAD)
  - ``tabula_iii_3d/tabula_iii.glb`` (Binary glTF 2.0 PBR mesh + copied to ``docsrc/_static/models/``)
  - ``tabula_iii_3d/tabula_iii.igz`` (native IngeTrazo 0.6.0 CAD project when run with IngeTrazo Python)
  - Optional ``--live`` push directly into a running IngeTrazo 0.6.0 viewport via MCP bridge (``127.0.0.1:4763``)
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

INGETRAZO_ROOT = Path("/home/phi/PROJECTS/phi-WORKS/ingetrazo")
if INGETRAZO_ROOT.exists():
    for _p in (INGETRAZO_ROOT, INGETRAZO_ROOT / "scripts"):
        if str(_p) not in sys.path:
            sys.path.insert(0, str(_p))

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tabula_iii_3d.components import CENTER_Z, ShimScene, build_tabula_iii_scene  # noqa: E402
from tabula_iii_3d.exporters import export_glb, export_obj_mtl  # noqa: E402

LIVE_BRIDGE_CODE = r"""
import importlib
import math
import sys
from pathlib import Path
from PySide6.QtGui import QVector3D

repo_root = Path("/home/phi/PROJECTS/geometor/kepler")
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

import tabula_iii_3d.components.primitives as _pr
import tabula_iii_3d.components.pedestal_cradle as _pc
import tabula_iii_3d.components.planetary_bowls as _pb
import tabula_iii_3d.components.platonic_scaffolds as _ps
import tabula_iii_3d.components as _comp

for _m in (_pr, _pc, _pb, _ps, _comp):
    importlib.reload(_m)

_comp.build_tabula_iii_scene(scene, scale_mode="exact", explode=0.0, include_pedestal=True)

renders_dir = repo_root / "tabula_iii_3d" / "renders"
renders_dir.mkdir(parents=True, exist_ok=True)

# 1. Tabula III 1597 Copperplate Hero Angle (three-quarter front-right elevated view)
viewport.camera.target = QVector3D(0.0, 0.0, 1.16)
viewport.camera.distance = 3.55
viewport.camera.yaw = math.radians(-32.0)
viewport.camera.pitch = math.radians(22.0)
viewport.camera.fov = 42.0
viewport.update()
viewport.render_image(2560, 1440).save(str(renders_dir / "ingetrazo_01_tabula_iii_hero.png"))

# 2. Inner Core Cutaway Macro (Cube -> Tetrahedron -> Mars -> Dodeca -> Earth -> Icosa -> Venus -> Octa -> Mercury -> Sol)
viewport.camera.target = QVector3D(0.0, 0.0, _pr.CENTER_Z - 0.02)
viewport.camera.distance = 1.05
viewport.camera.yaw = math.radians(-26.0)
viewport.camera.pitch = math.radians(30.0)
viewport.camera.fov = 38.0
viewport.update()
viewport.render_image(2560, 1440).save(str(renders_dir / "ingetrazo_02_inner_core_macro.png"))

result = {"groups": [g.name for g in scene.groups], "renders": 2}
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build Kepler's Tabula III (folio 0034) parametric 3D CAD model"
    )
    parser.add_argument(
        "--scale",
        choices=("exact", "expanded"),
        default="exact",
        help="Radial proportion schedule (default: exact Caput XIII)",
    )
    parser.add_argument(
        "--explode",
        type=float,
        default=0.0,
        help="Vertical assembly explode factor in [0.0, 1.0]",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="Push directly to running IngeTrazo 0.6.0 MCP bridge (127.0.0.1:4763)",
    )
    args = parser.parse_args()

    out_dir = REPO_ROOT / "tabula_iii_3d"
    out_dir.mkdir(parents=True, exist_ok=True)
    static_models_dir = REPO_ROOT / "docsrc" / "_static" / "models"
    static_models_dir.mkdir(parents=True, exist_ok=True)

    # 1. Build pure-Python CAD geometry -> export OBJ/MTL and Binary GLB (always works offline/sandboxed)
    shim_scene = ShimScene()
    radii = build_tabula_iii_scene(shim_scene, scale_mode=args.scale, explode=args.explode)

    obj_path = out_dir / "tabula_iii.obj"
    glb_path = out_dir / "tabula_iii.glb"
    n_verts_obj, n_faces_obj = export_obj_mtl(shim_scene, obj_path)
    n_verts_glb, n_tris_glb = export_glb(shim_scene, glb_path)

    # Copy compact .glb (and .obj/.mtl) into docsrc/_static/models/ for WebGL viewer & CAD downloads
    shutil.copy2(glb_path, static_models_dir / "tabula_iii.glb")
    shutil.copy2(obj_path, static_models_dir / "tabula_iii.obj")
    shutil.copy2(obj_path.with_suffix(".mtl"), static_models_dir / "tabula_iii.mtl")

    print(f"Built Tabula III CAD ({args.scale}, CENTER_Z={CENTER_Z:.3f}m, R_sat={radii.saturn_out:.3f}m):")
    print(f"  Groups: {len(shim_scene.groups)} ({', '.join(g.name for g in shim_scene.groups)})")
    print(f"  OBJ:    {obj_path} ({n_verts_obj} verts, {n_faces_obj} faces)")
    print(f"  GLB:    {glb_path} ({glb_path.stat().st_size / 1024:.1f} KB, {n_verts_glb} verts, {n_tris_glb} tris)")

    # 2. If running under IngeTrazo 0.6.0 Python environment, also write native .igz!
    try:
        os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
        from core.scene import Scene
        from formats.igz import save_scene
        from PySide6.QtWidgets import QApplication

        _app = QApplication.instance() or QApplication(sys.argv)
        igz_scene = Scene()
        build_tabula_iii_scene(igz_scene, scale_mode=args.scale, explode=args.explode)
        igz_path = out_dir / "tabula_iii.igz"
        save_scene(igz_scene, igz_path)
        shutil.copy2(igz_path, static_models_dir / "tabula_iii.igz")
        print(f"  IGZ:    {igz_path} ({igz_path.stat().st_size / 1024:.1f} KB, {len(igz_scene.groups)} groups)")
    except ImportError:
        print("  IGZ:    Skipped (run with /home/phi/PROJECTS/phi-WORKS/ingetrazo/.venv/bin/python to write .igz)")

    if args.live:
        import ingetrazo_mcp

        resp = ingetrazo_mcp._bridge("run_python", {"code": LIVE_BRIDGE_CODE})
        print("Live IngeTrazo 0.6.0 response:", resp)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
