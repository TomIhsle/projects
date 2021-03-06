#!/bin/bash

# Ensure DOCKERHUB_USERNAME is set or exit
if [ -z "${DOCKERHUB_USERNAME}" ]; then
    echo "Need to set DOCKERHUB_USERNAME env"
    exit 1
fi

# Build and tag our redis image
docker build -t "${DOCKERHUB_USERNAME}/uwiot-rpi-redis" .

# Log into docker
docker login

# Push our redis image
docker push "${DOCKERHUB_USERNAME}/uwiot-rpi-redis"