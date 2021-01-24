#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='inara_django',
      version='1.0',
      packages=find_packages(),
      install_requires =['django','Pillow','gunicorn'],
      scripts=['manage.py'])