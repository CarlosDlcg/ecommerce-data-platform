#!/bin/bash

set -e

cd /opt/project

export PYTHONPATH=/opt/project

echo "Starting extraction layer"

python -m src.extract.run_extractors

echo "Extraction completed"