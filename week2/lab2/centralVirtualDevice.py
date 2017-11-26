#!/usr/bin/python
# Inspired from centralEdgeV1-Client (Course 3/Week 1/Lab 1)
# Description: Send message
import time
import socket
import paho.mqtt.client as paho

hostname = "vm1337-iot-310b"
brokerHost = "test.mosquitto.org"     # Local MQTT broker
brokerPort   = 1883          # Local MQTT port
brokerTopic = "iot-310b-wolf"  # Local MQTT topic to monitor
brokerTimeout = 120          # Local MQTT session timeout

# The callback for when a CONNACK message is received from the broker.
def on_connect(client, userdata, flags, rc):
    print "CONNACK received with code %d." % rc

# Setup to Publish Sensor Data
mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.connect(brokerHost, brokerPort, brokerTimeout)

# initialize message dictionary
msg = {'topic':brokerTopic, 'host':hostname, 'time':"", 'qos':0, 'retain':False}

for i in range(1,9):
    localtime = time.asctime( time.localtime(time.time()) )
    msg['time'] = localtime
    print "Sending local time :", localtime
    mqttc.publish(brokerTopic, str(msg), 0)
    time.sleep(2.0)

print 'End of MQTT Messages'
quit()
