# this script is used to remote control the rover using keypresses
import keyboard
from drivers.Motor import *


def keyboardLoop():
    while True:
        if keyboard.is_pressed('up'):
            Forward()
            print("UP key pressed")
        if keyboard.is_pressed('down'):
            print("DOWN key pressed")
            Back()
        if keyboard.is_pressed('left'):
            print("LEFT key pressed")
            Left()
        if keyboard.is_pressed('right'):
            Right()
            print("RIGHT key pressed")


if __name__ == '__main__':
    keyboardLoop()