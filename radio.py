#!/usr/bin/python3
#Reference code obtained from "https://www.raspberrypi.org/forums/viewtopic.php?t=53680" by user: LinuxCircle
import smbus as smbus 
import subprocess
import curses
import curses.textpad
import time
import alsaaudio
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

#create variables and set default values
i2c = smbus.SMBus(1) # newer version RASP (512 megabytes)
i2c_address = 0x60
frequency = 100.1
volume = 50

HEIGHT = 1000
WIDTH = 1600
FREQUENZ = '104.1'
SENDER = 'Life-Radio'
RIHEIGHT = 300
RIWIDTH = 300

muted = False

#set names of radio-channels
S1 = 'Ö3'
S2='Kronehit'
S3='Bayern-3'
S4='Radio-Austria'
S5='Life-Radio'
S6='Radio-Tirol'

FCOLOR = '#526372'
F1color = '#424242'
TextColor = '#FAFAFA'
BUcolor = '#59bfff'

#define method to initalize the hardware
def init_radio(address):
    """initialize hardware"""
    i2c.write_quick(address)
    time.sleep(0.1)

#define method to set frequency
def set_freq(address, freq):
    """set Radio to specific frequency"""
    freq14bit = int (4 * (freq * 1000000 + 225000) / 32768) # Frequency distribution for two bytes (according to the data sheet)
    freqH = freq14bit>>8 #int (freq14bit / 256)
    freqL = freq14bit & 0xFF

    data = [0 for i in range(4)] # Descriptions of individual bits in a byte - viz.  catalog sheets
    init = freqH # freqH # 1.bajt (MUTE bit; Frequency H)  // MUTE is 0x80
    data[0] = freqL # 2.bajt (frequency L)
    data[1] = 0xB0 #0b10110000 # 3.bajt (SUD; SSL1, SSL2; HLSI, MS, MR, ML; SWP1)
    data[2] = 0x10 #0b00010000 # 4.bajt (SWP2; STBY, BL; XTAL; smut; HCC, SNC, SI)
    data[3] = 0x00 #0b00000000 # 5.bajt (PLREFF; DTC; 0; 0; 0; 0; 0; 0)
    try:
      i2c.write_i2c_block_data (address, init, data) # Setting a new frequency to the circuit
      print("Frequency set to: " + str(freq))
    except IOError:
      subprocess.call(['i2cdetect', '-y', '1'])

#define method to change volume
def changeVolume():
    global volume
    m.setvolume(volume)
    volumeText.set(str(volume))
    volumeScale.set(volume)

#define method to change volume by moving scale    
def ScaleChangeVolume():
    global volume
    volume = volumeScale.get()
    m.setvolume(volume)
    volumeText.set(str(volume))

#define methods for buttons to change volume manually
def setVolDown1():
    global volume
    volume -= 1
    changeVolume()
    
def setVolUp1():
    global volume
    volume += 1
    changeVolume()

#define methods for buttons to change frequency
def setDown1():
    global frequency
    frequency -= 1
    set_freq(i2c_address, frequency)
    setLabel()
    frequenzLabel.configure(image='')    
    time.sleep(0.1)
    
def setDown01():
    global frequency
    frequency -= 0.1
    set_freq(i2c_address, frequency)
    setLabel()
    frequenzLabel.configure(image='')
    time.sleep(0.1)
    
def setUp01():
    global frequency
    frequency += 0.1
    set_freq(i2c_address, frequency)
    setLabel()
    frequenzLabel.configure(image='')
    time.sleep(0.1)

def setUp1():
    global frequency
    frequency += 1
    set_freq(i2c_address, frequency)
    setLabel()
    frequenzLabel.configure(image='')
    time.sleep(0.1)

#define methods to play shortcut-channels
def setOe3():
    global frequency
    frequency = 99.7
    set_freq(i2c_address,frequency)
    setLabel()
    frequenzLabel.configure(image=b1photo)
    
