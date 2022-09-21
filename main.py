import pyautogui
from time import sleep
import random
from datetime import datetime

def pressKeyRandomTime(key):
    #print("Pressing: " + str(key))
    pyautogui.keyDown(key)
    randomTime = random.choice(range(350, 1500))
    #print ("keyUpDownInterval: " + str(randomTime) + " msecs.")
    sleep(randomTime / 1000.0)
    pyautogui.keyUp(key)


def mouseDrag():
    pyautogui.dragTo(random.randint(0, 1080), random.randint(0, 900), button='left', duration=1)



### Main
for a in range(4):
    print("Beginning in: " + str(4-a))
    sleep(1)



while(True):
    random.seed()
    
    list = []

    for a in range(random.choice(range(1, 4))):
        list.append(random.choice(["up", "down", "drag"]))

    for key in list:
        if key == "up" or key == "down":
            pressKeyRandomTime(key)
        else:
            mouseDrag()

    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    sleepTime = random.choice(range(244, 415))

    print(str(currentTime) + ": " + str(list) + ". Sleeping for: " + str(sleepTime))
    sleep(sleepTime)
