# Modified by 현자 to work with non-Raspberry Pi PC's
# Cam used: OV9732 Binocular Sync Camera Module, 72 Degree, 1 Million Pixel

import time
import cv2
import os
from datetime import datetime

# File for captured image
filename = './scenes/photo.png'

# Camera settimgs (at 640x240, its default frame rate = 25)
cam_width = 640  # Width must be dividable by 32
cam_height = 240  # Height must be dividable by 16

print("Camera Resolution: " + str(cam_width) + " x " + str(cam_height))

# Initialize the camera
camera = cv2.VideoCapture(0)
# Must set camera WORKING camera resolution to get Left/Right side by side
camera.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

t2 = datetime.now()
counter = 0
avgtime = 0
# Capture frames from the camera
while camera.isOpened():
    ret, frame = camera.read()
    counter += 1
    t1 = datetime.now()
    timediff = t1 - t2
    avgtime = avgtime + (timediff.total_seconds())
    cv2.imshow("Both Eyes", frame)
    key = cv2.waitKey(1) & 0xFF
    t2 = datetime.now()
    # if the `q` key was pressed, break from the loop and save last image
    if key == ord("q"):
        avgtime = avgtime / counter
        print("Average time between frames: " + str(avgtime))
        print("Average FPS: " + str(1 / avgtime))
        if (os.path.isdir("./scenes") == False):
            os.makedirs("./scenes")
        cv2.imwrite(filename, frame)
        break

camera.release()