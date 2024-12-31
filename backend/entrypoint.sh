#!/bin/sh
set -e
# apply latest migrations
python manage.py migrate
# run tests
#TODO: tests
# collect static files to serve
python manage.py collectstatic --no-input
# run with gunicorn
gunicorn project.wsgi
