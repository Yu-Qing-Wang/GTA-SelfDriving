from Utils import Frame, KeyRecord, SpeedDetection
from pynput.keyboard import Listener


if __name__ == "__main__":
    # SpeedDetection.cutTwoDigitsSpeedImg()

    # samples = SpeedDetection.formTrainingData()
    # model = SpeedDetection.defineSpeedDetectionModel()
    # model = SpeedDetection.trainSpeedDetectionModel(samples, model)

    Frame.captureFrames()
