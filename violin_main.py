import sensor, image, time, math
from pyb import Pin,UART,delay

# Connect switch to pin 0
pin0 = Pin('P0', Pin.IN, Pin.PULL_UP)

# UART init
uart = UART(3,115200,timeout_char=1000)

# Camera init
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA) # we run out of memory if the resolution is much bigger...
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
sensor.set_auto_whitebal(False)  # must turn this off to prevent image washout...
clock = time.clock()

# The apriltag code supports up to 6 tag families which can be processed at the same time.
# Returned tag objects will have their tag family and id within the tag family.
tag_families = 0
tag_families |= image.TAG16H5 # comment out to disable this family
# tag_families |= image.TAG25H7 # comment out to disable this family
# tag_families |= image.TAG25H9 # comment out to disable this family
# tag_families |= image.TAG36H10 # comment out to disable this family
# tag_families |= image.TAG36H11 # comment out to disable this family (default family)
# tag_families |= image.ARTOOLKIT # comment out to disable this family

# Set num of tags used in Programme
num_tags = 90
length_of_music = 290

def family_name(tag):
    if(tag.family() == image.TAG36H11):
        return "TAG36H11"
    if(tag.family() == image.TAG16H5):
        return "TAG16H5"
    if(tag.family() == image.TAG25H7):
        return "TAG25H7"
    if(tag.family() == image.TAG25H9):
        return "TAG25H9"
    if(tag.family() == image.TAG36H10):
        return "TAG36H10"
    if(tag.family() == image.ARTOOLKIT):
        return "ARTOOLKIT"

def number_of_seconds(tag, length_of_music):
    secs = (tag/num_tags) * length_of_music
    return int(secs)

while(True):
    img = sensor.snapshot()
    # Product/Robot is always on standby for button press
    if pin0.value()==False:
        clock.tick()
        for tag in img.find_apriltags(): # defaults to TAG36H11 without "families".
            img.draw_rectangle(tag.rect(), color = (255, 0, 0))
            img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
            print_args = (family_name(tag), tag.id(), (180 * tag.rotation()) / math.pi)
            #print("Tag Family %s, Tag ID %d, rotation %f (degrees)" % print_args)
            tag = tag.id()
            #print(tag)
            seconds = number_of_seconds(tag, length_of_music)
        # Sending message
        if 'seconds' in locals():
            uart.write(str(seconds) + "\n")
            print("Sent timing via UART: " + str(seconds) + " second in music")

