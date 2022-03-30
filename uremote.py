#! /usr/bin/python3

from tkinter import *
import time
import os
import platform
import threading
import socket


HEADER = 64
PORT = 5000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "dgscore.ddns.net"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
DataIn = ''
connected = True
step = '1000'
name_file = 'error'

if platform.system() == "Linux":
    os.system('xinput map-to-output 6 HDMI-1')
    root.config(cursor="none")
    root.attributes('-fullscreen', True)
    name_file = '/home/pi/uRemotePi/name.txt'


elif platform.system() == "Windows":
    name_file = 'name.txt'


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))


def SocketIn():
    global DataIn
    global connected
    print('listening...')
    while connected:
        DataIn = client.recv(2048).decode(FORMAT)
        if not DataIn:
            break
        print(DataIn)
        ####################### COMMANDS ##################
        if DataIn == 'Rover':
            roverStatus.config(text='Rover Online')
        elif DataIn == 'rOffline':
            roverStatus.config(text='Rover Offline')
        elif 'Bat:' in DataIn:
            roverModeD.config(text=DataIn)
        DataIn = ''
        time.sleep(.5)


with open(name_file) as f:
    name = f.readline()
    send(name)
    print(f"Connected as: {name}")
    send('site, devices')


root = Tk()


root.configure(background='black')
root.title("_Rover Remote_")
root.geometry('800x480+0+0')

text = ""
comData = ""
mynum = 0
Stop_t = False


def navView():
    Dash_view.place_forget()
    Pilot_view.place_forget()
    cam_view.place_forget()
    Nav_view.place(x=0, y=50)


def camView():
    Dash_view.place_forget()
    Pilot_view.place_forget()
    Nav_view.place_forget()
    cam_view.place(x=0, y=50)


def pilotView():
    Dash_view.place_forget()
    Nav_view.place_forget()
    cam_view.place_forget()
    Pilot_view.place(x=0, y=50)


def Dashboard():
    send('rover, status')
    Dash_view.place(x=0, y=50)
    Nav_view.place_forget()
    Pilot_view.place_forget()
    cam_view.place_forget()


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
    send(DISCONNECT_MESSAGE)
    time.sleep(1)
    connected = False
    global Stop_t
    Stop_t = True
    root.destroy()


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

pilotBtn = Button(root, height=3, width=10, text="Pilot\nCtrl",
                  bg="DarkOrange2", command=pilotView)
pilotBtn.place(x=675, y=100)

camBtn = Button(root, height=3, width=10, text="Vision\nCtrl",
                bg="DarkOrange2", command=camView)
camBtn.place(x=675, y=200)

navBtn = Button(root, height=3, width=10,
                text="Nav\nCtrl", bg="DarkOrange2", command=navView)
navBtn.place(x=675, y=300)

dashBtn = Button(root, height=3, width=10, text="Dashboard",
                 bg="DarkOrange2", command=Dashboard)
dashBtn.place(x=675, y=400)
###################################################################################
#################### CREATE FRAMES ##################################################

Dash_frame = Frame(root, bg="black")

Dash_view = LabelFrame(root, text="-Dashbord_Johnny-", font=("Arial", 20),
                       width=650, height=410, bd=5, bg="black", fg="orange")
Dash_view.place(x=2, y=50)

Pilot_view = LabelFrame(root, text="-Pilot_Ctrl-", font=("Arial", 20),
                        width=650, height=410, bd=5, bg="black", fg="orange")

cam_view = LabelFrame(root, text="-Vision_Ctrl-", font=("Arial", 20),
                      width=650, height=410, bd=5, bg="black", fg="orange")

Nav_view = LabelFrame(root, text="-Nav_Ctrl-", font=("Arial", 20),
                      width=650, height=410, bd=5, bg="black", fg="orange")
################ DASHBOARD #####################################

roverStatus = Label(Dash_view, text="Rover Offline",
                    bg="red", fg="black", font=("Arial", 25))
roverStatus.place(x=20, y=15)

roverModeD = Label(Dash_view, text="Mode = Safe", bg="black",
                   fg="orange", font=("Arial", 20))
roverModeD.place(x=20, y=85)

PID_view = LabelFrame(Dash_view, text=" PID_Config ", font=("Arial", 25),
                      width=250, height=200, bd=5, bg="black", fg="orange")
PID_view.place(x=300, y=75)

P_val = Label(PID_view, text="P = 3.5", bg="black",
              fg="white", font=("Arial", 20))
P_val.place(x=8, y=20)
I_val = Label(PID_view, text="I = 1.0", bg="black",
              fg="white", font=("Arial", 20))
I_val.place(x=8, y=65)
D_val = Label(PID_view, text="D = 0", bg="black",
              fg="white", font=("Arial", 20))
D_val.place(x=8, y=110)

################ NAV Ctrl ###############################

roverSpeed = Label(Nav_view, text="Mode = Safe", bg="black",
                   fg="white", font=("Arial", 20))
roverSpeed.place(x=50, y=20)

