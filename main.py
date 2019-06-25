import sensor
from pyb import Pin

# Reset and initialize sensor
sensor.reset()                      # Reset and initialize the sensor.
# Set greyscale
sensor.set_pixformat(sensor.GRAYSCALE)
# Set frame size to VGA (640 x 480)
sensor.set_framesize(sensor.VGA)
# V Res of 80 == less work (40 for 2X the speed). May need to tweak para
# https://docs.openmv.io/library/omv.sensor.html
sensor.set_windowing((480, 480))
# Wait for settings
sensor.skip_frames(time = 2000)

# Connect switch to pin 0
pin0 = Pin('P0', Pin.IN, Pin.PULL_UP)

while(True):
    if pin0.value()==False:
        img = sensor.snapshot()
        # call routine for preprocessing

        # strength of 1.8 is good for the 2.8mm lens.
        img.lens_corr(1.8)
        # call routine for translating to 1s and 0s

        # call routine to localise k by k window in 2k-1 by 2k-1

        # call action function based on location; in our case, music function

