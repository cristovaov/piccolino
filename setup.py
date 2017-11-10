#!/usr/bin/env python
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup, find_packages

__version__ = '0.1.0+development'

setup(
    name='piccolino',
    version=__version__,
    description='An exercice in python',
    url='https://github.com/cristovaov/piccolino',
    author='Cristovao Verstraeten',
    author_email='cristovao@apleasantview.com',
    license='TBD',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'piccolino = piccolino.cli:main'
        ]
    },
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')]
)
