from flask import Flask
from flask import render_template, request
import time
from rover import Rover

app = Flask(__name__)

rover = Rover()
a=1
@app.route("/")
def index():
    rover.start()
    return render_template('robot.html', name="robot")


@app.route("/up_side")
def up_side():
    rover.forward()
    return 'true'

@app.route("/down_side")
def down_side():
    rover.backward()
    return 'true'

@app.route("/left_side")
def left_side():
    rover.turn_left()
    return 'true'
    
@app.route("/right_side")
def right_side():
    rover.turn_right()
    return 'true'

@app.route("/stop")
def stop():
    rover.stop()
    return 'true'

if __name__ == "__main__":
 print("Start")
 app.run(host='0.0.0.0',port=8081)