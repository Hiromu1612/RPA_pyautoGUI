import pyautogui as ag

image=ag.screenshot(region=(0,0,300,300)) #x,y,w,h pixel
image.save("2章/スクショ, 画像マッチ/test.png")