import tkinter as tk
def update_state(event):
    bt["state"]=tk.DISABLED if boolvar.get() else tk.NORMAL

root=tk.Tk()
root.geometry("450x350+350+250")
boolvar=tk.BooleanVar()
checkbt=tk.Checkbutton(root,text="はい、同意します",variable=boolvar)

#stateオプションでボタンの状態を変更できる tk.NORMAL:通常 tk.DISABLED:無効化
bt=tk.Button(text="次へ",state=tk.DISABLED)
checkbt.pack()
bt.pack()
#チェックボックスの状態が変わったときにupdate_stateを呼び出す bindでイベントを設定
checkbt.bind("<Button-1>",update_state)
root.mainloop()

#PySimpleGUIで書くと以下のようになります。
import PySimpleGUI as sg
def update_state():
    window["-BT-"].update(disabled=values["-CK-"]) #disabledオプションでボタンの状態を変更できる

layout=[[sg.Checkbox("はい、同意します",key="-CK-")],
        [sg.Button("次へ",key="-BT-")]]
window=sg.Window("チェックボックス",layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="-CK-":
        update_state()

window.close()