#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is a requirement for Scribe. To learn more about installing Python 3 visit the following: https://realpython.com/installing-python/"
    exit 1
fi

# Check if pip3 is installed
if ! command -v pip3 &> /dev/null; then
    echo "Pip3 is a requirement for Scribe, I will install it for you. For a guide on installing pip3 manually, visit this link: https://pypi.org/project/pip/"
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv 
fi

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip in the virtual environment
python3 -m pip install --upgrade pip

# Install requirements
python3 -m pip install -r ./requirements.txt

# Run the main script
python3 ./src/main.py
