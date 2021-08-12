# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
#sys.path.append(os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'mdsanima-dev'
copyright = '2021, MDSANIMA'
author = 'Marcin Rozewski'
master_doc = 'index'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_panels',
    'sphinx_copybutton',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Markdown Parser
# myst_commonmark_only = True
# autosectionlabel_prefix_document = True
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_book_theme'
html_logo = "_static/icons/ic_mdsanima_08_lng_drp_sdw_c.png"
html_favicon = "_static/icons/ic_mdsanima_09_smp_w.png"
panels_add_bootstrap_css = False

html_theme_options = {
    "repository_url": "https://github.com/mdsanima-dev/mdsanima-dev",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": False,
    "home_page_in_toc": True,
    "show_navbar_depth": 2,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
