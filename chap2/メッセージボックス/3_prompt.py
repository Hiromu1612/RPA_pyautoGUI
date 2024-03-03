import pyautogui as ag

result=ag.prompt(text="テキストメッセージ",title="prompt関数",default="デフォルト値")
print(result)



#PySimpleGUIの場合
import PySimpleGUI as sg

layout = [
    [sg.Text('テキストメッセージ',justification="center")],
    [sg.InputText(default_text="デフォルト値")],
    [sg.Button('OK'), sg.Button('Cancel')]
]

window = sg.Window('prompt関数', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print(values[0])

window.close()