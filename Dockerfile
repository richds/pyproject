FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8
RUN apk --update add bash nano docker
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /app/requirements.txt
COPY ./app/ /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
