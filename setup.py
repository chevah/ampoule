#!/usr/bin/env python
# -*- test-case-name: ampoule -*-

# Copyright (c) 2008 Valentino Volonghi.
# See LICENSE for details.

"""
Distutils/Setuptools installer for AMPoule.
"""

from setuptools import setup

install_requires = ["Twisted>=17[tls]"]

description = """A process pool implementation in Twisted Matrix and AMP"""
long_description = open('README').read()

setup(
    version="17.12.0",
    name = "ampoule",
    author = "Valentino Volonghi",
    author_email = "dialtone@gmail.com",
    maintainer = "Glyph Lefkowitz",
    maintainer_email = "glyph@twistedmatrix.com",
    description = description,
    long_description = long_description,
    license = "MIT License",
    #install_requires=install_requires + ['incremental'],
    url="https://github.com/glyph/ampoule",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: System',
    ],
    packages=["ampoule", "ampoule.test", "twisted"],
    package_data={'twisted': ['plugins/ampoule_plugin.py']},
    #use_incremental=True,
    #setup_requires=['incremental'],
    include_package_data = True,
    zip_safe=False
)