def setKronehit():
    global frequency
    frequency = 107.4
    set_freq(i2c_address,frequency)
    setLabel()
    frequenzLabel.configure(image=b2photo)

def setBayern3():
    global frequency
    frequency = 96.4
    set_freq(i2c_address,frequency)
    setLabel()
    frequenzLabel.configure(image=b3photo)

def setRadioAustria():
    global frequency
    frequency = 104.0
    set_freq(i2c_address,frequency)
    setLabel()
    frequenzLabel.configure(image=b4photo)

def setLifeRadio():
    global frequency
    frequency = 89.9
    set_freq(i2c_address,frequency)
    setLabel()
    frequenzLabel.configure(image=b5photo)
    
def setRadioTirol():
    global frequency
    frequency = 94.7
    set_freq(i2c_address,frequency)
    setLabel()
    frequenzLabel.configure(image=b6photo)

#define method to mute radio
def muteRadio():
    global muted
    global volume
    if(muted == True):
        volume = 50
        changeVolume()
        muted = False
    else:
        volume = 0
        changeVolume()
        muted = True

#define method to format frequency (in order to avoid long decimal numbers
def setLabel():
    frequencyText.set("{:.1f}".format(frequency))

    
#call method to initalize radio
init_radio(i2c_address)

#get the mainmixer and set volume
m = alsaaudio.Mixer() 
m.setvolume(volume)


