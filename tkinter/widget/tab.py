import tkinter as tk
import tkinter.ttk as ttk

def press_btn1():
    label1["text"]="ボタン1が押されました"
def press_btn2():
    label2["text"]="ボタン2が押されました"

root=tk.Tk()
root.geometry("450x350+350+250")
root.title("ノートブック")
notebook=ttk.Notebook(root)
tab1=tk.Frame(notebook)
tab2=tk.Frame(notebook)
notebook.add(tab1,text="タブ1")
notebook.add(tab2,text="タブ2")

#タブのレスポンシブ対応
notebook.pack(expand=True,fill="both")

#タブ1のウィジェット
label1=tk.Label(tab1,text="ラベル1")
bt1=tk.Button(tab1,text="ボタン1",command=press_btn1)
label1.pack()
bt1.pack()
#タブ2のウィジェット
label2=tk.Label(tab2,text="ラベル2")
bt2=tk.Button(tab2,text="ボタン2",command=press_btn2)
label2.pack()
bt2.pack()

root.mainloop()