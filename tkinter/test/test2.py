import tkinter as tk

def action_btn_press():
    print("ボタンが押されました")

root=tk.Tk()
root.title("アクションの組み込み")
root.geometry("450x350+350+250")
lb=tk.Label(text="ラベル",font=("MS ゴシック",24),foreground="blue",background="yellow",relief="ridge",borderwidth=20)

#commandオプションに関数名を指定する
bt=tk.Button(text="ボタン",command=action_btn_press)
lb.pack()
bt.pack()

root.mainloop()

#PySimpleGUIで書くと以下のようになります。
import PySimpleGUI as sg

def execute():
    print("ボタンが押されました")

layout=[[sg.Text("ラベル",font=("MS ゴシック",24),text_color="blue",background_color="yellow",relief="ridge",pad=(20,20))],
        [sg.Button("ボタン",key="btn")]]
window=sg.Window("アクションの組み込み",layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="btn":
        execute()

window.close()