while True:
    #create the root
    root = Tk()
    
    #create string-variables
    frequencyText = StringVar()
    frequencyText.set(str(frequency))
    
    volumeText = StringVar()
    volumeText.set(str(volume))

    #create font
    functionFont = font.Font(size=30)
    
    #create canvas
    canvas = Canvas(root, height = HEIGHT, width = WIDTH)
    canvas.pack()
    
    #get and set background image
    background_image = Image.open('/home/pi/Documents/radio_background.jpg')
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label(root,image=background_photo)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)

    #get images for Buttons
    b1image= Image.open('/home/pi/Documents/oe3.jpg')
    b1photo = ImageTk.PhotoImage(b1image)

    b2image= Image.open('/home/pi/Documents/kronehit.jpg')
    b2photo = ImageTk.PhotoImage(b2image)

    b3image= Image.open('/home/pi/Documents/bayern3.jpg')
    b3photo = ImageTk.PhotoImage(b3image)

    b4image= Image.open('/home/pi/Documents/radioAustria.jpg')
    b4photo = ImageTk.PhotoImage(b4image)

    b5image= Image.open('/home/pi/Documents/lifeRadio.jpg')
    b5photo = ImageTk.PhotoImage(b5image)

    b6image= Image.open('/home/pi/Documents/radioTirol.jpg')
    b6photo = ImageTk.PhotoImage(b6image)

    #build frames
    frameOben = Frame(root, bg=F1color)
    frameOben.place(relx = 0.5, rely =0.025,relwidth = 0.25,relheight=0.3,anchor = 'n')

    frameMitte = Frame(root, bg= F1color)
    frameMitte.place(relx = 0.5, rely =0.35,relwidth = 0.6,relheight=0.2,anchor = 'n')

    frameUnten = Frame(root, bg = F1color)
    frameUnten.place(relx = 0.5, rely =0.6,relwidth = 0.8,relheight=0.3,anchor = 'n')
    
    frameVolume = Frame(root, bg = F1color)
    frameVolume.place(relx = 0.85, rely =0.025,relwidth = 0.35,relheight=0.3,anchor = 'n')
    

    #build label to show frequency
    frequenzLabel = Label(frameOben,textvariable=frequencyText,fg = TextColor, bg=F1color,font=('Arial',95))
    frequenzLabel.place(relx = 0.5, rely =0.1,relwidth = 0.7,relheight=0.7,anchor = 'n')

    #senderLabel = Label(frameOben,text = SENDER,fg = TextColor,bg=F1color,font=('Arial',55))
    #senderLabel.place(relx = 0.5, rely =0.8,relwidth = 0.9,relheight=0.2,anchor = 'n')
    
    #build label to show volume
    volumeLabel = Label(frameVolume, textvariable = volumeText, fg = TextColor, bg = F1color, font = ('Arial',95))
    volumeLabel.place(relx = 0.4, rely =0.1,relwidth = 0.8,relheight=0.7,anchor = 'n')
    
    #build scale to change volume
    volumeScale = Scale(frameVolume, from_=0, to= 100, orient = VERTICAL, width = 50, variable = volume, fg = TextColor, bg = F1color, font = ('Arial',25), command=lambda x:ScaleChangeVolume())
    volumeScale.place(relx = 0.8, rely = 0.05,relwidth = 0.2, relheight = 0.9, anchor = 'n')
    #set volume for the first time
    volumeScale.set(volume)

    #build buttons to adjust volume
    volMinus1Button=Button(frameVolume,text='-',font=functionFont,bg = FCOLOR,fg=TextColor, command=lambda:setVolDown1())
    volMinus1Button.place(relx = 0.25, rely =0.7,relwidth = 0.25,relheight=0.30,anchor = 'n')

    volPlus1Button=Button(frameVolume,text='+',font=functionFont,bg = FCOLOR,fg=TextColor, command=lambda:setVolUp1())
    volPlus1Button.place(relx = 0.55, rely =0.7,relwidth = 0.25,relheight=0.30,anchor = 'n')

    #build buttons to adjust frequency
    minus1Button=Button(frameMitte,text='<<',font=functionFont,bg = FCOLOR,fg=TextColor, command=lambda:setDown1())
    minus1Button.place(relx = 0.1, rely =0.1,relwidth = 0.15,relheight=0.8,anchor = 'n')

    minus01Button=Button(frameMitte,text='<',font=functionFont,bg = FCOLOR,fg=TextColor, command=lambda:setDown01())
    minus01Button.place(relx = 0.3, rely =0.1,relwidth = 0.15,relheight=0.8,anchor = 'n')

    plus01Button = Button(frameMitte,text='>',font=functionFont,bg = FCOLOR,fg=TextColor, command=lambda:setUp01())
    plus01Button.place(relx = 0.7, rely =0.1,relwidth = 0.15,relheight=0.8,anchor = 'n')

    plus1Button = Button(frameMitte,text='>>',font=functionFont,bg = FCOLOR,fg=TextColor, command=lambda:setUp1())
    plus1Button.place(relx = 0.9, rely =0.1,relwidth = 0.15,relheight=0.8,anchor = 'n')

    #build pause(mute) button
    pauseButton = Button(frameMitte,text='||',font=functionFont,bg = FCOLOR,fg=TextColor, command=lambda:muteRadio())
    pauseButton.place(relx = 0.5, rely =0.1,relwidth = 0.15,relheight=0.8,anchor = 'n')

    #build shortcut buttons for favorite channels
    S1Button =  Button(frameUnten,image= b1photo, command=lambda:setOe3())
    S1Button.place(relx = 0.1, rely =0.2,width = 220,height=220,anchor = 'n')

    S2Button =  Button(frameUnten,image= b2photo, command=lambda:setKronehit())
    S2Button.place(relx = 0.26, rely =0.2,width = 220,height=220,anchor = 'n')

    S3Button =  Button(frameUnten,image= b3photo,command=lambda:setBayern3())
    S3Button.place(relx = 0.42, rely =0.2,width = 220,height=220,anchor = 'n')

    S4Button =  Button(frameUnten,image= b4photo, command=lambda:setRadioAustria())
    S4Button.place(relx = 0.58, rely =0.2,width = 220,height=220,anchor = 'n')

    S5Button =  Button(frameUnten,image= b5photo, command=lambda:setLifeRadio())
    S5Button.place(relx = 0.74, rely =0.2,width = 220,height=220,anchor = 'n')

    S6Button =  Button(frameUnten,image= b6photo, command=lambda:setRadioTirol())
    S6Button.place(relx = 0.9, rely =0.2,width = 220,height=220,anchor = 'n')


    root.mainloop()
