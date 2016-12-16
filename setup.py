#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation
# All rights reserved.
#
# Distributed under the terms of the MIT License
#-------------------------------------------------------------------------

import setuptools
import sys

with open('README', 'r', encoding='utf-8') as f:
    long_description = f.read()

PACKAGES = ['pep514tools']

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Win32 (MS Windows)',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup_cfg = dict(
    name='pep514tools',
    version='0.1.0',
    description='Python module for finding, modifying and cleaning up registered Python environments',
    long_description=long_description,
    author='Steve Dower',
    author_email='steve.dower@python.org',
    url='https://github.com/zooba/pep514tools',
    packages=PACKAGES,
)

from setuptools import setup
setup(**setup_cfg)
