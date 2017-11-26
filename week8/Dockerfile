# Start from an image that is compliant with ARMv7 and is Debian based
# Pull base RPi image from Dockerhub
FROM resin/rpi-raspbian

RUN apt-get update

# Some packages required as dependencies for building 'azure-storage' package
RUN apt-get install -y --fix-missing wget \
                                    python \
                                    python-picamera \
                                    build-essential \
                                    libssl-dev \
                                    libffi-dev \
                                    python-dev

# Install pip
RUN wget -P / https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

# Install Microsoft Azure Storage SDK for Python
RUN pip install azure-storage

# Copy all local files to /app
COPY . /app

# Cleanup to save space
RUN rm -rf /tmp/*.dep

# Make it run when container is started
CMD ["python", "/app/centralCamera.py"]
