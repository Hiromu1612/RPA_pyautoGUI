import pyautogui as ag

ag.click()

ag.click(clicks=2)
ag.doubleClick()

ag.click(button='right')
ag.rightClick()

ag.click(x=1000,y=1000,button='left') #x,y座標移動後に左クリック

ag.tripleClick(button="middle")
ag.click(clicks=3, button="middle")