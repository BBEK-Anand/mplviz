import os
import sys
sys.path.insert(0, os.path.abspath('../src'))  # Adjust if your source code is elsewhere

project = 'mplviz'
author = 'BBEK-Anand'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary'
]
autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []

# Use the 'furo' theme for a modern look
# html_theme = 'furo'
# html_theme = 'sphinx_rtd_t/heme'
html_theme = 'alabaster'

# Static files (e.g., custom CSS)
html_static_path = ['_static']

# # Add custom CSS file
# html_css_files = [
#     'custom.css',
# ]

# Optional theme options (check furo docs for more)
html_theme_options = {
        # 'logo': 'logo.png',
    # 'logo_name': True,
    # 'description': 'A fluent, chainable wrapper around Matplotlib ',
    # 'github_user': 'BBEK-Anand',
    # 'github_repo': 'mplviz',
    # 'github_banner': True,
    # 'github_type': 'star',  # 'star' or 'fork'
    # 'fixed_sidebar': True,
    # 'show_powered_by': False,
    # 'show_related': True,
    # 'note_bg': '#FFF59C',
    # 'sidebar_width': '220px',
    # 'page_width': '980px',
}

# # Sidebar config example (optional)
# html_sidebars = {
#     '**': ['sidebar/brand.html', 'sidebar/search.html', 'sidebar/navigation.html', 'sidebar/ethical-ads.html'],
# }


