#!/usr/bin/python

from setuptools import setup
import os


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="disjunct_intervals",
    version = "0.1",
    description = "Python module for handling problem of get disjunct intervalls from a set of intervalls.",
    author = "Matyas Steiner",
    author_email = "steiner.matyas@gmail.com",
    url = "https://github.com/stma",
    license = "GPL",
    long_description =read('README'),
    py_modules = ["minints"],
    install_requires = [
        "python-constraint==1.1",
    ],
    dependency_links = [
        "http://labix.org/download/python-constraint/python-constraint-1.1.tar.bz2"
    ],
)
