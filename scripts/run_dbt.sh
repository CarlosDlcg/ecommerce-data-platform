#!/bin/bash

set -e

cd /opt/project

dbt run
dbt snapshot
dbt test