#! /usr/bin/env python3
# Porgram to reocord are users clock in or out

import time
import os

# {'username': {'clock_in':[], 'clock_out':[] }}
timeSheet = {}

msg = "When prompted enter user's Name, Clock event[in/out], press CTRL+c to exit"


try:
    while True:
        print(len(msg) * "=")
        print(msg)
        print(len(msg) * "=")
        username = input("Username: ")
        action = input("Clock [in/out]: ")
        if action == "in" and username not in timeSheet:
            timeSheet[username] = {'in':[], 'out':[]}
            timeSheet[username][action].append(time.ctime())
        elif action == "in" and\
                (len(timeSheet[username][action]) == len(timeSheet[username]['out'])):
            timeSheet[username][action].append(time.ctime())
        elif action == "in" and \
                 (len(timeSheet[username][action]) > len(timeSheet[username]['out'])):
            print("User has not Clocked out")
            print("Last Clock in at {}".format(str(timeSheet[username][action][-1])))
        elif action == "out" and username not in timeSheet:
            print("User not Clocked in")
        elif action == "out" and \
                 (len(timeSheet[username]['in']) > len(timeSheet[username][action])):
            timeSheet[username][action].append(time.ctime())
        elif action == "out" and \
                 (len(timeSheet[username]['in']) == len(timeSheet[username][action])):
            print("User has not Clocked In\n")
            print("Last Clock out at {}".format(str(timeSheet[username][action][-1])))
        else:
            pass

        print('\n', "User: {0}, Clock {1}  time  {2}".format(username, action,
                                                             str(timeSheet[username][action][-1])))
        another_update = input ('\nupdate another user? [y/n]')
        if another_update.lower() != "y":
            raise KeyboardInterrupt

except KeyboardInterrupt:
    print('\n\n   !!! Good Bye !!!')