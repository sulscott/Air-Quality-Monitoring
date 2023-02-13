#!/bin/bash

# Generate a diagram of the directory structure
tree -I "__pycache__" -I "venv" > directory_structure.txt

# Print the diagram
cat directory_structure.txt
