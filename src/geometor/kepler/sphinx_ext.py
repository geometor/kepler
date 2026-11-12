"""Runtime Sphinx & photon-platform/publish integration for GEOMETOR Kepler.

Ensures synchronized 4-track ``:layout: book`` companion navigation
(``en``, ``la``, ``summary``, ``notes``) and configures offline-safe local
``intersphinx`` inventories across sister GEOMETOR repositories.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.application import Sphinx

SISTER_REPOS: tuple[str, ...] = (
    "model",
    "euclid",
    "elements",
    "divine",
    "pacioli",
    "pappus",
    "proclus",
    "aristotle",
    "hilbert",
    "hoenen",
    "wildberger",
    "phyllotaxis",
    "ptolemy",
    "etc",
    "altshiller-court",
)


def register_latin_book_track() -> None:
    """Ensure ``<stem>-la`` Latin primary-source tracks are registered in ``book``."""
    try:
        from photon_platform.publish import book
    except ImportError:
        return

    la_pattern = (r"^(.+)[._-]la$", "la", "Latin")
    if not any(key == "la" for _pat, key, _lbl in book._TRACK_SUFFIX_PATTERNS):
        book._TRACK_SUFFIX_PATTERNS.append(la_pattern)

    book._AUX_TRACK_BASENAMES.add("la")
    la_aux_re = re.compile(r"^.+[._-]la$")
    if not any(p.pattern == la_aux_re.pattern for p in book._AUX_TRACK_PATTERNS):
        book._AUX_TRACK_PATTERNS.append(la_aux_re)


def configure_local_intersphinx(
    intersphinx_mapping: dict[str, Any],
    project_root: Path,
) -> None:
    """Bind local ``objects.inv`` files for sister GEOMETOR repositories offline."""
    geometor_dir = project_root.parent
    for sister in SISTER_REPOS:
        inv = geometor_dir / sister / "docs" / "objects.inv"
        if inv.is_file():
            intersphinx_mapping[sister] = (
                f"https://geometor.github.io/{sister}",
                (str(inv.resolve()), None),
            )
    for key in list(intersphinx_mapping.keys()):
        _uri, inv_target = intersphinx_mapping[key]
        if inv_target is None:
            intersphinx_mapping.pop(key, None)


def setup(app: Sphinx) -> dict[str, Any]:
    """Sphinx extension entry point."""
    _ = app
    register_latin_book_track()
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
