# this script's used to remote control the rover using keypresses
from Motor import *
from Servo import Servo


def keyboardLoop():
    # create the servo controller class
    servo = Servo()
    while True:
        key = input("Control the rover: ")
        key = key.lower()
        if key == "w":
            Forward()
            print("UP")
        elif key == "s":
            print("DOWN")
            Back()
        elif key == "a":
            print("LEFT")
            Left()
        elif key == "d":
            Right()
            print("RIGHT")
        # elif key == "q":
            
        # elif key == "e":

        else:
            Stop()


if __name__ == '__main__':
    keyboardLoop()