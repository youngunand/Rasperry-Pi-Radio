from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk


HEIGHT = 1000
WIDTH = 1600
FREQUENZ = '104.1'
SENDER = 'Life-Radio'

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


root = Tk()
functionFont = font.Font(size=30)

canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = Image.open('/home/andi/Dokumente/Coding/Python/Raspi-Radio/radio_background.jpg')
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root,image=background_photo)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

#Images für Buttons erstellen
b1image= Image.open('/home/andi/Dokumente/Coding/Python/Raspi-Radio/oe3.jpg')
b1photo = ImageTk.PhotoImage(b1image)

b2image= Image.open('/home/andi/Dokumente/Coding/Python/Raspi-Radio/kronehit.jpg')
b2photo = ImageTk.PhotoImage(b2image)

b3image= Image.open('/home/andi/Dokumente/Coding/Python/Raspi-Radio/bayern3.jpg')
b3photo = ImageTk.PhotoImage(b3image)

b4image= Image.open('/home/andi/Dokumente/Coding/Python/Raspi-Radio/radioAustria.jpg')
b4photo = ImageTk.PhotoImage(b4image)

b5image= Image.open('/home/andi/Dokumente/Coding/Python/Raspi-Radio/lifeRadio.jpg')
b5photo = ImageTk.PhotoImage(b5image)

b6image= Image.open('/home/andi/Dokumente/Coding/Python/Raspi-Radio/radioTirol.jpg')
b6photo = ImageTk.PhotoImage(b6image)

#Frames-baúen
frameOben = Frame(root, bg=F1color)
frameOben.place(relx = 0.5, rely =0.025,relwidth = 0.2,relheight=0.3,anchor = 'n')

frameMitte = Frame(root, bg= F1color)
frameMitte.place(relx = 0.5, rely =0.35,relwidth = 0.6,relheight=0.2,anchor = 'n')

frameUnten = Frame(root, bg = F1color)
frameUnten.place(relx = 0.5, rely =0.6,relwidth = 0.8,relheight=0.3,anchor = 'n')

#Obere Lebel für Frequenz/Sender bauen
frequenzLabel = Label(frameOben,text = FREQUENZ,fg = TextColor, bg=F1color,font=('Arial',105))
frequenzLabel.place(relx = 0.5, rely =0.1,relwidth = 1,relheight=0.7,anchor = 'n')

senderLabel = Label(frameOben,text = SENDER,fg = TextColor,bg=F1color,font=('Arial',55))
senderLabel.place(relx = 0.5, rely =0.8,relwidth = 1,relheight=0.2,anchor = 'n')

minus1Button=Button(frameMitte,text='<<',font=functionFont,bg = FCOLOR,fg=TextColor)
minus1Button.place(relx = 0.1, rely =0.1,relwidth = 0.15,relheight=0.8,anchor = 'n')

minus01Button=Button(frameMitte,text='<',font=functionFont,bg = FCOLOR,fg=TextColor)
minus01Button.place(relx = 0.3, rely =0.1,relwidth = 0.15,relheight=0.8,anchor = 'n')

pauseButton = Button(frameMitte,text='||',font=functionFont,bg = FCOLOR,fg=TextColor)
pauseButton.place(relx = 0.5, rely =0.1,relwidth = 0.15,relheight=0.8,anchor = 'n')

plus01Button = Button(frameMitte,text='>',font=functionFont,bg = FCOLOR,fg=TextColor)
plus01Button.place(relx = 0.7, rely =0.1,relwidth = 0.15,relheight=0.8,anchor = 'n')

plus1Button = Button(frameMitte,text='>>',font=functionFont,bg = FCOLOR,fg=TextColor)
plus1Button.place(relx = 0.9, rely =0.1,relwidth = 0.15,relheight=0.8,anchor = 'n')

#Shortcut-Buttons für Sender bauen

S1Button =  Button(frameUnten,image= b1photo)
S1Button.place(relx = 0.1, rely =0.2,width = 220,height=220,anchor = 'n')

S2Button =  Button(frameUnten,image= b2photo)
S2Button.place(relx = 0.26, rely =0.2,width = 220,height=220,anchor = 'n')

S3Button =  Button(frameUnten,image= b3photo)
S3Button.place(relx = 0.42, rely =0.2,width = 220,height=220,anchor = 'n')

S4Button =  Button(frameUnten,image= b4photo)
S4Button.place(relx = 0.58, rely =0.2,width = 220,height=220,anchor = 'n')

S5Button =  Button(frameUnten,image= b5photo)
S5Button.place(relx = 0.74, rely =0.2,width = 220,height=220,anchor = 'n')

S6Button =  Button(frameUnten,image= b6photo)
S6Button.place(relx = 0.9, rely =0.2,width = 220,height=220,anchor = 'n')




root.mainloop()