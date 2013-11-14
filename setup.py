#!/usr/bin/python

from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="disjunct_intervals",
    version="0.2",
    description="Python module for handling problem of get disjunct \
intervalls from a set of intervalls.",
    author="Matyas Steiner",
    author_email="steiner.matyas@gmail.com",
    url="https://github.com/stma",
    license="GPL",
    long_description=read('README.md'),
    py_modules=["minints"],
    install_requires=[
        "python-constraint==1.1",
    ],
    dependency_links=[
        "http://labix.org/download/python-constraint/\
        python-constraint-1.1.tar.bz2"
    ],
)
