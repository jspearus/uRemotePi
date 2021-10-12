#! /usr/bin/python3

from tkinter import *
import serial
import time
import os
import platform
import threading

from serial.serialutil import Timeout


hud = Tk()
root = Tk()


hud.configure(background='black')
hud.title("_Mantis_Blade_HUD")
hud.geometry('1280x720+801+0')

root.configure(background='gray40')
root.title("_Mantis_Blade_")
root.geometry('800x480+0+0')

text = ""
serBuffer = ""
mynum = 0
Stop_t = False

if platform.system() == "Linux":
    os.system('xinput map-to-output 6 HDMI-1')
    root.config(cursor="none")
    hud.attributes('-fullscreen', False)
    root.attributes('-fullscreen', True)
    try:
        port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=10)
        port.write(str.encode("comm#"))
    except serial.SerialException as e:
        print("device not detected")


elif platform.system() == "Windows":
    try:
        port = serial.Serial('COM10', baudrate=9600, timeout=10)
        print("COM10 Connected")
        port.write(str.encode("comm#"))
    except serial.SerialException as e:
        print("device not detected")


def Config():
    textBox.insert(END, "Config")
    textBox.yview(END)
    my_frame.place_forget()
    btn.place_forget()
    new_frame.place(x=40, y=60, width=300, height=200)
    btn2.place(x=700, y=350)
    Display("Configuation ")
    port.write(str.encode("config#"))


def Dashboard():
    textBox.insert(END, "Dashboard")
    textBox.yview(END)
    new_frame.place_forget()
    btn2.place_forget()
    btn.place(x=700, y=350)
    my_frame.place(x=40, y=60)
    Display("Dashboard      ")
    port.write(str.encode("dash#"))


def Display(x):
    myLabel = Label(root, bg="DarkOrange1", text=x)
    myLabel.place(x=250, y=10)


def Clear():
    textBox.delete(0, END)
    Display("Clear            ")


def EXOhud():
    EXO_Stats.place(x=15, y=100)
    BAT_Stats.place_forget()
    btn5.place(x=550, y=400)
    btn6.place_forget()


def BAThud():
    BAT_Stats.place(x=15, y=100)
    EXO_Stats.place_forget()
    btn5.place_forget()
    btn6.place(x=550, y=400)


def Quit():
    global Stop_t
    Stop_t = True
    root.destroy()
    hud.destroy()


def serialRead():
    serLabel.config(text="Serial Port Open")
    while True:
        data = port.readline()
        serLabel.config(text=data)
        time.sleep(.2)
        if Stop_t:
            break


################ MAIN DISPLAY #####################################
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
serLabel = Label(root, bg="black", fg="red", justify="left",
                 text='serial status   ')
newLabel.place(x=0, y=0)
secLabel.place(x=30, y=100)
serLabel.place(x=450, y=200)

btn2 = Button(root, height=2, width=8, text="Dashboard",
              bg="red", command=Dashboard)


Btn3 = Button(root, text="Quit", bg="blue", command=Quit)
Btn3.place(x=700, y=10)


osLabel = Label(root, bg="DarkOrange2",
                text="OS Detected: " + platform.system())
osLabel.place(x=40, y=20)


btn = Button(root, height=2, width=8,
             text="Config", bg="red", command=Config)
btn.place(x=700, y=350)


btn5 = Button(root, text="HUD_bat View", bg="blue", command=BAThud)
btn5.place(x=550, y=400)

btn6 = Button(root, text="HUD_EXO View", bg="blue", command=EXOhud)


btn4 = Button(root, text="clear", bg="blue", command=Clear)
btn4.place(x=40, y=440)


######################### HUD WIDGETS ############################


hudLabel = Label(hud, text="HUD view", font=(
    "Arial", 30),  bg="black", fg="orange")
hudLabel.place(x=20, y=20)

#################### HUD EXO FRAME ###############################

EXO_Stats = LabelFrame(hud, text=" EXO_Stats ", font=("Arial", 50),
                       width=1000, height=600, bd=15, bg="black", fg="orange")
EXO_Stats.place(x=15, y=100)

cMode = Label(EXO_Stats, text="Mode = armed",
              bg="red", fg="black", font=("Arial", 40))
cMode.place(x=20, y=15)

bladePos = Label(EXO_Stats, text="Pos = 100", bg="black",
                 fg="orange", font=("Arial", 35))
bladePos.place(x=20, y=85)

PID_Config = LabelFrame(EXO_Stats, text=" PID_Config ", font=("Arial", 35),
                        width=400, height=300, bd=10, bg="black", fg="orange")
PID_Config.place(x=300, y=150)

P_val = Label(PID_Config, text="P = 4", bg="black",
              fg="white", font=("Arial", 30))
P_val.place(x=8, y=20)
I_val = Label(PID_Config, text="I = 1", bg="black",
              fg="white", font=("Arial", 30))
I_val.place(x=8, y=65)
D_val = Label(PID_Config, text="D = 1", bg="black",
              fg="white", font=("Arial", 30))
D_val.place(x=8, y=125)


################### HUD BAT FRAME ##############################

BAT_Stats = LabelFrame(hud, text=" BAT_Stats ", font=("Arial", 50),
                       width=1000, height=600, bd=15, bg="black", fg="orange")
# BAT_Stats.place(x=20, y=100)

dBat = Label(BAT_Stats, text="Drive_pwr = 100 %",
             bg="gray8", fg="red", font=("Arial", 30))
dBat.place(x=20, y=15)

dBat1 = Label(BAT_Stats, text="Cell_1 = 4.1v",
              bg="gray8", fg="red", font=("Arial", 25))
dBat1.place(x=40, y=85)

dBat2 = Label(BAT_Stats, text="Cell_2 = 4.1v",
              bg="gray8", fg="red", font=("Arial", 25))
dBat2.place(x=40, y=135)

dBat3 = Label(BAT_Stats, text="Cell_3 = 4.1v",
              bg="gray8", fg="red", font=("Arial", 25))
dBat3.place(x=40, y=190)

dBat4 = Label(BAT_Stats, text="Cell_4 = 4.1v",
              bg="gray8", fg="red", font=("Arial", 25))
dBat4.place(x=40, y=250)

dBat_t = Label(BAT_Stats, text="DBat Temp = 25 C",
               bg="gray8", fg="red", font=("Arial", 40))
dBat_t.place(x=140, y=300)

cBat = Label(BAT_Stats, text="CTRL_pwr = 75 %",
             bg="gray8", fg="red", font=("Arial", 30))
cBat.place(x=375, y=370)
cBat_t = Label(BAT_Stats, text="CBat Temp = 20 C",
               bg="gray8", fg="red", font=("Arial", 40))
cBat_t.place(x=475, y=425)

serial = threading.Thread(target=serialRead, args=())
serial.setDaemon(True)
serial.start()

root.mainloop()
hud.mainloop()
