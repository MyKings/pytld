#!/usr/bin/env python
# coding: utf-8

from setuptools import find_packages, setup

setup(
    name='pytld',
    version='0.1.0',
    description='Tld is obtained by url or full domain name',
    author='MyKings',
    packages=find_packages(),
    include_package_data=True,
    author_email='xsseroot@gmail.com',
    url='https://github.com/MyKings/pytld',
    license='MPL 1.1/GPL 2.0/LGPL 2.1',
    install_requires=[
        'tld',
    ],
    extras_require={
        'test': [
            'pytest'
        ],
    }
)
