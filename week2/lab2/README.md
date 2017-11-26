# Intro to Containers

## Overview

This lab will help you get oriented with Docker and why we are using it. 

## Lab Links

- [Docker](https://www.docker.com/)
- [Docker Hub Registry](https://hub.docker.com/)
    - Images uploaded to this registry are maintained by the community and have no support from Docker directly.
- [Docker Store](https://store.docker.com/)
    - This link is only provided as a reference. More details on Docker Store can be found [here](https://docs.docker.com/docker-store/).
    - The Docker Store provides Docker Verified images (as well as access to Docker Hub images). These Docker Verified images are verified by Docker, have a high level of security, and generally subscribe to Docker best practices.
    - In an enterprise setting, this likely would be the route to choose (as depending on publisher) may include a paid support level.

## Use Case

Investigate a way to optimize application density at the edge devices.

## Docker Overview

"Docker provides a method of developing, shipping, and running applications. Docker provides the ability to package and run an application in a loosely isolated environment called a container. The isolation and security allow you to run many containers simultaneously on a given host. Containers are lightweight because they don’t need the extra load of a hypervisor, but run directly within the host machine’s kernel. This means you can run more containers on a given hardware combination than if you were using virtual machines. You can even run Docker containers within host machines that are actually virtual machines!" [Source](https://docs.docker.com/engine/docker-overview/)

In the context of Docker, an **image** is the binary file that contains your code, your code packages, and any system level dependencies. A **container** is an instance of an image. 

This will make more sense during the lab. Right now, it's important to note that at a high-level the following points are key takeaways for containers [Source](https://docs.docker.com/engine/docker-overview/#what-can-i-use-docker-for):

- Fast, consistent delivery of your applications
    - Work in standardized environments using local containers which provide your applications and services.
- Responsive deployment and scaling
    - Because of the portability and how lightweight Docker is, you can dynamically manage workloads, scale up/tear down services with ease in near real-time.
- Running more workloads on the same hardware
    - You can increase app density on the same hardware over hypervisor-based virtual machines, so you can use more of your compute capacity to achieve your business goals. Docker is perfect for high density environments and for small and medium deployments where you need to do more with fewer resources (e.g. the Raspberry Pi).

Let's get into it!

## Docker Overview

Docker project (open-sourced by dotCloud in March '13) consists of several main parts (applications) and elements (used by these parts) which are all [mostly] built on top of already existing functionality, libraries and frameworks offered by the Linux kernel and third-parties (e.g. LXC, device-mapper, aufs etc.).

### Main Docker Parts

- docker daemon: used to manage docker containers on the host it runs
- docker CLI: used to command and communicate with the docker daemon
- docker hub registry: a repository (public or private) for docker images
- docker store: a trusted repository of images maintained by docker or first-party developers

### Main Docker Elements

- docker containers: directories containing everything-your-application
- docker images: snapshots of containers or base OS (e.g. Ubuntu) images
- Dockerfiles: scripts automating the building process of images

## Installing Docker

We will install the **Docker Community Edition** on your host machine. You can download it here: [Docker Community Edition](https://www.docker.com/community-edition).

Verify successful installation by opening your host machine's shell and enter:

```bash
host$ docker run hello-world
```

You will see some output similar to:

```text
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

You can search for images available on Docker Hub by using the docker command with the `search` subcommand. For example, to search for the Ubuntu image, type:

```bash
host$ docker search ubuntu   
```

Alternatively, you can search on the [Docker Hub Registry](https://hub.docker.com/) website.

In the OFFICIAL column, OK indicates an image built and supported by the company behind the project. Once you've identified the image that you would like to use, you can download it to your computer using the `pull` subcommand, like so:

```bash
host$: docker pull ubuntu
```

After an image has been downloaded, you may then run a container using the downloaded image with the `run` subcommand. If an image has not been downloaded when docker is executed with the `run` subcommand, the Docker client will first download the image, then run a container using it:

```bash
host$: docker run ubuntu
```

To see the images that have been downloaded to your computer, type:

```bash
host$: docker images
```

The output should look similar to the following:

```text
Output
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              latest              d355ed3537e9        7 days ago          120.8 MB
hello-world         latest              1815c82652c0        2 weeks ago         967 B
```

The `hello-world` container you ran in the previous is an example of a container that runs and exits, after emitting a test message. Containers, however, can be much more useful than that, and they can be interactive. After all, they are similar to virtual machines, only more resource-friendly.

As an example, let's run a container using the latest image of Ubuntu. The combination of the -i and -t switches gives you interactive shell access into the container:

```bash
host$: docker run -it ubuntu
```

Your command prompt should change to reflect the fact that you're now working inside the container and should take this form:

```bash
root@33b7ca72ea69:/#
```

Important: Note the container id in the command prompt. In the above example, it is 33b7ca72ea69.

Now you may run any command inside the container. For example, let's update the package database inside the container. No need to prefix any command with sudo, because you're operating inside the container with root privileges:

```bash
container$: apt-get update
```

Then install any application in it. Let's install NodeJS, for example.

```bash
container$: apt-get install -y nodejs
```

This command pulled an [Ubuntu image from Docker Hub](https://hub.docker.com/_/ubuntu/). Docker uses a file called `Dockerfile` to describe how a Docker image should consist of, we'll see more of this later.

You can already see how powerful this can be... you've downloaded an Ubuntu environment that acts and works very similar to an Ubuntu VM except much more lightweight than the VMs.

In the next step we'll recreate what we did in Lab 1 but within containers.

## Containerize `centralVirtualDevice.py`

Let's go ahead and download a Docker container that already has Python 2.7 installed. 

Open the included file called `Dockerfile`, go line by line and read what is happening. We can add more comments if necessary, but at a high-level it's equivalent to the provisioning we did within the `Vagrantfile`.

Because we created our own `Dockerfile` we need to build a image and have Docker run all the commands we have told it. The following command will build the image (layer by layer), tag it with a name, and use the `Dockerfile` in the current directory.

```bash
host ~/week2/lab2$ docker build -t central_virtual_device .
```

Look at the new image you've made at:

```bash
host$ docker images
```

Now run your container:

```bash
host$ docker run -it central_virtual_device
```

This will instantiate a new container based off of the `central_virtual_device` image and will latch onto your terminal. 

If you want to run in a daemonized mode, run:

```bash
host$ docker run -d central_virtual_device
```

## Pushing up to Docker Hub

We can also push the image we created to Docker Hub.

- [Signup for Docker Hub](https://hub.docker.com/)

You can now log into Docker Hub from the terminal:

```bash
# Use the username and password you used in Docker Hub
host$ docker login
```

We are going to add another tag for our custom image that will work with Docker Hub Registry

```bash
# Usage: docker tag [image] [new image name]
#   Example: docker tag central_virtual_device [dockerHubUsername]/central_virtual_device
host$ docker tag central_virtual_device richardjortega/central_virtual_device
```

We can push your image up to Docker Hub so other people can download it:

```bash
host$ docker push richardjortega/central_virtual_device
```

I can now view my uploaded image at Docker Hub: [https://hub.docker.com/r/richardjortega/central_virtual_device/](https://hub.docker.com/r/richardjortega/central_virtual_device/)

Other people can directly pull the image and run on their machine:

```bash
host $: docker pull richardjortega/central_virtual_device
```

## Hacker Edition: Learn about adding app data within containers

- Add a `test.txt` file (with your own arbitrary text) to the image we created using `Dockerfile`. Upload the new image to DockerHub and provide a link to your DockerHub.
    - Tip: Use `COPY` command: [https://docs.docker.com/engine/reference/builder/#copy](https://docs.docker.com/engine/reference/builder/#copy)

- In a standard development workflow with Docker, developers will typically mount their host's application  folder to the container's application folder providing a way to edit code locally on the host and it reflecting immediately within the container.
    - You can read more about this on [Manage data in containers](https://docs.docker.com/engine/tutorials/dockervolumes/) under the section [Mount a Host Directory as a Data Volume](https://docs.docker.com/engine/tutorials/dockervolumes/#mount-a-host-directory-as-a-data-volumeMount)