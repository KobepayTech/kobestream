#!/bin/bash
set -e

git submodule update --init --recursive
git submodule update --remote --merge

git status
