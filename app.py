#!/usr/bin/env python3
"""
Main application file for the Graph Editor.

A comprehensive graph editing application built with wxPython that supports
creating, editing, and managing graphs with nodes and edges.
"""


print("🚀 DEBUG: main.py started - debug code is active!")

import sys
import os

# Check if wxPython is available
try:
    import wx
except ImportError:
    print("Error: wxPython is not installed.")
    print("Please install it using: pip install wxPython")
    sys.exit(1)


# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import MainWindow


class GraphEditorApp(wx.App):
    """Main application class."""

    def OnInit(self):
        """Initialize the application."""

        # Create and show the main window
        self.main_window = MainWindow()
        self.main_window.Show()
        self.SetTopWindow(self.main_window)

        return True

    def OnExit(self):
        """Handle application exit."""
        # Perform any cleanup here if needed
        if hasattr(self, 'main_window'):
            self.main_window.Destroy()
        return super().OnExit()
