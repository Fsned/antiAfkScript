import pyautogui
from time import sleep
import random


def pressKeyRandomTime(key):
    print("Pressing: " + str(key))
    pyautogui.keyDown(key)
    randomTime = random.choice(range(100, 700))
    print ("keyUpDownInterval: " + str(randomTime) + " msecs.")
    sleep(randomTime / 1000.0)
    pyautogui.keyUp(key)




### Main
while(True):
    random.seed()
    
    list = []

    for a in range(random.choice(range(1, 4))):
        list.append(random.choice(["up", "down"]))

    for a in list:
        pressKeyRandomTime(a)

    sleepTime = random.choice(range(332, 801))

    print ("Returning in: " + str(sleepTime) + " secs")
    sleep(sleepTime)
