import pyautogui as ag
import time
import pyperclip as pc

time.sleep(3)

#日本語をクリップボードにコピーしてからペースト
pc.copy("こんにちは、みなさん") #pyperclip.copy()関数でクリップボードに文字列をコピー
ag.hotkey("ctrl","v")