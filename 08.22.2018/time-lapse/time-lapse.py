# If your Pi doesn't have ImageMagick installed, in the Pi terminal type:
# sudo apt-get update
# sudo apt-get install imagemagick -y

from picamera import PiCamera
from time import sleep
from os import system
import time 

camera = PiCamera()
camera.resolution = (1024, 768) # This sets the resolution of the photos smaller to save time for making the .gif

# Take all the photos
for i in range (40):
    sleep(2) # At least 2 seconds before capturing are required to give the sensor time to set its light levels.

    date = time.strftime(' %m-%d-%Y %H:%M:%S') # Get the date and time.
    
    # Save the photo 
    camera.capture('/home/pi/Desktop/lapse/image{0:04d}'.format(i) + date + '.jpg')

# Make the .gif
delay = 50 # This is the amount of time (in 100ths of a sec) between frames.
loop = 0 # This is the number of times the gif will loop. 0 means to loop forever.

system('convert -delay ' + str (delay) + ' -loop ' + str (loop) + ' image*.jpg animation.gif') # This line only works if you have ImageMagic installed.
# If the upper line doesn't work, in the terminal simply change the directory (cd) to the folder where all the photos are located and type 'convert -delay 10 -loop 0 image*.jpg animation.gif'.

print('Work finished!')
