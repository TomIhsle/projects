# Start from base RPi image from Dockerhub
FROM richardjortega/uwiot-rpi-baseimage

RUN apt-get update

# Add flask
RUN pip install flask

# Copy all local files to /app
COPY . /app
WORKDIR /app

# Flask requires an environment variable of the script to be set
# Note: If you change the filename, change this
ENV FLASK_APP /app/centralCameraServer.py

EXPOSE 5000

# Make it run when container is started
# Add host info for externally visible
CMD ["flask", "run", "--host=0.0.0.0"]
