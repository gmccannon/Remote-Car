#!/usr/bin/python

"""
PCA9685.py

Description:
This file contains a Python class for interfacing with the PCA9685 PWM/Servo driver via the I2C protocol.
The PCA9685 is a 16-channel, 12-bit PWM driver designed for controlling servos, motors, and LEDs.
It is configured here for use with a Raspberry Pi.

Key Features:
- Supports motor control using the dedicated `setMotorPwm` method.
- Provides utility for setting servo pulses for 50Hz servos with the `setServoPulse` method.
- Allows precise frequency adjustment for all channels using the `setPWMFreq` method.
- Enables direct control of individual PWM channels with `setPWM`.

Usage:
1. Connect the PCA9685 to the I2C pins (SDA, SCL) on the Raspberry Pi.
2. Ensure the default I2C address (0x40) matches or adjust it if necessary.
3. Instantiate the PCA9685 class:
   `pwm = PCA9685(0x40)`
4. Use methods like `setPWM`, `setPWMFreq`, and `setServoPulse` to control motors, servos, or LEDs.

Method Descriptions:
- `__init__(address)`: Initializes the PCA9685 object and sets the I2C address. Default is 0x40.
- `setPWMFreq(freq)`: Sets the PWM frequency for all channels. For servo control, this is typically set to 50Hz.
- `setPWM(channel, on, off)`: Directly sets the on and off times for a specified PWM channel. Useful for fine-grained control of duty cycles.
- `setMotorPwm(channel, duty)`: Controls a motor by setting the duty cycle (percentage of time the signal is on) for a specified channel.
- `setServoPulse(channel, pulse)`: Sets the pulse width for a servo on a specified channel. Input is in microseconds (e.g., 1500 for a 1.5ms pulse, corresponding to 0° or mid-position).
"""

import time
import math
import smbus

class PCA9685:

  # Registers/etc.
  __SUBADR1            = 0x02
  __SUBADR2            = 0x03
  __SUBADR3            = 0x04
  __MODE1              = 0x00
  __PRESCALE           = 0xFE
  __LED0_ON_L          = 0x06
  __LED0_ON_H          = 0x07
  __LED0_OFF_L         = 0x08
  __LED0_OFF_H         = 0x09
  __ALLLED_ON_L        = 0xFA
  __ALLLED_ON_H        = 0xFB
  __ALLLED_OFF_L       = 0xFC
  __ALLLED_OFF_H       = 0xFD

  def __init__(self, address=0x40, debug=False):
    self.bus = smbus.SMBus(1)
    self.address = address
    self.debug = debug
    self.write(self.__MODE1, 0x00)
    
  def write(self, reg, value):
    "Writes an 8-bit value to the specified register/address"
    self.bus.write_byte_data(self.address, reg, value)
      
  def read(self, reg):
    "Read an unsigned byte from the I2C device"
    result = self.bus.read_byte_data(self.address, reg)
    return result
    
  def setPWMFreq(self, freq):
    "Sets the PWM frequency"
    prescaleval = 25000000.0    # 25MHz
    prescaleval /= 4096.0       # 12-bit
    prescaleval /= float(freq)
    prescaleval -= 1.0
    prescale = math.floor(prescaleval + 0.5)
    oldmode = self.read(self.__MODE1);
    newmode = (oldmode & 0x7F) | 0x10
    self.write(self.__MODE1, newmode)        
    self.write(self.__PRESCALE, int(math.floor(prescale)))
    self.write(self.__MODE1, oldmode)
    time.sleep(0.005)
    self.write(self.__MODE1, oldmode | 0x80)

  def setPWM(self, channel, on, off):
    "Sets a single PWM channel"
    self.write(self.__LED0_ON_L+4*channel, on & 0xFF)
    self.write(self.__LED0_ON_H+4*channel, on >> 8)
    self.write(self.__LED0_OFF_L+4*channel, off & 0xFF)
    self.write(self.__LED0_OFF_H+4*channel, off >> 8)
    
  def setMotorPwm(self,channel,duty):
    self.setPWM(channel,0,duty)
    
  def setServoPulse(self, channel, pulse):
    "Sets the Servo Pulse,The PWM frequency must be 50HZ"
    pulse = pulse*4096/20000 #50HZ (20000us period)
    self.setPWM(channel, 0, int(pulse))

if __name__=='__main__':
    pass
