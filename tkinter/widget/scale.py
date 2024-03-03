import tkinter as tk
import tkinter.ttk as ttk

def upd_scale(event=None):
    message["text"]=var_scale.get()
root=tk.Tk()
root.geometry("450x350+350+250")
root.title("scale")
var_scale=tk.DoubleVar()
message=tk.Label(text="スケールの値")
scale=ttk.Scale(root,from_=-10,to=10,variable=var_scale,command=upd_scale)
var_scale.set(0.0)
scale.pack()
message.pack()
root.mainloop()