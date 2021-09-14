#! /usr/bin/env python3
# spiralDraw.py: user pyautogui to draw a spiral in macOS paintbrush

import pyautogui
import time


time.sleep(5)
pyautogui.click(210, 210)
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2, button='left')
    distance = distance -5
    pyautogui.dragRel(0, distance, duration=0.2,  button='left')
    pyautogui.dragRel(-distance, 0, duration=0.2, button='left')
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2,  button='left')