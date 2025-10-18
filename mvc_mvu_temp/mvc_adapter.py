"""Fallback minimal MVC adapter and UI state container."""

from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional


@dataclass
class UIState:
    model_snapshot: Optional[Any] = None

    def __post_init__(self):
        self._widgets: Dict[str, Any] = {}

    def bind_widget(self, name: str, widget: Any) -> None:
        self._widgets[name] = widget

    def get_widget(self, name: str) -> Optional[Any]:
        return self._widgets.get(name)


class MVUAdapter:
    def __init__(self, initial_model: Any, update_fn: Callable[[Any, Any], Any], ui_state: UIState, ui_render: Callable[[UIState, Any], None]) -> None:
        self.model = initial_model
        self.update_fn = update_fn
        self.ui_state = ui_state
        self.ui_render = ui_render
        self.ui_state.model_snapshot = None

    def dispatch(self, message: Any) -> None:
        try:
            result = self.update_fn(message, self.model)
            # result is expected to have .model
            self.model = getattr(result, 'model', self.model)
            self.ui_render(self.ui_state, self.model)
        except Exception:
            # In fallback, swallow to keep UI running
            pass


