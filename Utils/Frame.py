import cv2
from keras.models import load_model
from PIL import Image
import conf
from mss import mss
import numpy as np
import Utils.KeyRecord as KeyRecord
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

def load_models():
    speedDetectModel = load_model("models/speed_detector.h5")
    return speedDetectModel

def get_index_with_max_score(scores):
    maxScore = float("-Inf")
    index = None
    for i, score in enumerate(scores):
        if score > maxScore:
            maxScore = score
            index = i
    return index

def captureFrames():
    mainSct = mss()
    date = "2020-05-15"
    # speedDetectModel = load_models()
    frame = 0
    while True:
        mainSct.get_pixels(conf.mainROI)
        # convert to gray scale by R * 299/1000 + G * 587/1000+ B * 114/1000
        mainImg = np.array(Image.frombytes('RGB', (mainSct.width, mainSct.height), mainSct.image).convert('L'))

        speedImg = mainImg[conf.speedROIHeightRange[0]:conf.speedROIHeightRange[1], conf.speedROIWidthRange[0]:conf.speedROIWidthRange[1]]
        frontImg = mainImg[conf.laneROIHeightRange[0]:conf.laneROIHeightRange[1], conf.laneROIWidthRange[0]:conf.laneROIWidthRange[1]]


        # canniedLaneImg = LaneDetection.detect(laneImg)

        # reshape to nSamples * nChannel * height * width
        # levelsScore = speedDetectModel.predict(np.array(speedImg).reshape(1, 1, conf.speedROIHeight, conf.speedROIWidth))
        # speedLevel = get_index_with_max_score(levelsScore[0])

        cv2.imshow('Main ROI', mainImg)
        cv2.imshow('Front ROI', frontImg)
        cv2.imshow('Speed ROI', speedImg)

        action = KeyRecord.catchRegisteredKeys()
        if action == conf.LEFT or action == conf.RIGHT or action == conf.SLOW or frame % conf.FRAMES_PER_SAMPLE == 0:
            # make time same for front img and speed img
            capTime = time()
            cv2.imwrite("data/front_img_for_training/{}/{}_{}.png".format(date, capTime, action), frontImg)
            cv2.imwrite("data/speed_img_for_training/{}/{}_{}.png".format(date, capTime, action), speedImg)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        frame += 1
        if frame == 1000:
            frame = 0