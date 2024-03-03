import tkinter as tk
def file_open():
    label["text"]="ファイルを開く"
def file_save():
    label["text"]="ファイルを保存"
def file_copy():
    label["text"]="コピー"
def file_paste():
    label["text"]="ペースト"
root=tk.Tk()
root.geometry("450x350+350+250")
root.title("メニュー")

#メニューバーの作成
menubar=tk.Menu(root)
#メニューを作成
menu1=tk.Menu(menubar,tearoff=0)
menu2=tk.Menu(menubar,tearoff=0)
#メニューにアイテムを追加
menu1.add_command(label="開く",command=file_open)
menu2.add_command(label="コピー",command=file_copy)
#セパレーターを追加
menu1.add_separator()
menu2.add_separator()
menu1.add_command(label="保存",command=file_save)
menu2.add_command(label="ペースト",command=file_paste)
#メニューをカスケード
menubar.add_cascade(label="ファイル",menu=menu1)
menubar.add_cascade(label="編集",menu=menu2)
#メニューバーを配置
root["menu"]=menubar
lavel=tk.Label(root)
lavel.pack()
root.mainloop()