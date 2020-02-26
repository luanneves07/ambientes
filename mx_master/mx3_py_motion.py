#!/usr/bin/env python3

import os
import moosegesture
from time import time
from time import sleep
from pymouse import PyMouse
from pykeyboard import PyKeyboard

mouse = PyMouse()
keyBoard = PyKeyboard()

def debounce_mouse_position():
    gestures = []
    timeout = time() + (1/5)
    while time() < timeout:
        gestures.append(mouse.position())
        sleep(0.010)
    return gestures

def execute(command):
    if(moosegesture.RIGHT == command):
        os.system('i3 workspace next')
        #keyBoard.press_keys(['Control_L','Alt_L', 'Right'])
    elif(moosegesture.LEFT == command):
        os.system('i3 workspace prev')
        #keyBoard.press_keys(['Control_L','Alt_L', 'Left'])
    elif(moosegesture.UP == command):
        os.system('google-chrome')
        #keyBoard.press_keys(['Super_L'])
    elif(moosegesture.DOWN == command):
        os.system('i3 layout toggle')
        #keyBoard.press_keys(['Super_L','d'])
    else:
        os.system('notify-send "Master MX 3" "Command not defined"')

def perform_gesture():
    initial_position = mouse.position()
    timeout = time() + 1
    while (time() < timeout) and (initial_position==mouse.position()):
        sleep(0.025)

    if initial_position==mouse.position():
        os.system('gnome-terminal')
    else:
        movements = debounce_mouse_position()
        gesture = moosegesture.getGesture(movements)
        execute(gesture[0])

perform_gesture()
