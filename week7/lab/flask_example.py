from flask import Flask  
from flask import request
app = Flask(__name__)

# http://<RASPBERRY_PI_IP>/take_photo?timeout=1000
# Pass a query parameter of timeout for when to take photo
# Timeout should be in milliseconds
@app.route('/take_photo', methods=['GET'])
def take_photo():
    return "OK"

# http://<RASPBERRY_PI_IP>/take_video?timeout=1000
# Pass a query parameter of timeout for when to take photo
# Timeout should be in milliseconds
@app.route('/take_video', methods=['GET'])
def take_video():  
    return "OK"

if __name__ == '__main__':  
    app.run()
