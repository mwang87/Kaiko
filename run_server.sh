#!/bin/bash

python ./main.py
#gunicorn -w 4 -b 0.0.0.0:5100 --timeout 3600 main:app
