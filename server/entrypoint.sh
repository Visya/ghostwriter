#!/bin/bash

gunicorn -b 0.0.0.0:5050 --reload app:app
