import pyautogui as ag
import time
for i in range(10):
    number=i+1
    message=str(number)+"番目の場所にマウスカーソルを合わせてください" #str(number)は数値を文字列に変換する
    ag.alert(text=message)
    time.sleep(2)
    result=str(number)+"番目の座標:"+str(ag.position())
    print(result)