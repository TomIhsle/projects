#!/usr/bin/python
import time
import socket
import paho.mqtt.client as paho
from sense import PiSenseHat

hostname = "iot7643"
brokerHost = "test.mosquitto.org"     # Local MQTT broker
brokerPort   = 1883          # Local MQTT port
brokerTopic = "iot-310b"  # Local MQTT topic to monitor
brokerTimeout = 120          # Local MQTT session timeout

# The callback for when a CONNACK message is received from the broker.
def on_connect(client, userdata, flags, rc):
    print "CONNACK received with code %d." % rc

# display one row of blue LEDs (just for fun)
def displayLine(row):
    blue = (0, 0, 255)
    for i in range(0,8):
        x = i % 8
        y = (i / 8) + row
        # print("set pixel x:%d y:%d" % (x,y))
        pi_sense.set_pixel(x,y,blue)
        time.sleep(0.02)

# Create a sense-hat object
pi_sense = PiSenseHat()
print 'PI SenseHat Object Created'

# Setup to Publish Sensor Data
mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.connect(brokerHost, brokerPort, brokerTimeout)

# initialize message dictionary
msg = {'topic':brokerTopic, 'payload':"", 'qos':0, 'retain':False}

pi_sense.clear_display()
# loop
print('Getting Sensor Data')
for i in range(1,9):
    print("SensorSet[%d]" % (i))
    displayLine(i-1)
    sensors = pi_sense.getAllSensors()

    sensors['host'] = hostname
    msg['payload'] = str(sensors)
    print "msg["+str(i)+"]:"+msg['payload']

    mqttc.publish(brokerTopic, msg['payload'], 0)
    time.sleep(2.0)

# clear LED Matrix
pi_sense.clear_display()

print 'End of MQTT Messages'
quit()
