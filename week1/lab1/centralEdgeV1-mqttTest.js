// Based on mqtt_publish.py created by Drew Gislason

// Usage: node centralEdgeV1-mqttTest.js

// Define the websocket MQTT endpoint
var wsMQTTConnectionString = "ws://iot.eclipse.org:80/ws"

// Require MQTT
var mqtt = require('mqtt')
var client = mqtt.connect(wsMQTTConnectionString)

client.on('connect', function () {
  // Confirm connection
  screenPrint('CONNECTED TO: ' + wsMQTTConnectionString)

  // Subscribe to channel
  var topic = 'iot-310b'
  client.subscribe(topic)
  screenPrint('SUBSCRIBED TO: ' + topic)

  // Send test message
  var testMessage = 'Hello mqtt'
  screenPrint('SENDING TEST MQTT MSG: ' + testMessage)
  client.publish(topic, 'Hello mqtt')
})

client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
  screenPrint('<span style="color: blue;">RESPONSE: ' + message + '</span>')
})

function screenPrint(message) {
  // Append to div
  console.log(message)
};