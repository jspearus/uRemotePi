#! /usr/bin/python3

from tkinter import *
import serial
import time
import os
import platform
import threading

from serial.serialutil import Timeout


root = Tk()


root.configure(background='black')
root.title("_Mantis_Blade_")
root.geometry('2080x730+0+0')

text = ""
serBuffer = "Mode = Armed"
mynum = 0
Stop_t = False

if platform.system() == "Linux":
    os.system('xinput map-to-output 6 HDMI-1')
    root.config(cursor="none")
    root.attributes('-fullscreen', False)
    try:
        port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=10)
        port.write(str.encode("comm#"))
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


def alert(x):
    alertLabel = Label(root, bg="red", font=("Arial", 40), text=x)
    alertLabel.place(x=400, y=200)
    BAThud()
    cBata.place(x=375, y=370)


def Clear():
    textBox.delete(0, END)
    Display("Clear            ")


def EXOhud():
    EXO_Stats.place(x=850, y=100)
    BAT_Stats.place_forget()
    btn5.place(x=550, y=380)
    btn6.place_forget()
    port.write(str.encode("exov#"))


def BAThud():
    BAT_Stats.place(x=850, y=100)
    EXO_Stats.place_forget()
    btn5.place_forget()
    btn6.place(x=550, y=380)
    port.write(str.encode("ctrlt#"))


def Quit():
    global Stop_t
    Stop_t = True
    root.destroy()


def serialRead():
    global serBuffer
    serLabel.config(text="Serial Port Open")
    while True:
        data = port.readline()
        data = data.split(b"\r")
        serLabel.config(text=data[0])
        if b'config' in data[0]:
            cMode.config(text='Config Mode')
            EXOhud()

        elif b'armed' in data[0]:
            cMode.config(text='System Armed')
            EXOhud()

        elif b'mode = 0' in data[0]:
            bladePos.config(text='Mode = Safe')

        elif b'mode = 1' in data[0]:
            bladePos.config(text='Mode = Sync')

        elif b'mode = 2' in data[0]:
            bladePos.config(text='Mode = Hold')

        elif b'Ctrl Bat Temp' in data[0]:
            cBat_t.config(text=data[0])

        elif b'Drv Bat Temp' in data[0]:
            dBat_t.config(text=data[0])

        elif b'Drv_Pwr' in data[0]:
            dBat.config(text=data[0])

        elif b'Ctrl Bat V' in data[0]:
            cBat.config(text=data[0])

        elif b'Cell 1 Status' in data[0]:
            dBat1.config(text=data[0])

        elif b'Cell 2 Status' in data[0]:
            dBat2.config(text=data[0])

        elif b'Cell 3 Status' in data[0]:
            dBat3.config(text=data[0])

        elif b'Cell 4 Status' in data[0]:
            dBat4.config(text=data[0])

        elif b'ctrlblow' in data[0]:
            alert('Ctrl Bat V Low')

        elif b'alert' in data[0]:
            alert('Drive Bat V Low')
        data = ''
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
                 text=serBuffer)
secLabel = Label(new_frame, bg="black", justify="left",
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
btn5.place(x=550, y=380)

btn6 = Button(root, text="HUD_EXO View", bg="blue", command=EXOhud)


btn4 = Button(root, text="clear", bg="blue", command=Clear)
btn4.place(x=40, y=440)


######################### HUD WIDGETS ############################


hudLabel = Label(root, text="HUD view", font=(
    "Arial", 30),  bg="black", fg="orange")
hudLabel.place(x=850, y=20)

#################### HUD EXO FRAME ###############################

EXO_Stats = LabelFrame(root, text=" EXO_Stats ", font=("Arial", 50),
                       width=1000, height=600, bd=15, bg="black", fg="orange")
EXO_Stats.place(x=850, y=100)

cMode = Label(EXO_Stats, text=serBuffer,
              bg="red", fg="black", font=("Arial", 40))
cMode.place(x=20, y=15)

bladePos = Label(EXO_Stats, text="Mode = Safe", bg="black",
                 fg="orange", font=("Arial", 35))
bladePos.place(x=20, y=85)

PID_Config = LabelFrame(EXO_Stats, text=" PID_Config ", font=("Arial", 35),
                        width=350, height=300, bd=10, bg="black", fg="orange")
PID_Config.place(x=400, y=150)

P_val = Label(PID_Config, text="P = 4", bg="black",
              fg="white", font=("Arial", 30))
P_val.place(x=8, y=20)
I_val = Label(PID_Config, text="I = 1", bg="black",
              fg="white", font=("Arial", 30))
I_val.place(x=8, y=65)
D_val = Label(PID_Config, text="D = 1", bg="black",
              fg="white", font=("Arial", 30))
D_val.place(x=8, y=125)


# ################### HUD BAT FRAME ##############################

BAT_Stats = LabelFrame(root, text=" BAT_Stats ", font=("Arial", 50),
                       width=1000, height=600, bd=15, bg="black", fg="orange")
# BAT_Stats.place(x=20, y=100)

dBat = Label(BAT_Stats, text="Drive_pwr = 100 %",
             bg="black", fg="red", font=("Arial", 30))
dBat.place(x=20, y=15)

dBat1 = Label(BAT_Stats, text="Cell_1 = 4.1v",
              bg="black", fg="red", font=("Arial", 25))
dBat1.place(x=40, y=85)

dBat2 = Label(BAT_Stats, text="Cell_2 = 4.1v",
              bg="black", fg="red", font=("Arial", 25))
dBat2.place(x=40, y=135)

dBat3 = Label(BAT_Stats, text="Cell_3 = 4.1v",
              bg="black", fg="red", font=("Arial", 25))
dBat3.place(x=40, y=190)

dBat4 = Label(BAT_Stats, text="Cell_4 = 4.1v",
              bg="black", fg="red", font=("Arial", 25))
dBat4.place(x=40, y=250)

dBat_t = Label(BAT_Stats, text="DBat Temp = 25 C",
               bg="black", fg="red", font=("Arial", 40))
dBat_t.place(x=140, y=300)

cBat = Label(BAT_Stats, text="CTRL_pwr = LOW",
             bg="black", fg="red", font=("Arial", 30))
cBat.place(x=375, y=370)

cBata = Label(BAT_Stats, text="CTRL_pwr = LOW",
              bg="black", fg="red", font=("Arial", 30))

cBat_t = Label(BAT_Stats, text="CBat Temp = 20 C",
               bg="black", fg="red", font=("Arial", 40))
cBat_t.place(x=400, y=425)

serial = threading.Thread(target=serialRead, args=())
serial.setDaemon(True)
serial.start()

root.mainloop()
