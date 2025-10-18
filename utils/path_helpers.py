"""
Utilities to ensure the project and optional sibling dependencies are importable
both when running as a source checkout (python main.py) and when installed as a
package (entry points).
"""

import os
import sys
from typing import Optional


def ensure_project_on_path(anchor_file: Optional[str] = None) -> None:
    """Ensure project root is on sys.path for direct execution.

    If anchor_file is provided, it is used to resolve the project root; otherwise
    we walk up from this file.
    """
    try:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        root = base
        if anchor_file:
            root = os.path.dirname(os.path.abspath(anchor_file))
        if root not in sys.path:
            sys.path.insert(0, root)
    except Exception:
        pass


def ensure_mvc_mvu_on_path() -> None:
    """Ensure the optional MVC_MVU sibling repo is importable if present."""
    try:
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sibling = os.path.join(root, 'MVC_MVU')
        if os.path.isdir(sibling) and sibling not in sys.path:
            sys.path.insert(0, sibling)
    except Exception:
        pass


