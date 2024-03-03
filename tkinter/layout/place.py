import tkinter as tk
root=tk.Tk()
root.geometry("450x350+350+250")

frame1=tk.Frame(root,relief="groove",width=200,height=100,background="lightblue")
label1=tk.Label(frame1,text="frame1 600x300",relief="groove",background="lightgreen")

frame1.pack()
#xは絶対的なx座標 relxは相対的なx座標 1が100%
label1.place(relx=0.1,rely=0.6)

root.mainloop()