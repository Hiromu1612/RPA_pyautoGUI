import tkinter as tk
def get_ckval():
    #チェックされているかの判定
    lb["text"]="チェックされている" if boolvar.get() else "チェックされていない"

root=tk.Tk()
root.geometry("450x350+350+250")
boolvar=tk.BooleanVar()
lb=tk.Label()
ck=tk.Checkbutton(text="チェックボックス",variable=boolvar)
bt=tk.Button(text="判定",command=get_ckval)
lb.pack()
ck.pack()
bt.pack()

root.mainloop()

#PySimpleGUIで書くと以下のようになります。
import PySimpleGUI as sg
def get_ckval():
    #チェックされているかの判定
    window["-LB-"].update("チェックされている" if values["-CK-"] else "チェックされていない")

layout=[[sg.Text(size=(20,1),key="-LB-")],
        [sg.Checkbox("チェックボックス",key="-CK-"),sg.Button("判定",key="-BTN-")]]
window=sg.Window("チェックボックス",layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="-BTN-":
        get_ckval()

window.close()