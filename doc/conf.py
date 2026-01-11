# Configuration file for the Sphinx documentation builder.

project = 'Project Specification'
copyright = '2026, Project Team'
author = 'Project Team'

extensions = [
    'sphinxcontrib.mermaid',
    'sphinx.ext.todo',
]

todo_include_todos = True


mermaid_cmd = 'npx @mermaid-js/mermaid-cli'
mermaid_output_format = 'png'


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'

