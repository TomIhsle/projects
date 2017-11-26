# Start from an image that is compliant with ARMv7 and is Debian based
# Pull base RPi image from Dockerhub
FROM resin/rpi-raspbian

# Inspired by: https://github.com/remonlam/rpi-docker-weather/blob/master/Dockerfile
RUN apt-get update
RUN apt-get install -y wget \
                       python

# Install pip
RUN wget -P / https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

RUN pip install redis 

COPY tester.py /

# Cleanup to save space
RUN rm -rf /tmp/*.dep

CMD ["python", "tester.py"]