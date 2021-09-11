#! /usr/bin/env python3

import threading
import time


def takeANap(*args, **kwargs):
    time.sleep(5)
    print(*args, sep=kwargs['sep'])


print("Start of Program \n")
threadObj = threading.Thread(target=takeANap, args=['Cats', 'Dogs', "Frogs"], kwargs={'sep': ' & '})
threadObj.start()

print('End of Program')