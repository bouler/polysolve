# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import polysolve
from datetime import date

project = 'polysolve'
author = polysolve.__author__
release = polysolve.__version__
copyright = f'{author}, {date.today().year}'

extensions = [
"sphinx.ext.autodoc",
"sphinx.ext.napoleon",
"sphinx.ext.autosummary",
"sphinx_autodoc_typehints",
"sphinx.ext.intershinx"
]

intersphinx_mapping = {'python': ('https://docs.python.org/3/', None)}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
