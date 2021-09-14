from tkinter import *
import serial
import time
import os
import platform

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

root = Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')
root.title("uRemote For All")
root.geometry('480x640')

text = ""


def Execute():
    Display("Execute")


def Reset():
    Display("Reset      ")


def Display(x):
    print(x)
    myLabel = Label(root, text=x)
    myLabel.place(x=200, y=100)


osLabel = Label(root, text= "OS Detected: " + platform.system())
osLabel.place(x=100, y=20)

btn = Button(root, text="Execute", command=Execute)
btn.place(x=350, y=575)


btn2 = Button(root, text="RESET", bg="blue", command=Reset)
btn2.place(x=250, y=575)



Btn3 = Button(root, text="Quit", command=root.destroy)
Btn3.place(x=400, y=10)

root.mainloop()
