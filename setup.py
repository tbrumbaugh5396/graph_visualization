#!/usr/bin/env python3
"""
Setup script for Dependency Chart (Graph Editor) Desktop Application
"""

from setuptools import setup, find_packages


setup(
	name="dependency-chart",
	version="0.1.0",
	description="Dependency Chart / Graph Editor (wxPython)",
	packages=find_packages(include=[
		"gui",
		"event_handlers",
		"models",
		"file_io",
		"utils",
		"mvu",
		"gui.*",
		"event_handlers.*",
		"models.*",
		"file_io.*",
		"utils.*",
		"mvu.*",
	]),
	py_modules=["main", "app"],
	include_package_data=True,
	package_data={
		"utils": [
			"config/*.json",
			"managers/theme_manager/*.json",
		],
	},
	install_requires=[
		"mvc-mvu @ git+https://github.com/tbrumbaugh5396/wxPython-MVC-MVU-architecture.git@76cfa1e78aaf33b92273402cc9f92bcc3eabca8e",
		"numpy<2.0.0",
		"typing_extensions==4.14.0",
		"wxPython==4.2.1",
		"Pillow==10.1.0",
	],
	entry_points={
		"console_scripts": [
			"dependency-chart=main:main",
		],
		"gui_scripts": [
			"dependency-chart-gui=main:main",
		],
	},
	python_requires=">=3.9",
)
