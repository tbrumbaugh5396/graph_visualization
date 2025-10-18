#!/usr/bin/env python3
"""
Main application file for the Graph Editor.

A comprehensive graph editing application built with wxPython that supports
creating, editing, and managing graphs with nodes and edges.
"""

import sys
import os
from utils.path_helpers import ensure_project_on_path, ensure_mvc_mvu_on_path

# Ensure paths work for both source and package execution
ensure_project_on_path(__file__)
ensure_mvc_mvu_on_path()

from app import GraphEditorApp


def main():
    """Main entry point."""
    try:
        # Create and run the application
        app = GraphEditorApp(False)
        app.MainLoop()
    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt. Shutting down gracefully...")
        if hasattr(app, 'main_window'):
            app.main_window.Close()
        sys.exit(0)


if __name__ == "__main__":
    main()
