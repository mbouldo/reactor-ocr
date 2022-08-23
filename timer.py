import threading
import keyboard  # using module keyboard
import sys
import os

enabled = True



def printit():
    threading.Timer(5.0, printit).start()
    print("Hello, World!")
    os._exit()

def secondKeyboard():
    while True:
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('a'):  # if key 'q' is pressed 
                print(enabled)
                enabled = False
                break
        except:
            sys.exit()
            break  # if user pressed a key otheqqqqr than the given key the loop will break        




while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            printit()
            secondKeyboard()
            break
    except:
        sys.exit()
        break  # if user pressed a key otheqqqqr than the given key the loop will break

