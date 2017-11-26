# Full Dockefile reference: https://docs.docker.com/engine/reference/builder/

# Start from a base Docker image
#   Use Python with version 2.7
#   Docker Hub Python: https://hub.docker.com/_/python/
#   Dockerfile reference for python:2.7: https://github.com/docker-library/python/blob/1ca4a57b20a2f66328e5ef72df866f701c0cd306/2.7/Dockerfile
FROM python:2.7

# The RUN will run any arbitrary text after as if it were on the shell
RUN echo "I'm making a Docker container!"
RUN apt-get update
RUN apt-get install -y python
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install paho-mqtt
RUN python --version

# Copy a file locally to the image at a specified path
COPY centralVirtualDevice.py /centralVirtualDevice.py

# Set working directory to root directory for all future commands.
WORKDIR /

# Execute the command and stay attached (unless program quits)
CMD ["python", "centralVirtualDevice.py"]
