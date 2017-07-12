#!/bin/bash

export DEBUG='true'
export FLASK_DEBUG=1
export LANG='C.UTF-8'
export LC_ALL='C.UTF-8'
export FLASK_APP='quickvue/__init__.py'

# this is pretty specific to my system running Linux Subsystem for Windows with conda
if [ ! -d venv ]; then
    python3.5 -m venv --without-pip venv
    source venv/bin/activate
    curl https://bootstrap.pypa.io/get-pip.py | python
    deactivate
fi

source venv/bin/activate

pip install -r requirements.txt

# run the dev server
flask run -h 0.0.0.0
