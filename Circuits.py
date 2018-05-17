#SensorEd Workshop V0.1
#Author - Jacob Ulasevich
#Circuit Introduction

"""
Knowledge of circtuis is powerful information to have.  By connecting
your Raspberry Pi board to an external apparatus we will bring your code
to life!
"""

"""
Be sure you set up your circuit board correctly according to the worskhop
documentation before moving on to the software. 
"""

import RPi.GPIO as GPIO
import time

"""
GPIO is used to set up the pins on your Raspberry Pi to get them ready
for data collection.

Time is used to control the board by giving specific periods of waiting
time.
"""

#How many times do you want the LED light to blink?
repeat = 20

#The following sets up the entire board.
GPIO.setmode(GPIO.BOARD)

#Sets up pin 16 on the board for reaiding data.
GPIO.setup(16, GPIO.OUT)

'''
To turn the light on you use the function
GPIO.output(PIN_NUMBER, GPIO.HIGH)

To turn the light off you use the function
GPIO.output(PIN_NUMBER, GPIO.LOW)

To tell the board to "wait" you can use the function
time.sleep(WAIT_PERIOD)
'''


#Fill in the while loop to make the LED blink!
while(repeat > 10):
    GPIO.output(16, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(16, GPIO.LOW)
    time.sleep(.5)
    repeat -=1
    

#Its important to always clean up your mess
GPIO.cleanup()
