#!/usr/bin/env python
# coding: utf-8

import codecs
import os

from setuptools import find_packages, setup


def read(fname):
    """
    """
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pytld',
    version='0.2.0',
    description='Tld is obtained by url or full domain name',
    long_description=read('README'),
    author='MyKings',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
    ],
    keywords='tld, top level domain names, python',
    packages=find_packages(),
    package_dir={},
    package_data={},
    include_package_data=True,
    author_email='xsseroot@gmail.com',
    url='https://github.com/MyKings/pytld',
    license='MPL 1.1/GPL 2.0/LGPL 2.1',
    entry_points={
        "console_scripts": [
            "pytld = pytld.cli:main"
        ]
    },
    extras_require={
        'test': [
            'pytest'
        ],
    }
)
