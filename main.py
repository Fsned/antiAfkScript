import pyautogui
from time import sleep
import random
from datetime import datetime

def pressKeyRandomTime(key):
    #print("Pressing: " + str(key))
    pyautogui.keyDown(key)
    randomTime = random.choice(range(100, 700))
    #print ("keyUpDownInterval: " + str(randomTime) + " msecs.")
    sleep(randomTime / 1000.0)
    pyautogui.keyUp(key)




### Main

for a in range(4):
    print("Beginning in: " + str(4-a))
    sleep(1)



while(True):
    random.seed()
    
    list = []

    for a in range(random.choice(range(1, 4))):
        list.append(random.choice(["up", "down"]))

    for a in list:
        pressKeyRandomTime(a)

    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    sleepTime = random.choice(range(300, 800))

    print(str(currentTime) + ": " + str(list) + ". Sleeping for: " + str(sleepTime))
    sleep(sleepTime)
