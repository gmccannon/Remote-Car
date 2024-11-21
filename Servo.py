import time
from PCA9685 import PCA9685


class Servo:
    def __init__(self):
        self.PwmServo = PCA9685(0x40, debug=True)
        self.PwmServo.setPWMFreq(50)
        self.PwmServo.setServoPulse(8,1500)
        self.PwmServo.setServoPulse(9,1500)
    def setServoPwm(self,channel,angle,error=10):
        angle=int(angle)
        if channel=='0':
            self.PwmServo.setServoPulse(8,2500-int((angle+error)/0.09))
        elif channel=='1':
            self.PwmServo.setServoPulse(9,500+int((angle+error)/0.09))
        elif channel=='2':
            self.PwmServo.setServoPulse(10,500+int((angle+error)/0.09))
        elif channel=='3':
            self.PwmServo.setServoPulse(11,500+int((angle+error)/0.09))
        elif channel=='4':
            self.PwmServo.setServoPulse(12,500+int((angle+error)/0.09))
        elif channel=='5':
            self.PwmServo.setServoPulse(13,500+int((angle+error)/0.09))
        elif channel=='6':
            self.PwmServo.setServoPulse(14,500+int((angle+error)/0.09))
        elif channel=='7':
            self.PwmServo.setServoPulse(15,500+int((angle+error)/0.09))

if __name__ == '__main__':
    print("Rotate to 90°.") 
    print("If they have already been at 90°, nothing will happen.")
    print("Keep the program running!!! installing servos...")
    pwm=Servo()
    try:
        while True:
            for i in range(50,110,1):
                pwm.setServoPwm('0',i)
                time.sleep(0.01)
            for i in range(110,50,-1):
                pwm.setServoPwm('0',i)
                time.sleep(0.01)
            for i in range(80,150,1):
                pwm.setServoPwm('1',i)
                time.sleep(0.01)
            for i in range(150,80,-1):
                pwm.setServoPwm('1',i)
                time.sleep(0.01)
        except KeyboardInterrupt:
                pwm.setServoPwm('0',90)
                pwm.setServoPwm('1',90)
