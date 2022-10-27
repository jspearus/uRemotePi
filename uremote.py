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
serBuffer = "System Safe"
comData = ""
mynum = 0
Stop_t = False
foreground = "red"
mode = 0
S
armed = False

if platform.system() == "Linux":
    os.system('xinput map-to-output 6 HDMI-1')
    root.config(cursor="none")
    root.attributes('-fullscreen', False)
    try:  # /dev/ttyACM0
        port = serial.Serial('/dev/serial0', baudrate=115200,
                             bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        port.write(str.encode("comm#"))
        port.write(str.encode("comm#"))
    except serial.SerialException as e:
        print("device not detected")


elif platform.system() == "Windows":

    try:
        port = serial.Serial('COM10', baudrate=115200, timeout=10)
        print("COM10 Connected")
        port.write(str.encode("comm#"))
    except serial.SerialException as e:
        print("device not detected")


def Enable():
    global armed
    armed = True
    Enablebtn.place_forget()
    Disablebtn.place(x=300, y=75)
    quickMode.config(text="Quick Mode = En")
    cMode.config(text='System Armed')
    CMode.config(text='System Armed')
    port.write(str.encode("qen#"))


def Open():
    global armed
    if armed == True:
        open_btn.place_forget()
        close_btn.place(x=260, y=240)
        bladeStat.config(text="Arm = Opened")
        port.write(str.encode("hopen#"))


def Close():
    close_btn.place_forget()
    open_btn.place(x=260, y=240)
    bladeStat.config(text="Arm = Closed")
    port.write(str.encode("hclose#"))


def Disable():
    global armed
    armed = False
    Disablebtn.place_forget()
    Enablebtn.place(x=300, y=75)
    quickMode.config(text="Quick Mode = Dis")
    cMode.config(text='System Safe')
    CMode.config(text='System Safe')
    port.write(str.encode("qdis#"))


def Config():
    Dash_view.place_forget()
    btn.place_forget()
    Config_view.place(x=10, y=50)
    btn2.place(x=625, y=350)
    port.write(str.encode("config#"))


def Dashboard():
    Config_view.place_forget()
    btn2.place_forget()
    btn.place(x=625, y=350)
    Dash_view.place(x=10, y=50)
    port.write(str.encode("dash#"))


def Display(x):
    myLabel = Label(root, bg="DarkOrange1", text=x)
    myLabel.place(x=250, y=10)


def alert(x):
    Dashboard()
    alertLabel = Label(root, bg="red", font=("Arial", 25), text=x)
    alertLabel.place(x=25, y=250)
    BAThud()
    cBata.place(x=20, y=250)
    CBata.place(x=20, y=250)


def EXOhud():
    EXO_Stats.place(x=900, y=100)
    BAT_Stats.place_forget()
    btn5.place(x=625, y=250)
    btn6.place_forget()
    port.write(str.encode("exov#"))


def BAThud():
    BAT_Stats.place(x=900, y=100)
    EXO_Stats.place_forget()
    btn5.place_forget()
    btn6.place(x=625, y=250)
    port.write(str.encode("ctrlt#"))


def Quit():
    global Stop_t
    Stop_t = True
    root.destroy()


def SerialOut(com):
    port.write(com)


def serialRead():
    global serBuffer
    global mode
    serLabel.config(text="Device not Connected...")
    while True:
        Data = port.readline()
        Data = str(Data, 'UTF-8')
        data = Data.split(',')
        # serLabel.config(text=data[0])
        if 'MANTIS' in data[0]:
            serLabel.config(text="M.A.N.T.I.S. Arm Detected")
        elif 'config' in data[0]:
            cMode.config(text='Config Mode')
            CMode.config(text='Config Mode')
            EXOhud()

        elif 'armed' in data[0]:
            if mode > 0:
                cMode.config(text='System Armed')
                CMode.config(text='System Armed')
            else:
                cMode.config(text='System Safe')
                CMode.config(text='System Safe')
            EXOhud()

        elif 'mode = 0' in data[0]:
            mode = 0
            bladePos.config(text='Mode = Safe')
            bladePOS.config(text='Mode = Safe')
            BladePos.config(text='Mode = Safe')

        elif 'mode = 1' in data[0]:
            mode = 1
            bladePos.config(text='Mode = Sync')
            bladePOS.config(text='Mode = Sync')
            BladePos.config(text='Mode = Sync')

        elif 'mode = 2' in data[0]:
            mode = 2
            bladePos.config(text='Mode = Hold')
            bladePOS.config(text='Mode = Hold')
            BladePos.config(text='Mode = Hold')

        elif 'mode = 4' in data[0]:
            mode = 4
            bladePos.config(text='Mode = Quick')
            bladePOS.config(text='Mode = Quick')
            BladePos.config(text='Mode = Quick')

        elif 'stat' in data[0]:
            dBat.config(text='Drv_Pwr = ' + data[1]+' V')
            DBat.config(text='Drv_Pwr = ' + data[1]+' V')
            dBat_t.config(text='Drv_Temp = ' + data[2]+' C')
            DBat_t.config(text='Drv_Temp = ' + data[2]+' C')
            dBat1.config(text='Cell_1 = ' + data[3])
            DBat1.config(text='Cell_1 = ' + data[3])
            dBat2.config(text='Cell_2 = ' + data[4])
            DBat2.config(text='Cell_2 = ' + data[4])
            dBat3.config(text='Cell_3 = ' + data[5])
            DBat3.config(text='Cell_3 = ' + data[5])
            dBat4.config(text='Cell_4 = ' + data[6])
            DBat4.config(text='Cell_4 = ' + data[6])
            cBat.config(text='Ctrl_V = ' + data[8]+' V')
            CBat.config(text='Ctrl_V = ' + data[8]+' V')
            cBat_t.config(text='Ctrl_Temp = ' + data[7]+' C')
            CBat_t.config(text='Ctrl_Temp = ' + data[7]+' C')

        elif 'ctrlblow' in data[0]:
            alert('Ctrl Bat V Low')

        elif 'alert' in data[0]:
            alert('Drive Bat V Low')
        data = ''
        time.sleep(.2)
        if Stop_t:
            break


################ MAIN DISPLAY #####################################
# create frame and scrollbar
Dash_frame = Frame(root, bg="black")

Dash_view = LabelFrame(root, text="-Dashbord-", font=("Arial", 20),
                       width=600, height=350, bd=5, bg="black", fg=foreground)
Dash_view.place(x=10, y=50)

Config_view = LabelFrame(root, text="-Configuration-", font=("Arial", 20),
                         width=600, height=350, bd=5, bg="black", fg=foreground)

Bat_view = LabelFrame(Dash_view, text="-PowerMGMT-",
                      bg="black", fg=foreground, height=225, width=300)
Bat_view.place(x=250, y=75)

DBat = Label(Bat_view, text="Drive_pwr = 99 V",
             bg="black", fg="white", font=("Arial", 15))
DBat.place(x=7, y=5)

DBat1 = Label(Bat_view, text="Cell_1 = 99",
              bg="black", fg="white", font=("Arial", 10))
DBat1.place(x=12, y=30)

DBat2 = Label(Bat_view, text="Cell_2 = 99",
              bg="black", fg="white", font=("Arial", 10))
DBat2.place(x=12, y=50)

DBat3 = Label(Bat_view, text="Cell_3 = 99",
              bg="black", fg="white", font=("Arial", 10))
DBat3.place(x=12, y=70)

DBat4 = Label(Bat_view, text="Cell_4 = 99",
              bg="black", fg="white", font=("Arial", 10))
DBat4.place(x=12, y=90)

DBat_t = Label(Bat_view, text="DBat Temp = 99 C",
               bg="black", fg="white", font=("Arial", 11))
DBat_t.place(x=130, y=60)

CBat = Label(Bat_view, text="CTRL_pwr = 99 V",
             bg="black", fg="white", font=("Arial", 15))
CBat.place(x=42, y=135)

CBata = Label(Bat_view, text="CTRL_pwr = LOW",
              bg="black", fg="white", font=("Arial", 17))

CBat_t = Label(Bat_view, text="CBat Temp = 99 C",
               bg="black", fg="white", font=("Arial", 17))
CBat_t.place(x=45, y=165)


CMode = Label(Dash_view, text=serBuffer,
              bg="red", fg="black", font=("Arial", 20))
CMode.place(x=20, y=15)

BladePos = Label(Dash_view, text="Mode = Safe", bg="black",
                 fg=foreground, font=("Arial", 15))
BladePos.place(x=20, y=85)

quickMode = Label(Dash_view, text="Quick Mode = Dis", bg="black",
                  fg="white", font=("Arial", 10))
quickMode.place(x=20, y=125)
################CONFIG VIEW DASH###############################
bladePOS = Label(Config_view, text="Mode = Safe", bg="black",
                 fg="white", font=("Arial", 20))
bladePOS.place(x=50, y=20)

bladeStat = Label(Config_view, text="Arm = Closed", bg="black",
                  fg="white", font=("Arial", 15))
bladeStat.place(x=275, y=175)

safebtn = Button(Config_view, text="Safe", height=3,
                 width=10, bg=foreground, fg="black", font=("Arial", 10), command=lambda: SerialOut(b"modeS#"))
safebtn.place(x=475, y=60)

syncbtn = Button(Config_view, text="Sync", height=3,
                 width=10, bg=foreground, fg="black", font=("Arial", 10), command=lambda: SerialOut(b"modes#"))
syncbtn.place(x=475, y=150)

holdbtn = Button(Config_view, text="Hold", height=3,
                 width=10, bg=foreground, fg="black", font=("Arial", 10), command=lambda: SerialOut(b"modeh#"))
holdbtn.place(x=475, y=240)

open_btn = Button(Config_view, height=2, width=5,
                  text="open", bg=foreground, command=Open)
open_btn.place(x=260, y=240)

close_btn = Button(Config_view, height=2, width=5,
                   text="close", bg=foreground, command=Close)


Enablebtn = Button(Config_view, text="Enable \nQuick", height=3,
                   width=10, bg=foreground, fg="black", font=("Arial", 10), command=Enable)
Enablebtn.place(x=300, y=75)

Disablebtn = Button(Config_view, text="Disable \nQuick", height=3,
                    width=10, bg=foreground, fg="black", font=("Arial", 10), command=Disable)


PID_view = LabelFrame(Config_view, text=" PID_Config ", font=("Arial", 20),
                      width=200, height=200, bd=5, bg="black", fg=foreground)
PID_view.place(x=50, y=75)

P_val = Label(PID_view, text="P = 3.5", bg="black",
              fg="white", font=("Arial", 20))
P_val.place(x=8, y=20)
I_val = Label(PID_view, text="I = 1.0", bg="black",
              fg="white", font=("Arial", 20))
I_val.place(x=8, y=65)
D_val = Label(PID_view, text="D = 1", bg="black",
              fg="white", font=("Arial", 20))
D_val.place(x=8, y=110)

serLabel = Label(root, bg="black", fg=foreground, font=("Arial", 15), justify="left",
                 text='serial status   ')
serLabel.place(x=300, y=100)

btn2 = Button(root, height=3, width=10, text="Dashboard",
              bg=foreground, command=Dashboard)


Btn3 = Button(root, text="Quit", bg=foreground, command=Quit)
Btn3.place(x=675, y=10)

osLabel = Label(root, bg=foreground, fg="white", font=(
    "Arial", 10), height=1, width=75, justify="left")
osLabel.place(x=40, y=20)

if platform.system() == "Linux":
    osLabel.config(
        text="Device: Cyber Deck v 2.0.0                                                                                           ", justify="left")

elif platform.system() == "Windows":
    osLabel.config(
        text="Device: PC                                                                                                          ")

btn = Button(root, height=3, width=10,
             text="Config", bg=foreground, command=Config)
btn.place(x=625, y=350)


btn5 = Button(root, text="HUD_bat \nView", height=3,
              width=10, bg=foreground, command=BAThud)
btn5.place(x=625, y=250)

btn6 = Button(root, text="HUD_EXO \nView", height=3,
              width=10, bg=foreground, command=EXOhud)


######################### HUD WIDGETS ############################


hudLabel = Label(root, text="HUD view", font=(
    "Arial", 30),  bg="black", fg=foreground)
hudLabel.place(x=900, y=20)

#################### HUD EXO FRAME ###############################

EXO_Stats = LabelFrame(root, text=" EXO_Stats ", font=("Arial", 50),
                       width=1000, height=600, bd=15, bg="black", fg=foreground)
EXO_Stats.place(x=900, y=100)

cMode = Label(EXO_Stats, text=serBuffer,
              bg="red", fg="black", font=("Arial", 40))
cMode.place(x=20, y=15)

bladePos = Label(EXO_Stats, text="Mode = Safe", bg="black",
                 fg=foreground, font=("Arial", 35))
bladePos.place(x=20, y=85)

PID_Config = LabelFrame(EXO_Stats, text=" PID_Config ", font=("Arial", 35),
                        width=350, height=300, bd=10, bg="black", fg=foreground)
PID_Config.place(x=400, y=150)

P_val = Label(PID_Config, text="P = 3.5", bg="black",
              fg="white", font=("Arial", 30))
P_val.place(x=8, y=20)
I_val = Label(PID_Config, text="I = 1.0", bg="black",
              fg="white", font=("Arial", 30))
I_val.place(x=8, y=65)
D_val = Label(PID_Config, text="D = 1", bg="black",
              fg="white", font=("Arial", 30))
D_val.place(x=8, y=125)


# ################### HUD BAT FRAME ##############################

BAT_Stats = LabelFrame(root, text=" BAT_Stats ", font=("Arial", 50),
                       width=1000, height=600, bd=15, bg="black", fg=foreground)
# BAT_Stats.place(x=20, y=100)

dBat = Label(BAT_Stats, text="Drive_pwr = 99",
             bg="black", fg=foreground, font=("Arial", 32))
dBat.place(x=20, y=15)

dBat1 = Label(BAT_Stats, text="Cell_1 = 99",
              bg="black", fg="white", font=("Arial", 28))
dBat1.place(x=40, y=85)

dBat2 = Label(BAT_Stats, text="Cell_2 = 99",
              bg="black", fg="white", font=("Arial", 28))
dBat2.place(x=40, y=135)

dBat3 = Label(BAT_Stats, text="Cell_3 = 99",
              bg="black", fg="white", font=("Arial", 28))
dBat3.place(x=40, y=190)

dBat4 = Label(BAT_Stats, text="Cell_4 = 99",
              bg="black", fg="white", font=("Arial", 28))
dBat4.place(x=40, y=250)

dBat_t = Label(BAT_Stats, text="DBat Temp = 99 C",
               bg="black", fg=foreground, font=("Arial", 40))
dBat_t.place(x=400, y=150)

cBat = Label(BAT_Stats, text="CTRL_pwr = LOW",
             bg="black", fg=foreground, font=("Arial", 30))
cBat.place(x=400, y=370)

cBata = Label(BAT_Stats, text="CTRL_pwr = LOW",
              bg="black", fg="red", font=("Arial", 30))

cBat_t = Label(BAT_Stats, text="CBat Temp = 99 C",
               bg="black", fg=foreground, font=("Arial", 40))
cBat_t.place(x=400, y=425)

serial = threading.Thread(target=serialRead, args=())
serial.setDaemon(True)
serial.start()

root.mainloop()
