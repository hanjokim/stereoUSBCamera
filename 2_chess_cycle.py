# Copyright (C) 2019 Eugene Pomazov, <stereopi.com>, virt2real team
#
# This file is part of StereoPi tutorial scripts.
#
# StereoPi tutorial is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# StereoPi tutorial is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with StereoPi tutorial.
# If not, see <http://www.gnu.org/licenses/>.
#
# Most of this code is updated version of 3dberry.org project by virt2real
#
# Thanks to Adrian and http://pyimagesearch.com, as there are lot of
# code in this tutorial was taken from his lessons.
#
# ================================================
# Modified by 현자 to work with non-Raspberry Pi PC's
# Cam used: OV9732 Binocular Sync Camera Module, 72 Degree, 1 Million Pixel

import os
import time
from datetime import datetime
import cv2
import numpy as np

# Photo session settings
total_photos = 30  # Number of images to take
countdown = 5  # Interval for count-down timer, seconds
font = cv2.FONT_HERSHEY_SIMPLEX  # Cowntdown timer font

# Camera settimgs (at 640x240, its default frame rate = 25)
cam_width = 640  # Width must be dividable by 32
cam_height = 240  # Height must be dividable by 16

# capture = np.zeros((img_height, img_width, 4), dtype=np.uint8)
print("Final resolution: " + str(cam_width) + " x " + str(cam_height))

# Initialize the camera
camera = cv2.VideoCapture(0)
# Must set camera WORKING camera resolution to get Left/Right side by side
camera.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

# Lets start taking photos!
counter = 0
t2 = datetime.now()
print("Starting photo sequence")
while camera.isOpened():
    ret, frame = camera.read()
    t1 = datetime.now()
    cntdwn_timer = countdown - int((t1 - t2).total_seconds())
    # If cowntdown is zero - let's record next image
    if cntdwn_timer == -1:
        counter += 1
        filename = './scenes/scene_' + str(cam_width) + 'x' + str(cam_height) + '_' + \
                   str(counter) + '.png'
        cv2.imwrite(filename, frame)
        print(' [' + str(counter) + ' of ' + str(total_photos) + '] ' + filename)
        t2 = datetime.now()
        time.sleep(1)
        cntdwn_timer = 0  # To avoid "-1" timer display
        next
    # Draw cowntdown counter, seconds
    cv2.putText(frame, str(cntdwn_timer), (50, 50), font, 2.0, (0, 0, 255), 4, cv2.LINE_AA)
    cv2.imshow("pair", frame)
    key = cv2.waitKey(1) & 0xFF

    # Press 'Q' key to quit, or wait till all photos are taken
    if (key == ord("q")) | (counter == total_photos):
        break

print("Photo sequence finished")
camera.release()