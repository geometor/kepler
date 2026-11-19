/* =========================================================================
   GEOMETOR • kepler — Interactive 3D Mysterium Cosmographicum & Star Polyhedra
   Exact Q(phi) Platonic & Kepler-Poinsot coordinates, unified global depth
   sorting across all 5 nested solids, 3-point studio lighting, translucent
   planetary orbs, HiDPI canvas, theme-adaptive dark/light mode, orbit & zoom.
   ========================================================================= */
(function () {
  "use strict";

  var PHI = (1 + Math.sqrt(5)) / 2;
  var SQRT3 = Math.sqrt(3);
  var SQRT5 = Math.sqrt(5);

  // Exact Caput XIII circumsphere radii normalized to R_Earth = 1
  var R_ICOSA_RATIO = Math.sqrt((5 + 2 * SQRT5) / 15); // ~0.7946544723
  var EXACT_RADII = {
    saturn: (3 * SQRT3) / R_ICOSA_RATIO, // ~6.538678
    jupiter: 3 / R_ICOSA_RATIO,          // ~3.775108
    mars: 1 / R_ICOSA_RATIO,             // ~1.258369
    earth: 1.0,
    venus: R_ICOSA_RATIO,                // ~0.794654
    mercury: R_ICOSA_RATIO / SQRT3,      // ~0.458794
  };

  // Visual stepped radii preserving Kepler's exact nesting order
  var STEPPED_RADII = {
    saturn: 1.0,
    jupiter: 0.78,
    mars: 0.60,
    earth: 0.45,
    venus: 0.32,
    mercury: 0.20,
  };

  var SOLID_META = [
    { key: "cube",   name: "Cube",         interval: "Saturn–Jupiter", ratio: "1/√3 ≈ 0.577",  rgb: [251, 191, 36],  hex: "#fbbf24" },
    { key: "tetra",  name: "Tetrahedron",  interval: "Jupiter–Mars",   ratio: "1/3 ≈ 0.333",   rgb: [248, 113, 113], hex: "#f87171" },
    { key: "dodeca", name: "Dodecahedron", interval: "Mars–Earth",     ratio: "0.795",         rgb: [192, 132, 252], hex: "#c084fc" },
    { key: "icosa",  name: "Icosahedron",  interval: "Earth–Venus",    ratio: "0.795",         rgb: [96, 165, 250],  hex: "#60a5fa" },
    { key: "octa",   name: "Octahedron",   interval: "Venus–Mercury",  ratio: "1/√3 ≈ 0.577",  rgb: [56, 189, 248],  hex: "#38bdf8" },
  ];

  var PLANET_META = [
    { key: "saturn",  label: "♄ Saturn",  rgb: [251, 191, 36] },
    { key: "jupiter", label: "♃ Jupiter", rgb: [248, 113, 113] },
    { key: "mars",    label: "♂ Mars",    rgb: [192, 132, 252] },
    { key: "earth",   label: "⊕ Earth",   rgb: [52, 211, 153] },
    { key: "venus",   label: "♀ Venus",   rgb: [96, 165, 250] },
    { key: "mercury", label: "☿ Mercury", rgb: [56, 189, 248] },
  ];

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
    var faces = [];
    for (var vi = 0; vi < 12; vi++) {
      var adj = [];
      ico.faces.forEach(function (f, fi) {
        if (f.indexOf(vi) !== -1) adj.push(fi);
      });
      var axis = ico.verts[vi];
      var ref = vNorm(vSub(v[adj[0]], vScale(axis, vDot(v[adj[0]], axis))));
      var tan = vCross(axis, ref);
      adj.sort(function (a, b) {
        return Math.atan2(vDot(v[a], tan), vDot(v[a], ref)) - Math.atan2(vDot(v[b], tan), vDot(v[b], ref));
      });
      faces.push(adj);
    }
    faces = orientFacesOutward(v, faces);
    return { verts: v, faces: faces, edges: edgesFromFaces(faces) };
  }

  function makeSmallStellatedDodecahedron(R) {
    // Exact coplanar stellation: R_core / R_apex = sqrt(3 / (5 + 2*sqrt(5))) ~ 0.5627774
    var coreR = R * Math.sqrt(3 / (5 + 2 * SQRT5));
    var dodeca = makeDodecahedron(coreR);
    var verts = dodeca.verts.slice();
    var faces = [];
    dodeca.faces.forEach(function (f) {
      var c = [0, 0, 0];
      f.forEach(function (idx) { c = vAdd(c, dodeca.verts[idx]); });
      var apexIdx = verts.length;
      verts.push(vScale(vNorm(c), R));
      for (var i = 0; i < f.length; i++) {
        faces.push([f[i], f[(i + 1) % f.length], apexIdx]);
      }
    });
    faces = orientFacesOutward(verts, faces);
    return { verts: verts, faces: faces, edges: edgesFromFaces(faces) };
  }

  function makeGreatStellatedDodecahedron(R) {
    // Exact coplanar stellation: R_core / R_apex = sqrt(1 + phi^2) / (phi^2 * sqrt(3)) ~ 0.4194695
    var coreR = (R * Math.sqrt(1 + PHI * PHI)) / (PHI * PHI * SQRT3);
    var ico = makeIcosahedron(coreR);
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

  function isStellatedScene(sceneName) {
    return sceneName === "harmonices_stellated" || sceneName === "star_polyhedra";
  }

  function KeplerWidget(mount) {
    this.mount = mount;
    var rawScene = mount.getAttribute("data-scene") || "mysterium_nested_solids";
    this.scene = isStellatedScene(rawScene) ? "harmonices_stellated" : "mysterium_nested_solids";
    this.rx = 0.40;
    this.ry = 0.58;
    this.zoom = 1.0;
    this.autoRotate = true;
    this.renderMode = "glass"; // "glass" | "wireframe" | "solid"
    this.scaleMode = "stepped"; // "stepped" | "exact"
    this.stellationMode = "small"; // "small" | "great" | "both"
    this.showOrbs = true;
    this.showLabels = true;
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
        ? "<strong>Harmonices Mundi II.26 (Plates Ss &amp; Tt)</strong> — Kepler–Poinsot Star Polyhedra"
        : "<strong>Mysterium Cosmographicum (Tabula III)</strong> — Interactive 3D Nested Platonic Polyhedra";
    header.appendChild(title);

    var controls = document.createElement("div");
    controls.className = "kepler-3d-controls";

    var self = this;
    if (this.scene === "mysterium_nested_solids") {
      [
        ["stepped", "Stepped Nesting"],
        ["exact", "Exact Caput XIII"],
      ].forEach(function (pair) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "kepler-3d-btn" + (self.scaleMode === pair[0] ? " is-active" : "");
        btn.textContent = pair[1];
        btn.setAttribute("data-mode", pair[0]);
        btn.addEventListener("click", function () {
          self.scaleMode = pair[0];
          controls.querySelectorAll(".kepler-3d-btn[data-mode]").forEach(function (b) {
            b.classList.toggle("is-active", b.getAttribute("data-mode") === pair[0]);
          });
        });
        controls.appendChild(btn);
      });

      var orbBtn = document.createElement("button");
      orbBtn.type = "button";
      orbBtn.className = "kepler-3d-btn is-active";
      orbBtn.textContent = "Orbs";
      orbBtn.addEventListener("click", function () {
        self.showOrbs = !self.showOrbs;
        orbBtn.classList.toggle("is-active", self.showOrbs);
      });
      controls.appendChild(orbBtn);

      var lblBtn = document.createElement("button");
      lblBtn.type = "button";
      lblBtn.className = "kepler-3d-btn is-active";
      lblBtn.textContent = "Labels";
      lblBtn.addEventListener("click", function () {
        self.showLabels = !self.showLabels;
        lblBtn.classList.toggle("is-active", self.showLabels);
      });
      controls.appendChild(lblBtn);
    } else {
      [
        ["small", "Small Stellated {5/2, 5} (Ss)"],
        ["great", "Great Stellated {5/2, 3} (Tt)"],
        ["both", "Compare Both"],
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

    var modeBtn = document.createElement("button");
    modeBtn.type = "button";
    modeBtn.className = "kepler-3d-btn";
    modeBtn.textContent = "Glass";
    modeBtn.addEventListener("click", function () {
      var order = ["glass", "wireframe", "solid"];
      var labels = { glass: "Glass", wireframe: "Wireframe", solid: "Solid" };
      self.renderMode = order[(order.indexOf(self.renderMode) + 1) % order.length];
      modeBtn.textContent = labels[self.renderMode];
    });
    controls.appendChild(modeBtn);

    var resetBtn = document.createElement("button");
    resetBtn.type = "button";
    resetBtn.className = "kepler-3d-btn";
    resetBtn.textContent = "Reset";
    resetBtn.addEventListener("click", function () {
      self.rx = 0.40;
      self.ry = 0.58;
      self.zoom = 1.0;
    });
    controls.appendChild(resetBtn);

    this.rotBtn = document.createElement("button");
    this.rotBtn.type = "button";
    this.rotBtn.className = "kepler-3d-btn is-active";
    this.rotBtn.textContent = "Orbit";
    this.rotBtn.addEventListener("click", function () {
      self.autoRotate = !self.autoRotate;
      self.rotBtn.classList.toggle("is-active", self.autoRotate);
    });
    controls.appendChild(this.rotBtn);

    header.appendChild(controls);
    this.mount.appendChild(header);

    if (this.scene === "mysterium_nested_solids") {
      var legend = document.createElement("div");
      legend.className = "kepler-3d-legend";
      SOLID_META.forEach(function (item) {
        var pill = document.createElement("button");
        pill.type = "button";
        pill.className = "kepler-3d-layer is-active";
        pill.title = "Toggle " + item.name + " (" + item.interval + ", r/R = " + item.ratio + ")";
        pill.innerHTML =
          '<span class="kepler-3d-swatch" style="background:' + item.hex + '"></span>' +
          item.name + " <small>(" + item.interval + ")</small>";
        pill.addEventListener("click", function () {
          self.visibleSolids[item.key] = !self.visibleSolids[item.key];
          pill.classList.toggle("is-active", self.visibleSolids[item.key]);
        });
        legend.appendChild(pill);
      });
      this.mount.appendChild(legend);
    }

    var heightAttr = parseInt(this.mount.getAttribute("data-height") || "480", 10);
    this.logicalW = 820;
    this.logicalH = isNaN(heightAttr) ? 480 : heightAttr;

    this.canvas = document.createElement("canvas");
    this.canvas.className = "kepler-3d-canvas";
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    this.canvas.width = Math.round(this.logicalW * dpr);
    this.canvas.height = Math.round(this.logicalH * dpr);
    this.ctx = this.canvas.getContext("2d");
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    this.mount.appendChild(this.canvas);

    var footer = document.createElement("div");
    footer.className = "kepler-3d-footer";
    footer.textContent =
      this.scene === "harmonices_stellated"
        ? "Drag to orbit · Scroll to zoom · Exact coplanar Q(φ) pentagram faces {5/2, 5} & {5/2, 3}"
        : "Drag to orbit · Scroll to zoom · Toggle solids above · Exact Q(φ) & √3 Caput XIII Platonic ratios";
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
      if (self.rotBtn) self.rotBtn.classList.remove("is-active");
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
      self.zoom = Math.max(0.45, Math.min(3.2, self.zoom * (e.deltaY > 0 ? 0.92 : 1.08)));
    }, { passive: false });
  };

  KeplerWidget.prototype.project = function (v, scale, cx, cy) {
    var persp = 4.4 / (4.4 - v[2] * 0.58);
    return [cx + v[0] * scale * persp, cy - v[1] * scale * persp, v[2], persp];
  };

  KeplerWidget.prototype.drawOrbRing = function (radius, rgb, scale, cx, cy, isLight) {
    var ctx = this.ctx;
    var steps = 64;
    // Equatorial circle in 3D + front silhouette circle
    ctx.beginPath();
    ctx.arc(cx, cy, radius * scale, 0, Math.PI * 2);
    ctx.strokeStyle = "rgba(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + "," + (isLight ? 0.34 : 0.22) + ")";
    ctx.setLineDash([4, 4]);
    ctx.lineWidth = 1.0;
    ctx.stroke();
    ctx.setLineDash([]);

    // Tilted 3D ecliptic ring
    ctx.beginPath();
    for (var i = 0; i <= steps; i++) {
      var ang = (i / steps) * Math.PI * 2;
      var rv = rotVec([radius * Math.cos(ang), 0, radius * Math.sin(ang)], this.rx, this.ry);
      var p = this.project(rv, scale, cx, cy);
      if (i === 0) ctx.moveTo(p[0], p[1]);
      else ctx.lineTo(p[0], p[1]);
    }
    ctx.strokeStyle = "rgba(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + "," + (isLight ? 0.28 : 0.24) + ")";
    ctx.lineWidth = 0.9;
    ctx.stroke();
  };

  KeplerWidget.prototype.drawSceneMeshes = function (meshSpecs, scale, cx, cy, isLight) {
    var ctx = this.ctx;
    var keyLight = vNorm([0.52, 0.72, 0.85]);
    var fillLight = vNorm([-0.60, -0.25, 0.55]);
    var rimLight = vNorm([0.15, -0.70, -0.68]);

    var baseAlpha = this.renderMode === "wireframe" ? 0.03 : this.renderMode === "solid" ? 0.72 : 0.26;
    if (this.scene === "harmonices_stellated" && this.renderMode === "glass") {
      baseAlpha = 0.62;
    }

    var faceQueue = [];
    var edgeQueue = [];

    var self = this;
    meshSpecs.forEach(function (spec) {
      var rVerts = spec.mesh.verts.map(function (v) { return rotVec(v, self.rx, self.ry); });
      var proj = rVerts.map(function (v) { return self.project(v, scale, spec.cx != null ? spec.cx : cx, spec.cy != null ? spec.cy : cy); });

      spec.mesh.faces.forEach(function (f) {
        var zSum = 0;
        for (var i = 0; i < f.length; i++) zSum += rVerts[f[i]][2];
        var n = vNorm(vCross(vSub(rVerts[f[1]], rVerts[f[0]]), vSub(rVerts[f[2]], rVerts[f[0]])));
        var diffKey = Math.max(0, vDot(n, keyLight));
        var diffFill = Math.max(0, vDot(n, fillLight)) * 0.35;
        var diffRim = Math.max(0, Math.abs(vDot(n, rimLight))) * 0.20;
        var lum = Math.min(1.15, 0.24 + diffKey * 0.76 + diffFill + diffRim);
        faceQueue.push({
          proj: proj,
          f: f,
          z: zSum / f.length,
          rgb: spec.rgb,
          alpha: spec.alpha != null ? spec.alpha : baseAlpha,
          lum: lum,
        });
      });

      spec.mesh.edges.forEach(function (e) {
        var zMid = 0.5 * (rVerts[e[0]][2] + rVerts[e[1]][2]);
        edgeQueue.push({
          p0: proj[e[0]],
          p1: proj[e[1]],
          z: zMid,
          rgb: spec.rgb,
          lw: spec.lw || 1.25,
        });
      });
    });

    faceQueue.sort(function (a, b) { return a.z - b.z; });
    edgeQueue.sort(function (a, b) { return a.z - b.z; });

    faceQueue.forEach(function (item) {
      if (item.alpha <= 0.01) return;
      ctx.beginPath();
      for (var idx = 0; idx < item.f.length; idx++) {
        var pt = item.proj[item.f[idx]];
        if (idx === 0) ctx.moveTo(pt[0], pt[1]);
        else ctx.lineTo(pt[0], pt[1]);
      }
      ctx.closePath();
      var r = Math.min(255, Math.round(item.rgb[0] * item.lum));
      var g = Math.min(255, Math.round(item.rgb[1] * item.lum));
      var b = Math.min(255, Math.round(item.rgb[2] * item.lum));
      ctx.fillStyle = "rgba(" + r + "," + g + "," + b + "," + item.alpha + ")";
      ctx.fill();
    });

    edgeQueue.forEach(function (ed) {
      var depthFade = Math.max(0.35, Math.min(1.0, 0.72 + ed.z * 0.28));
      var r = isLight ? Math.round(ed.rgb[0] * 0.72) : ed.rgb[0];
      var g = isLight ? Math.round(ed.rgb[1] * 0.72) : ed.rgb[1];
      var b = isLight ? Math.round(ed.rgb[2] * 0.72) : ed.rgb[2];
      ctx.beginPath();
      ctx.moveTo(ed.p0[0], ed.p0[1]);
      ctx.lineTo(ed.p1[0], ed.p1[1]);
      ctx.strokeStyle = "rgba(" + r + "," + g + "," + b + "," + (depthFade * 0.92).toFixed(2) + ")";
      ctx.lineWidth = ed.lw;
      ctx.stroke();
    });
  };

  KeplerWidget.prototype.render = function () {
    var ctx = this.ctx;
    var w = this.logicalW, h = this.logicalH;
    var cx = w / 2, cy = h / 2;
    var scale = Math.min(w, h) * 0.37 * this.zoom;
    var isLight = document.body.classList.contains("light-mode");

    ctx.clearRect(0, 0, w, h);
    var bgGrad = ctx.createRadialGradient(cx, cy, 12, cx, cy, Math.max(w, h) * 0.65);
    if (isLight) {
      bgGrad.addColorStop(0, "#ffffff");
      bgGrad.addColorStop(1, "#eef2f6");
    } else {
      bgGrad.addColorStop(0, "#151922");
      bgGrad.addColorStop(1, "#0b0e14");
    }
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, w, h);

    if (this.scene === "harmonices_stellated") {
      if (this.stellationMode === "both") {
        this.drawSceneMeshes([
          { mesh: makeSmallStellatedDodecahedron(0.84), rgb: [251, 191, 36], cx: w * 0.29, cy: cy, lw: 1.15 },
          { mesh: makeGreatStellatedDodecahedron(0.84), rgb: [192, 132, 252], cx: w * 0.71, cy: cy, lw: 1.15 },
        ], scale, cx, cy, isLight);
        ctx.font = "600 12px var(--book-font-sans, sans-serif)";
        ctx.textAlign = "center";
        ctx.fillStyle = isLight ? "#334155" : "#cbd5e1";
        ctx.fillText("Plate Ss — Small Stellated {5/2, 5}", w * 0.29, h - 18);
        ctx.fillText("Plate Tt — Great Stellated {5/2, 3}", w * 0.71, h - 18);
      } else {
        var mesh = this.stellationMode === "small"
          ? makeSmallStellatedDodecahedron(1.0)
          : makeGreatStellatedDodecahedron(1.0);
        var col = this.stellationMode === "small" ? [251, 191, 36] : [192, 132, 252];
        this.drawSceneMeshes([{ mesh: mesh, rgb: col, lw: 1.3 }], scale, cx, cy, isLight);
      }
      return;
    }

    var useExact = this.scaleMode === "exact";
    var norm = useExact ? 1 / EXACT_RADII.saturn : 1;
    var orbRadii = {
      saturn: (useExact ? EXACT_RADII.saturn : STEPPED_RADII.saturn) * norm,
      jupiter: (useExact ? EXACT_RADII.jupiter : STEPPED_RADII.jupiter) * norm,
      mars: (useExact ? EXACT_RADII.mars : STEPPED_RADII.mars) * norm,
      earth: (useExact ? EXACT_RADII.earth : STEPPED_RADII.earth) * norm,
      venus: (useExact ? EXACT_RADII.venus : STEPPED_RADII.venus) * norm,
      mercury: (useExact ? EXACT_RADII.mercury : STEPPED_RADII.mercury) * norm,
    };

    var self = this;
    if (this.showOrbs) {
      PLANET_META.forEach(function (pm) {
        self.drawOrbRing(orbRadii[pm.key], pm.rgb, scale, cx, cy, isLight);
      });
    }

    var activeMeshes = [];
    var builders = {
      cube:   { fn: makeCube,         r: orbRadii.saturn,  rgb: [251, 191, 36] },
      tetra:  { fn: makeTetrahedron,  r: orbRadii.jupiter, rgb: [248, 113, 113] },
      dodeca: { fn: makeDodecahedron, r: orbRadii.mars,    rgb: [192, 132, 252] },
      icosa:  { fn: makeIcosahedron,  r: orbRadii.earth,   rgb: [96, 165, 250] },
      octa:   { fn: makeOctahedron,   r: orbRadii.venus,   rgb: [56, 189, 248] },
    };
    SOLID_META.forEach(function (meta) {
      if (self.visibleSolids[meta.key]) {
        var b = builders[meta.key];
        activeMeshes.push({ mesh: b.fn(b.r), rgb: b.rgb, lw: 1.25 });
      }
    });

    this.drawSceneMeshes(activeMeshes, scale, cx, cy, isLight);

    // Radiant Solar core at origin
    var sunGlow = ctx.createRadialGradient(cx, cy, 1, cx, cy, 14);
    sunGlow.addColorStop(0, "rgba(253, 224, 71, 0.95)");
    sunGlow.addColorStop(0.45, "rgba(251, 191, 36, 0.45)");
    sunGlow.addColorStop(1, "rgba(251, 191, 36, 0)");
    ctx.fillStyle = sunGlow;
    ctx.beginPath();
    ctx.arc(cx, cy, 14, 0, Math.PI * 2);
    ctx.fill();
    ctx.beginPath();
    ctx.arc(cx, cy, 3.8, 0, Math.PI * 2);
    ctx.fillStyle = "#f59e0b";
    ctx.fill();

    // Planetary orb labels on right radial meridian
    if (this.showOrbs && this.showLabels) {
      ctx.font = "600 11px var(--book-font-sans, sans-serif)";
      ctx.textAlign = "left";
      ctx.textBaseline = "middle";
      var labelAngles = {
        saturn: -0.35,
        jupiter: -0.15,
        mars: 0.12,
        earth: 0.42,
        venus: 0.78,
        mercury: 1.18,
      };
      PLANET_META.forEach(function (pm) {
        var rPx = orbRadii[pm.key] * scale;
        if (rPx < 12) return;
        var ang = labelAngles[pm.key];
        var lx = cx + Math.cos(ang) * (rPx + 6);
        var ly = cy + Math.sin(ang) * (rPx + 6);
        ctx.fillStyle = isLight ? "#1e293b" : "rgba(" + pm.rgb[0] + "," + pm.rgb[1] + "," + pm.rgb[2] + ",0.92)";
        ctx.fillText(pm.label, lx, ly);
      });
    }
  };

  KeplerWidget.prototype.loop = function () {
    var self = this;
    function tick() {
      if (self.autoRotate) self.ry += 0.0042;
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
