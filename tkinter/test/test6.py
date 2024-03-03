import tkinter as tk
import tkinter.scrolledtext as tksc
root=tk.Tk()

#縦スクロールバー付きのテキストボックス
st=tksc.ScrolledText(width=40,height=10)
st.pack()
root.mainloop()

#PySimpleGUIで書くと以下のようになります。
import PySimpleGUI as sg

layout=[[sg.Multiline(size=(40,10),key="-ST-")]]
window=sg.Window("スクロールテキスト",layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break

window.close()