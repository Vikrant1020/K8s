#!/bin/bash

apt update
redis-server &>/dev/null &
celery -A cleary.celery worker --pool=solo -l info -P gevent &>/dev/null & 
# celery -A cleary beat -l info &>/dev/null & 
python3 manage.py runserver 0.0.0.0:8000