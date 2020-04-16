import cv2
from PIL import Image
import conf
from mss import mss
import numpy as np
import Utils.KeyRecord as KeyRecord


def captureFrames():
    sct = mss()
    while True:
        action = KeyRecord.catchRegisteredKeys()

        sct.get_pixels(conf.ROI)
        img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
        cv2.imshow('GTA Self Driving', np.array(img))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
