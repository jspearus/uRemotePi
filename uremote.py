from tkinter import *
import serial
import time
import os
import platform


root = Tk()
root.configure(background='black')
root.title("uRemote For All")
root.geometry('800x480')


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
    my_frame.place_forget()
    new_frame.place(x=40, y=60, width=300, height=200)
    btn5.place(x=700, y=200)
    Display("Execute")


def Reset():
    textBox.insert(END, "Reset")
    textBox.yview(END)
    new_frame.place_forget()
    btn5.place_forget()
    my_frame.place(x=40, y=60)
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

new_frame = Frame(root, bg="blue")

newLabel = Label(new_frame, bg="red", justify="left", text='this is a test')
secLabel = Label(new_frame, bg="grey", justify="left",
                 text='this is a new test')
newLabel.place(x=0, y=0)
secLabel.place(x=30, y=100)

btn5 = Button(root, text="new button", bg="red", command=Reset)


Btn3 = Button(root, text="Quit", bg="blue", command=root.destroy)
Btn3.place(x=700, y=10)


osLabel = Label(root, bg="blue", text="OS Detected: " + platform.system())
osLabel.place(x=40, y=20)


btn = Button(root, text="Execute", bg="red", command=Execute)
btn.place(x=700, y=400)


btn2 = Button(root, text="RESET", bg="blue", command=Reset)
btn2.place(x=600, y=400)

btn4 = Button(root, text="clear", bg="blue", command=Clear)
btn4.place(x=40, y=440)


root.mainloop()
