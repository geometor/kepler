"""Pure-Python CAD exporters for Kepler's Tabula III (Wavefront OBJ/MTL & Binary glTF 2.0 GLB)."""

from __future__ import annotations

import json
import math
import struct
from pathlib import Path
from typing import Any

from .components.primitives import MATERIALS, v_cross, v_norm, v_sub


def _face_pts(face: Any) -> list[tuple[float, float, float]]:
    """Extract float (x, y, z) tuples from either a ShimFace or IngeTrazo Face."""
    if hasattr(face, "pts"):
        return list(face.pts)
    # IngeTrazo native Face stores vertices via loop/vertices
    verts = getattr(face, "vertices", None)
    if verts is not None:
        out = []
        for v in verts:
            pos = getattr(v, "pos", v)
            out.append((float(pos.x()), float(pos.y()), float(pos.z())) if callable(getattr(pos, "x", None)) else (float(pos.x), float(pos.y), float(pos.z)))
        return out
    return []


def _face_mat_key(face: Any) -> str:
    attrs = getattr(face, "attrs", {}) or {}
    return str(attrs.get("_mat") or "pedestal_bronze")


def export_obj_mtl(scene: Any, obj_path: Path) -> tuple[int, int]:
    """Export a CAD scene (Z-up, meters) to standard Wavefront ``.obj`` + ``.mtl``."""
    mtl_path = obj_path.with_suffix(".mtl")
    mtl_lines = [
        "# GEOMETOR Kepler — Tabula III (1596/1597, folio 0034) CAD Materials",
        "",
    ]
    for name, props in MATERIALS.items():
        r, g, b = props["color"]
        rough = float(props.get("roughness", 0.45))
        metal = float(props.get("metallic", 0.5))
        emissive = bool(props.get("emissive", False))
        ns = max(4.0, (1.0 - rough) ** 2 * 400.0)
        mtl_lines.append(f"newmtl {name}")
        mtl_lines.append(f"Ka {r * 0.22:.4f} {g * 0.22:.4f} {b * 0.22:.4f}")
        mtl_lines.append(f"Kd {r:.4f} {g:.4f} {b:.4f}")
        ks = 0.25 + 0.65 * metal
        mtl_lines.append(f"Ks {ks:.4f} {ks:.4f} {ks:.4f}")
        if emissive:
            mtl_lines.append(f"Ke {r * 1.4:.4f} {g * 1.4:.4f} {b * 1.4:.4f}")
        mtl_lines.append(f"Ns {ns:.1f}")
        mtl_lines.append(f"Pr {rough:.4f}")
        mtl_lines.append(f"Pm {metal:.4f}")
        mtl_lines.append("d 1.0000")
        mtl_lines.append("illum 2")
        mtl_lines.append("")
    mtl_path.write_text("\n".join(mtl_lines), encoding="utf-8")

    obj_lines = [
        "# GEOMETOR Kepler — Tabula III (Mysterium Cosmographicum, 1596/1597, folio 0034)",
        "# Units: meters | Coordinate system: Z-up",
        f"mtllib {mtl_path.name}",
        "",
    ]

    v_index = 1
    total_verts = 0
    total_faces = 0

    for grp in scene.groups:
        faces = getattr(grp.mesh, "faces", [])
        if not faces:
            continue
        obj_lines.append(f"o {grp.name}")
        obj_lines.append(f"g {grp.name}")

        # Group-local vertex deduplication
        v_map: dict[tuple[int, int, int], int] = {}
        active_mat = None

        for face in faces:
            pts = _face_pts(face)
            if len(pts) < 3:
                continue
            mat_key = _face_mat_key(face)
            if mat_key != active_mat:
                obj_lines.append(f"usemtl {mat_key}")
                active_mat = mat_key
            idxs: list[int] = []
            for x, y, z in pts:
                q = (round(x * 1e6), round(y * 1e6), round(z * 1e6))
                vi = v_map.get(q)
                if vi is None:
                    vi = v_index
                    v_index += 1
                    v_map[q] = vi
                    total_verts += 1
                    obj_lines.append(f"v {x:.6f} {y:.6f} {z:.6f}")
                idxs.append(vi)
            # Fan-triangulate polygons > 4 vertices, preserve tris & quads cleanly
            if len(idxs) <= 4:
                obj_lines.append("f " + " ".join(str(i) for i in idxs))
                total_faces += 1
            else:
                for k in range(1, len(idxs) - 1):
                    obj_lines.append(f"f {idxs[0]} {idxs[k]} {idxs[k + 1]}")
                    total_faces += 1
        obj_lines.append("")

    obj_path.write_text("\n".join(obj_lines), encoding="utf-8")
    return total_verts, total_faces


