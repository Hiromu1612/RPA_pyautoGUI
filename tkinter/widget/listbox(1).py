import tkinter as tk
root=tk.Tk()
root.geometry("450x350+350+250")
root.title("listbox")
listbox=tk.Listbox(root,height=5)
for i in ["Python","Ruby","Perl","PHP"]:
    listbox.insert(tk.END,i)
listbox.pack()
root.mainloop()