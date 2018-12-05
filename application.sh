#!/bin/sh
export FLASK_APP=./application.py
source venv/bin/activate
flask run -h 0.0.0.0