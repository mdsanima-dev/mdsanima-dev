#!/usr/bin/python3

# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Setuptools ``mdsanima-dev`` dynamic package. This setup allow to build
Sphinx Documentation and SHELL Script."""


import json
import pathlib
import sys

import setuptools


# path variable
HERE = pathlib.Path(__file__).parent

# get python current and required version from users
CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

# initial stderr checking print variable
m_sep = "=" * 26
m_uns = "Unsupported Python Version"
m_ver = "This version of mdsanima-dev requires Python {}.{}"
m_ins = "but you're trying to install it on Python {}.{}"

# this check and everything above must remain compatible with Python 3.6
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        (m_sep, "\n", m_uns, "\n", m_sep, "\n", m_ver, "\n", m_ins).format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)

# load data from package.json file
with open(HERE / "package.json") as dt:
    data_package = json.load(dt)

# load data from README.md file
with open(HERE / "README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# setuptools dynamic package arguments
setuptools.setup(
    name=data_package["name"],
    version=data_package["version"],
    author=data_package["author"]["name"],
    author_email=data_package["author"]["email"],
    description=data_package["description"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=data_package["homepage"],
    project_urls=data_package["project_urls"],
    classifiers=data_package["classifiers"],
    package_dir={"": "src"},
    package_data={"": ["json/*.json"]},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    license=data_package["license"],
    extras_require=data_package["extra_require"],
    keywords=data_package["keywords"],
    command_options={
        "build_sphinx": {
            "version": ("setup.py", data_package["version"]),
            "release": ("setup.py", data_package["version"]),
            "source_dir": ("setup.py", "docs"),
            "build_dir": ("setup.py", "build"),
            "builder": ("setup.py", "dirhtml"),
        }
    },
    entry_points={
        "console_scripts": [
            "mdsanima-dev = mdsanima_dev.utils.converts:main",
        ],
    },
)
