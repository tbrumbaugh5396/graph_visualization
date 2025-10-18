"""
Shim package to make `from mvc_mvu import ...` imports work whether running
from source checkout or as an installed package.

If a sibling MVC_MVU repository exists one level up, this shim will ensure it's
importable. Otherwise, it provides minimal placeholders and helpful errors.
"""

import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SIBLING = os.path.join(_ROOT, 'MVC_MVU')
if os.path.isdir(_SIBLING) and _SIBLING not in sys.path:
    sys.path.insert(0, _SIBLING)

# Re-export if real package is available
try:
    from mvc_mvu.core import *  # type: ignore
    from mvc_mvu.messages import *  # type: ignore
    from mvc_mvu.effects import *  # type: ignore
    from mvc_mvu.mvc_adapter import *  # type: ignore
except Exception:
    # Provide friendly guidance if the real framework isn't present
    def __getattr__(name):  # pragma: no cover
        raise ImportError(
            "mvc_mvu framework not found. Ensure MVC_MVU is available next to the project, "
            "or install the framework, or vendor it into the package.")


