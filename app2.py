from flask import Flask, render_template
import time
from Motor import Motor

app = Flask(__name__)
PWM = Motor()

# Adjustments to compensate for drift (tune these values based on your testing)
pos_motor_adjustment = -60  # Slightly increase the speed of left motors (FL, BL) to correct right drift
neg_motor_adjustment = 60  # Slightly decrease the speed of right motors (FR, BR) to correct right drift

@app.route("/drive_forward")
def drive_forward():
    # Adjust FL and BL motors slightly to balance drift
    PWM.setMotorModel(800 + pos_motor_adjustment, 800 + pos_motor_adjustment, 800 + neg_motor_adjustment, 800 + neg_motor_adjustment)
    return "Moving Forward"

@app.route("/drive_backward")
def drive_backward():
    # Adjust FL and BL motors slightly to balance drift
    PWM.setMotorModel(-800 + neg_motor_adjustment, -800 + neg_motor_adjustment, -800 + pos_motor_adjustment, -800 + pos_motor_adjustment)
    return "Moving Backward"

@app.route("/drive_left")
def drive_left():
    PWM.setMotorModel(-800, 800, 800, -800)
    return "Turning Left"

@app.route("/drive_right")
def drive_right():
    # Increase power on right motors to counteract rotation
    PWM.setMotorModel(870, -950, -870, 950)  # Adjusted values to prevent counter-clockwise spin
    return "Turning Right"
    
@app.route("/rotate_left")
def rotate_left():
    PWM.setMotorModel(-800, -800, 800, 800)
    return "Rotating Left"

@app.route("/rotate_right")
def rotate_right():
    PWM.setMotorModel(800, 800, -800, -800)
    return "Rotating Right"
    
@app.route("/drive_up_left")
def drive_up_left():
    PWM.setMotorModel(0, 800, 800, 0)
    return "Moving Up Left"

@app.route("/drive_up_right")
def drive_up_right():
    PWM.setMotorModel(800, 0, 0, 800)
    return "Moving Up Right"

@app.route("/drive_down_left")
def drive_down_left():
    PWM.setMotorModel(-800, 0, 0, -800)
    return "Moving Down Left"

@app.route("/drive_down_right")
def drive_down_right():
    PWM.setMotorModel(0, -800, -800, 0)
    return "Moving Down Right"

@app.route("/stop")
def stop():
    PWM.setMotorModel(0, 0, 0, 0)
    return "Stopped"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
