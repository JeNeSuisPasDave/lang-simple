#! /bin/bash
#

# Check whether we are running in a python virtual environment
#
export VENV_RUNNING=`env | grep VIRTUAL_ENV | wc -l | tr -d [[:space:]]`
#echo "VENV_RUNNING: ${VENV_RUNNING}"
if [ 0 == ${VENV_RUNNING} ]; then
  echo "ERROR: Python virtual environment not running"
  echo
  echo "Try '. venv34/bin/activate' to start the virtual environment, and"
  echo "then try './test.sh' again."
  echo
  exit 1
fi

# Check whether we are running Python 3
#
export PYVER_=`python --version 2>&1 | grep "^Python 3\." | wc -l | tr -d [[:space:]]`
if [ 0 == ${PYVER_} ]; then
  echo "ERROR: Python 3 is required. Found "`python --version`"."
  echo
  echo "Deactivate the current virtual environment."
  echo "Try '. venv34/bin/activate' to start the virtual environment, and"
  echo "then try '${SCRIPTNAME_}' again."
  echo
  exit 1
fi

# Check whether pyPEG2 is installed
#
PYPEG2_INSTALLED_=`pip list | grep "^pyPEG2 (" | wc -l | tr -d [[:space:]]`
if [ 0 == ${PYPEG2_INSTALLED_} ]; then
  echo "ERROR: pyPEG2 is not installed"
  echo
  echo "Try 'pip install pyPEG2' to install pyPEG2, and"
  echo "then try '${SCRIPTNAME_}' again."
  echo
  exit 1
fi

# Run the test
#
export PYTHONPATH=`pwd`/src
# python -i -m pdb ./src/parsing/parsing_simple.py
# python -i -m parsing.parsing_simple
python  -i