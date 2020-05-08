from time import time
from keras import layers, Model, optimizers
from keras.utils import np_utils
import pandas as pd
import numpy as np
from conf import speedROI
import cv2
import os


def cutTwoDigitsSpeedImg():
    files = os.listdir("data/speed/")
    for file in files:
        if (file[0] == "."):
            continue
        img = cv2.imread(os.path.join("data/speed/", file))
        print(file)
        print(img.shape)
        height, width, channels = img.shape
        numberA = img[:, :width//2]
        numberB = img[:, width//2:]
        print(numberA)
        cv2.imwrite("data/cutted_speed/{}.png".format(time()), numberA)
        cv2.imwrite("data/cutted_speed/{}.png".format(time()), numberB)

def formatTrainingData(X, Y):
    # Y to one hot. TODO: check map relation
    Y = np_utils.to_categorical(Y).tolist()
    samples = []
    for x, y in zip(X, Y):
        samples.append(x+y)
    return pd.DataFrame(samples)

def formTrainingData():
    levels = os.listdir("data/speed")
    X = []
    Y = []
    for i, level in enumerate(levels):
        imgs = os.listdir(os.path.join("data/speed", level))
        for img in imgs:
            imgPath = os.path.join("data/speed/", level, img)
            # read as gray scale and flatten
            x = np.array(cv2.imread(imgPath, 0)).flatten().tolist()
            X.append(x)
            Y.append(i)
    samples = formatTrainingData(X, Y)
    samples = samples.sample(frac=1).reset_index(drop=True)  # make shuffle
    return samples
            
def defineSpeedDetectionModel():
    imgFlattenLength = speedROI["width"]*speedROI["height"]

    inputLayer = layers.Input(shape=[imgFlattenLength], name="input")
    dense_1 = layers.Dense(units=128, input_shape=(imgFlattenLength, ), activation="relu", use_bias=True, name="dense_1")(inputLayer)
    output = layers.Dense(units=11, input_shape=(128, ), activation="softmax", use_bias=True, name="output")(dense_1)

    model = Model(inputLayer, output)
    opt = optimizers.Adam(lr=0.001)

    model.compile(opt, loss="categorical_crossentropy", metrics=["accuracy"])
    return model

def trainSpeedDetectionModel(samples, model):
    X = samples.iloc[:, :-11]
    Y = samples.iloc[:, -11:]
    Y.columns = ["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
    model.fit(X, Y, epochs=30)
    return model


if __name__ == '__main__':
    cutTwoDigitsSpeedImg()

