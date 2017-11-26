# Multi-container services on RPi

This lab will be entirely done ad-hoc in class. Please review the video for information. We will add links here as the class goes on and as questions are asked.

## Install Docker on RPi

[https://www.raspberrypi.org/blog/docker-comes-to-raspberry-pi/](https://www.raspberrypi.org/blog/docker-comes-to-raspberry-pi/)

Effectively run this command:

```bash
# Install Docker on RPi
pi$ curl -sSL https://get.docker.com | sh

# Add docker to a non-root user
pi$ sudo usermod -aG docker pi

# Pull base RPi image from Dockerhub
pi$ docker pull resin/rpi-raspbian

# Play around (use "bash" command on resin/rpi-raspbian iamge)
pi$ docker run -it resin/rpi-raspbian bash

# Build image (this reads from Dockerfile in local directory)
pi$ docker build -t sense .

# Review images currently on system
pi$ docker images

# Run in privileged mode
pi$ docker run -d --privileged=true sense

# Upload image to Dockerhub
pi$ docker login
# Replace [DOCKERHUB_USERNAME]
pi$ docker tag sense [DOCKERHUB_USERNAME]/sense
pi$ docker push [DOCKERHUB_USERNAME]/sense
```

## Use Case 1 - Live Edition

Ensure each sensor app is decoupled from each other at the edge.