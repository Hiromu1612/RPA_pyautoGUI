import tkinter as tk
root=tk.Tk()
root.geometry("450x350+350+250")
root.title("ラベルフレーム")

#ラベルフレームの作成
frame=tk.LabelFrame(text="ラベルフレーム",foreground="blue")
intvar=tk.IntVar()
intvar.set(0)
radio1=tk.Radiobutton(frame,text="ラジオ1",variable=intvar,value=1)
radio2=tk.Radiobutton(frame,text="ラジオ2",variable=intvar,value=2)
radio3=tk.Radiobutton(frame,text="ラジオ3",variable=intvar,value=3)
radio1.pack()
radio2.pack()
radio3.pack()
frame.pack()
root.mainloop()

#PySimpleGUIで書くと以下のようになります。
import PySimpleGUI as sg

layout=[[sg.Frame("ラベルフレーム",
        [[sg.Radio("ラジオ1",group_id=1)], 
        [sg.Radio("ラジオ2",group_id=1)], 
        [sg.Radio("ラジオ3",group_id=1)]])]]
window=sg.Window("ラベルフレーム",layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break

window.close()