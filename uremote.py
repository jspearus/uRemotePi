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
comData = ""
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
    Dash_view.place_forget()
    btn.place_forget()
    Config_view.place(x=0, y=50)
    btn2.place(x=700, y=350)
    port.write(str.encode("config#"))


def Dashboard():
    Config_view.place_forget()
    btn2.place_forget()
    btn.place(x=700, y=350)
    Dash_view.place(x=0, y=50)
    port.write(str.encode("dash#"))


def Display(x):
    myLabel = Label(root, bg="DarkOrange1", text=x)
    myLabel.place(x=250, y=10)


def alert(x):
    alertLabel = Label(root, bg="red", font=("Arial", 40), text=x)
    alertLabel.place(x=400, y=200)
    BAThud()
    cBata.place(x=375, y=370)


def EXOhud():
    EXO_Stats.place(x=850, y=100)
    BAT_Stats.place_forget()
    btn5.place(x=700, y=250)
    btn6.place_forget()
    port.write(str.encode("exov#"))


def BAThud():
    BAT_Stats.place(x=850, y=100)
    EXO_Stats.place_forget()
    btn5.place_forget()
    btn6.place(x=700, y=250)
    port.write(str.encode("ctrlt#"))


def Quit():
    global Stop_t
    Stop_t = True
    root.destroy()


def SerialOut(com):
    port.write(com)


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
Dash_frame = Frame(root, bg="black")

Dash_view = LabelFrame(root, text="-Dashbord-", font=("Arial", 20),
                       width=650, height=350, bd=5, bg="black", fg="orange")
Dash_view.place(x=0, y=50)

Config_view = LabelFrame(root, text="-Configuration-", font=("Arial", 20),
                         width=650, height=350, bd=5, bg="black", fg="orange")

Bat_view = LabelFrame(Dash_view, text="-PowerMGMT-",
                      bg="black", fg="orange", height=225, width=300)
Bat_view.place(x=300, y=75)

dBat = Label(Bat_view, text="Drive_pwr = 16.4 V",
             bg="black", fg="white", font=("Arial", 15))
dBat.place(x=7, y=5)

dBat1 = Label(Bat_view, text="Cell_1 = Good",
              bg="black", fg="white", font=("Arial", 10))
dBat1.place(x=12, y=30)

dBat2 = Label(Bat_view, text="Cell_2 = Good",
              bg="black", fg="white", font=("Arial", 10))
dBat2.place(x=12, y=50)

dBat3 = Label(Bat_view, text="Cell_3 = Good",
              bg="black", fg="white", font=("Arial", 10))
dBat3.place(x=12, y=70)

dBat4 = Label(Bat_view, text="Cell_4 = Good",
              bg="black", fg="white", font=("Arial", 10))
dBat4.place(x=12, y=90)

dBat_t = Label(Bat_view, text="DBat Temp = 25 C",
               bg="black", fg="white", font=("Arial", 12))
dBat_t.place(x=115, y=60)

cBat = Label(Bat_view, text="CTRL_pwr = 4.0 V",
             bg="black", fg="white", font=("Arial", 17))
cBat.place(x=42, y=135)

cBata = Label(Bat_view, text="CTRL_pwr = LOW",
              bg="black", fg="white", font=("Arial", 17))

cBat_t = Label(Bat_view, text="CBat Temp = 20 C",
               bg="black", fg="white", font=("Arial", 20))
cBat_t.place(x=45, y=165)


cMode = Label(Dash_view, text=serBuffer,
              bg="red", fg="black", font=("Arial", 20))
cMode.place(x=20, y=15)

bladePos = Label(Dash_view, text="Mode = Safe", bg="black",
                 fg="orange", font=("Arial", 15))
bladePos.place(x=20, y=85)
################CONFIG VIEW DASH###############################
bladePOS = Label(Config_view, text="Mode = Safe", bg="black",
                 fg="white", font=("Arial", 20))
bladePOS.place(x=50, y=20)

