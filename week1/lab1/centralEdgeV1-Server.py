#!/usr/bin/python
import time
import paho.mqtt.client as paho
import json
import ast

hostname = "iot7643"
brokerHost = "test.mosquitto.org"     # Local MQTT broker
brokerPort   = 1883          # Local MQTT port
brokerTopic = "iot-310b"  # Local MQTT topic to monitor
brokerTimeout = 120          # Local MQTT session timeout

# The callback for when a CONNACK message is received from the broker.
def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))
    mqttc.subscribe(brokerTopic, 0)

def on_message(mosq, obj, msg):
    global message
    print("Topic Rx:" + msg.topic + " QoS:" + str(msg.qos) + "\n")
    clean_json = ast.literal_eval(msg.payload)
    print ("Payload: ")
    # import pdb; pdb.set_trace()
    print json.dumps(clean_json, indent=4, sort_keys=True)
    # message = msg.payload

print('Establish MQTT Broker Connection')
# Setup to listen on topic`
mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect(brokerHost, brokerPort, brokerTimeout)
print('MQTT Listener Loop <ctl-C> to break...')
mqttc.loop_forever()
