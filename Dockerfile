FROM 722277795083.dkr.ecr.us-west-1.amazonaws.com/python-app:latest
# first image only FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8
# only for build environment RUN apk --update add bash nano docker curl
COPY ./requirements.txt /app/requirements.txt
COPY ./app/ /app
WORKDIR /app
EXPOSE 80
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
