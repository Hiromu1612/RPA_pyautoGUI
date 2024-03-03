import tkinter as tk
root=tk.Tk()
root.geometry("450x350+350+250")
label=tk.Label(root,text='fill=y,expand=True,padx=10,pady=20',relief="groove")
#fill yで縦拡大 expandで横拡大のレスポンシブ reliefで枠線を設定
label.pack(fill="y",expand=True,padx=10,pady=20)
root.mainloop()