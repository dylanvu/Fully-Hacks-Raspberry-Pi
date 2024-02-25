# this script is used to remote control the rover using keypresses
import keyboard
from drivers.Motor import MotorController

controller = MotorController()

def keyboardLoop():
    while True:
        if keyboard.is_pressed('up'):
            controller.Forward()
            print("UP key pressed")
        if keyboard.is_pressed('down'):
            print("DOWN key pressed")
            controller.Back()
        if keyboard.is_pressed('left'):
            print("LEFT key pressed")
            controller.Left()
        if keyboard.is_pressed('right'):
            controller.Right()
            print("RIGHT key pressed")


if __name__ == '__main__':
    keyboardLoop()