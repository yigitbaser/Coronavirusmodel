#TODO Add to description
"""

"""
"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='CoronavirusModel',
    version='0.0.1',
    license='yigit.baser',
    description='Environment for modelling NCOV19',

    author='Yigit Baser',

    url="https://github.com/yigitbaser/Coronavirusmodel",

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires="requirements.txt",

    entry_points={
        'console_scripts': [
            'tasks = tasks.cli:tasks_cli',
        ]
    },
)