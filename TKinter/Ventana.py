from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root,padding=30)
frm.grid()
ttk.Label(frm, text="Lidio pagate la coca").grid(column=1, row=0)
ttk.Button(frm, text="OK, cuando vaya a Cordoba", command=root.destroy).grid(column=0,row=1)
ttk.Button(frm, text="Sacar a Leo del grupo", command=root.destroy).grid(column=2,row=1)
root.mainloop()