#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='ASE-QE',
    version='0.1.1',
    author='Paweł T. Jochym',
    author_email='pawel.jochym@ifj.edu.pl',
    packages=['ase-qe', 'ase-qe.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/ASE-QE/',
    license='LICENSE.txt',
    description='ASE interface to Quantum-Espresso',
    long_description=open('README.md').read(),
    install_requires=[
        "ase >= 3.0.0",
        "scipy",
        "numpy",
        "matplotlib"
    ],
)

