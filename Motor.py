"""
Motor.py

Description:
This file contains a Python class (`Motor`) to control a robot's four wheels using the PCA9685 PWM/Servo driver. 
It allows precise motor control for forward, backward, and rotational movements, along with a utility for testing 
basic movement commands.

Key Features:
- Provides individual control for each wheel: left upper, left lower, right upper, and right lower.
- Automatically adjusts motor duty cycles to stay within a valid range using `duty_range`.
- Supports combined motor control via the `setMotorModel` method for coordinated movement.
- Includes a `Rotate` method to perform rotational movements based on an angle.
- Provides a testing loop for forward, backward, left, right, and stop commands.

Dependencies:
- PCA9685 module for PWM control.
- ADC module for battery level compensation during rotations.
- Python's built-in `math` and `time` modules for trigonometric calculations and delays.

Class and Method Descriptions:
- `Motor`:
  - `__init__`: Initializes the motor controller, sets up the PCA9685, and sets a default PWM frequency of 50Hz.
  - `duty_range(duty1, duty2, duty3, duty4)`: Ensures all motor duty cycles are within the valid range (-4095 to 4095).
  - `left_Upper_Wheel(duty)`: Controls the left upper wheel, moving forward, backward, or stopping based on duty.
  - `left_Lower_Wheel(duty)`: Controls the left lower wheel, with similar functionality as `left_Upper_Wheel`.
  - `right_Upper_Wheel(duty)`: Controls the right upper wheel.
  - `right_Lower_Wheel(duty)`: Controls the right lower wheel.
  - `setMotorModel(duty1, duty2, duty3, duty4)`: Controls all four wheels simultaneously with specified duty cycles.
  - `Rotate(n)`: Rotates the robot by a specified angle `n` while compensating for battery voltage.

Usage:
1. Instantiate the `Motor` class: `PWM = Motor()`.
2. Use the `setMotorModel` method to control all four wheels.
   Example: `PWM.setMotorModel(2000, 2000, 2000, 2000)` for forward motion.
3. Use the `Rotate` method for rotation, or call `loop()` for predefined movements.

Testing:
- The `loop` function demonstrates basic movements: forward, backward, left, right, and stop.
- The `destroy` function ensures the motors stop safely upon exiting the program.

Run:
- Execute the script directly to observe predefined movements, or use the methods for custom control.
"""

import time
import math
from PCA9685 import PCA9685
from ADC import *

class Motor:
    def __init__(self):
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.setPWMFreq(50)
        self.time_proportion = 3
        self.adc = Adc()
      
    def duty_range(self,duty1,duty2,duty3,duty4):
        if duty1>4095:
            duty1=4095
        elif duty1<-4095:
            duty1=-4095        
        
        if duty2>4095:
            duty2=4095
        elif duty2<-4095:
            duty2=-4095
            
        if duty3>4095:
            duty3=4095
        elif duty3<-4095:
            duty3=-4095
            
        if duty4>4095:
            duty4=4095
        elif duty4<-4095:
            duty4=-4095
        return duty1,duty2,duty3,duty4
        
    def left_Upper_Wheel(self,duty):
        if duty>0:
            self.pwm.setMotorPwm(0,0)
            self.pwm.setMotorPwm(1,duty)
        elif duty<0:
            self.pwm.setMotorPwm(1,0)
            self.pwm.setMotorPwm(0,abs(duty))
        else:
            self.pwm.setMotorPwm(0,4095)
            self.pwm.setMotorPwm(1,4095)
    def left_Lower_Wheel(self,duty):
        if duty>0:
            self.pwm.setMotorPwm(3,0)
            self.pwm.setMotorPwm(2,duty)
        elif duty<0:
            self.pwm.setMotorPwm(2,0)
            self.pwm.setMotorPwm(3,abs(duty))
        else:
            self.pwm.setMotorPwm(2,4095)
            self.pwm.setMotorPwm(3,4095)
    def right_Upper_Wheel(self,duty):
        if duty>0:
            self.pwm.setMotorPwm(6,0)
            self.pwm.setMotorPwm(7,duty)
        elif duty<0:
            self.pwm.setMotorPwm(7,0)
            self.pwm.setMotorPwm(6,abs(duty))
        else:
            self.pwm.setMotorPwm(6,4095)
            self.pwm.setMotorPwm(7,4095)
    def right_Lower_Wheel(self,duty):
        if duty>0:
            self.pwm.setMotorPwm(4,0)
            self.pwm.setMotorPwm(5,duty)
        elif duty<0:
            self.pwm.setMotorPwm(5,0)
            self.pwm.setMotorPwm(4,abs(duty))
        else:
            self.pwm.setMotorPwm(4,4095)
            self.pwm.setMotorPwm(5,4095)
            
 
    def setMotorModel(self,duty1,duty2,duty3,duty4):
        duty1,duty2,duty3,duty4=self.duty_range(duty1,duty2,duty3,duty4)
        self.left_Upper_Wheel(duty1)
        self.left_Lower_Wheel(duty2)
        self.right_Upper_Wheel(duty3)
        self.right_Lower_Wheel(duty4)
            
    def Rotate(self,n):
        angle = n
        battery_level_compensate =7.5/(self.adc.recvADC(2)*3)
        while True:
            W = 2000

            VY = int(2000 * math.cos(math.radians(angle)))
            VX = -int(2000 * math.sin(math.radians(angle)))

            FR = VY - VX + W
            FL = VY + VX - W
            BL = VY - VX - W
            BR = VY + VX + W

            PWM.setMotorModel(FL, BL, FR, BR)
            print("rotating")
            time.sleep(5*self.time_proportion*battery_level_compensate/1000)
            angle -= 5


PWM=Motor()   

def test_motors(): 
    PWM.setMotorModel(2000,2000,2000,2000)       #Forward
    time.sleep(3)
    PWM.setMotorModel(-2000,-2000,-2000,-2000)   #Back
    time.sleep(3)
    PWM.setMotorModel(-500,-500,2000,2000)       #Left 
    time.sleep(3)
    PWM.setMotorModel(2000,2000,-500,-500)       #Right    
    time.sleep(3)
    PWM.setMotorModel(0,0,0,0)                   #Stop
    
def stop_now():
    PWM.setMotorModel(0,0,0,0)    
  
if __name__=='__main__':
    try:
        test_motors()
    except KeyboardInterrupt:
        stop_now()
