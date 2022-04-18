#!/bin/bash
set -e

MYPYPATH=./typings mypy --ignore-missing-imports -p RlGlue

export PYTHONPATH=RlGlue
python3 -m unittest discover -p "*test_*.py"
