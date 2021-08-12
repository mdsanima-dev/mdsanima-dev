"""
mdsanima-dev Setup Package
"""

import sys
import json
import setuptools
import pathlib

HERE = pathlib.Path(__file__).parent

# Get python current and required version from users.
CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

# Initial stderr checking print variable.
mds_sep = ("=" * 26)
mds_uns = "Unsupported Python Version"
mds_ver = "This version of mdsanima-dev requires Python {}.{}"
mds_ins = "but you're trying to install it on Python {}.{}"

# This check and everything above must remain compatible with Python 3.6.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write((
        mds_sep, "\n", mds_uns, "\n", mds_sep, "\n",
        mds_ver, "\n", mds_ins
    ).format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

# Load data from package.json file.
with open(HERE / "package.json") as dt:
    data_package = json.load(dt)

# Load data from README.md file.
with open(HERE / "README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setuptools dynamic package arguments, nice and clean.
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
        'build_sphinx': {
            'version': ('setup.py', data_package["version"]),
            'release': ('setup.py', data_package["version"]),
            'build_dir': ('setup.py', "docs"),
            'source_dir': ('setup.py', "docs/source")}},
)
