from time import time
from keras import layers, Model, optimizers
from keras.utils import np_utils
import pandas as pd
import numpy as np
from conf import speedROIWidth, speedROIHeight
import cv2
import os


def formatTrainingData(X, Y):
    # Y to one hot. TODO: check map relation
    Y = np_utils.to_categorical(Y).tolist()
    samples = []
    for x, y in zip(X, Y):
        samples.append([x, y])
    samples = pd.DataFrame(samples, columns=["X", "Y"])
    samples = samples.sample(frac=1).reset_index(drop=True)
    # convert back to np array after shuffle
    X = np.array([x for x in samples["X"]])
    print(X.shape)
    Y = np.array([y for y in samples["Y"]])
    print(Y.shape)
    return X, Y

def formTrainingData():
    levels = os.listdir("data/speed")
    X = []
    Y = []
    # level seq is [0, 1, 10, 2, ...] so just use dirname as label
    for level in levels:
        imgs = os.listdir(os.path.join("data/speed", level))
        for img in imgs:
            imgPath = os.path.join("data/speed/", level, img)
            # read as gray scale and keep left half img
            # cvImg = cv2.imread(imgPath, 0) # can't read img with chinese character
            cvImg = cv2.imdecode(np.fromfile(imgPath, dtype=np.uint8), -1)
            x = np.array(cvImg).reshape((1, speedROIHeight, speedROIWidth))
            X.append(x)
            Y.append(int(level))
    print("0: {}".format(len([y for y in Y if y == 0])))
    print("1: {}".format(len([y for y in Y if y == 1])))
    print("2: {}".format(len([y for y in Y if y == 2])))
    print("3: {}".format(len([y for y in Y if y == 3])))
    print("4: {}".format(len([y for y in Y if y == 4])))
    print("5: {}".format(len([y for y in Y if y == 5])))
    print("6: {}".format(len([y for y in Y if y == 6])))
    print("7: {}".format(len([y for y in Y if y == 7])))
    print("8: {}".format(len([y for y in Y if y == 8])))
    print("9: {}".format(len([y for y in Y if y == 9])))
    # nSamples * channel * height * width
    X, Y = formatTrainingData(X, Y)
    return X, Y
            
def defineSpeedDetectionModel():
    imgFlattenLength = speedROIWidth * speedROIHeight

    inputLayer = layers.Input(shape=(1, speedROIHeight, speedROIWidth))

    conv1 = layers.Conv2D(filters=32, kernel_size=5, strides=1, padding='same', activation='relu')(inputLayer)
    maxPooling1 = layers.MaxPooling2D(pool_size=(4, 4), padding="same")(conv1)

    # conv2 = layers.Conv2D(filters=64, kernel_size=10, strides=1, padding='same', activation='relu')(maxPooling1)
    # maxPooling2 = layers.MaxPooling2D(pool_size=(4, 4), padding="same")(conv2)

    flatten = layers.Flatten()(maxPooling1)
    dense = layers.Dense(units=256, activation='relu', use_bias=True)(flatten)
    output = layers.Dense(units=10, input_shape=(128, ), activation="softmax", use_bias=True, name="output")(dense)
    model = Model(inputLayer, output)
    opt = optimizers.Adam(lr=0.001)

    model.compile(opt, loss="categorical_crossentropy", metrics=["accuracy"])
    return model

def trainSpeedDetectionModel(X, Y, model):
    model.fit(X, Y, epochs=20)
    return model


if __name__ == '__main__':
    cutTwoDigitsSpeedImg()

