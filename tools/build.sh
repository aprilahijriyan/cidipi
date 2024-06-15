#!/bin/bash

SRC_MODULE=cidipi
python tools/generator.py
autoflake -r --in-place --expand-star-imports --remove-all-unused-imports --ignore-init-module-imports $SRC_MODULE
pre-commit run -a
