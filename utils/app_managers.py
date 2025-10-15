"""
Container for application managers accessible via main_window.managers.
"""


from utils.managers.undo_redo_manager import UndoRedoManager
from utils.managers.hotkey_manager import HotkeyManager
from utils.managers.clipboard_manager import ClipboardManager
from utils.managers.layout_manager import LayoutManager
from utils.managers.file_manager import FileManager
from utils.managers.theme_manager import ThemeManager


class AppManagers:
    def __init__(self, main_window):
        # Instantiate core managers
        self.undo_redo_manager = UndoRedoManager(max_history=50)
        self.clipboard_manager = ClipboardManager()
        self.layout_manager = LayoutManager(main_window)
        self.file_manager = FileManager(main_window)
        self.hotkey_manager = HotkeyManager(main_window)
        self.theme_manager = ThemeManager()

        # Ensure a default theme is set and expose theme database on main_window
        if not self.theme_manager.get_current_theme():
            self.theme_manager.set_theme("Light")
        # Provide legacy access path for existing code
        try:
            main_window.theme_database = self.theme_manager.theme_database
        except Exception:
            # In case main_window isn't fully constructed; ignore
            pass


