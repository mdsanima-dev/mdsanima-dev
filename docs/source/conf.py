# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Sphinx configuration file for ``mdsanima-dev`` package documentation."""


import os
import sys


# append path
sys.path.append(os.path.abspath("."))


# project information
project = "mdsanima-dev"
copyright = "2021-2022, Marcin Różewski MDSANIMA"
author = "Marcin Różewski"
master_doc = "index"
language = "en"

# sphinx extension modules
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
]

# markdown parser
source_suffix = {
    ".txt": "markdown",
    ".md": "markdown",
}

# path options
templates_path = ["_templates"]
exclude_patterns = ["_images"]
html_static_path = ["_static"]
html_css_files = ["css/furo-mdsanima.css"]
html_js_files = ["js/furo-mdsanima.js"]

# theme options
html_theme = "furo"
html_logo = "_static/svg/logo_mdsanima_default_14-lime.svg"
html_favicon = "_static/svg/logo_mdsanima_default_14-lime.svg"

# html options
html_show_sphinx = True

# theme options custom
html_theme_options = {
    "navigation_with_keys": True,
    "sidebar_hide_name": False,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/mdsanima-dev/mdsanima-dev/",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}

# extlinks options
extlinks = {
    "issue": ("https://github.com/mdsanima-dev/mdsanima-dev/issues/%s", "#"),
    "pull": ("https://github.com/mdsanima-dev/mdsanima-dev/pull/%s", "PR #"),
    "pypi": ("https://pypi.org/project/%s/", ""),
}
