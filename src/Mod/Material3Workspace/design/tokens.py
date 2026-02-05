#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1-or-later

"""Material 3 design tokens for the Material 3 Workspace.

This module centralizes the design primitives (colors, typography, shape,
spacing, elevation) used by the Material 3 Workspace so that:

* Qt widgets and QSS rules can share a single source of truth.
* The visual language stays consistent as the workspace grows.
* Future theming (e.g. dark mode or different seed colors) can be
  introduced by swapping token values without rewriting UI code.

The values are chosen to approximate Google Material 3 while remaining
practical to implement with Qt/QSS. They intentionally avoid depending on
platform APIs so that the workbench behaves consistently across systems.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


# ---------------------------------------------------------------------------
# Color system
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ColorScheme:
    """Simplified Material 3 color scheme.

    Hex values are in the form "#RRGGBB". The roles follow the Material 3
    naming where practical, but are trimmed to those that are useful for
    a CAD UI (panels, app bar, buttons, chips, and overlays).
    """

    primary: str
    on_primary: str
    primary_container: str
    on_primary_container: str

    secondary: str
    on_secondary: str

    surface: str
    surface_container_low: str
    surface_container: str
    surface_container_high: str

    surface_variant: str
    on_surface: str
    on_surface_variant: str

    outline: str
    outline_variant: str

    error: str
    on_error: str

    background: str
    on_background: str


# A light scheme tuned for a neutral–blue, workspace-friendly appearance.
LIGHT_COLOR_SCHEME = ColorScheme(
    primary="#146C94",
    on_primary="#FFFFFF",
    primary_container="#D0E4FF",
    on_primary_container="#001D33",
    secondary="#556370",
    on_secondary="#FFFFFF",
    surface="#F9FBFF",
    surface_container_low="#F1F4FA",
    surface_container="#E5E9F2",
    surface_container_high="#D7DEE9",
    surface_variant="#D7E2EE",
    on_surface="#111318",
    on_surface_variant="#404753",
    outline="#707783",
    outline_variant="#B6C0CC",
    error="#BA1A1A",
    on_error="#FFFFFF",
    background="#F3F5FB",
    on_background="#111318",
)


#: Exposed alias for the scheme currently used by the workspace.
#:
#: When dark mode or alternative colorways are introduced, the workspace
#: can swap this binding while keeping QSS and widget code unchanged.
COLOR_SCHEME: ColorScheme = LIGHT_COLOR_SCHEME


# ---------------------------------------------------------------------------
# Typography
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class TypeStyle:
    """Logical typography token.

    The values are intended to be mapped to :class:`QtGui.QFont` instances
    by UI code or helper functions:

    * ``family``       → QFont family name
    * ``size``         → point size
    * ``weight``       → QFont weight (e.g. 400 normal, 500 medium, 600 semi-bold)
    * ``letter_spacing`` → additional spacing in percentage (Qt uses 100 = normal)
    * ``line_height``  → multiple of font point size (for layout calculations)
    """

    family: str
    size: int
    weight: int
    letter_spacing: float
    line_height: float


DEFAULT_FONT_FAMILY = "Segoe UI"  # Reasonable default on Windows; Qt will fall back.


TYPE_SCALE: Dict[str, TypeStyle] = {
    # Panel titles, major labels
    "headlineSmall": TypeStyle(
        family=DEFAULT_FONT_FAMILY,
        size=18,
        weight=500,
        letter_spacing=0.0,
        line_height=1.25,
    ),
    # Dock / section headers, app bar title
    "titleMedium": TypeStyle(
        family=DEFAULT_FONT_FAMILY,
        size=15,
        weight=500,
        letter_spacing=0.0,
        line_height=1.25,
    ),
    # Primary button labels, prominent controls
    "labelLarge": TypeStyle(
        family=DEFAULT_FONT_FAMILY,
        size=13,
        weight=500,
        letter_spacing=0.1,
        line_height=1.15,
    ),
    # General body copy in panels
    "bodyMedium": TypeStyle(
        family=DEFAULT_FONT_FAMILY,
        size=12,
        weight=400,
        letter_spacing=0.0,
        line_height=1.4,
    ),
}


# ---------------------------------------------------------------------------
# Shape & spacing
# ---------------------------------------------------------------------------

# Corner radii in device-independent pixels.
SHAPE_RADIUS_SMALL = 4
SHAPE_RADIUS_MEDIUM = 8
SHAPE_RADIUS_LARGE = 12


# Spacing scale in device-independent pixels.
SPACING_XS = 4
SPACING_SM = 8
SPACING_MD = 12
SPACING_LG = 16
SPACING_XL = 24


# ---------------------------------------------------------------------------
# Elevation
# ---------------------------------------------------------------------------

#: Logical elevation levels used to differentiate surfaces.
#:
#: These are not pixel values by themselves; instead, they are intended to
#: drive QSS rules (e.g. slightly darker background, stronger border, or
#: shadow) for different component containers.
ELEVATION_LEVELS: Dict[str, int] = {
    "level0": 0,  # base window background
    "level1": 1,  # standard panels and app bar
    "level2": 2,  # raised cards or in-viewport overlays
    "level3": 3,  # transient surfaces (menus, popovers)
}


__all__ = [
    "ColorScheme",
    "ColorScheme",
    "COLOR_SCHEME",
    "LIGHT_COLOR_SCHEME",
    "TypeStyle",
    "TYPE_SCALE",
    "DEFAULT_FONT_FAMILY",
    "SHAPE_RADIUS_SMALL",
    "SHAPE_RADIUS_MEDIUM",
    "SHAPE_RADIUS_LARGE",
    "SPACING_XS",
    "SPACING_SM",
    "SPACING_MD",
    "SPACING_LG",
    "SPACING_XL",
    "ELEVATION_LEVELS",
]

