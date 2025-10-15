#!/usr/bin/env python3
"""
Main application file for the Graph Editor.

A comprehensive graph editing application built with wxPython that supports
creating, editing, and managing graphs with nodes and edges.
"""

import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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