def export_glb(scene: Any, glb_path: Path) -> tuple[int, int]:
    """Export a CAD scene to standard Binary glTF 2.0 (``.glb``, Y-up PBR) with named nodes.

    Converts Z-up CAD coordinates ``(x, y, z)`` into glTF Y-up ``(x, z, -y)``
    (exact +90 deg rotation around X preserving right-handedness and CCW winding).
    """
    mat_names = sorted(MATERIALS.keys())
    mat_index_map = {name: i for i, name in enumerate(mat_names)}
    gltf_materials = []
    for name in mat_names:
        props = MATERIALS[name]
        r, g, b = props["color"]
        m_dict: dict[str, Any] = {
            "name": name,
            "pbrMetallicRoughness": {
                "baseColorFactor": [float(r), float(g), float(b), 1.0],
                "metallicFactor": float(props.get("metallic", 0.6)),
                "roughnessFactor": float(props.get("roughness", 0.35)),
            },
            "doubleSided": False,
        }
        if props.get("emissive"):
            m_dict["emissiveFactor"] = [min(1.0, float(r)), min(1.0, float(g)), min(1.0, float(b))]
        gltf_materials.append(m_dict)

    bin_chunks = bytearray()
    buffer_views: list[dict[str, Any]] = []
    accessors: list[dict[str, Any]] = []
    meshes: list[dict[str, Any]] = []
    nodes: list[dict[str, Any]] = []

    def append_bytes(data: bytes, target: int) -> int:
        # Pad buffer offset to 4-byte alignment
        while len(bin_chunks) % 4 != 0:
            bin_chunks.append(0)
        offset = len(bin_chunks)
        bin_chunks.extend(data)
        bv_idx = len(buffer_views)
        buffer_views.append({
            "buffer": 0,
            "byteOffset": offset,
            "byteLength": len(data),
            "target": target,
        })
        return bv_idx

    total_tris = 0
    total_verts = 0

    for grp in scene.groups:
        faces = getattr(grp.mesh, "faces", [])
        if not faces:
            continue

        # Bucket triangles by material key inside this group
        buckets: dict[str, tuple[list[float], list[float], list[int]]] = {}

        for face in faces:
            pts = _face_pts(face)
            if len(pts) < 3:
                continue
            mat_key = _face_mat_key(face)
            if mat_key not in mat_index_map:
                mat_key = "pedestal_bronze"
            if mat_key not in buckets:
                buckets[mat_key] = ([], [], [])
            pos_arr, norm_arr, idx_arr = buckets[mat_key]

            # Convert Z-up (x, y, z) -> Y-up glTF (x, z, -y)
            ypts = [(x, z, -y) for (x, y, z) in pts]
            # Compute crisp flat face normal (ideal for machined CAD bevels & architectural facets)
            n = v_norm(v_cross(v_sub(ypts[1], ypts[0]), v_sub(ypts[2], ypts[0])))
            if math.isnan(n[0]):
                n = (0.0, 1.0, 0.0)

            base_v = len(pos_arr) // 3
            for px, py, pz in ypts:
                pos_arr.extend((px, py, pz))
                norm_arr.extend(n)
            for k in range(1, len(ypts) - 1):
                idx_arr.extend((base_v, base_v + k, base_v + k + 1))
                total_tris += 1
            total_verts += len(ypts)

        primitives = []
        for mat_key, (pos_arr, norm_arr, idx_arr) in buckets.items():
            if not idx_arr:
                continue
            n_verts = len(pos_arr) // 3
            xs = pos_arr[0::3]
            ys = pos_arr[1::3]
            zs = pos_arr[2::3]

            pos_bytes = struct.pack(f"<{len(pos_arr)}f", *pos_arr)
            norm_bytes = struct.pack(f"<{len(norm_arr)}f", *norm_arr)
            idx_bytes = struct.pack(f"<{len(idx_arr)}I", *idx_arr)

            bv_pos = append_bytes(pos_bytes, 34962)   # ARRAY_BUFFER
            bv_norm = append_bytes(norm_bytes, 34962) # ARRAY_BUFFER
            bv_idx = append_bytes(idx_bytes, 34963)   # ELEMENT_ARRAY_BUFFER

            acc_pos = len(accessors)
            accessors.append({
                "bufferView": bv_pos,
                "componentType": 5126,  # FLOAT
                "count": n_verts,
                "type": "VEC3",
                "min": [min(xs), min(ys), min(zs)],
                "max": [max(xs), max(ys), max(zs)],
            })
            acc_norm = len(accessors)
            accessors.append({
                "bufferView": bv_norm,
                "componentType": 5126,  # FLOAT
                "count": n_verts,
                "type": "VEC3",
            })
            acc_idx = len(accessors)
            accessors.append({
                "bufferView": bv_idx,
                "componentType": 5125,  # UNSIGNED_INT
                "count": len(idx_arr),
                "type": "SCALAR",
            })
            primitives.append({
                "attributes": {"POSITION": acc_pos, "NORMAL": acc_norm},
                "indices": acc_idx,
                "material": mat_index_map[mat_key],
            })

        if primitives:
            mesh_idx = len(meshes)
            meshes.append({"name": grp.name, "primitives": primitives})
            nodes.append({"name": grp.name, "mesh": mesh_idx})

    while len(bin_chunks) % 4 != 0:
        bin_chunks.append(0)

    gltf_json = {
        "asset": {
            "version": "2.0",
            "generator": "GEOMETOR Kepler Tabula III 3D CAD Builder",
        },
        "scene": 0,
        "scenes": [{"name": "Tabula_III_1596", "nodes": list(range(len(nodes)))}],
        "nodes": nodes,
        "meshes": meshes,
        "materials": gltf_materials,
        "accessors": accessors,
        "bufferViews": buffer_views,
        "buffers": [{"byteLength": len(bin_chunks)}],
    }

    json_bytes = json.dumps(gltf_json, separators=(",", ":")).encode("utf-8")
    while len(json_bytes) % 4 != 0:
        json_bytes += b" "

    total_length = 12 + 8 + len(json_bytes) + 8 + len(bin_chunks)
    header = struct.pack("<4sII", b"glTF", 2, total_length)
    chunk0 = struct.pack("<I4s", len(json_bytes), b"JSON") + json_bytes
    chunk1 = struct.pack("<I4s", len(bin_chunks), b"BIN\x00") + bytes(bin_chunks)

    glb_path.write_bytes(header + chunk0 + chunk1)
    return total_verts, total_tris
