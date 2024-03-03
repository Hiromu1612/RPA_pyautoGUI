import tkinter as tk
from tkinter import filedialog

def get_filepath():
    #.txt,.py,全てのファイルの場合
    filetype_list=[("テキストファイル","*.txt"),("Pythonファイル","*.py"),("全てのファイル","*.*")]
    #ファイルパスの取得
    filepath=filedialog.askopenfilename(filetypes=filetype_list,title="select file")
    message["text"]=filepath

root=tk.Tk()
root.geometry("450x350+350+250")
root.title("filedialog")
message=tk.Label(text="ファイルパス")
bt=tk.Button(text="ファイルを開く",command=get_filepath)
message.pack()
bt.pack()
root.mainloop()

#PySimpleGUIで書くと以下のようになります。
import PySimpleGUI as sg

layout=[[sg.Text("ファイルパス")],
        [sg.Button("ファイルを開く",key="-BTN-")]]
window=sg.Window("filedialog",layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="-BTN-":
        filepath=sg.popup_get_file("ファイルを選択してください",file_types=(("テキストファイル","*.txt"),("Pythonファイル","*.py"),("全てのファイル","*.*")))
        window["-BTN-"].update(filepath)

window.close()