FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8
RUN apk --update add bash nano docker curl
COPY ./requirements.txt /app/requirements.txt
COPY ./app/ /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