scanBtn = Button(Nav_view, text="Scan\nAll", height=3,
                 width=10, bg="orange", fg="black", font=("Arial", 10), command=lambda: sendMove(f'rover, scan'))
scanBtn.place(x=525, y=100)

scanEnBtn = Button(Nav_view, text="Enable", height=3,
                   width=10, bg="orange", fg="black", font=("Arial", 10), command=lambda: send('rover, eSonar'))
scanEnBtn.place(x=525, y=200)

scanDisBtn = Button(Nav_view, text="Disable", height=3,
                    width=10, bg="orange", fg="black", font=("Arial", 10), command=lambda: send('rover, dSonar'))
scanDisBtn.place(x=525, y=300)

################# VISION VIEW ########################################
camSpeed = Label(cam_view, text=f"Speed = MED", bg="black",
                 fg="white", font=("Arial", 15))
camSpeed.place(x=475, y=20)
cLowBtn = Button(cam_view, text="LOW", height=2,
                 width=5, bg="orange", fg="black", font=("Arial", 8), command=lambda: setCamSpeed(f'rover, cam-clow'))
cLowBtn.place(x=430, y=70)
cMedBtn = Button(cam_view, text="MED", height=2,
                 width=5, bg="orange", fg="black", font=("Arial", 8), command=lambda: setCamSpeed(f'rover, cam-cmed'))
cMedBtn.place(x=500, y=70)
cHiBtn = Button(cam_view, text="HI", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 8), command=lambda: setCamSpeed(f'rover, cam-chi'))
cHiBtn.place(x=570, y=70)

cUpBtn = Button(cam_view, text="Up", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: send(f'rover, cam-cup'))
cUpBtn.place(x=475, y=190)
cdnBtn = Button(cam_view, text="Down", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: send(f'rover, cam-cdown'))
cdnBtn.place(x=475, y=310)
cLfBtn = Button(cam_view, text="Left", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: send(f'rover, cam-cleft'))
cLfBtn.place(x=410, y=250)
cRtBtn = Button(cam_view, text="Right", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: send(f'rover, cam-cright'))
cRtBtn.place(x=540, y=250)

cLeftBtn = Button(cam_view, text="Look\nLeft", height=2,
                  width=5, bg="orange", fg="black", font=("Arial", 15), command=lambda: send(f'rover, cam-pLeft'))
cLeftBtn.place(x=25, y=300)
cFrontBtn = Button(cam_view, text="Look\nFront", height=2,
                   width=5, bg="orange", fg="black", font=("Arial", 15), command=lambda: send(f'rover, cam-pFront'))
cFrontBtn.place(x=125, y=300)
cRightBtn = Button(cam_view, text="Look\nRight", height=2,
                   width=5, bg="orange", fg="black", font=("Arial", 15), command=lambda: send(f'rover, cam-pRight'))
cRightBtn.place(x=225, y=300)


################# PILOT VIEW ########################################

roverSpeed = Label(Pilot_view, text=f"Speed = {step}", bg="black",
                   fg="white", font=("Arial", 15))
roverSpeed.place(x=200, y=115)

pUpBtn = Button(Pilot_view, text="Forward", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: sendMove(f'rover, move-f-'))
pUpBtn.place(x=130, y=170)
pdnBtn = Button(Pilot_view, text="Back", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: sendMove(f'rover, move-b-'))
pdnBtn.place(x=130, y=290)
pLfBtn = Button(Pilot_view, text="Left", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: sendMove(f'rover, move-l-'))
pLfBtn.place(x=65, y=230)
pRtBtn = Button(Pilot_view, text="Right", height=2,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: sendMove(f'rover, move-r-'))
pRtBtn.place(x=195, y=230)

pLeftBtn = Button(Pilot_view, text="Rotate\nLeft", height=2,
                  width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: sendMove(f'rover, move-rl-'))
pLeftBtn.place(x=20, y=320)
pFrontBtn = Button(Pilot_view, text="Rotate\nRight", height=2,
                   width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: sendMove(f'rover, move-rr-'))
pFrontBtn.place(x=230, y=320)
pStopBtn = Button(Pilot_view, text="STOP", height=2,
                  width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: sendMove(f'rover, move-s-s'))
pStopBtn.place(x=550, y=320)

pseedLabel = Label(Pilot_view, text="1000                    Speed Select                    13000", bg="black",
                   fg="white", font=("Arial", 10))
pseedLabel.place(x=20, y=0)
pspeed = Scale(Pilot_view, bg="orange", fg="black",
               font=("Arial", 10), from_=1000, to=13000, tickinterval=3000, width=35, length=300, orient=HORIZONTAL)
pspeed.place(x=20, y=25)
setBtn = Button(Pilot_view, text="Set", height=1,
                width=5, bg="orange", fg="black", font=("Arial", 10), command=lambda: setSpeed(f'{pspeed.get()}'))
setBtn.place(x=25, y=125)

SockThread = threading.Thread(target=SocketIn, args=())
SockThread.setDaemon(True)
SockThread.start()

send(name)

root.mainloop()
