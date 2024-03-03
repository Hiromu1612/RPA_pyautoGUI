import pyautogui as ag
import time

car_position=ag.locateAllOnScreen("chap2/screenshot, img_match/car_button.png",confidence=0.4,grayscale=True)

for position in car_position:
    print(position)
    time.sleep(1)