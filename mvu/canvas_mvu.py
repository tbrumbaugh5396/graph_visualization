from typing import Any, Optional

from mvc_mvu.core import UpdateResult


def update(t: Any, d: dict, model) -> Optional[UpdateResult]:
    name = getattr(t, 'name', None)
    if name == 'SET_GRID_COLOR':
        new_model = type(model)(**{**model.__dict__, 'grid_color': (int(d['r']), int(d['g']), int(d['b']))})
        return UpdateResult(model=new_model)
    if name in ('SET_GRID_VISIBLE', 'TOGGLE_GRID'):
        visible = (not model.grid_visible) if name == 'TOGGLE_GRID' else bool(d['visible'])
        new_model = type(model)(**{**model.__dict__, 'grid_visible': visible})
        return UpdateResult(model=new_model)
    if name in ('SET_SNAP_ENABLED', 'TOGGLE_SNAP'):
        enabled = (not model.snap_enabled) if name == 'TOGGLE_SNAP' else bool(d['enabled'])
        new_model = type(model)(**{**model.__dict__, 'snap_enabled': enabled})
        return UpdateResult(model=new_model)
    if name in ('ZOOM_IN', 'ZOOM_OUT', 'ZOOM_FIT'):
        action = 'in' if name == 'ZOOM_IN' else ('out' if name == 'ZOOM_OUT' else 'fit')
        new_model = type(model)(**{**model.__dict__, 'zoom_seq': model.zoom_seq + 1, 'last_zoom_action': action})
        return UpdateResult(model=new_model)
    if name == 'SET_MOVE_SENSITIVITY':
        new_model = type(model)(**{**model.__dict__, 'move_x_sens': float(d['x']), 'move_y_sens': float(d['y']), 'move_inverted': bool(d['inverted'])})
        return UpdateResult(model=new_model)
    if name == 'SET_ZOOM_SENSITIVITY':
        new_model = type(model)(**{**model.__dict__, 'zoom_sensitivity': float(d['value'])})
        return UpdateResult(model=new_model)
    if name == 'SET_ROTATION':
        new_model = type(model)(**{**model.__dict__, 'rotation_deg': float(d['angle'])})
        return UpdateResult(model=new_model)
    return None


def render(ui_state, model, last) -> None:
    try:
        mw = ui_state.get_widget('main_window') if ui_state else None
        if not mw or not hasattr(mw, 'canvas') or not mw.canvas:
            return
        # Grid color
        if model.grid_color is not None and (last is None or getattr(last, 'grid_color', None) != model.grid_color):
            mw.canvas.grid_color = model.grid_color
            if hasattr(mw, 'grid_color_btn'):
                import wx as _wx
                mw.grid_color_btn.SetBackgroundColour(_wx.Colour(*model.grid_color))
            mw.canvas.Refresh()
        # Grid visibility
        if last is None or getattr(last, 'grid_visible', None) != model.grid_visible:
            mw.canvas.grid_style = 'grid' if model.grid_visible else 'none'
            mw.canvas.Refresh()
        # Snap
        if last is None or getattr(last, 'snap_enabled', None) != model.snap_enabled:
            if hasattr(mw.canvas, 'grid_snapping_enabled'):
                mw.canvas.grid_snapping_enabled = model.snap_enabled
            if hasattr(mw.canvas, 'snap_to_grid'):
                mw.canvas.snap_to_grid = model.snap_enabled
        # Zoom sequence
        if last is None or getattr(last, 'zoom_seq', None) != model.zoom_seq:
            try:
                if model.last_zoom_action == 'in':
                    mw.canvas.zoom_in_at_mouse()
                elif model.last_zoom_action == 'out':
                    mw.canvas.zoom_out_at_mouse()
                elif model.last_zoom_action == 'fit':
                    mw.canvas.zoom_to_fit()
                if hasattr(mw, 'update_status_bar'):
                    mw.update_status_bar()
            except Exception:
                pass
        # Move sensitivity
        if last is None or getattr(last, 'move_x_sens', None) != model.move_x_sens or getattr(last, 'move_y_sens', None) != model.move_y_sens or getattr(last, 'move_inverted', None) != model.move_inverted:
            mw.canvas.set_move_sensitivity(model.move_x_sens, model.move_y_sens, model.move_inverted)
        # Zoom sensitivity
        if last is None or getattr(last, 'zoom_sensitivity', None) != model.zoom_sensitivity:
            if hasattr(mw.canvas, 'set_zoom_sensitivity'):
                mw.canvas.set_zoom_sensitivity(model.zoom_sensitivity)
            else:
                setattr(mw.canvas, 'zoom_sensitivity', model.zoom_sensitivity)
        # Rotation
        if last is None or getattr(last, 'rotation_deg', None) != model.rotation_deg:
            mw.canvas.set_world_rotation(model.rotation_deg)
    except Exception as e:
        print(f"canvas_mvu.render error: {e}")


