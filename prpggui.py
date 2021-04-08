from tkinter import *
import time

window = Tk()
window.geometry('500x500')
window.title('PRPG (ver.1.1)')
window.option_add("*Font",'맑은고딕 25')

#변수
weapon = 'nothing'
cash = 100
strength = 1
pig = 500
pigs = 500

def shopcommand():
    shopbtn.pack_forget()
    huntbtn.pack_forget()
    exitbtn.pack_forget()
    sexitbtn.pack()
    woodswordBtn.pack()
    stoneswordBtn.pack()
    IronswordBtn.pack()
    DiamondswordBtn.pack()
    cashlabel.config(text='Your cash:'+str(cash))
    cashlabel.pack()

def buywoodsword():
    global cash
    if cash >= 100:
        global weapon
        weapon = 'woodsword'
        cash = cash - 100
        cashlabel.config(text='Your cash:'+str(cash))
        cashlabel.pack()
    else:
        alertlabel.pack()
        time.sleep(2)
        alertlabel.pack_forget()
        cashlabel.config(text='Your cash:'+str(cash))
        cashlabel.pack()

def buystonesword():
    global cash
    if cash >= 500:
        global weapon
        weapon = 'stonesword'
        cash = cash - 500
        cashlabel.config(text='Your cash:'+str(cash))
        cashlabel.pack()
    else:
        alertlabel.pack()
        time.sleep(2)
        alertlabel.pack_forget()
        cashlabel.config(text='Your cash:'+str(cash))
        cashlabel.pack()

def buyironsword():
    global cash
    if cash >= 3000:
        global weapon
        weapon = 'ironsword'
        cash = cash - 3000
        cashlabel.config(text='Your cash:'+str(cash))
        cashlabel.pack()
    else:
        alertlabel.pack()
        time.sleep(2)
        alertlabel.pack_forget()
        cashlabel.config(text='Your cash:'+str(cash))
        cashlabel.pack()
def buydiamondsword():
    global cash
    if cash >= 6000:
        global weapon
        weapon = 'diamondsword'
        cash = cash - 6000
        cashlabel.config(text='Your cash:'+str(cash))
        cashlabel.pack()
    else:
        alertlabel.pack()
        time.sleep(2)
        alertlabel.pack_forget()
        cashlabel.config(text='Your cash:'+str(cash))
        cashlabel.pack()

def huntcommand():
    hexitbtn.pack()
    print(weapon)
    pig = 500
    huntlabel.config(text='You found a pig')
    huntlabel.pack()
    huntingbtn.pack()
    shopbtn.pack_forget()
    huntbtn.pack_forget()
    exitbtn.pack_forget()
    cashlabel.config(text='Your cash:'+str(cash))
    cashlabel.pack()

def huntexit():
    shopbtn.pack()
    huntbtn.pack()
    exitbtn.pack()
    woodswordBtn.pack_forget()
    stoneswordBtn.pack_forget()
    IronswordBtn.pack_forget()
    DiamondswordBtn.pack_forget()
    hexitbtn.pack_forget()
    huntlabel.pack_forget()
    huntingbtn.pack_forget()
    Piglabel.pack_forget()
    wlertlabel.pack_forget()
    cashlabel.config(text='Your cash:'+str(cash))
    cashlabel.pack()


def hitcommand():
    global weapon
    global pig
    global cash
    global pigs
    if weapon == 'woodsword':
        pig = pig - 20
        if pig <= 0:
            huntedalert.pack()
            Piglabel.config(text='You hunted Pig!')
            cash = cash + 250
            cashlabel.config(text='Your cash:'+str(cash))
            cashlabel.pack()
            pigs = pigs + 100
            pig = pigs
        else:
            Piglabel.config(text="Pig's hp:"+str(pig))
            Piglabel.pack()

    if weapon == 'stonesword':
        pig = pig - 100
        if pig <= 0:
            huntedalert.pack()
            Piglabel.config(text='You hunted Pig!')
            cash = cash + 250
            cashlabel.config(text='Your cash:'+str(cash))
            cashlabel.pack()
            pigs = pigs + 100
            pig = pigs
        else:
            Piglabel.config(text="Pig's hp:"+str(pig))
            Piglabel.pack()

    if weapon == 'ironsword':
        pig = pig - 150
        if pig <= 0:
            huntedalert.pack()
            Piglabel.config(text='You hunted Pig!')
            cash = cash + 250
            cashlabel.config(text='Your cash:'+str(cash))
            cashlabel.pack()
            pigs = pigs + 100
            pig = pigs
        else:
            Piglabel.config(text="Pig's hp:"+str(pig))
            Piglabel.pack()
            
    if weapon == 'diamonesword':
        pig = pig - 250
        if pig <= 0:
            huntedalert.pack()
            Piglabel.config(text='You hunted Pig!')
            cash = cash + 250
            cashlabel.config(text='Your cash:'+str(cash))
            cashlabel.pack()
            pigs = pigs + 100
            pig = pigs
        else:
            Piglabel.config(text="Pig's hp:"+str(pig))
            Piglabel.pack()
            
    else:
        wlertlabel.pack()

def sexitcommand():
    shopbtn.pack()
    huntbtn.pack()
    exitbtn.pack()
    woodswordBtn.pack_forget()
    stoneswordBtn.pack_forget()
    IronswordBtn.pack_forget()
    DiamondswordBtn.pack_forget()
    sexitbtn.pack_forget()

def exitc():
    exit()
        

        

shopbtn = Button(window, text='Shop', command=shopcommand)
shopbtn.pack()

huntbtn = Button(window, text='Hunt', command=huntcommand)
huntbtn.pack()

huntingbtn = Button(window, text='Hit', command=hitcommand)

sexitbtn = Button(window, text='Exit', command=sexitcommand)

woodswordBtn = Button(window, text='Wood Sword: 100 cash', command=buywoodsword)
stoneswordBtn = Button(window, text='Stone Sword: 500 cash', command=buystonesword)
IronswordBtn = Button(window, text='Iron Sword: 3000 cash', command=buyironsword)
DiamondswordBtn = Button(window, text='Diamond Sword: 6000 cash', command=buydiamondsword)

alertlabel = Label(window)
alertlabel.config(text='You do not have enought cash')

wlertlabel = Label(window)
wlertlabel.config(text='You do not have weapon')

huntlabel = Label(window)
huntlabel.config(text='')

Piglabel = Label(window)
Piglabel.config(text="Pig's hp:"+str(pig))

huntedalert = Label(window)
huntlabel.config(text='You hunted a Pig!')

exitbtn = Button(window)
exitbtn.config(text='exit',command=exitc)
exitbtn.pack()

hexitbtn = Button(window)
hexitbtn.config(text='exit',command=huntexit)

cashlabel = Label(window)
cashlabel.config(text='Your cash:'+str(cash))

window.mainloop()
    
 