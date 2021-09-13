from tkinter import *

root = Tk()
root.title("uRemote")
root.geometry('700x400')
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

btn = Button(root, text="Execute")
btn.place(x=600, y=350)
btn2 = Button(root, text="RESET")
btn2.place(x=525, y=350)

root.mainloop()
