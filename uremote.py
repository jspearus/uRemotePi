from tkinter import *
#import serial
import time

#port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

root = Tk()
root.title("uRemote")
root.geometry('700x400')

text = ""


def Execute():
    Display("Execute")


def Reset():
    Display("Reset      ")


def Display(x):
    print(x)
    myLabel = Label(root, text=x)
    myLabel.place(x=100, y=200)


btn = Button(root, text="Execute", command=Execute)
btn.place(x=600, y=350)
btn2 = Button(root, text="RESET", command=Reset)
btn2.place(x=525, y=350)

root.mainloop()
