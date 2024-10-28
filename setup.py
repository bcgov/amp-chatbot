"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from os import path

from setuptools import setup, find_packages


HERE = path.abspath(path.dirname(__file__))
DESCRIPTION = 'CDW Hello World Project Stub Python module'

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


setup(
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    #
    # $ pip install helloworld
    #
    name='helloworld',  # Required

    # Versions should comply with https://www.python.org/dev/peps/pep-0440/:
    # At this point we are using an incremental version number as we do not
    # expect to use/have an API and thus do not need to convey anything about
    # stability from that point of view
    version='1',  # Required

    # This is a one-line DESCRIPTION or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description=DESCRIPTION,  # Required
    long_description=LONG_DESCRIPTION,  # Optional
    long_description_content_type='text/markdown',  # Optional

    # This should be a valid link to your project's main homepage.
    url='https://dev.azure.com/BC-ISDBI',  # Optional

    # This should be your name or the name of the organization which owns the
    # project.
    author='BC-ISDBI',  # Optional

    # This should be a valid email address corresponding to the author
    author_email='sean.hayes@gov.bc.ca',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    keywords='cdw database core hello world helloworld',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'env', 'tests']),  # Required
    install_requires=['requests>=2.27.1'],  # Optional
    extras_require={  # Optional
        'dev': ['pycodestyle>=2.8.0', 'pylint>=2.12.2'],
        'test': ['pytest-cov>=3.0.0', 'pytest>=7.0.1', 'bandit>=1.7.4'],
        'docs': [
            'sphinx_rtd_theme>=1.2.0',
            'myst-parser>=1.0.0',
            'sphinx-mdinclude>=0.5.3',
            'sphinx>=6.1.3',
            'sphinxcontrib.jquery>=4.1',
        ],
    },
)
