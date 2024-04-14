#!/bin/bash
# Xiang Wang(ramwin@qq.com)

rm -r _build
sphinx-autobuild -j auto --port 18011 . _build/html/
