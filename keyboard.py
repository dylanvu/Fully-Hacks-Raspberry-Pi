# this script is used to remote control the rover using keypresses
from drivers.Motor import *


def keyboardLoop():
    while True:
        key = input("Control the rover: ")
        key = key.lower()
        if key is "w":
            Forward()
            print("UP")
        if key is "s":
            print("DOWN")
            Back()
        if key is "a":
            print("LEFT")
            Left()
        if key is "d":
            Right()
            print("RIGHT")


if __name__ == '__main__':
    keyboardLoop()