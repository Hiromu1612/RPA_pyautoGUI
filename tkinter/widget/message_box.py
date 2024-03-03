import tkinter as tk
from tkinter import messagebox

def msg_info():
    #情報メッセージボックス
    label["text"]=str(messagebox.showinfo("情報","情報メッセージボックス"))
def msg_warning():
    #警告メッセージボックス
    label["text"]=str(messagebox.showwarning("警告","警告メッセージボックス"))
def msg_error():
    #エラーメッセージボックス
    label["text"]=str(messagebox.showerror("エラー","エラーメッセージボックス"))
def msg_askokcancel():
    #OKキャンセルメッセージボックス
    label["text"]=str(messagebox.askokcancel("OKキャンセル","OKキャンセルメッセージボックス"))
def msg_askyesno():
    #YesNoメッセージボックス
    label["text"]=str(messagebox.askyesno("YesNo","YesNoメッセージボックス"))
def msg_askyesnocancel():
    #YesNoキャンセルメッセージボックス
    label["text"]=str(messagebox.askyesnocancel("YesNoキャンセル","YesNoキャンセルメッセージボックス"))

root=tk.Tk()
root.geometry("450x350+350+250")
root.title("messagebox")
label=tk.Label(root)
label.pack()
#ボタンの作成
bt1=tk.Button(text="情報",command=msg_info)
bt2=tk.Button(text="警告",command=msg_warning)
bt3=tk.Button(text="エラー",command=msg_error)
bt4=tk.Button(text="OKキャンセル",command=msg_askokcancel)
bt5=tk.Button(text="YesNo",command=msg_askyesno)
bt6=tk.Button(text="YesNoキャンセル",command=msg_askyesnocancel)
bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()
bt5.pack()
bt6.pack()
root.mainloop()