# RPi, SenseHAT, and MQTT Revisited with a little Node.js

## Overview

This lab is to get us collectively back to a stable point with our RPis and make sure everyone is on the same page. All version, libs, etc are running smoothly. We will run through some previous labs to get us up and running, these files have been modified to fit the Course 3 theme and focus only on their specific use case

Some files require system `python` dependencies to be installed. These were covered in Course 1, however, here are links to the packages.
- `mqtt` library can be found at the [Paho MQTT site](https://pypi.python.org/pypi/paho-mqtt/1.1#installation).
- `sense-hat` library can be found at the [SenseHAT site](https://github.com/RPi-Distro/python-sense-hat).

**Note**: Originally some files attempted to detect hostname and that worked well in class, but doesn't work well outside of class so this was removed in favor of a more manual approach. 

## Lab Links

- [MQTT python module](https://pypi.python.org/pypi/paho-mqtt/)
- [SenseHAT python module](https://github.com/RPi-Distro/python-sense-hat)
- [Node](https://nodejs.org/en/)
- [NPM](https://www.npmjs.com/)
- [MQTT npm module](https://github.com/mqttjs/MQTT.js)

## Use Case

Send and receive sensor data from device gateways across the city.

## Read SenseHAT data (from Course 1)

Let's find a file that grabs all the data we need from the SenseHAT and provides a JSON object we can use to send to a MQTT broker. Luckily, we built something similar in Course 1!

This file has been added for your convenience as `centralEdgeV1DeviceTest.py` within this directory. 

## Sending test data via MQTT client (from Course 2)

Let's try something a little different, we've converted a `python` file from Course 2 to be written in `javascript` that we will run on the RPi using `node` for the runtime.

This file has been added for your convenience as `centralEdgeV1-mqttTest.js` wthin this directory.

### Install Node.js and NPM

The following commands will install `node` and `npm` binaries to your RPi.

```bash
pi$ curl -sL http://deb.nodesource.com/setup_4.x | sudo -E bash
pi$ sudo apt-get -y install nodejs
```

### Verify successful installation

```bash
pi$ node --version
# v4.8.3
pi$ npm --version
# 2.15.11
```

### Install dependecies via `npm`

Run the following command from the **week1/lab1** folder.

```bash
~host/week1/lab1: $ npm install
```

### Run the code

Run the following command from the **week1/lab1** folder.

```bash
~host/week1/lab1: $ node centralEdgeV1-mqttTest.js
# Exit with CTRL+C
``` 

## Setup a MQTT Client and send SenseHAT data

Time to send some real data over the interwebs!

Using the `centralEdgeV1-Client.py` file provided, modify the `hostname` variable to include your own. We will use a topic channel of **iot-310b** with a subtopic of your hostname.


## Setup a MQTT Server for the RPi and Receive Other SenseHAT data

Have the RPi listen to other RPi messages (we've done this before, but good practice). 

Using the `centralEdgeV1-Server.py` file provided, modify the `hostname` variable to include your own. We will use a topic channel of **iot-310b** with a subtopic of your hostname.

## HACKER EDITION: Error Handling for MQTT Server

Currently, `centralEdgeV1-Server.py` will work fine for strings that contain JSON objects (as it will pase those JSON objects and turn it into a Python dictionary), however if a non-JSON compliant payload is sent it fails and exits. Update the code to support handling of general text (i.e. disregard non-JSON payloads).