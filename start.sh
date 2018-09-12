#!/bin/bash

export DEBUG='true'
export FLASK_DEBUG=1
export FLASK_ENV='development'
export LANG='C.UTF-8'
export LC_ALL='C.UTF-8'
export FLASK_APP='quickvue/__init__.py'

# this is pretty specific to my system running Linux Subsystem for Windows with conda
if [ ! -d venv ]; then
    python3 -m venv --without-pip venv
    source venv/bin/activate
    curl https://bootstrap.pypa.io/get-pip.py | python
    deactivate
fi

source venv/bin/activate

# easy way to update requirements to latest version
# just delete requirements.txt
if [ ! -f requirements.txt ]; then
    pip install -r requirements-base.txt
    pip freeze > requirements.txt
fi

pip check -q || pip install -r requirements.txt

# run the dev server
flask run -h 0.0.0.0