safebtn = Button(Config_view, text="Safe", height=3,
                 width=10, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(b"modeS#"))
safebtn.place(x=525, y=60)

syncbtn = Button(Config_view, text="Sync", height=3,
                 width=10, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(b"modes#"))
syncbtn.place(x=525, y=150)

holdbtn = Button(Config_view, text="Hold", height=3,
                 width=10, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(b"modeh#"))
holdbtn.place(x=525, y=240)

PID_view = LabelFrame(Config_view, text=" PID_Config ", font=("Arial", 25),
                      width=250, height=200, bd=5, bg="black", fg="orange")
PID_view.place(x=50, y=75)

P_val = Label(PID_view, text="P = 4", bg="black",
              fg="white", font=("Arial", 20))
P_val.place(x=8, y=20)
I_val = Label(PID_view, text="I = 1", bg="black",
              fg="white", font=("Arial", 20))
I_val.place(x=8, y=65)
D_val = Label(PID_view, text="D = 1", bg="black",
              fg="white", font=("Arial", 20))
D_val.place(x=8, y=110)

serLabel = Label(root, bg="black", fg="white", font=("Arial", 15), justify="left",
                 text='serial status   ')
serLabel.place(x=450, y=100)

btn2 = Button(root, height=3, width=12, text="Dashboard",
              bg="DarkOrange2", command=Dashboard)


Btn3 = Button(root, text="Quit", bg="DarkOrange2", command=Quit)
Btn3.place(x=700, y=10)

osLabel = Label(root, bg="DarkOrange2", fg="white", font=(
    "Arial", 10), height=1, width=75, justify="left")
osLabel.place(x=40, y=20)

if platform.system() == "Linux":
    osLabel.config(
        text="Device: M.A.N.T.I.S. Blade                                                                                 ", justify="left")

elif platform.system() == "Windows":
    osLabel.config(
        text="Device: PC                                                                                 ")


btn = Button(root, height=3, width=12,
             text="Config", bg="DarkOrange2", command=Config)
btn.place(x=700, y=350)


btn5 = Button(root, text="HUD_bat \nView", height=3,
              width=12, bg="DarkOrange2", command=BAThud)
btn5.place(x=700, y=250)

btn6 = Button(root, text="HUD_EXO \nView", height=3,
              width=12, bg="DarkOrange2", command=EXOhud)


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
             bg="black", fg="DarkOrange2", font=("Arial", 30))
dBat.place(x=20, y=15)

dBat1 = Label(BAT_Stats, text="Cell_1 = 4.1v",
              bg="black", fg="white", font=("Arial", 25))
dBat1.place(x=40, y=85)

dBat2 = Label(BAT_Stats, text="Cell_2 = 4.1v",
              bg="black", fg="white", font=("Arial", 25))
dBat2.place(x=40, y=135)

dBat3 = Label(BAT_Stats, text="Cell_3 = 4.1v",
              bg="black", fg="white", font=("Arial", 25))
dBat3.place(x=40, y=190)

dBat4 = Label(BAT_Stats, text="Cell_4 = 4.1v",
              bg="black", fg="white", font=("Arial", 25))
dBat4.place(x=40, y=250)

dBat_t = Label(BAT_Stats, text="DBat Temp = 25 C",
               bg="black", fg="DarkOrange2", font=("Arial", 40))
dBat_t.place(x=140, y=300)

cBat = Label(BAT_Stats, text="CTRL_pwr = LOW",
             bg="black", fg="DarkOrange2", font=("Arial", 30))
cBat.place(x=375, y=370)

cBata = Label(BAT_Stats, text="CTRL_pwr = LOW",
              bg="black", fg="red", font=("Arial", 30))

cBat_t = Label(BAT_Stats, text="CBat Temp = 20 C",
               bg="black", fg="DarkOrange2", font=("Arial", 40))
cBat_t.place(x=400, y=425)

serial = threading.Thread(target=serialRead, args=())
serial.setDaemon(True)
serial.start()

root.mainloop()
