import pyautogui as ag
import time

time.sleep(2)

ag.keyDown("ctrl")
ag.press("c")
ag.keyUp("ctrl")

time.sleep(2)

ag.keyDown("ctrl")
ag.press("v")
ag.keyUp("ctrl")