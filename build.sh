#! /usr/bin/env bash

set -o errexit   #  exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations user
python manage.py makemigrations music
python manage.py migrate
