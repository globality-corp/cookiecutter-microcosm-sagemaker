#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

REPO_NAME="papaya-extractor"
rm -rf "$REPO_NAME"
cookiecutter . --no-input
