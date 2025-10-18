"""Fallback minimal side-effect helpers.

These provide command factories that return simple descriptors. The app treats
them as opaque objects; the real framework would execute them.
"""

from typing import Any, Callable, Dict


class Commands:
    @staticmethod
    def read_file(path: str, on_success: Callable[[str], Any], on_error: Callable[[Exception], Any]) -> Dict[str, Any]:
        return {
            "type": "read_file",
            "path": path,
            "on_success": on_success,
            "on_error": on_error,
        }

    @staticmethod
    def write_file(path: str, content: str, on_success: Callable[[], Any], on_error: Callable[[Exception], Any]) -> Dict[str, Any]:
        return {
            "type": "write_file",
            "path": path,
            "content": content,
            "on_success": on_success,
            "on_error": on_error,
        }


