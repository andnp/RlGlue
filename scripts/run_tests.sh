#!/bin/bash
set -e

MYPYPATH=./typings mypy -p RlGlue

export PYTHONPATH=RlGlue
python3 -m unittest discover -p "*test_*.py"
