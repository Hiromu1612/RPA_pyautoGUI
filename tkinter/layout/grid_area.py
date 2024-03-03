import tkinter as tk
root=tk.Tk()
root.geometry("450x350+350+250")
frame1=tk.Frame(root,relief="groove",background="lightblue")
frame2=tk.Frame(root,relief="groove",background="lightgreen")

#ラベルの範囲
label1_area=tk.Label(frame1,text="r0,c0,rs2",relief="groove")
label1_area.grid(row=0,column=0,rowspan=1)
label1=tk.Label(frame1,text="r0,c1",relief="groove")
label1.grid(row=0,column=1)

label2_area=tk.Label(frame2,text="r0,c0,cs2",relief="groove")
label2_area.grid(row=0,column=0,columnspan=2)
label2=tk.Label(frame2,text="r0,c2",relief="groove")
label2.grid(row=0,column=2)

frame1.pack(fill="both",expand=True,padx=10,pady=10)
frame2.pack(fill="both",expand=True,padx=10,pady=10)

root.mainloop()