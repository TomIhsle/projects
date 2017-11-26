#!/usr/bin/python
import time
import socket
import os
import redis

hostname = os.environ["HOSTNAME"]

r = redis.StrictRedis(host='broker', port=6379, db=0)
p = r.pubsub()
p.subscribe('msg-topic-name')

while True:
    message = p.get_message()
    if message:
        print "Subscriber: %s" % message['data']
    time.sleep(1)