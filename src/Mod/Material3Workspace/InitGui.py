#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1-or-later

"""GUI initialization for the Material 3 Workspace workbench."""

import FreeCAD

if FreeCAD.GuiUp:
    import FreeCADGui

    # Import the Python workbench class that defines the Material 3 workspace.
    from .workbench import Material3WorkspaceWorkbench

    # Register the workbench with FreeCAD's GUI.
    FreeCADGui.addWorkbench(Material3WorkspaceWorkbench())

