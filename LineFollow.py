import time
from Motor import *
from gpiozero import LineSensor

IR01 = 14
IR02 = 15
IR03 = 23
IR01_sensor = LineSensor(IR01)
IR02_sensor = LineSensor(IR02)
IR03_sensor = LineSensor(IR03)


class Line_Tracking:
    def __init__(self):
        pass

    def test_Infrared(self):
        try:
            while True:
                if IR01_sensor.value !=True and IR02_sensor.value == True and IR03_sensor.value !=True:
                    print ('Middle')
                elif IR01_sensor.value !=True and IR02_sensor.value != True and IR03_sensor.value ==True:
                    print ('Right')
                elif IR01_sensor.value ==True and IR02_sensor.value != True and IR03_sensor.value !=True:
                    print ('Left')
        except KeyboardInterrupt:
            print ("\nEnd of program")
        
    def run(self):
        while True:
            self.LMR = 0  
            if IR01_sensor.value:
                self.LMR = self.LMR + 4  
            if IR02_sensor.value:
                self.LMR = self.LMR + 2  
            if IR03_sensor.value:
                self.LMR = self.LMR + 1  
            
            if self.LMR == 2:  
                PWM.setMotorModel(600, 600, 600, 600)
            elif self.LMR == 4:  
                PWM.setMotorModel(-600, -600, 600, 600)
            elif self.LMR == 6:  
                PWM.setMotorModel(-600, -600, 600, 6000)
            elif self.LMR == 1:  
                PWM.setMotorModel(600, 600, -600, -600)
            elif self.LMR == 3:  
                PWM.setMotorModel(600, 600, -600, -600)
            elif self.LMR == 7: 
                PWM.setMotorModel(0, 0, 0, 0)



if __name__ == '__main__':
    infrared=Line_Tracking()
    print ('Program is starting')
    try:
        infrared.run()
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
