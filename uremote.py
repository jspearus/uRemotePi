from tkinter import *
import serial
import time
import os
import platform


root = Tk()
root.configure(background='black')
root.title("uRemote For All")
root.geometry('640x480')


text = ""

if platform.system() == "Linux":
    port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
    root.config(cursor="none")
    root.attributes('-fullscreen', True)
elif platform.system() == "Windows":
    #port = serial.Serial("COM7", baudrate=115200, timeout=3.0)
    pass


def Execute():
    textBox.insert(END, "Execute")
    textBox.yview(END)
    Display("Execute")


def Reset():
    textBox.insert(END, "Reset")
    textBox.yview(END)
    Display("Reset      ")


def Display(x):
    myLabel = Label(root, bg="blue", text=x)
    myLabel.place(x=250, y=10)


def Clear():
    textBox.delete(0, END)
    Display("Clear      ")


# create frame and scrollbar
my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)


textBox = Listbox(my_frame, bg="blue", width=40, height=20,
                  justify="left", yscrollcommand=my_scrollbar.set)

# config scrollar
my_scrollbar.config(command=textBox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.place(x=40, y=60)
textBox.pack()


osLabel = Label(root, bg="blue", text="OS Detected: " + platform.system())
osLabel.place(x=40, y=20)

btn = Button(root, text="Execute", bg="red", command=Execute)
btn.place(x=350, y=400)


btn2 = Button(root, text="RESET", bg="blue", command=Reset)
btn2.place(x=175, y=400)

btn4 = Button(root, text="clear", bg="blue", command=Clear)
btn4.place(x=40, y=400)


Btn3 = Button(root, text="Quit", bg="blue", command=root.destroy)
Btn3.place(x=500, y=10)

root.mainloop()
