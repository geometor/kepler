"""Sphinx configuration for GEOMETOR Kepler."""

from __future__ import annotations

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _PROJECT_ROOT.parent

for _front_path in (
    _PROJECT_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
):
    if _front_path.exists() and str(_front_path) not in sys.path:
        sys.path.insert(0, str(_front_path))

_VENV_SITE = _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages"
if _VENV_SITE.exists() and str(_VENV_SITE) not in sys.path:
    sys.path.append(str(_VENV_SITE))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.kepler as module  # noqa: E402
from geometor.kepler.sphinx_ext import (  # noqa: E402
    configure_local_intersphinx,
    register_latin_book_track,
)

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "kepler"
repo_name = "kepler"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

site_title = "Johannes Kepler"
project = site_title
html_title = f"{site_title} • {org_name}"
author = "Johannes Kepler"
copyright = "1596 / 1611 / 1619 / 1621 · 1858–1868 Frisch · Digital Codex GEOMETOR"

if "geometor.kepler.sphinx_ext" not in extensions:  # noqa: F405
    extensions.append("geometor.kepler.sphinx_ext")  # noqa: F405

register_latin_book_track()
configure_local_intersphinx(intersphinx_mapping, _PROJECT_ROOT)  # noqa: F405

html_static_path = ["_static"]
html_css_files = [
    *globals().get("html_css_files", []),
    "kepler_codex.css",
]

autoapi_dirs = [str(_PROJECT_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
if "modules/api/geometor/kepler/index.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("modules/api/geometor/kepler/index.rst")  # noqa: F405
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]

mathjax3_config = {
    "tex": {
        "inlineMath": [["\\(", "\\)"], ["$", "$"]],
        "displayMath": [["\\[", "\\]"], ["$$", "$$"]],
    }
}
