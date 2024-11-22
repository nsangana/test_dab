"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the dabs_start project.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import dabs_start

setup(
    name="dabs_start",
    version=dabs_start.__version__,
    url="https://databricks.com",
    author="naveen.sangana@databricks.com",
    description="wheel file based on dabs_start/src",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={
        "packages": [
            "main=dabs_start.main:main"
        ]
    },
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
)
