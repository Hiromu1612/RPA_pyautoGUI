import tkinter as tk
def enter_label(event):
    event.widget["background"]="#bfb"
def leave_label(event):
    event.widget["background"]="#bbf"

root=tk.Tk()
root.geometry("450x350+350+250")

label=tk.Label(root,text="mouse here",background="#bbf")
#<Enter><Leave>でマウスが乗った時と外れた時のイベントを設定
label.bind("<Enter>",enter_label)
label.bind("<Leave>",leave_label)
label.pack(ipadx=100,ipady=20)

root.mainloop()

#PySimpleGUIで書くと以下のようになります。
import PySimpleGUI as sg
def enter_label(event):
    window["-LB-"].update(background_color="#bfb")
def leave_label(event):
    window["-LB-"].update(background_color="#bbf")

layout=[[sg.Text("mouse here",key="-LB-",background_color="#bbf",size=(20,20))]]
window=sg.Window("マウスイベント",layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="-LB-<Enter>":
        enter_label(event)
    if event=="-LB-<Leave>":
        leave_label(event)

window.close()