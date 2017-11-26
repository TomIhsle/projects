# Welcome to the IOT 310B: Internet of Things: Cloud Computing & Analytics
Thomas Ihsle

Data is the key to success in the internet of things. In this course you’ll get an overview of the various techniques used to visualize, present and utilize data effectively, so agents of the internet of things system can drive results. We’ll explore data flow, cleansing, processing and analysis, all of which are critical to producing a result worth investing in by the customer. You’ll take a deep dive on concepts such as distributed computing, storage and end-user client applications, all in the context of the cloud. We’ll concentrate on extracting value from the data collected from devices, and from other relevant data, to generate an event or result.

Topics include:

How to store, process, present and visualize data from the internet of things.
- Setting up microservices in the cloud, including data schema, database, API development and server elements
- Simple and complex visualization tools
- Analysis of datasets 

This course expects that you have taken either Course 1 or Course 2 (preferrably both) of the UW IoT Certification Course (or are familiar with programming and the RPi sensors).

## Disclaimer

The materials of this course are the property of the University of Washington, and
are not to be posted on the internet or other forums.

They are for the personal use of the students attending the course.


## Instructor and Classroom Information

**Online Meeting Room:** [https://uwtest.zoom.us/j/546556168](https://uwtest.zoom.us/j/546556168)

**GitLab Repo Links**
- [Labs](https://gitlab.com/richardjortega/iot-310b-student.git)
- [Slides](https://gitlab.com/richardjortega/iot-310b-slides.git)

**MQTT Public Brokers**

If you run into a situation where a MQTT broker is not responding or refusing connection, feel free to change the broker.

- [IoT Eclipse MQTT Broker](https://iot.eclipse.org/getting-started#tutorials)
- [Mosquitto MQTT Broker](http://test.mosquitto.org/)

**Instructor: Richard Ortega**, Email: [riortega@uw.edu](mailto:riortega@uw.edu)

**TA: Bryan Palmer**, Email: [bpalmer@uw.edu](bpalmer@uw.edu)

**Class Sessions:** Thurdays 6:00 pm - 9:00 pm, PT. June 22nd - August 24th, 2017.

**Class Location:** 2445 140th Avenue N.E., Ste. B-100, Bellevue, WA 98005-1879 (Links to an external site.), Room 210

**In-Class Wi-Fi:**  
SSID: **UW-IoT110-R**  
Password: **piIoT110**  (Note: "I" in IoT is  "capital I" and not "lowercase L")

## Various Links

[UW-PCE IoT Website](https://www.pce.uw.edu/certificates/internet-of-things)  
[Canvas](https://canvas.uw.edu/)  

## Raspberry Pi 3 Information

*Note*: Link is from Course 2

[How to Setup your RPi3](https://gitlab.com/Gislason/iot-210B-student/tree/master/Lab1/PI_SETUP.md)

## Course 3 Required Lab Equipment List

**Note**: [Course 1](https://gitlab.com/iot110/iot110-student/) had more sensors/actuators to use, feel free to use those but primarily we will be using the SenseHAT for collecting data. 

| ITEM #  | DESCRIPTION |  QTY  | COST | COMPONENT | BUY URL| OTHER |
| :-----: | :---------- | :---: | ---: | :--------: | :-----------------| :-------- |
| 1  | Raspberry Pi 3 Kit | 1 | $89.95 | [RaspberryPi3](https://www.raspberrypi.org/) | [Adafruit](https://www.adafruit.com/products/3058) |  [Alternate](https://www.amazon.com/dp/B01C6Q4GLE?psc=1) |      
| 2  | Pi Sensor HAT    | 1 | $39.95 | Sensors | [Adafruit](https://www.adafruit.com/products/2738) | [Astro-Pi](https://astro-pi.org/) |
| 3  | Camera Module V2 | 1 | $29.60 | Sensors | [Amazon](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS)
| 4  | TFT 5 inch Monitor |	1 | $59.95| | [Adafruit](https://www.adafruit.com/products/2232) | | |
| 5  | HDMI Flat Cable | 1 | $11.29 | | [Adafruit](https://www.adafruit.com/products/2197) | |
| 6  | Logitech Wireless Touch Keyboard K400 | 1 | $24.99 | | [Amazon](https://www.amazon.com/Logitech-920-007119-Wireless-Keyboard-Connected/dp/B014EUQOGK/) |
| 7 | Micro USB Charge Sync GOLD Data Cable | 2 |	$9.98 |	| [Amazon](http://amzn.to/2e49OHk) |
| 8 | Anker 24W Dual USB Wall Charger PowerPort 2 | 1 | $12.49 | | [Amazon](http://amzn.to/2ejevvC) |

## Session Breakdown

Section 1 | Time Allotted | Schedule
----- | ------ | ----
Lecture  | 30 Mins | 6:00-6:30pm
Lab  | 25 Mins | 6:30-6:55pm
Break  | 10 Mins | 6:55-7:05pm
Lab Continued  | 25 Mins | 7:05-7:30pm

Section 2 | Time Allotted | Schedule
----- | ------ | ----
Lecture  | 30 Mins | 7:30-8:00pm
Break  | 10 Mins | 8:00-8:10pm
Lab  | 50 Mins | 8:10-9:00pm

## Syllbus and Labs

Week | Date | Lab | Description
----- | ------ | ---- | -----
W1 | Jun 22 | [Lab 1]() | CENTRAL Edge v1 (NodeJS), CENTRAL FieldView (Electron)
W2 | Jun 29  | [Lab 2]() | CENTRAL Edge v2 (Docker), CENTRAL City API (App Service)
W3 | Jul 06 | [Lab 3]() | CENTRAL Link [Cloud Gateway (IoT Hub) <-> Device Gateway]
W4 | Jul 13 | [Lab 4]() | CENTRAL Citizen Finder (Face)/CENTRAL Citizen Happiness (Emotion)
W5 | Jul 20 | [Lab 5]() | Citizen Engagement Mobile App (Ionic), Mini-Capstone
W6 | Jul 27  | [Lab 6]() | CENTRAL Feedback (LUIS), CENTRAL Feedback Translator (Translator)
W7 | Aug 03 | [Lab 7]() | CENTRAL Ask Jarvis (Bot Framework, LUIS)
W8 | Aug 10 | [Lab 8]() | CENTRAL Precog 1 (Machine Learning)
W9 | Aug 17 | [Lab 9]() | CENTRAL Precog 2 (Machine Learning) 
W10 | Aug 24 | n/a   | Class IoT Hackathon: Smart Cities
