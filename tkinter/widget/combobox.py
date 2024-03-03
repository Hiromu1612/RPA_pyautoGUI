import tkinter as tk
import tkinter.ttk as ttk

#コンボボックスの値を取得
def get_comboitem():
    print(combobox.get())
root=tk.Tk()
root.geometry("450x350+350+250")
root.title("combobox")
combobox=ttk.Combobox(root,values=["Python","Ruby","Perl","PHP"])
bt=tk.Button(text="出力",command=get_comboitem)
combobox.pack()
bt.pack()
root.mainloop()

#PySimpleGUIで書くと以下のようになります。
import PySimpleGUI as sg

layout=[[sg.Combo(["Python","Ruby","Perl","PHP"],key="-COMBO-"),sg.Button("出力",key="-BTN-")]]
window=sg.Window("combobox",layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSE:
        break
    if event=="-BTN-":
        print(values["-COMBO-"])

window.close()