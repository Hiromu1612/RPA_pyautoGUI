import tkinter as tk
class Application(tk.Frame):
    def __init__(self,master=None):
        #親クラスの初期化メソッドを呼び出す
        super().__init__(master)
        master.title("テキストボックスの取得")
        master.geometry("450x350+350+250")
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.lb=tk.Label(text="ラベル")
        self.lb.pack(side="top")

        self.en=tk.Entry(self)
        self.en.pack()
        self.en.focus_set()

        self.bt=tk.Button(text="ボタン",command=self.action_btn_press)
        self.bt.pack(side="bottom")

    def action_btn_press(self):
        val_en=self.en.get()
        print(val_en)

root=tk.Tk()
app=Application(master=root)
app.mainloop()