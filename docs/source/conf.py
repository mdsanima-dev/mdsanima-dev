# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Sphinx configuration file for ``mdsanima-dev`` documentation package."""


import os
import sys


# append path
sys.path.append(os.path.abspath("."))


# project information
project = "mdsanima-dev"
copyright = "2021-2022, Marcin Różewski MDSANIMAs"
author = "Marcin Różewski"
master_doc = "index"

# sphinx extension modules
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_panels",
    "sphinx_inline_tabs",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
]

# path templates
templates_path = ["_templates"]

# path static
html_static_path = ["_static"]

# markdown parser
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# path ignore direcotry
exclude_patterns = []

# theme options
html_theme = "furo"
html_logo = "_static/icons/ic_mdsanima_08_lng_drp_sdw_c.png"
html_favicon = "_static/icons/ic_mdsanima_09_smp_w.png"

# html options
html_use_modindex = False
html_use_index = False
panels_add_bootstrap_css = False

# theme options custom
html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/mdsanima-dev/mdsanima-dev",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "_blank",
        },
    ],
    "navigation_with_keys": True,
    "dark_css_variables": {
        "color-highlight-on-target": "#082542",
    },
}

# options for extlinks
extlinks = {
    "issue": ("https://github.com/mdsanima-dev/mdsanima-dev/issues/%s", "#"),
    "pull": ("https://github.com/mdsanima-dev/mdsanima-dev/pull/%s", "PR #"),
    "pypi": ("https://pypi.org/project/%s/", ""),
}
