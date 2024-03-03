import tkinter as tk
#root(Main Window)を作成
root=tk.Tk()
root.title("位置指定")
#Windowの位置指定(幅x高さ+X座標+Y座標)
root.geometry("450x350+350+250")

#部品(Widjet)の作成
lb=tk.Label(text="ラベル")
bt=tk.Button(text="ボタン")
#配置
lb.pack()
bt.pack()

#main処理の実行
root.mainloop()