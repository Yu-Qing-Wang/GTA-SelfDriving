from Utils import Frame, KeyRecord, SpeedDetection
from pynput.keyboard import Listener


if __name__ == "__main__":
    # # train speed detection model
    # X, Y = SpeedDetection.formTrainingData()
    # model = SpeedDetection.defineSpeedDetectionModel()
    # model = SpeedDetection.trainSpeedDetectionModel(X, Y, model)
    # model.save("models/speed_detector.h5")
    
    Frame.captureFrames()
