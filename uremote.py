from tkinter import *

root = Tk()
root.title("uRemote")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

root.geometry('700x400')
btn = Button(root, text="Execute")

btn.grid(column=30, row=100)

root.mainloop()
