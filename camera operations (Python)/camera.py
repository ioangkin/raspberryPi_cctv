#The file has been created with Raspberry Pi (RP) Python
#Sits in RP's SD card, under: /home/pi

from picamera import PiCamera
from time import sleep

# New camera object
camera = PiCamera()

# Set resolution. Max res
#   for photos: 2592 x 1944,
#   for videos: 1920 x 1080
#   Default: monitor's actual res.
# minimum resolution allowed:  64 x 64

camera.resolution = (200, 200)
camera.framerate = 15 #  frame rate needs to be at 15 to enable maximum resolution

# Open preview window
camera.start_preview()
# Alters window's transparency. values between 0 and 255
# camera.start_preview(alpha=200)

# Rotate the view if needed,accepted values: 0, 90, 180, 270
camera.rotation = 180

# add text in the photos only (no in vid)
# camera.annotate_text = "Hello world!"

# Capture stills
camera.capture('/home/pi/Desktop/stills/images.jpg') #Still shot

# Capture sequence of stills
#for i in range(5):
#    sleep(2) # must be at least 2 (seconds) to give the sensor time to set its light levels before capturing. 
#    camera.capture('/home/pi/Desktop/stills/image%s.jpg' % i) #Still shot

#Capture a vid
# camera.start_recording('/home/pi/video.h264')
# sleep(7) #Video duration
# camera.stop_recording()
#To play the video, run following in terminal: omxplayer video.h264

#Close preview window
# sleep(10) # you may keep the preview open for a set time
camera.stop_preview()


# more effects: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/8
# such as:
#    Brightness #camera.brightness = 50 #0-100. def: 50
#    Contrast #camera.contrast = 50 #0-100. def: 50
#    fade a sequence of stills
#    annotation colours
#    image effects


