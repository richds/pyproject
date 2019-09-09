#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -p 1337:80 \
  --name=${app} \
  ${app}
