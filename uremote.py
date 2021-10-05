from tkinter import *
import serial
import time
import os
import platform


hud = Tk()
root = Tk()


root.configure(background='gray40')
root.title("_Mantis_Blade_")
root.geometry('800x480+0+0')

hud.configure(background='black')
hud.title("_Mantis_Blade_HUD")
hud.geometry('700x480+800+0')


text = ""

if platform.system() == "Linux":
    port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
    root.config(cursor="none")
    root.attributes('-fullscreen', True)
    hud.attributes('-fullscreen', True)
elif platform.system() == "Windows":
    #port = serial.Serial("COM7", baudrate=115200, timeout=3.0)
    pass


def Config():
    textBox.insert(END, "Config")
    textBox.yview(END)
    my_frame.place_forget()
    btn.place_forget()
    new_frame.place(x=40, y=60, width=300, height=200)
    btn2.place(x=700, y=200)
    Display("Configuation ")


def Dashboard():
    textBox.insert(END, "Dashboard")
    textBox.yview(END)
    new_frame.place_forget()
    btn2.place_forget()
    btn.place(x=700, y=350)
    my_frame.place(x=40, y=60)
    Display("Dashboard      ")


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


btn = Button(root, height=2, width=8,
             text="Config", bg="red", command=Config)
btn.place(x=700, y=350)


btn5 = Button(root, text="HUD_bat View", bg="blue", command=BAThud)
btn5.place(x=550, y=400)

btn6 = Button(root, text="HUD_EXO View", bg="blue", command=EXOhud)


btn4 = Button(root, text="clear", bg="blue", command=Clear)
btn4.place(x=40, y=440)

######################### HUD WIDGETS ############################

hudLabel = Label(hud, text="HUD view", bg="black", fg="orange")
hudLabel.place(x=20, y=20)

#################### HUD EXO FRAME ###############################

EXO_Stats = LabelFrame(hud, text=" EXO_Stats ",
                       width=400, height=300, bg="black", fg="orange")
EXO_Stats.place(x=15, y=100)

cMode = Label(EXO_Stats, text="Mode = armed",
              bg="red", fg="black", font=("Arial", 15))
cMode.place(x=20, y=10)

bladePos = Label(EXO_Stats, text="Pos = 100", bg="black",
                 fg="orange", font=("Arial", 15))
bladePos.place(x=20, y=55)

PID_Config = LabelFrame(EXO_Stats, text=" PID_Config ",
                        width=175, height=200, bg="black", fg="orange")
PID_Config.place(x=220, y=75)

P_val = Label(PID_Config, text="P = 4", bg="black",
              fg="white", font=("Arial", 15))
P_val.place(x=5, y=10)
I_val = Label(PID_Config, text="I = 1", bg="black",
              fg="white", font=("Arial", 15))
I_val.place(x=5, y=40)
D_val = Label(PID_Config, text="D = 1", bg="black",
              fg="white", font=("Arial", 15))
D_val.place(x=5, y=70)


################### HUD BAT FRAME ##############################

BAT_Stats = LabelFrame(hud, text=" BAT_Stats ",
                       width=400, height=300, bg="black", fg="orange")
#BAT_Stats.place(x=20, y=100)

dBat = Label(BAT_Stats, text="Drive_pwr = 100 %",
             bg="gray8", fg="red", font=("Arial", 15))
dBat.place(x=20, y=10)

dBat1 = Label(BAT_Stats, text="Cell_1 = 4.1v",
              bg="gray8", fg="red", font=("Arial", 8))
dBat1.place(x=40, y=45)

dBat2 = Label(BAT_Stats, text="Cell_2 = 4.1v",
              bg="gray8", fg="red", font=("Arial", 8))
dBat2.place(x=40, y=65)

dBat3 = Label(BAT_Stats, text="Cell_3 = 4.1v",
              bg="gray8", fg="red", font=("Arial", 8))
dBat3.place(x=40, y=85)

dBat4 = Label(BAT_Stats, text="Cell_4 = 4.1v",
              bg="gray8", fg="red", font=("Arial", 8))
dBat4.place(x=40, y=105)

dBat_t = Label(BAT_Stats, text="DBat Temp = 25 C",
               bg="gray8", fg="red", font=("Arial", 15))
dBat_t.place(x=140, y=80)
cBat = Label(BAT_Stats, text="CTRL_pwr = 75 %",
             bg="gray8", fg="red", font=("Arial", 15))
cBat.place(x=20, y=175)

cBat_t = Label(BAT_Stats, text="CBat Temp = 20 C",
               bg="gray8", fg="red", font=("Arial", 15))
cBat_t.place(x=75, y=220)

################ HUD BATm FRAME #######################################

BAT_Stats_mini = LabelFrame(hud, text=" BAT_Stats ",
                            width=150, height=100, bg="black", fg="orange")
BAT_Stats_mini.place(x=500, y=20)

dBat = Label(BAT_Stats_mini, text="Drive_pwr = 100",
             bg="red", fg="black", font=("Arial", 10))
dBat.place(x=10, y=10)
cBat = Label(BAT_Stats_mini, text="CTRL_pwr = 75",
             bg="red", fg="black", font=("Arial", 10))
cBat.place(x=10, y=40)


root.mainloop()
hud.mainloop()
