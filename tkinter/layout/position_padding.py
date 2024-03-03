import tkinter as tk
root=tk.Tk()
#位置指定
label_position1=tk.Label(root,text="top")
label_position2=tk.Label(root,text="bottom")
label_position3=tk.Label(root,text="left")
label_position4=tk.Label(root,text="right")
label_position1.pack(side="top")
label_position2.pack(side="bottom")
label_position3.pack(side="left")
label_position4.pack(side="right")

#余白指定
label_padding=tk.Label(root,text="padx=10,pady=20,ipadx=30,ipady=40",background="red")
label_padding.pack(padx=10,pady=20,ipadx=30,ipady=40)


root.geometry("450x350+350+250")
root.mainloop()