# Copyritht © 2021-2023 Marcin Różewski MDSANIMA


"""Setuptools dynamic package. This setup allow to build Sphinx Documentation only."""


import setuptools

from mdsanima_dev._version import __version__  # pylint: disable=E0611 disable=E0401


# Setuptools dynamic package arguments.
setuptools.setup(
    command_options={
        "build_sphinx": {
            "version": ("setup.py", __version__),
            "release": ("setup.py", __version__),
            "source_dir": ("setup.py", "docs"),
            "build_dir": ("setup.py", "build"),
            "builder": ("setup.py", "dirhtml"),
        }
    },
)
