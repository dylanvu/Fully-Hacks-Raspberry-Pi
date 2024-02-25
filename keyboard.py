# this script's used to remote control the rover using keypresses
from drivers.Motor import *


def keyboardLoop():
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
        else:
            Stop()


if __name__ == '__main__':
    keyboardLoop()