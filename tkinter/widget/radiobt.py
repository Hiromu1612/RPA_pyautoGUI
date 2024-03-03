import tkinter as tk
root=tk.Tk()

#選択値を取得する
def get_rdval():
    print(intvar.get())

root.geometry("450x350+350+250")
root.title("ラジオボタン")
intvar=tk.IntVar()

#初期値をセット
intvar.set(0)
#ラジオボタンの作成
rb1=tk.Radiobutton(text="ラジオ1",variable=intvar,value=1)
rb2=tk.Radiobutton(text="ラジオ2",variable=intvar,value=2)
bt=tk.Button(text="判定",command=get_rdval)
rb1.pack()
rb2.pack()
bt.pack()

#値ではなく文字列にすることもできる
strvar=tk.StringVar()
strvar.set("0")
rd_abc=tk.Radiobutton(text="ABC",variable=strvar,value="ABC")
rd_def=tk.Radiobutton(text="DEF",variable=strvar,value="DEF")
bt2=tk.Button(text="判定2",command=lambda:print(strvar.get()))
rd_abc.pack()
rd_def.pack()
bt2.pack()

root.mainloop()