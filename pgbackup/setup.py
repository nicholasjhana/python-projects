"""
Setup is a standard file for creating insallable packages.

This runs a setup function that determiens dependencies, looks for packages that need to be built, and creates the metadata for publishing in pypy.

"""

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_descrption = f.read()

setup(
        name='pgbackup',
        version='0.1.0',
        author='Nicholas Jhana',
        author_email='nicholas@nicholasjhana.com,
        descrption='A utility for backing up PostgreSQL databases.',
        long_descrption=long_descrption,

        #indicates the type of long descrption and how to parse
        long_descrption_content_type='text/markdown',

        #where this project can be found
        url='https://github.com/nicholasjhana/python-projects/pgbackup',

        # find the packages that make up this project.
        packages=find_packages('src')
)
