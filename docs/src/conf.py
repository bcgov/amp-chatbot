'''
docs.src.conf.py

Sphinx docs configuration file
'''

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import re

# # Parse project, author, release from setup.py
with open('../../LICENSE', 'r', encoding='utf-8') as file:
    license_file = file.read()

with open('../../setup.py', 'r', encoding='utf-8') as file:
    setup_file = file.read()

PARSE_QUOTES = r"[\'\"](.*?)[\'\"]"  # parse text between quotes

package_name = re.search(r"name=[\'\"](.*?)[\'\"]", setup_file).group()
package_name = re.search(PARSE_QUOTES, package_name).group()
package_name = package_name.strip('\'').strip('\"')

version_num = re.search(r"version=[\'\"](.*?)[\'\"]", setup_file).group()
version_num = re.search(PARSE_QUOTES, version_num).group()
version_num = version_num.strip('\'').strip('\"')

author_tag = re.search(r"author=[\'\"](.*?)[\'\"]", setup_file).group()
author_tag = re.search(PARSE_QUOTES, author_tag).group()
author_tag = author_tag.strip('\'').strip('\"')

sys.path.insert(0, os.path.abspath(f'../{package_name}/'))  # replace with project name
sys.path.insert(0, os.path.abspath('../'))


# required
project = package_name
copyright = license_file  # pylint: disable=redefined-builtin
author = author_tag
release = version_num

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx_mdinclude', 'sphinxcontrib.jquery']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # pylint: disable=invalid-name
