#!/usr/bin/env python

from setuptools import setup

def requirements_from_file(file_name):
    return open(file_name).read().splitlines()

setup(
    name="maai",
    version="0.0.2",
    description="Real-time and Continuous Non-verbal Behavior (Maai) Generation Software",
    author="MaAI team",
    author_email="inoue@sap.ist.i.kyoto-u.ac.jp",
    url="https://github.com/MaAI-Kyoto/MaAI",
    packages=["maai"],
    install_requires=requirements_from_file('requirements.txt'),
)