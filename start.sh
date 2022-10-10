#!/bin/bash

apt update

celery -A cleary.celery worker --pool=solo -l info 
celery -A cleary beat -l info&>/dev/null & 
python3 manage.py runserver 0.0.0.0:8000