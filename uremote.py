from tkinter import *
import serial
import time
import os
import platform


root = Tk()
root.configure(background='black')
root.title("uRemote For All")
root.geometry('480x640')


text = ""

if platform.system() == "Linux":
    port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
    root.config(cursor="none")
    root.attributes('-fullscreen', True)
elif platform.system() == "Windows":
    #port = serial.Serial("COM7", baudrate=115200, timeout=3.0)
    pass


def Execute():
    textBox['text'] += "Execute" + "\n"
    Display("Execute")


def Reset():
    textBox['text'] += "Reset" + "\n"
    Display("Reset      ")


def Display(x):
    myLabel = Label(root, bg="blue", text=x)
    myLabel.place(x=40, y=420)


def Clear():
    textBox['text'] = ""
    Display("Clear      ")


textBox = Label(root, bg="blue", width=45, height=20,
                anchor="nw", justify="left")
textBox.place(x=40, y=60)


osLabel = Label(root, bg="blue", text="OS Detected: " + platform.system())
osLabel.place(x=40, y=20)

btn = Button(root, text="Execute", bg="blue", command=Execute)
btn.place(x=350, y=575)


btn2 = Button(root, text="RESET", bg="blue", command=Reset)
btn2.place(x=175, y=575)

btn4 = Button(root, text="clear", bg="blue", command=Clear)
btn4.place(x=40, y=575)


Btn3 = Button(root, text="Quit", bg="blue", command=root.destroy)
Btn3.place(x=400, y=10)

root.mainloop()
