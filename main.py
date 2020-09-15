from detect_ball import BallDetector
#from motor import Rover
from dummy import Rover
import time

move = Rover()
sense = BallDetector()

N = 3 # Number of Retrys
TIME_LIMIT = 10 #seconds

t = 0

detected = False
forward = False
right = False
restr = False

def right_or_left():
    if right:
        move.control("right")
    else:
        move.control("left")


try:
    while True:
        for i in range(N):
            detected, forward, right, rest = sense.getValue()
            if detected:
                break

        if forward:
            move.control("forward")
            if not detected:
                if (t == 0):
                    t = time.time()
                elif (time.time() - t) > TIME_LIMIT:
                    t = 0
                    right_or_left()
            
        else:
            t = 0
            if rest:
                move.control('stop')
            else:
                right_or_left()
        
except KeyboardInterrupt:
    move.close()
    sense.close()
