# Week 2: Virtual Machines and Containers

Welcome to Week 2 everyone... it's going to be a fun ride, please provide feedback along the way.

- [Lab 1: Intro to Virtual Machines](lab1/README.md) 
- [Lab 2: Intro to Containers](lab2/README.md)

# Homework

*Note*: The homework can be turned in via screenshots, links to repos, and/or any other reference links. 

1. Modify the shell script in **lab1** inside `Vagrantfile` and install a non-installed Ubuntu package via `apt-get`. Take a screenshot of a successfully installed package. Along with a link to your `Vagrantfile`

2. Using your **centralView** dekstop app from Week1/Lab2, setup a custom MQTT topic that receives data from two new virtual devices:
    - One from a VM (instantiated with Vagrant/VirtualBox) - send a screenshot with VirtualBox GUI showing your VM and the message coming into centralView.
    - One from a container (instantiated from Docker) - send a screenshot of the output of `host$ docker ps -a` that should show a "Running" container. Have that adjacent to your centralView.