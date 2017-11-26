# Multiple Containers & Serverless [Continued]

For this week, please review Week 4 video for any in-class recap. 

We are going to finish our own implementation of our Sensor Gateway. 

We will detail what's happening in a Serverless app.


## Walkthrough

### Install Docker Compose

Ensure `pip` (version 6.0) is installed:

```bash
# https://pip.pypa.io/en/stable/installing/
pi$ wget https://bootstrap.pypa.io/get-pip.py

pi$ sudo python get-pip.py
```

Exit your session and SSH back into your RPi.

Install `docker-compose` using `pip`.

```bash
# https://docs.docker.com/compose/install/
# Expects pip version greater than 6.0
pi$ sudo pip install docker-compose
```

### Verify `docker-compose` install

```bash
pi$ docker-compose version
# docker-compose version 1.14.0, build c7bdf9e
```

## Create a `docker-compose.yml` file

[https://docs.docker.com/compose/gettingstarted/#step-3-define-services-in-a-compose-file](https://docs.docker.com/compose/gettingstarted/#step-3-define-services-in-a-compose-file)

Build the Docker build

```bash
pi$ docker-compose build
```

Verify it's been created with:

```bash
pi@iot7643:~/Code/iot-310b-student/week4/lab1 $ docker images
# REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
# lab1_sensorclient      latest              d9b73efd0f21        2 minutes ago       282MB
```

Review the `docker-compose.yml` file to understand what's happening. This file provides a descriptive way of instantiating multiple containers and options that those containers may use. For instance, we used `docker run --privileged=true sensorclient` previously and our `docker-compose.yml` file now has the same option added under the service `sensorclient`. We also added an [env_file](https://docs.docker.com/compose/compose-file/compose-file-v2/#env_file) option as well.

Run the `docker-compose.yml` file using:

```bash
pi$ docker-compose up
```

You can instantiate a container anytime using (for instance using `bash`):

```bash
pi$ docker-compose run --rm serviceclient bash
```

