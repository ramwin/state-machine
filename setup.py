#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 09:31:01



import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "state-machine-2",
    version = "0.0.1",
    author="Xiang Wang",
    author_email="ramwin@qq.com",
    description="a state machine that support multi process",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ramwin/state-machine",
    packages=["state_machine"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
)
