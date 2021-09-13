from tkinter import *
import serial
import time

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

root = Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')
root.title("uRemote")
root.geometry('600x400')

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
btn.place(x=550, y=350)


btn2 = Button(root, text="RESET", bg="blue", command=Reset)
btn2.place(x=475, y=350)

Btn3 = Button(root, text="Quit", command=root.destroy)
Btn3.place(x=550, y=20)

root.mainloop()
