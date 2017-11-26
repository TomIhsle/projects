# Raspbian base image for UW IoT Class
FROM resin/rpi-raspbian

RUN apt-get update

# Add support for RPi Camera, SenseHAT, and Python2
RUN apt-get install -y wget \
                       python \
                       sense-hat \
                       python-picamera \
                       build-essential \
                       libssl-dev \
                       libffi-dev \
                       python-dev
# Install pip
RUN wget -P / https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

# Install paho-mqtt
RUN pip install paho-mqtt

# Install Microsoft Azure Python SDK
RUN pip install azure

# Install Redis client
RUN pip install redis

# Cleanup to save space
RUN rm -rf /tmp/*.dep