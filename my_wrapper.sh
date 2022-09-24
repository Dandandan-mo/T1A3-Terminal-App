#!/bin/bash

#check if Python3 is installed
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python3, but it looks like Python3 is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi

# check if pip3 is installed and upgraded.
if ! [[ -x "$(command -v pip)" ]]
then
  if [[ $1 == "Linux" ]] || [[ $1 == "MacOS" ]]
  then
    python3 -m ensurepip --upgrade
  elif [[ $1 == "Windows" ]]
  then
    py -m ensurepip --upgrade
  fi
fi

if --version pip != 3
then
  if [[ $1 == "Linux" ]] || [[ $1 == "MacOS" ]]
  then
    python3 -m pip install --upgrade pip
  elif [[ $1 == "Windows" ]]
  then
    py -m pip install --upgrade pip
  fi
fi

# create a virtual environment, install packages
python3 -m venv .venv
source  .venv/bin/activate
pip install -r requirements.txt

# run python main.py to start executing the app
python3 main.py
