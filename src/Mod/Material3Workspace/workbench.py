#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1-or-later

"""Workbench definition for the Material 3 Workspace."""

import os

import FreeCAD

try:
    import FreeCADGui
except Exception:  # pragma: no cover - FreeCADGui not available in non-Gui runs
    FreeCADGui = None


if FreeCADGui:

    class Material3WorkspaceWorkbench(FreeCADGui.Workbench):
        """Experimental Material 3–styled FreeCAD workbench.

        At this stage the workbench only sets up its identity (icon,
        menu text, tooltip) and basic lifecycle hooks. Layout, theming,
        and Material 3 components will be added in later phases.
        """

        def __init__(self):
            def QT_TRANSLATE_NOOP(context, text):
                return text

            resource_dir = os.path.join(
                FreeCAD.getResourceDir(),
                "Mod",
                "Material3Workspace",
            )

            # Icon path is a placeholder; the SVG can be added later.
            self.__class__.Icon = os.path.join(
                resource_dir,
                "Resources",
                "icons",
                "Material3Workspace.svg",
            )
            self.__class__.MenuText = QT_TRANSLATE_NOOP(
                "Material3Workspace",
                "Material 3 Workspace",
            )
            self.__class__.ToolTip = QT_TRANSLATE_NOOP(
                "Material3Workspace",
                "Experimental Material 3–styled workspace for FreeCAD.",
            )

        def Initialize(self):
            """Executed once when the workbench is first loaded."""
            FreeCAD.Console.PrintLog(
                "Loading Material 3 Workspace workbench, done.\n"
            )

        def Activated(self):
            """Executed when entering the workbench."""
            FreeCAD.Console.PrintLog(
                "Material 3 Workspace workbench activated.\n"
            )

        def Deactivated(self):
            """Executed when leaving the workbench."""
            FreeCAD.Console.PrintLog(
                "Material 3 Workspace workbench deactivated.\n"
            )

        def GetClassName(self):
            """Return the type of workbench."""
            return "Gui::PythonWorkbench"

