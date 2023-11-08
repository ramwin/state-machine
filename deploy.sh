#!/bin/bash
# Xiang Wang @ 2021-01-20 21:58:26

rm -rf dist/*
python3 setup.py sdist bdist_wheel
twine upload dist/*
