from flask import Flask  
from flask import request
import centralcamera 

app = Flask(__name__)

# http://<RASPBERRY_PI_IP>/take_photo?timeout=10000
@app.route('/take_photo', methods=['GET'])
def take_photo():
    timeout_ms = request.args.get("timeout")

    if isinstance(timeout_ms, int):
        print "Taking photo with a {} timeout".format(str(timeout_ms))
        centralcamera.take_photo(timeout_ms)
    else:
        # If timeout is not provided take a photo in 3 seconds
        print "Taking photo with a {} timeout".format(str(timeout_ms))
        centralcamera.take_photo(3000)

    return "OK"

# http://<RASPBERRY_PI_IP>/take_video?timeout=10000
@app.route('/take_video', methods=['GET'])
def take_video():  
    timeout_ms = request.args.get("timeout")

    if isinstance(timeout_ms, int):
        print "Taking video with a {} timeout".format(str(timeout_ms))
        centralcamera.take_video(timeout_ms)
    else:
        # If timeout is not provided take a video for 3 seconds
        print "Taking video with a {} timeout".format(str(timeout_ms))
        centralcamera.take_video(3000)

    return "OK"

if __name__ == '__main__':  
    app.run()
