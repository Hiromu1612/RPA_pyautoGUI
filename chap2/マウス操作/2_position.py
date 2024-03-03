import pyautogui as ag
import time
for i in range(10):
    current_position=ag.position()
    print(current_position)
    time.sleep(1)