#!/usr/bin/env bash

RC=0

if [[ ! -d venv ]]; then
    echo "Error: venv not found, creating ..."
    ./setup_venv.sh
    RC=$?
fi

if [[ RC -eq 0 ]]; then
  source venv/bin/activate
  ./link2.py
fi

exit ${RC}
