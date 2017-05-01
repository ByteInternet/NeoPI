#!/usr/bin/env python
import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name="neopitool",
      version="0.2",
      description="Byte-patched version of NeoPI",
      url="https://github.com/ByteInternet/NeoPI",
      packages=["neopitool"],
      author="Rik",
      author_email="rik@byte.nl",
      install_requires=[],
      entry_points={
	  'console_scripts': [
	      'neopi = neopi'
	  ],
      },
    )
