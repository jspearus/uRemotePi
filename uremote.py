from tkinter import *
import serial
import time
import os
import platform


root = Tk()
hud = Tk()

root.configure(background='black')
root.title("_Mantis_Blade_")
root.geometry('800x480')

hud.configure(background='black')
hud.title("_Mantis_Blade_")
hud.geometry('600x300')


text = ""

if platform.system() == "Linux":
    port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
    root.config(cursor="none")
    root.attributes('-fullscreen', True)
elif platform.system() == "Windows":
    #port = serial.Serial("COM7", baudrate=115200, timeout=3.0)
    pass


def Config():
    textBox.insert(END, "Config")
    textBox.yview(END)
    my_frame.place_forget()
    new_frame.place(x=40, y=60, width=300, height=200)
    btn2.place(x=700, y=200)
    Display("Execute")


def Dashboard():
    textBox.insert(END, "Dashboard")
    textBox.yview(END)
    new_frame.place_forget()
    btn2.place_forget()
    my_frame.place(x=40, y=60)
    Display("Reset      ")


def Display(x):
    myLabel = Label(root, bg="DarkOrange1", text=x)
    myLabel.place(x=250, y=10)


def Clear():
    textBox.delete(0, END)
    Display("Clear      ")


def Quit():
    root.destroy()
    hud.destroy()


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

new_frame = Frame(root, bg="snow")

newLabel = Label(new_frame, bg="Orange", justify="left",
                 text='Mantis_Blade_config')
secLabel = Label(new_frame, bg="grey", justify="left",
                 text='this is a new test')
newLabel.place(x=0, y=0)
secLabel.place(x=30, y=100)

btn2 = Button(root, text="Dashboard", bg="red", command=Dashboard)


Btn3 = Button(root, text="Quit", bg="blue", command=Quit)
Btn3.place(x=700, y=10)


osLabel = Label(root, bg="DarkOrange2",
                text="OS Detected: " + platform.system())
osLabel.place(x=40, y=20)


btn = Button(root, text="Config", bg="red", command=Config)
btn.place(x=700, y=400)


#btn2 = Button(root, text="Dashboard", bg="blue", command=Dashboard)
#btn2.place(x=600, y=400)

btn4 = Button(root, text="clear", bg="blue", command=Clear)
btn4.place(x=40, y=440)


root.mainloop()
hud.mainloop()
