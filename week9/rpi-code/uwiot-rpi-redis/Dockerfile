# Start from a Raspbian image with Python2 and pip installed
FROM richardjortega/uwiot-rpi-baseimage

RUN apt-get update
RUN apt-get install -y git gcc

WORKDIR /
RUN git clone --branch 4.0 https://github.com/antirez/redis.git

WORKDIR /redis
RUN make

EXPOSE 6379
WORKDIR /redis/src
CMD ["./redis-server"]