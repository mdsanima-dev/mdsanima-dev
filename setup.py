# Copyritht © 2021-2023 Marcin Różewski MDSANIMA


"""Setuptools dynamic package. This setup allow to build Sphinx Documentation only."""


from __future__ import annotations

import json
import pathlib

import setuptools


HERE = pathlib.Path(__file__).parent

with open(HERE / "package.json", "r", encoding="utf-8") as data:
    package = json.load(data)

setuptools.setup(
    command_options={
        "build_sphinx": {
            "version": ("setup.py", package["version"]),
            "release": ("setup.py", package["version"]),
            "source_dir": ("setup.py", "docs"),
            "build_dir": ("setup.py", "build"),
            "builder": ("setup.py", "dirhtml"),
        }
    },
)
