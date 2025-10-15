"""
Selector for the graph editor application.
"""


import gui.main_window as m_main_window
import gui.tool_selector as m_tool_selector

import event_handlers.sidebar_event_handler as m_sidebar_event_handler


def update_selection_display(main_window: "m_main_window.MainWindow"):
    """Update the selection display in the sidebar."""

    selected_nodes = main_window.current_graph.get_selected_nodes()
    selected_edges = main_window.current_graph.get_selected_edges()
    print(
        f"DEBUG: 🎯 update_selection_display: {len(selected_nodes)} nodes, {len(selected_edges)} edges selected"
    )

    if not selected_nodes and not selected_edges:
        main_window.selection_label.SetLabel("Nothing selected")
        main_window.properties_btn.Enable(False)
        m_sidebar_event_handler.hide_curve_controls(main_window)
    elif len(selected_nodes) == 1 and not selected_edges:
        main_window.selection_label.SetLabel(
            f"Node: {selected_nodes[0].text or 'Unnamed'}")
        main_window.properties_btn.Enable(True)
        print("Properties button ENABLED for node")
        m_sidebar_event_handler.hide_curve_controls(main_window)
    elif len(selected_edges) == 1 and not selected_nodes:
        edge = selected_edges[0]
        main_window.selection_label.SetLabel(f"Edge: {edge.text or 'Unnamed'}")
        main_window.properties_btn.Enable(True)
        print("Properties button ENABLED for edge")

        # Update directed checkbox to match selected edge
        main_window.edge_directed_cb.SetValue(edge.directed)
        
        # Show curve controls for ALL edge types (including straight lines with 0 control points)
        edge_type = edge.rendering_type if edge.rendering_type else main_window.canvas.edge_rendering_type
        m_sidebar_event_handler.show_curve_controls(main_window, edge, edge_type)
    else:
        total = len(selected_nodes) + len(selected_edges)
        main_window.selection_label.SetLabel(f"{total} items selected")
        main_window.properties_btn.Enable(False)

        # If multiple edges are selected, sync checkbox with their directed state
        if selected_edges and not selected_nodes:
            # Check if all edges have the same directed state
            first_directed = selected_edges[0].directed
            all_same = all(edge.directed == first_directed
                            for edge in selected_edges)

            if all_same:
                main_window.edge_directed_cb.SetValue(first_directed)
            else:
                # Mixed states - could use 3-state checkbox, but for simplicity use first edge's state
                main_window.edge_directed_cb.SetValue(first_directed)

        m_sidebar_event_handler.hide_curve_controls(main_window)


def on_selection_changed(main_window: "m_main_window.MainWindow"):
    """Handle selection change in canvas."""
    update_selection_display(main_window)
    try:
        if hasattr(main_window, 'mvu_adapter'):
            from mvc_mvu.messages import make_message
            import mvu.main_mvu as m_main_mvu
            nodes = len(main_window.current_graph.get_selected_nodes())
            edges = len(main_window.current_graph.get_selected_edges())
            # For status bar totals we still want all counts, not selected counts
            all_nodes = len(main_window.current_graph.get_all_nodes())
            all_edges = len(main_window.current_graph.get_all_edges())
            main_window.mvu_adapter.dispatch(make_message(m_main_mvu.Msg.SET_COUNTS, nodes=all_nodes, edges=all_edges))
    except Exception:
        pass
