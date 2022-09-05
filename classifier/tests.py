from django.test import TestCase

# Create your tests here.
import numpy as np
import morphologicalMask as morphMask
import cv2
import keyboard
cam = cv2.VideoCapture(2)
cv2.namedWindow("video", cv2.WINDOW_NORMAL)    
cv2.resizeWindow("video", 1920, 1080)
while True:

    check, frame = cam.read()
    frame = cv2.resize(frame, (256,256), interpolation = cv2.INTER_AREA)
    processImg = morphMask.morphologicalMasking(frame)
    processImg = np.concatenate((np.array(frame),np.array(processImg)),axis=2)
    processImg = morphMask.rgba2rgb(np.array(processImg))
    cv2.imshow('video', processImg)

    key = cv2.waitKey(1)
    if keyboard.is_pressed('q'):
        break

cam.release()
cv2.destroyAllWindows()

