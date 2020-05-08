import cv2
from PIL import Image
import conf
from mss import mss
import numpy as np
import Utils.KeyRecord as KeyRecord
from Utils import LaneDetection
from time import time

def region_of_interest(img, vertices):
    """
        Get region of interest from given image
    """
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def captureFrames():
    # TODO: resize the lane sct ROI
    mainSct = mss()
    while True:
        mainSct.get_pixels(conf.mainROI)
        # convert to gray scale by R * 299/1000 + G * 587/1000+ B * 114/1000
        mainImg = np.array(Image.frombytes('RGB', (mainSct.width, mainSct.height), mainSct.image).convert('L'))

        speedImg = region_of_interest(mainImg, np.array([conf.speedROI], np.int32))
        canniedMainImg = LaneDetection.detect(mainImg)
        laneImg = region_of_interest(canniedMainImg, np.array([conf.laneROI], np.int32))

        cv2.imshow('Main ROI', mainImg)
        cv2.imshow('Lane ROI', laneImg)
        cv2.imshow('Speed ROI', speedImg)

        action = KeyRecord.catchRegisteredKeys()
        # cv2.imwrite("data/speed/{}.png".format(time()), speedImg)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break