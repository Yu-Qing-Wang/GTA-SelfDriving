
from keras import layers, Model, optimizers
from keras.utils import np_utils
import pandas as pd
import numpy as np
from conf import speedROIWidth, speedROIHeight, laneROIWidth, laneROIHeight, frontDataBaseDir, speedDataBaseDir
import cv2
import os


def formTrainingData():
    dates = os.listdir(frontDataBaseDir)
    XFront = []
    XSpeed = []
    Y = []
    for date in dates:
        frontDataDateDir = os.path.join(frontDataBaseDir, date)
        imgs = os.listdir(frontDataDateDir)
        for img in imgs:
            action = (img.split("_")[1]).split(".")[0]
            imgPath = os.path.join(frontDataDateDir, img)
            x = cv2.imread(imgPath, 0)

    # # nSamples * channel * height * width
    # X, Y = formatTrainingData(X, Y)
    # return X, Y