FROM 722277795083.dkr.ecr.us-west-1.amazonaws.com/python-app
RUN apk --update add bash nano docker curl
COPY ./requirements.txt /app/requirements.txt
COPY ./app/ /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
