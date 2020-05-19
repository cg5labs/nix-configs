#!/usr/bin/env bash

PY_BINARY="/usr/local/bin/python3"
VIRTUALENV=$(which virtualenv)
REQUIREMENTS="requirements.txt"
RC=0

if [[ -z ${VIRTUALENV} ]]; then
    echo "Error: virtualenv script not found."
    RC=1
fi

if [[ -d venv ]]; then
    echo "Error: venv already exists, skipping."
    RC=2
fi

if [[ ! -f requirements.txt ]]; then
    echo "Error: requirements.txt does not exist."
    RC=3
fi

if [[ RC -eq 0 ]]; then
  virtualenv -p "${PY_BINARY}" venv
  source venv/bin/activate
  pip3 install -r "${REQUIREMENTS}"
fi

exit ${RC}
