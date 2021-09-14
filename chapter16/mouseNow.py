#! /usr/bin/env python3
# mouseNow.py - Displays the mouse cursor's current position.
import time

import pyautogui

print('Press CTRL+c to quit.')
try:
    while True:
        x, y = pyautogui.position()
        position = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position, end='')
        time.sleep(.5)
        print('\b' * len(position), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
