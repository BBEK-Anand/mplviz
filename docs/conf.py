import os
import sys

sys.path.insert(0, os.path.abspath('../src/mplviz'))

print("sys.path:", sys.path)

project = 'mplvis'
copyright = '2025, BBEK-Anand'
author = 'BBEK-Anand'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',       # for Google/Numpy-style docstrings
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_typehints = 'description'  # keeps type hints in descriptions, less clutter

html_theme = "sphinx_rtd_theme" # if installed
html_static_path = ['_static']
