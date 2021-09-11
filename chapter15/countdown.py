#! /usr/bin/env python3
# countdown.py : simple count down program


import time
import subprocess


time_left = 10
while time_left > 0:
    print(time_left, end=' ')
    time.sleep(1)
    time_left -= 1

subprocess.Popen(['open', 'alarm.wav'])
