#!/bin/bash

set -e

cd /opt/project

export PYTHONPATH=/opt/project

echo "Starting Spark transformations"

python -m src.transform.run_transformations

echo "Transformations completed"