# Graph Editor Tool

A comprehensive graph editing application built with wxPython that supports creating, editing, and managing graphs with nodes and edges.

## Features

- **Graph Management**: Create, load, save, import, copy, and delete graphs
- **DOT Format Support**: Full import/export compatibility with Graphviz DOT format
- **Cluster/Container System**: Hierarchical node organization with expand/collapse functionality
- **Node and Edge Editing**: Add, delete, copy, and modify graph elements
- **Advanced Edge Types**: Straight, curved, Bézier, B-spline, NURBS, polyline, and composite curves
- **Selection Tools**: Select nodes, edges, or everything including convex shape selection
- **3D Positioning**: Set x, y, z coordinates for nodes and edges
- **Infinite Zoom**: Zoom in and out of the canvas infinitely
- **Layout Algorithms**: Apply various layout algorithms to organize graphs
- **Metadata Support**: Add and modify metadata for graphs, nodes, and edges
- **Drag and Drop**: Move elements around the canvas with smart snapping

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

## Project Structure

- `main.py` - Main application entry point
- `models/` - Data models for graphs, nodes, and edges
- `gui/` - GUI components and windows
- `file_io/` - File import/export functionality (DOT format, JSON)
- `utils/` - Utility functions and algorithms
- `examples/` - Sample graph files, demos, and documentation
- `data/` - Application data and templates

## Documentation

- `examples/README_layouts.md` - Layout algorithms guide
- `examples/README_clusters.md` - DOT cluster and container integration guide 