#!/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="whycarnotgo",
    version="0.0.1",
    description=("Simple OBD-II Scanner"),
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: System :: Monitoring",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
    ],
    keywords="obd obdii obd-ii obd2 car serial vehicle diagnostic",
    author="Adam Novak",
    author_email="anovak@soe.ucsc.edu",
    url="http://github.com/adamnovak/whycarnotgo",
    license="GNU GPLv2",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['obd==0.6.1-adamnovak'],
    # Note that we suggest this patched obd module until https://github.com/brendan-w/python-OBD/issues/101 is fixed
    dependency_links=['git+https://github.com/adamnovak/python-OBD.git@3f1804fe4ca3f01803a5d011d3ce389669a5a914#egg=obd-0.6.1-adamnovak'],
    py_modules=['whycarnotgo'],
    entry_points={
        'console_scripts': ['whycarnotgo=whycarnotgo:main']
    }
)
