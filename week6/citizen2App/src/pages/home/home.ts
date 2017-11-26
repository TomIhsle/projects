import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  constructor(public navCtrl: NavController) {

  }

}

// Define the websocket MQTT endpoint
var wsMQTTConnectionString = "ws://test.mosquitto.org:8080/"

import mqtt from 'mqtt'
import $ from 'jquery'
var client  = mqtt.connect(wsMQTTConnectionString)

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
    $("#output").append('<p>' + message + '</p>');
};