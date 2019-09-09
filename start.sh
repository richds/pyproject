#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -d -p 1337:80 \
  --name=${app} \
  ${app}
