# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))  # So Sphinx can find mplviz

# -- Project information -----------------------------------------------------
project = 'mplviz'
author = 'BBEK-Anand'
copyright = '2025, BBEK-Anand'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',  # Enables Markdown support
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']
