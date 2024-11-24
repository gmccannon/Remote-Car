from flask import Flask, render_template
import time
from Motor import Motor

app = Flask(__name__)
PWM = Motor()

@app.route("/drive_forward")
def drive_forward():
    PWM.setMotorModel(800, 800, 800, 800)
    return "Moving Forward"

@app.route("/drive_backward")
def drive_backward():
    PWM.setMotorModel(-800, -800, -800, -800)
    return "Moving Backward"

@app.route("/drive_left")
def drive_left():
    PWM.setMotorModel(-800, 800, 800, -800)
    return "Turning Left"

@app.route("/drive_right")
def drive_right():
    PWM.setMotorModel(800, -800, -800, 800)
    return "Turning Right"
    
@app.route("/rotate_left")
def rotate_left():
    PWM.setMotorModel(-800, -800, 800, 800)
    return "Rotating Left"

@app.route("/rotate_right")
def rotate_right():
    PWM.setMotorModel(800, 800, -800, -800)
    return "Rotating Right"

@app.route("/stop")
def stop():
    PWM.setMotorModel(0, 0, 0, 0)
    return "Stopped"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
