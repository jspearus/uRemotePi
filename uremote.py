#! /usr/bin/python3

from tkinter import *
import serial
import time
import os
import platform
import threading




DataIn = ''
connected = True
step = '1000'
name_file = 'error'

if platform.system() == "Linux":
    # os.system('xinput map-to-output 6 HDMI-1')
    # root.config(cursor="none")
    # root.attributes('-fullscreen', False)
    # name_file = '/home/pi/uRemotePi/name.txt'
    name_file = '/home/jeff/Documents/Github/uRemotePi/name.txt'
    try:
        port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=10)
        port.write(str.encode("comm#"))
        port.write(str.encode("comm#"))
    except serial.SerialException as e:
        print("device not detected")


root = Tk()


root.configure(background='black')
root.title("_Rover Remote_")
root.geometry('800x480+0+0')

text = ""
comData = ""
mynum = 0
Stop_t = False


def pilotView():
    Dash_view.place_forget()
    Pilot_view.place(x=0, y=50)


def Dashboard():
    Dash_view.place(x=0, y=50)
    Pilot_view.place_forget()


def Display(x):
    myLabel = Label(root, bg="DarkOrange1", text=x)
    myLabel.place(x=250, y=10)


def alert(x):
    Dashboard()
    alertLabel = Label(root, bg="red", font=("Arial", 40), text=x)
    alertLabel.place(x=400, y=200)


def setSpeed(x):
    global step
    step = x
    roverSpeed.config(text=f"Speed = {step}")


def setCamSpeed(x):
    send(x)
    if"clow" in x:
        speed = "LOW"
    elif"cmed" in x:
        speed = "MED"
    elif"chi" in x:
        speed = "HI"
    camSpeed.config(text=f"Speed = {speed}")


def sendMove(x):
    global step
    event = x + step
    send(event)


def Quit():
    global connected
    connected = False
    global Stop_t
    Stop_t = True
    root.destroy()

def SerialOut(com):
    port.write(com)


def serialRead():
    global serBuffer
    serLabel.config(text="Device not Connected...")
    while True:
        Data = port.readline()
        Data = str(Data, 'UTF-8')
        data = Data.split(',')
        # serLabel.config(text=data[0])
        if 'MANTIS' in data[0]:
            serLabel.config(text="M.A.N.T.I.S. Blade Detected")

        elif 'config' in data[0]:
            cMode.config(text='Config Mode')
            CMode.config(text='Config Mode')
            EXOhud()

        elif 'ctrlblow' in data[0]:
            alert('Ctrl Bat V Low')

        elif 'alert' in data[0]:
            alert('Drive Bat V Low')
        data = ''
        time.sleep(.2)
        if Stop_t:
            break



############################ ROOT DISPLAY #################################
osLabel = Label(root, bg="DarkOrange2", fg="white", font=(
    "Arial", 10), height=1, width=75, justify="left")
osLabel.place(x=40, y=20)

if platform.system() == "Linux":
    osLabel.config(
        text="Device: uRemote                                                                            ", justify="left")

elif platform.system() == "Windows":
    osLabel.config(
        text="Device: PC                                                                                 ", justify="left")
############################ ROOT BUTTONS ##########################################
quitBtn = Button(root, text="Quit", bg="DarkOrange2", command=Quit)
quitBtn.place(x=725, y=10)

pilotBtn = Button(root, height=3, width=10, text="Manual\nCtrl",
                  bg="DarkOrange2", command=pilotView)
pilotBtn.place(x=675, y=100)

# camBtn = Button(root, height=3, width=10, text="Vision\nCtrl",
#                 bg="DarkOrange2", command=camView)
# camBtn.place(x=675, y=200)

# navBtn = Button(root, height=3, width=10,
#                 text="Nav\nCtrl", bg="DarkOrange2", command=navView)
# navBtn.place(x=675, y=300)

dashBtn = Button(root, height=3, width=10, text="Dashboard",
                 bg="DarkOrange2", command=Dashboard)
dashBtn.place(x=675, y=400)
###################################################################################
#################### CREATE FRAMES ##################################################

Dash_frame = Frame(root, bg="black")

Dash_view = LabelFrame(root, text="-ANT.ini-Dashboard", font=("Arial", 20),
                       width=650, height=410, bd=5, bg="black", fg="orange")
Dash_view.place(x=2, y=50)

Pilot_view = LabelFrame(root, text="-ANT.ini-Manual_Ctrl-", font=("Arial", 20),
                        width=650, height=410, bd=5, bg="black", fg="orange")
################ DASHBOARD #####################################

roverStatus = Label(Dash_view, text="ANT.ini Offline",
                    bg="red", fg="black", font=("Arial", 25))
roverStatus.place(x=20, y=15)

roverModeD = Label(Dash_view, text="Mode = Sit", bg="black",
                   fg="orange", font=("Arial", 20))
roverModeD.place(x=20, y=85)


################# PILOT VIEW ########################################

# roverSpeed = Label(Pilot_view, text=f"Speed = {step}", bg="black",
#                    fg="white", font=("Arial", 15))
# roverSpeed.place(x=200, y=115)

pUpBtn = Button(Pilot_view, text="Forward", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(b"stepf#"))
pUpBtn.place(x=130, y=170)
pdnBtn = Button(Pilot_view, text="Back", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(b"stepb#"))
pdnBtn.place(x=130, y=290)
pLfBtn = Button(Pilot_view, text="Left", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(b"stepl#"))
pLfBtn.place(x=65, y=230)
pRtBtn = Button(Pilot_view, text="Right", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(b"stepr#"))
pRtBtn.place(x=195, y=230)

pLeftBtn = Button(Pilot_view, text="Stand", height=2,
                  width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(b"stand#"))
pLeftBtn.place(x=20, y=320)
pFrontBtn = Button(Pilot_view, text="Sit", height=2,
                   width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(b"sit#"))
pFrontBtn.place(x=230, y=320)
pStopBtn = Button(Pilot_view, text="Attack", height=2,
                  width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(b"attack#"))
pStopBtn.place(x=550, y=320)

# pseedLabel = Label(Pilot_view, text="1000                    Speed Select                    13000", bg="black",
#                    fg="white", font=("Arial", 10))
# pseedLabel.place(x=20, y=0)
# pspeed = Scale(Pilot_view, bg="orange", fg="black",
#                font=("Arial", 10), from_=1000, to=13000, tickinterval=3000, width=35, length=300, orient=HORIZONTAL)
# pspeed.place(x=20, y=25)
# setBtn = Button(Pilot_view, text="Set", height=1,
#                 width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: SerialOut(f'{pspeed.get()}'))
# setBtn.place(x=25, y=125)

serial = threading.Thread(target=serialRead, args=())
serial.setDaemon(True)
serial.start()

root.mainloop()
