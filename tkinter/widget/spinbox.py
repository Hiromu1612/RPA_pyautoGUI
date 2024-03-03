import tkinter as tk

#スピンボックスの値を取得
def upd_spinbox(event=None):
    lavel["text"]=var_spinbox.get()
root=tk.Tk()
root.geometry("450x350+350+250")
root.title("spinbox")
var_spinbox=tk.StringVar()
lavel=tk.Label(text="スピンボックスの値")

#スピンボックスの作成 -10から10まで 0.5ずつ
spinbox=tk.Spinbox(root,from_=-10,to=10,increment=0.5,textvariable=var_spinbox,command=upd_spinbox)
var_spinbox.set(0.0)
spinbox.bind("<Return>",upd_spinbox)
lavel.pack()
spinbox.pack()
root.mainloop()