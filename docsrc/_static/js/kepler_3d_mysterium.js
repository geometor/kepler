/* =========================================================================
   GEOMETOR • kepler — Interactive 3D Mysterium Cosmographicum & Star Polyhedra
   Exact Q(phi) Platonic & Kepler-Poinsot coordinates, 3-point studio lighting,
   layer toggles, exact vs. stepped nesting scale, drag-rotate & zoom.
   ========================================================================= */
(function () {
  "use strict";

  var PHI = (1 + Math.sqrt(5)) / 2;
  var INV_PHI = PHI - 1;

  // Exact Caput XIII circumsphere radii normalized to R_Earth = 1
  var R_ICOSA_RATIO = Math.sqrt((5 + 2 * Math.sqrt(5)) / 15); // ~0.794654
  var EXACT_RADII = {
    saturn: 3 * Math.sqrt(3) / R_ICOSA_RATIO, // ~6.5387 -> normalized to outer = 1 in exact mode
    jupiter: 3 / R_ICOSA_RATIO,               // ~3.7751
    mars: 1 / R_ICOSA_RATIO,                  // ~1.2584
    earth: 1.0,
    venus: R_ICOSA_RATIO,                     // ~0.7947
    mercury: R_ICOSA_RATIO / Math.sqrt(3),    // ~0.4588
  };

  var STEPPED_RADII = {
    cube: 1.0,
    tetra: 0.78,
    dodeca: 0.60,
    icosa: 0.44,
    octa: 0.30,
  };

  function vAdd(a, b) { return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]; }
  function vSub(a, b) { return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]; }
  function vScale(a, s) { return [a[0] * s, a[1] * s, a[2] * s]; }
  function vDot(a, b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
  function vCross(a, b) {
    return [
      a[1] * b[2] - a[2] * b[1],
      a[2] * b[0] - a[0] * b[2],
      a[0] * b[1] - a[1] * b[0],
    ];
  }
  function vLen(a) { return Math.sqrt(vDot(a, a)); }
  function vNorm(a) { var l = vLen(a) || 1; return [a[0] / l, a[1] / l, a[2] / l]; }

  function normVerts(verts, radius) {
    return verts.map(function (v) { return vScale(vNorm(v), radius); });
  }

  function edgesFromFaces(faces) {
    var seen = {};
    var edges = [];
    faces.forEach(function (f) {
      for (var i = 0; i < f.length; i++) {
        var a = f[i], b = f[(i + 1) % f.length];
        var k = a < b ? a + ":" + b : b + ":" + a;
        if (!seen[k]) {
          seen[k] = true;
          edges.push([a, b]);
        }
      }
    });
    return edges;
  }

  function orientFacesOutward(verts, faces) {
    return faces.map(function (f) {
      var c = [0, 0, 0];
      f.forEach(function (idx) { c = vAdd(c, verts[idx]); });
      c = vScale(c, 1 / f.length);
      var n = vCross(vSub(verts[f[1]], verts[f[0]]), vSub(verts[f[2]], verts[f[0]]));
      return vDot(n, c) < 0 ? f.slice().reverse() : f;
    });
  }

  function makeTetrahedron(R) {
    var v = normVerts([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], R);
    var f = orientFacesOutward(v, [[0, 1, 2], [0, 3, 1], [0, 2, 3], [1, 3, 2]]);
    return { verts: v, faces: f, edges: edgesFromFaces(f) };
  }

  function makeCube(R) {
    var raw = [];
    [-1, 1].forEach(function (x) {
      [-1, 1].forEach(function (y) {
        [-1, 1].forEach(function (z) { raw.push([x, y, z]); });
      });
    });
    var v = normVerts(raw, R);
    var f = orientFacesOutward(v, [
      [0, 1, 3, 2], [4, 6, 7, 5], [0, 4, 5, 1],
      [2, 3, 7, 6], [0, 2, 6, 4], [1, 5, 7, 3],
    ]);
    return { verts: v, faces: f, edges: edgesFromFaces(f) };
  }

  function makeOctahedron(R) {
    var v = normVerts([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], R);
    var f = orientFacesOutward(v, [
      [0, 2, 4], [0, 4, 3], [0, 3, 5], [0, 5, 2],
      [1, 4, 2], [1, 3, 4], [1, 5, 3], [1, 2, 5],
    ]);
    return { verts: v, faces: f, edges: edgesFromFaces(f) };
  }

  function makeIcosahedron(R) {
    var raw = [
      [0, 1, PHI], [0, -1, PHI], [0, 1, -PHI], [0, -1, -PHI],
      [1, PHI, 0], [-1, PHI, 0], [1, -PHI, 0], [-1, -PHI, 0],
      [PHI, 0, 1], [-PHI, 0, 1], [PHI, 0, -1], [-PHI, 0, -1],
    ];
    var v = normVerts(raw, R);
    var f = orientFacesOutward(v, [
      [0, 1, 8], [0, 8, 4], [0, 4, 5], [0, 5, 9], [0, 9, 1],
      [1, 6, 8], [8, 6, 10], [8, 10, 4], [4, 10, 2], [4, 2, 5],
      [5, 2, 11], [5, 11, 9], [9, 11, 7], [9, 7, 1], [1, 7, 6],
      [3, 6, 7], [3, 10, 6], [3, 2, 10], [3, 11, 2], [3, 7, 11],
    ]);
    return { verts: v, faces: f, edges: edgesFromFaces(f) };
  }

  function makeDodecahedron(R) {
    var ico = makeIcosahedron(1);
    var raw = ico.faces.map(function (f) {
      return vNorm(vAdd(vAdd(ico.verts[f[0]], ico.verts[f[1]]), ico.verts[f[2]]));
    });
    var v = normVerts(raw, R);
    // 12 pentagonal faces: 5 dual faces around each icosahedron vertex
    var faces = [];
    for (var vi = 0; vi < 12; vi++) {
      var adj = [];
      ico.faces.forEach(function (f, fi) {
        if (f.indexOf(vi) !== -1) adj.push(fi);
      });
      // Order adj cyclically around ico.verts[vi]
      var axis = ico.verts[vi];
      var ref = vNorm(vSub(v[adj[0]], vScale(axis, vDot(v[adj[0]], axis))));
      var tan = vCross(axis, ref);
      adj.sort(function (a, b) {
        var angA = Math.atan2(vDot(v[a], tan), vDot(v[a], ref));
        var angB = Math.atan2(vDot(v[b], tan), vDot(v[b], ref));
        return angA - angB;
      });
      faces.push(adj);
    }
    faces = orientFacesOutward(v, faces);
    return { verts: v, faces: faces, edges: edgesFromFaces(faces) };
  }

  function makeSmallStellatedDodecahedron(R) {
    // 12 dodecahedron face centers raised to stellation apexes (pyramids on pentagon faces)
    var dodeca = makeDodecahedron(R / PHI);
    var verts = dodeca.verts.slice();
    var faces = [];
    var apexHeight = R;
    dodeca.faces.forEach(function (f) {
      var c = [0, 0, 0];
      f.forEach(function (idx) { c = vAdd(c, dodeca.verts[idx]); });
      c = vScale(vNorm(c), apexHeight);
      var apexIdx = verts.length;
      verts.push(c);
      for (var i = 0; i < f.length; i++) {
        faces.push([f[i], f[(i + 1) % f.length], apexIdx]);
      }
    });
    faces = orientFacesOutward(verts, faces);
    return { verts: verts, faces: faces, edges: edgesFromFaces(faces) };
  }

  function makeGreatStellatedDodecahedron(R) {
    // 20 icosahedron faces raised to sharp trihedral spikes
    var ico = makeIcosahedron(R * 0.56);
    var verts = ico.verts.slice();
    var faces = [];
    ico.faces.forEach(function (f) {
      var c = vAdd(vAdd(ico.verts[f[0]], ico.verts[f[1]]), ico.verts[f[2]]);
      var apexIdx = verts.length;
      verts.push(vScale(vNorm(c), R));
      for (var i = 0; i < 3; i++) {
        faces.push([f[i], f[(i + 1) % 3], apexIdx]);
      }
    });
    faces = orientFacesOutward(verts, faces);
    return { verts: verts, faces: faces, edges: edgesFromFaces(faces) };
  }

  function rotVec(v, rx, ry) {
    var cy = Math.cos(ry), sy = Math.sin(ry);
    var cx = Math.cos(rx), sx = Math.sin(rx);
    var x1 = v[0] * cy + v[2] * sy;
    var z1 = -v[0] * sy + v[2] * cy;
    var y2 = v[1] * cx - z1 * sx;
    var z2 = v[1] * sx + z1 * cx;
    return [x1, y2, z2];
  }

  function KeplerWidget(mount) {
    this.mount = mount;
    this.scene = mount.getAttribute("data-scene") || "mysterium_nested_solids";
    this.rx = 0.42;
    this.ry = 0.62;
    this.zoom = 1.0;
    this.autoRotate = true;
    this.opacity = 0.28;
    this.scaleMode = "stepped"; // "stepped" | "exact"
    this.stellationMode = "small"; // "small" | "great"
    this.showOrbs = true;
    this.visibleSolids = { cube: true, tetra: true, dodeca: true, icosa: true, octa: true };

    this.buildUI();
    this.bindEvents();
    this.loop();
  }

  KeplerWidget.prototype.buildUI = function () {
    this.mount.innerHTML = "";
    this.mount.classList.add("kepler-3d-widget");

    var header = document.createElement("div");
    header.className = "kepler-3d-header";

    var title = document.createElement("div");
    title.className = "kepler-3d-title";
    title.innerHTML =
      this.scene === "harmonices_stellated"
        ? "<strong>Harmonices Mundi II.26</strong> — Kepler–Poinsot Star Polyhedra"
        : "<strong>Mysterium Cosmographicum (Tabula III)</strong> — Nested Platonic Polyhedra";
    header.appendChild(title);

    var controls = document.createElement("div");
    controls.className = "kepler-3d-controls";

    var self = this;
    if (this.scene === "mysterium_nested_solids") {
      [
        ["stepped", "Stepped Scale"],
        ["exact", "Exact Caput XIII Ratios"],
      ].forEach(function (pair) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "kepler-3d-btn" + (self.scaleMode === pair[0] ? " is-active" : "");
        btn.textContent = pair[1];
        btn.addEventListener("click", function () {
          self.scaleMode = pair[0];
          controls.querySelectorAll(".kepler-3d-btn[data-mode]").forEach(function (b) {
            b.classList.toggle("is-active", b.getAttribute("data-mode") === pair[0]);
          });
        });
        btn.setAttribute("data-mode", pair[0]);
        controls.appendChild(btn);
      });

      var orbBtn = document.createElement("button");
      orbBtn.type = "button";
      orbBtn.className = "kepler-3d-btn is-active";
      orbBtn.textContent = "Planetary Orbs";
      orbBtn.addEventListener("click", function () {
        self.showOrbs = !self.showOrbs;
        orbBtn.classList.toggle("is-active", self.showOrbs);
      });
      controls.appendChild(orbBtn);
    } else {
      [
        ["small", "Small Stellated {5/2, 5}"],
        ["great", "Great Stellated {5/2, 3}"],
      ].forEach(function (pair) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "kepler-3d-btn" + (self.stellationMode === pair[0] ? " is-active" : "");
        btn.textContent = pair[1];
        btn.setAttribute("data-stel", pair[0]);
        btn.addEventListener("click", function () {
          self.stellationMode = pair[0];
          controls.querySelectorAll(".kepler-3d-btn[data-stel]").forEach(function (b) {
            b.classList.toggle("is-active", b.getAttribute("data-stel") === pair[0]);
          });
        });
        controls.appendChild(btn);
      });
    }

    var rotBtn = document.createElement("button");
    rotBtn.type = "button";
    rotBtn.className = "kepler-3d-btn is-active";
    rotBtn.textContent = "Auto-Rotate";
    rotBtn.addEventListener("click", function () {
      self.autoRotate = !self.autoRotate;
      rotBtn.classList.toggle("is-active", self.autoRotate);
    });
    controls.appendChild(rotBtn);

    header.appendChild(controls);
    this.mount.appendChild(header);

    if (this.scene === "mysterium_nested_solids") {
      var legend = document.createElement("div");
      legend.className = "kepler-3d-legend";
      [
        ["cube", "Cube (Saturn–Jupiter)", "#fbbf24"],
        ["tetra", "Tetrahedron (Jupiter–Mars)", "#f87171"],
        ["dodeca", "Dodecahedron (Mars–Earth)", "#c084fc"],
        ["icosa", "Icosahedron (Earth–Venus)", "#60a5fa"],
        ["octa", "Octahedron (Venus–Mercury)", "#38bdf8"],
      ].forEach(function (item) {
        var pill = document.createElement("button");
        pill.type = "button";
        pill.className = "kepler-3d-layer is-active";
        pill.innerHTML = '<span class="kepler-3d-swatch" style="background:' + item[2] + '"></span>' + item[1];
        pill.addEventListener("click", function () {
          self.visibleSolids[item[0]] = !self.visibleSolids[item[0]];
          pill.classList.toggle("is-active", self.visibleSolids[item[0]]);
        });
        legend.appendChild(pill);
      });
      this.mount.appendChild(legend);
    }

    this.canvas = document.createElement("canvas");
    this.canvas.className = "kepler-3d-canvas";
    this.canvas.width = 760;
    this.canvas.height = 460;
    this.mount.appendChild(this.canvas);
    this.ctx = this.canvas.getContext("2d");

    var footer = document.createElement("div");
    footer.className = "kepler-3d-footer";
    footer.textContent = "Drag to orbit · Scroll to zoom · Exact Q(φ) Platonic & Kepler-Poinsot vertices";
    this.mount.appendChild(footer);
  };

  KeplerWidget.prototype.bindEvents = function () {
    var self = this;
    var dragging = false, lx = 0, ly = 0;
    this.canvas.addEventListener("pointerdown", function (e) {
      dragging = true;
      lx = e.clientX;
      ly = e.clientY;
      self.autoRotate = false;
      var rb = self.mount.querySelector(".kepler-3d-btn:last-child");
      if (rb) rb.classList.remove("is-active");
      self.canvas.setPointerCapture(e.pointerId);
    });
    this.canvas.addEventListener("pointermove", function (e) {
      if (!dragging) return;
      self.ry += (e.clientX - lx) * 0.008;
      self.rx += (e.clientY - ly) * 0.008;
      lx = e.clientX;
      ly = e.clientY;
    });
    this.canvas.addEventListener("pointerup", function () { dragging = false; });
    this.canvas.addEventListener("wheel", function (e) {
      e.preventDefault();
      self.zoom = Math.max(0.45, Math.min(2.6, self.zoom * (e.deltaY > 0 ? 0.92 : 1.08)));
    }, { passive: false });
  };

  KeplerWidget.prototype.drawPoly = function (mesh, rgb, alpha, scale, cx, cy) {
    var ctx = this.ctx;
    var rVerts = mesh.verts.map(function (v) { return rotVec(v, this.rx, this.ry); }, this);
    var proj = rVerts.map(function (v) {
      var persp = 4.2 / (4.2 - v[2] * 0.55);
      return [cx + v[0] * scale * persp, cy - v[1] * scale * persp, v[2]];
    });

    var light = vNorm([0.55, 0.72, 0.85]);
    var facesSorted = mesh.faces.map(function (f) {
      var zSum = 0;
      f.forEach(function (i) { zSum += rVerts[i][2]; });
      var n = vNorm(vCross(vSub(rVerts[f[1]], rVerts[f[0]]), vSub(rVerts[f[2]], rVerts[f[0]])));
      return { f: f, z: zSum / f.length, lum: Math.max(0.22, Math.abs(vDot(n, light))) };
    }).sort(function (a, b) { return a.z - b.z; });

    facesSorted.forEach(function (item) {
      ctx.beginPath();
      item.f.forEach(function (vi, idx) {
        if (idx === 0) ctx.moveTo(proj[vi][0], proj[vi][1]);
        else ctx.lineTo(proj[vi][0], proj[vi][1]);
      });
      ctx.closePath();
      var r = Math.round(rgb[0] * item.lum);
      var g = Math.round(rgb[1] * item.lum);
      var b = Math.round(rgb[2] * item.lum);
      ctx.fillStyle = "rgba(" + r + "," + g + "," + b + "," + alpha + ")";
      ctx.fill();
    });

    ctx.strokeStyle = "rgba(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + ",0.88)";
    ctx.lineWidth = 1.25;
    mesh.edges.forEach(function (e) {
      ctx.beginPath();
      ctx.moveTo(proj[e[0]][0], proj[e[0]][1]);
      ctx.lineTo(proj[e[1]][0], proj[e[1]][1]);
      ctx.stroke();
    });
  };

  KeplerWidget.prototype.render = function () {
    var ctx = this.ctx;
    var w = this.canvas.width, h = this.canvas.height;
    var cx = w / 2, cy = h / 2;
    var scale = Math.min(w, h) * 0.36 * this.zoom;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = "#101216";
    ctx.fillRect(0, 0, w, h);

    if (this.scene === "harmonices_stellated") {
      var mesh = this.stellationMode === "small"
        ? makeSmallStellatedDodecahedron(1.0)
        : makeGreatStellatedDodecahedron(1.0);
      var col = this.stellationMode === "small" ? [251, 191, 36] : [192, 132, 252];
      this.drawPoly(mesh, col, 0.55, scale, cx, cy);
      return;
    }

    var norm = this.scaleMode === "exact" ? 1 / EXACT_RADII.saturn : 1;
    var specs = [
      { key: "cube",   mesh: makeCube((this.scaleMode === "exact" ? EXACT_RADII.saturn : STEPPED_RADII.cube) * norm),    rgb: [251, 191, 36], orb: (this.scaleMode === "exact" ? EXACT_RADII.saturn : STEPPED_RADII.cube) * norm },
      { key: "tetra",  mesh: makeTetrahedron((this.scaleMode === "exact" ? EXACT_RADII.jupiter : STEPPED_RADII.tetra) * norm), rgb: [248, 113, 113], orb: (this.scaleMode === "exact" ? EXACT_RADII.jupiter : STEPPED_RADII.tetra) * norm },
      { key: "dodeca", mesh: makeDodecahedron((this.scaleMode === "exact" ? EXACT_RADII.mars : STEPPED_RADII.dodeca) * norm),  rgb: [192, 132, 252], orb: (this.scaleMode === "exact" ? EXACT_RADII.mars : STEPPED_RADII.dodeca) * norm },
      { key: "icosa",  mesh: makeIcosahedron((this.scaleMode === "exact" ? EXACT_RADII.earth : STEPPED_RADII.icosa) * norm),   rgb: [96, 165, 250],  orb: (this.scaleMode === "exact" ? EXACT_RADII.earth : STEPPED_RADII.icosa) * norm },
      { key: "octa",   mesh: makeOctahedron((this.scaleMode === "exact" ? EXACT_RADII.venus : STEPPED_RADII.octa) * norm),    rgb: [56, 189, 248],  orb: (this.scaleMode === "exact" ? EXACT_RADII.venus : STEPPED_RADII.octa) * norm },
    ];

    var self = this;
    specs.forEach(function (s) {
      if (self.showOrbs) {
        ctx.beginPath();
        ctx.arc(cx, cy, s.orb * scale, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(" + s.rgb[0] + "," + s.rgb[1] + "," + s.rgb[2] + ",0.22)";
        ctx.setLineDash([4, 4]);
        ctx.lineWidth = 1;
        ctx.stroke();
        ctx.setLineDash([]);
      }
      if (self.visibleSolids[s.key]) {
        self.drawPoly(s.mesh, s.rgb, self.opacity, scale, cx, cy);
      }
    });

    if (this.showOrbs) {
      var mercR = (this.scaleMode === "exact" ? EXACT_RADII.mercury : 0.17) * norm;
      ctx.beginPath();
      ctx.arc(cx, cy, mercR * scale, 0, Math.PI * 2);
      ctx.strokeStyle = "rgba(148, 163, 184, 0.35)";
      ctx.setLineDash([3, 3]);
      ctx.stroke();
      ctx.setLineDash([]);
    }
    // Solar center dot
    ctx.beginPath();
    ctx.arc(cx, cy, 3.5, 0, Math.PI * 2);
    ctx.fillStyle = "#fbbf24";
    ctx.fill();
  };

  KeplerWidget.prototype.loop = function () {
    var self = this;
    function tick() {
      if (self.autoRotate) self.ry += 0.0045;
      self.render();
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  };

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".kepler-3d-mount").forEach(function (el) {
      new KeplerWidget(el);
    });
  });
})();
