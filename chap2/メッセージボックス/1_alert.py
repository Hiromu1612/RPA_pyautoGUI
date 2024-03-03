import pyautogui as ag

result=ag.alert(text="テキストメッセージ",title="alert関数",button="OK")
print(result)

import PySimpleGUI as sg

result=sg.popup("テキストメッセージ",title="alert関数")
print(result)