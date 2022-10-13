### FOR DOCKER-COMPOSE ###########################

FROM python:3.9 

WORKDIR /app

COPY requriments.txt /app

RUN python -m pip install --upgrade pip
RUN pip install -r requriments.txt

COPY . /app 

EXPOSE 8000 6379

# RUN celery upgrade settings /app/cleary/settings.py
# RUN celery -A cleary.celery worker --pool=solo -l info &>/dev/null & 
# RUN celery -A cleary beat -l info &>/dev/null &

# ENTRYPOINT [ "sh","start.sh" ]
# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate


# CMD ["python","manage.py","runserver","0.0.0.0:8000"]





################## BASE IMAGE PYTHON ###############


# FROM python:3.9 as builder

# WORKDIR /app

# COPY requriments.txt /app

# RUN python -m pip install --upgrade pip
# RUN pip install -r requriments.txt

# COPY . /app 

# EXPOSE 8000 6379

# RUN celery upgrade settings /app/cleary/settings.py
# RUN celery -A cleary.celery worker --pool=solo -l info &>/dev/null & 
# RUN celery -A cleary beat -l info &>/dev/null &

# ENTRYPOINT [ "sh","start.sh" ]

# CMD ["python","manage.py","runserver","0.0.0.0:8000"]



################## BASE IMAGE REDIS ###############

# FROM redis

# RUN apt update
# RUN apt install python3.9 -y 
# RUN apt install python3-pip -y

# WORKDIR /app

# COPY requriments.txt /app

# RUN python3 -m pip install --upgrade pip
# RUN pip install -r requriments.txt

# COPY . /app 

# EXPOSE 8000 6379

# ENTRYPOINT [ "sh","start.sh" ]

##################### BASE IMAGE UBUNTU ################
# FROM ubuntu:20.04

# WORKDIR /app

# ### FOR REDIS #################

# RUN apt update
# RUN apt install curl -y && apt install gpg -y
# RUN apt install lsb-release -y
# RUN curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
# RUN echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | tee -a /etc/apt/sources.list.d/redis.list
# RUN apt-get update && apt install redis -y
# # RUN redis-server &

# ### FOR MAIN CELERY ############
# RUN apt install python3.9 -y 
# RUN apt install python3-pip -y

# COPY requriments.txt /app

# RUN python3 -m pip install --upgrade pip
# RUN pip install -r requriments.txt

# COPY . /app 

# EXPOSE 8000 6379

# ENTRYPOINT [ "sh","start.sh" ]

