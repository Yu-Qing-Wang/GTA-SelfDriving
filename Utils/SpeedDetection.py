from time import time
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

def formTrainingData():
    pass


if __name__ == '__main__':
    cutTwoDigitsSpeedImg()

