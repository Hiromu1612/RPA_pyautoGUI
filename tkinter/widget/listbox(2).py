import tkinter as tk
#選択中のリストボックスの項目
def get_listitem():
    print(listbox.curselection())
root=tk.Tk()
root.geometry("450x350+350+250")
root.title("get listitem")
strvar=tk.StringVar()
strvar.set(["Python","Ruby","Perl","PHP","Java","C#", "C++","C","Go","Kotlin"])
listbox=tk.Listbox(root,listvariable=strvar,height=5,selectmode="multiple")
bt=tk.Button(text="選択中の項目",command=get_listitem)

#アイテム自体の削除
def del_listitem():
    for i in listbox.curselection():
        listbox.delete(i)
bt2=tk.Button(text="選択中の項目を削除",command=del_listitem)

#スクロールバーの追加 右に配置 縦にいっぱいに広げる
frame=tk.Frame(width=200,height=100)
scrollbar=tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill="y")

#部品の動きを連動させる
listbox["yscrollcommand"]=scrollbar.set
#スクロールバーの動きを連動させる
scrollbar["command"]=listbox.yview

listbox.pack()
bt.pack()
bt2.pack()
root.mainloop()