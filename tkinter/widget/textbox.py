import tkinter as tk

def print_txtval():
    #テキストボックスの値を取得 .get()で取得
    val_en=en.get()
    print(val_en)

root=tk.Tk()
root.title("テキストボックス")
root.geometry("450x350+350+250")
lb=tk.Label(text="ラベル")
#テキストボックスの作成
en=tk.Entry()
bt=tk.Button(text="ボタン",command=print_txtval)

#配置
lb.pack()
bt.pack()
en.pack()

root.mainloop()