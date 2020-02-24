#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from setuptools import setup, find_packages

###################################################################

PACKAGES = []
META_PATH = os.path.join("kcrw", "apple_news", "__init__.py")

KEYWORDS = ['kcrw.apple_news', ]
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

###################################################################

about = {}
base = os.path.dirname(__file__)
with open(os.path.join(base, "kcrw", "apple_news", "__init__.py")) as f:
    exec(f.read(), about)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['requests[security]', 'six', 'click', 'click-log', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    name=about["__title__"],
    author=about["__author__"],
    author_email=about["__email__"],
    version=about["__version__"],
    description=about["__summary__"],
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    license=about["__license__"],
    url=about["__url__"],
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(include=['kcrw.apple_news']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
    entry_points='''
        [console_scripts]
        apple_news_api=kcrw.apple_news.command:cli
    '''
)
