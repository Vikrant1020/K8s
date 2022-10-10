FROM python:3.9

WORKDIR /app

COPY requriments.txt /app

RUN python -m pip install --upgrade pip
RUN pip install -r requriments.txt

COPY . /app 

EXPOSE 8000 6379

RUN celery upgrade settings /app/cleary/settings.py
# RUN celery -A cleary.celery worker --pool=solo -l info &>/dev/null & 
# RUN celery -A cleary beat -l info &>/dev/null &

ENTRYPOINT [ "sh","start.sh" ]

# CMD ["python","manage.py","runserver","0.0.0.0:8000"]