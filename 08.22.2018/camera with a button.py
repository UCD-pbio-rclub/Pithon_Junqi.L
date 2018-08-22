# Use 2 jumper wires to connect a button between GND and pin 23

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin pos$
GPIO.setmode(GPIO.BCM)

switch_pin = 23

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    for i in range (90):
        if GPIO.input(switch_pin) == False:
            print("Say Cheese!")
            date = time.strftime(' %m-%d-%Y %H:%M:%S')
            camera.capture('/home/pi/Desktop/image{0:04d}'.format(i) + date + '.jpg')
        sleep(0.2)
