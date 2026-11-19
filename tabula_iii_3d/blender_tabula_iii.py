#!/usr/bin/env python3
"""Kepler Tabula III (folio 0034) — Native Blender 5.x Scene & Studio Render Generator.

Mirrors ``GOR-9/tower_3d/blender_sequence.py``: loads the exact modular CAD geometry
from ``tabula_iii_3d/components/``, builds PBR metallic/silver/marble Principled BSDF
shaders with museum 3-point lighting, saves ``tabula_iii_3d/tabula_iii.blend``, and
renders high-resolution ``2560x1440`` QHD still plates in ``tabula_iii_3d/renders/``.

Run:
    blender --background --python tabula_iii_3d/blender_tabula_iii.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import bpy
from mathutils import Vector

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tabula_iii_3d.components import (  # noqa: E402
    CENTER_Z,
    MATERIALS,
    ShimScene,
    build_tabula_iii_scene,
)


def _clear_blender_scene() -> None:
    bpy.ops.wm.read_factory_settings(use_empty=True)


def _build_pbr_materials() -> dict[str, bpy.types.Material]:
    mats: dict[str, bpy.types.Material] = {}
    for key, spec in MATERIALS.items():
        mat = bpy.data.materials.new(name=key)
        mat.use_nodes = True
        nt = mat.node_tree
        bsdf = nt.nodes.get("Principled BSDF")
        r, g, b = spec["color"]
        bsdf.inputs["Base Color"].default_value = (r, g, b, 1.0)
        bsdf.inputs["Metallic"].default_value = float(spec.get("metallic", 0.6))
        bsdf.inputs["Roughness"].default_value = float(spec.get("roughness", 0.35))
        if spec.get("emissive"):
            if "Emission Color" in bsdf.inputs:
                bsdf.inputs["Emission Color"].default_value = (r, g, b, 1.0)
                bsdf.inputs["Emission Strength"].default_value = 4.5
        mats[key] = mat
    return mats


def _import_shim_scene(
    shim_scene: ShimScene,
    mat_map: dict[str, bpy.types.Material],
    collection: bpy.types.Collection,
) -> list[bpy.types.Object]:
    objs: list[bpy.types.Object] = []
    for grp in shim_scene.groups:
        verts: list[tuple[float, float, float]] = []
        v_map: dict[tuple[int, int, int], int] = {}
        faces: list[list[int]] = []
        face_mats: list[str] = []

        for f in grp.mesh.faces:
            if len(f.pts) < 3:
                continue
            idxs: list[int] = []
            for x, y, z in f.pts:
                q = (round(x * 1e6), round(y * 1e6), round(z * 1e6))
                vi = v_map.get(q)
                if vi is None:
                    vi = len(verts)
                    v_map[q] = vi
                    verts.append((x, y, z))
                idxs.append(vi)
            faces.append(idxs)
            face_mats.append(str(f.attrs.get("_mat") or "pedestal_bronze"))

        if not faces:
            continue

        me = bpy.data.meshes.new(name=grp.name)
        me.from_pydata(verts, [], faces)

        # Assign per-face materials cleanly
        local_mat_idx: dict[str, int] = {}
        for mkey in face_mats:
            if mkey not in local_mat_idx:
                local_mat_idx[mkey] = len(me.materials)
                me.materials.append(mat_map.get(mkey, mat_map["pedestal_bronze"]))

        is_bowl_or_sol = ("Bowl" in grp.name) or ("Sol" in grp.name)
        for poly, mkey in zip(me.polygons, face_mats, strict=False):
            poly.material_index = local_mat_idx[mkey]
            poly.use_smooth = is_bowl_or_sol

        me.update()
        obj = bpy.data.objects.new(grp.name, me)
        collection.objects.link(obj)
        objs.append(obj)
    return objs


def _setup_studio_world_and_lights() -> None:
    scene = bpy.context.scene
    world = bpy.data.worlds.new("TabulaIII_Museum_World")
    scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes.get("Background")
    if bg:
        bg.inputs["Color"].default_value = (0.032, 0.038, 0.052, 1.0)
        bg.inputs["Strength"].default_value = 0.65

    # Ground museum display plinth plane
    bpy.ops.mesh.primitive_plane_add(size=14.0, location=(0.0, 0.0, -0.001))
    floor = bpy.context.active_object
    floor.name = "Studio_Museum_Floor"
    fmat = bpy.data.materials.new("MuseumFloor")
    fmat.use_nodes = True
    fbsdf = fmat.node_tree.nodes.get("Principled BSDF")
    fbsdf.inputs["Base Color"].default_value = (0.025, 0.028, 0.036, 1.0)
    fbsdf.inputs["Roughness"].default_value = 0.35
    fbsdf.inputs["Metallic"].default_value = 0.15
    floor.data.materials.append(fmat)

    def add_area_light(name: str, loc: tuple[float, float, float], target: tuple[float, float, float], energy: float, size: float, color: tuple[float, float, float]) -> None:
        ldata = bpy.data.lights.new(name=name, type="AREA")
        ldata.energy = energy
        ldata.size = size
        ldata.color = color
        lobj = bpy.data.objects.new(name=name, object_data=ldata)
        bpy.context.scene.collection.objects.link(lobj)
        lobj.location = loc
        direction = Vector(target) - Vector(loc)
        lobj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()

    # Warm museum key light (upper front-left, echoing 1597 copperplate cross-hatching)
    add_area_light("Key_Warm", (-3.2, -3.4, 4.2), (0.0, 0.0, 1.25), 520.0, 2.4, (1.0, 0.94, 0.84))
    # Cool museum rim fill (right-rear, illuminating beveled metallic jambs & bowls)
    add_area_light("Rim_Cool", (3.6, 2.2, 2.8), (0.0, 0.0, 1.35), 320.0, 2.2, (0.76, 0.88, 1.0))
    # Overhead top skylight illuminating directly INTO the cutaway hemispherical bowls!
    add_area_light("Top_Bowl_Key", (0.2, -0.6, 4.8), (0.0, 0.0, CENTER_Z), 260.0, 1.8, (1.0, 0.98, 0.94))
    # Subtle warm point light inside Sol center
    sol_l = bpy.data.lights.new(name="Sol_Core_Light", type="POINT")
    sol_l.energy = 18.0
    sol_l.color = (1.0, 0.80, 0.34)
    sol_l.shadow_soft_size = 0.04
    sol_obj = bpy.data.objects.new("Sol_Core_Light", sol_l)
    bpy.context.scene.collection.objects.link(sol_obj)
    sol_obj.location = (0.0, 0.0, CENTER_Z)


def _setup_camera(loc: tuple[float, float, float], target: tuple[float, float, float], lens: float = 48.0) -> bpy.types.Object:
    cam_data = bpy.data.cameras.new("StudioCam")
    cam_data.lens = lens
    cam_data.clip_start = 0.01
    cam_data.clip_end = 100.0
    cam = bpy.data.objects.new("StudioCam", cam_data)
    bpy.context.scene.collection.objects.link(cam)
    cam.location = loc
    direction = Vector(target) - Vector(loc)
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = cam
    return cam


def main() -> int:
    _clear_blender_scene()
    scene = bpy.context.scene

    # Configure high-quality EEVEE / Cycles renderer (EEVEE Next on Blender 5.x is fast & studio-crisp)
    available_engines = {e.identifier for e in scene.render.bl_rna.properties["engine"].enum_items}
    if "BLENDER_EEVEE_NEXT" in available_engines:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
        scene.eevee.taa_render_samples = 64
    elif "BLENDER_EEVEE" in available_engines:
        scene.render.engine = "BLENDER_EEVEE"
        scene.eevee.taa_render_samples = 64
    else:
        scene.render.engine = "CYCLES"
        scene.cycles.samples = 48

    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1440
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"

    mat_map = _build_pbr_materials()
    _setup_studio_world_and_lights()

    # Build Nested Exact Tabula III Collection
    col = bpy.data.collections.new("Tabula_III_Nested")
    scene.collection.children.link(col)
    shim = ShimScene()
    build_tabula_iii_scene(shim, scale_mode="exact", explode=0.0, include_pedestal=True)
    _import_shim_scene(shim, mat_map, col)

    # Camera 1: Exact Christoph Leibfried 1597 Tabula III framing (front-left window unobstructed, full pedestal framed!)
    cam = _setup_camera((-0.82, -3.95, 2.65), (0.0, 0.0, 1.06), lens=44.0)

    blend_path = SCRIPT_DIR / "tabula_iii.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"Saved Blender CAD scene: {blend_path}")

    renders_dir = SCRIPT_DIR / "renders"
    renders_dir.mkdir(parents=True, exist_ok=True)

    # Render 3 nested studio views
    shots = [
        ("blender_01_tabula_iii_plate_angle.png", (-0.82, -3.95, 2.65), (0.0, 0.0, 1.06), 44.0),
        ("blender_02_cutaway_bowls_top.png",      (-0.35, -1.75, 3.65), (0.0, 0.0, CENTER_Z - 0.12), 48.0),
        ("blender_03_inner_core_macro.png",       (-0.22, -0.82, CENTER_Z + 0.40), (0.0, 0.0, CENTER_Z - 0.02), 62.0),
    ]
    for fname, loc, target, lens in shots:
        cam.location = loc
        cam.data.lens = lens
        cam.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
        out_png = renders_dir / fname
        scene.render.filepath = str(out_png)
        bpy.ops.render.render(write_still=True)
        print(f"Rendered: {out_png}")

    # Render 4th view: Exploded Vertical CAD Assembly!
    for obj in list(col.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    shim_exp = ShimScene()
    build_tabula_iii_scene(shim_exp, scale_mode="exact", explode=0.85, include_pedestal=True)
    _import_shim_scene(shim_exp, mat_map, col)
    cam.location = (-1.15, -4.65, 2.95)
    cam.data.lens = 42.0
    cam.rotation_euler = (Vector((0.0, 0.0, 1.55)) - Vector(cam.location)).to_track_quat("-Z", "Y").to_euler()
    exp_png = renders_dir / "blender_04_exploded_assembly.png"
    scene.render.filepath = str(exp_png)
    bpy.ops.render.render(write_still=True)
    print(f"Rendered: {exp_png}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
