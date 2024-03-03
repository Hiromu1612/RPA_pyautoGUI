import pyautogui as ag
import time

#符号の初期値 -1はマウスを左に移動させるため
sign = -1

time.sleep(5)

for i in range(20):
    #符号を反転させる
    sign = sign * -1

    move_amount_x=sign*(200-i*10)
    #左クリックしながら、x軸方向にドラッグ
    ag.drag(move_amount_x, None, button="left") #Noneは移動しないことを意味する
    
    move_amount_y=sign*(200-i*5)
    ag.drag(None,move_amount_y, button="left")