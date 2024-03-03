import pyautogui as ag

ag.mouseDown()#左クリック
ag.mouseUp()

ag.mouseDown(button='right')#右クリック
ag.mouseUp(button='right')

ag.mouseDown()#現在のマウス位置から座標へドラッグ
ag.mouseUp(x=1000,y=1000)