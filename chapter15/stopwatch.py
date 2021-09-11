#! /usr/bin/env python3
# stopwatch.py -- A simple stopwatch program.


import time


# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. '
      'Press CTRL+c to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #{0}: {1} ({2})'.format
              (str(lapNum).rjust(2), str(totalTime).rjust(5), str(lapTime).rjust(6), end=''))
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')
