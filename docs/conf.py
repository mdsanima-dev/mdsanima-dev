# Copyritht © 2021-2023 Marcin Różewski MDSANIMA


"""Sphinx documentation configuration file for `mdsanima-dev` package."""


import os
import sys


# Append absolute path.
sys.path.append(os.path.abspath("."))


# Project information.
project = "mdsanima-dev"
copyright = "2021-2023, Marcin Różewski MDSANIMA"
author = "Marcin Różewski"
master_doc = "index"
language = "en"

# Sphinx extension modules.
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxext.opengraph",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
]

# Markdown parser.
source_suffix = {
    ".md": "markdown",
}

# Fontawesome options.
FONTAWESOME_CSS_A = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css"
FONTAWESOME_CSS_B = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css"
FONTAWESOME_CSS_C = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css"

# Path options.
templates_path = ["_templates"]
exclude_patterns = ["_images"]
html_static_path = ["_static"]
html_js_files = ["mdsanima.js"]
html_css_files = ["mdsanima.css", FONTAWESOME_CSS_A, FONTAWESOME_CSS_B, FONTAWESOME_CSS_C]

# Theme options.
html_theme = "furo"
html_logo = "_static/images/mdsanima_logo_rc2_light_01_cyan.png"
html_favicon = "_static/images/mdsanima_logo_rc2_light_01_cyan.svg"

# HTML options.
html_show_sphinx = True
html_last_updated_fmt = "%d %B %Y, at %H:%M:%S"

# Theme custom options.
html_theme_options = {
    "navigation_with_keys": True,
    "sidebar_hide_name": False,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/mdsanima-dev/mdsanima-dev/",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}

# External links options.
extlinks = {
    "issue": ("https://github.com/mdsanima-dev/mdsanima-dev/issues/%s", "#"),
    "pull": ("https://github.com/mdsanima-dev/mdsanima-dev/pull/%s", "PR #"),
    "pypi": ("https://pypi.org/project/%s/", ""),
}

# Meta tags config.
ogp_site_url = "https://mdsanima-dev.github.io/mdsanima-dev/"
ogp_image = ogp_site_url + "_static/images/mdsanima_dev_python_package.webp"
ogp_custom_meta_tags = [
    '<meta property="twitter:card" content="summary_large_image" />',
]

# Myst parser config.
myst_all_links_external = True
myst_heading_anchors = 4
