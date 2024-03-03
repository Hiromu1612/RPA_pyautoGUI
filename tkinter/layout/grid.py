import tkinter as tk
root=tk.Tk()
root.geometry("450x350+350+250")

#grid(格子状)で配置 row=行 column=列
label1=tk.Label(root,text="row=0,column=0",relief="groove")
label1.grid(row=0,column=0)
label2=tk.Label(root,text="row=0,column=1",relief="groove")
label2.grid(row=0,column=1)
label3=tk.Label(root,text="row=1,column=0",relief="groove")
label3.grid(row=1,column=0)
label4=tk.Label(root,text="row=1,column=1",relief="groove")
label4.grid(row=1,column=1)

root.mainloop()

#PySimpleGUIで書くと以下のようになります。
import PySimpleGUI as sg
#padding=余白
layout=[[sg.Text("row=0,column=0",relief="groove"),sg.Text("row=0,column=1",relief="groove")],
        [sg.Text("row=1,column=0",relief="groove"),sg.Text("row=1,column=1",relief="groove")]]
window=sg.Window("grid(格子状)で配置",layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break

window.close()