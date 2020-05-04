import cv2

def detect(img):
    cannyImg = cv2.Canny(img, 100, 200)
    return cannyImg