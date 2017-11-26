#!/usr/bin/python

from picamera import PiCamera
from time import sleep
import time
import os

# timeout (int): Time to take photo (in milliseconds)
# Camera will add 2 seconds to timeout at beginning to allow for light adjustment
def take_photo(timeout):
    filename, filepath = take_blob("IMAGE", timeout)
    return filename, filepath

# timeout (int): Duration to record video (in milliseconds)
# Camera will start recording after allowing for 2 seconds for light adjustment
def take_video(timeout):
    filename, filepath = take_blob("VIDEO", timeout)
    return filename, filepath

# This method initializes the camera for 3 seconds
# blob_type can be ["IMAGE", "image"] or ["VIDEO", "video"]
def take_blob(blob_type, timeout):
    # Initialize camera
    camera = PiCamera()
    print 'Camera initialized'

    # Set proper rotation (if defined)
    if "ROTATION" in os.environ:
        print 'Rotating camera to: {} degrees'.format(os.getenv("ROTATION"))
        camera.rotation = int(os.getenv("ROTATION"))

    ## Start up camera and preview mode
    print 'Starting preview mode...'
    camera.start_preview()

    # Allow for light adjustment
    sleep(2)

    # UTC Timestamp from epoch
    timestamp = int(time.time())
    filename = ""
    filepath = ""

    # Depending on blob_type (IMAGE OR VIDEO)
    if blob_type in ["IMAGE", "image"]: 
        # Set image filename and filepath
        filename = "img_{}.jpg".format(str(timestamp))
        filepath = "/app/images/{}".format(filename)

        # Time to take photo
        timeout_seconds = timeout / 1000
        sleep(timeout_seconds)

        # Capture image
        camera.capture(filepath)

        print 'Photo stored as: {}'.format(filename)
        print 'Files stored within host "images" folder'
    elif blob_type in ["VIDEO", "video"]:
        # Set image filename and filepath
        filename = "video_{}.jpg".format(str(timestamp))
        filepath = "/app/videos/{}".format(filename)

        # Start recording
        camera.start_recording(filepath)

        # Duration of recording
        timeout_seconds = timeout / 1000
        sleep(timeout_seconds)

        # End recording
        camera.stop_recording()

        print 'Video stored as: {}'.format(filename)
        print 'Files stored within host "videos" folder'
    else:
        print 'Please specify a valid blob_type of either "IMAGE" or "VIDEO"'

    camera.stop_preview()
    print 'Preview mode ended.'

    return filename, filepath