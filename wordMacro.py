import pyautogui
import time

msg1 = input("wassup bro? ")
times = int(input("how many times you want? "))
realTime = 0
def click():
    print("clicking to discord...")
    time.sleep(1)
    pyautogui.click(81,1052)
    time.sleep(0.5)
    pyautogui.click(200,344)
    time.sleep(0.5)
    pyautogui.typewrite("discord")
    time.sleep(0.5)
    pyautogui.click(506,648)
    time.sleep(3)
    pyautogui.click(499,989)
    time.sleep(1)
    print("Process Success")



def spam():
    print("Spaming the message...")
    pyautogui.typewrite(msg1)
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(0.2)
    print("Process Success")

click()
while realTime < times:
    spam()
    realTime += 1
    realTimeStr = str(realTime)
    print("times: " + realTimeStr)