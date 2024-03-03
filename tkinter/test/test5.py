import tkinter as tk
def return_press(event):
    en_val=strvar.get()
    print(en_val)
    #テキストボックスの値を削除(更新)
    strvar.set("")

root=tk.Tk()
strvar=tk.StringVar()
tx=tk.Text()
#Returnキーが押されたときにイベントを発生させる
tx.bind("<Return>",return_press)
tx.pack()
root.mainloop()