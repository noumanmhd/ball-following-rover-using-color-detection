import numpy as np
import cv2
import csv
import imutils
import time
from detector import MaskDetector

MIN_DISTANCE = 0  # cm
# at
MAX_RADIUS = 500

MAX_DISTANCE = 100
# at
MIN_RADIUS = 20

# Map funtion


def map_values(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class BallDetector(object):
    def __init__(self, filename='config.csv', video=0):
        self.mask = None
        self.detected = False
        self.right = True
        self.forward = False
        self.rest = False
        self.frame = np.zeros([600, 600, 3], dtype=np.uint8).fill(255)
        self.distance = 0
        self.vs = cv2.VideoCapture(video)
        self.mask_detector = MaskDetector(filename)

    def getFrame(self):
        _, img = self.vs.read()
        self.frame = img
        self.frame = imutils.resize(self.frame, width=600)
        self.view = self.frame.copy()
        return self.frame

    def detectBall(self):
        self.mask = self.mask_detector.getMask(self.getFrame())
        cnts = cv2.findContours(self.mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        radius = 0
        self.rest = False
        self.detected = False
        if len(cnts) > 0:
            self.detected = True
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            cv2.circle(self.view, (int(x), int(y)), int(radius),
                       (0, 255, 255), 2)

            distance = 0
            if (radius > MIN_RADIUS) and (radius < MAX_RADIUS):
                # Values range
                distance = map_values(radius, MIN_RADIUS,
                                      MAX_RADIUS, MIN_DISTANCE, MAX_DISTANCE)
                distance = abs(distance - 100)
                print(distance)

                self.rest = True
                self.forward = False

                if distance > 20:
                    self.rest = False
                    if (x >= 0) and (x < 100):
                        self.right = False
                    elif (x >= 100) and (x < 500):
                        self.forward = True
                    else:
                        self.right = True

    def getValue(self):
        self.detectBall()
        cv2.imshow("Frame", self.view)
        cv2.waitKey(1)
        return self.detected, self.forward, self.right, self.rest

    def close(self):
        self.vs.release()
