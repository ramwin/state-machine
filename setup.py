#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 09:31:01



import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "state-machine-2",
    version = "0.2.4",
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
    install_requires=[
        "redis",
    ],
    python_requires=">=3.7",
    package_data={
        "state_machine": ["py.typed"],
    }
)
