import pyautogui as ag
import time

time.sleep(5)
ag.write("Hello, World!")
ag.write("Hello, World!",interval=0.5) #intervalは文字と文字の入力の間の時間
ag.write("日本語入力はできません",interval=0.5) #日本語入力するにはPyperclipモジュールを使う