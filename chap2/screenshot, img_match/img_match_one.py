import pyautogui as ag

#フォルダは日本語禁止 パスを指定 一致度は低めに設定
car_position=ag.locateOnScreen("chap2/screenshot, img_match/car_button.png",confidence=0.3,grayscale=True)
walking_position=ag.locateOnScreen("chap2/screenshot, img_match/walking_button.PNG",confidence=0.3,grayscale=True)
print(car_position)
print(walking_position)