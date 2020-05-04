import cv2
from PIL import Image
import conf
from mss import mss
import numpy as np
import Utils.KeyRecord as KeyRecord
from Utils import LaneDetection
from time import time


def captureFrames():
    # TODO: resize the lane sct ROI
    laneSct = mss()
    speedSct = mss()
    while True:
        laneSct.get_pixels(conf.ROI)
        speedSct.get_pixels(conf.speedROI)
        # convert to gray scale by R * 299/1000 + G * 587/1000+ B * 114/1000
        laneImg = np.array(Image.frombytes('RGB', (laneSct.width, laneSct.height), laneSct.image).convert('L'))
        # laneImg = LaneDetection.detect(laneImg)
        speedImg = np.array(Image.frombytes('RGB', (speedSct.width, speedSct.height), speedSct.image).convert('L'))
        cv2.imshow('Lane Image', laneImg)
        cv2.imshow('Speed Image', speedImg)

        action = KeyRecord.catchRegisteredKeys()
        # cv2.imwrite("data/lane/{}_{}.png".format(action, time()), laneImg)
        cv2.imwrite("data/speed/{}.png".format(time()), speedImg)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break