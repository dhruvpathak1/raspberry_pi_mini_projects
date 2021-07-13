from gpiozero import LED
import RPi.GPIO as GPIO
import time
import tkinter

red = LED(17)
green = LED (27)



def ron():
    red.on()

def roff():
    red.off()

def gon():
    green.on()

def goff():
    green.off()

def blinkr():
    led = red
    for i in range(0,3):
        led.off()
        time.sleep(0.2)
        led.on()
        time.sleep(0.2)

def blinkg():
    led = green
    for i in range(0,3):
        led.off()
        time.sleep(0.2)
        led.on()
        time.sleep(0.2)

    
win = tkinter.Tk()
win.title('LED Panel')

b1 = tkinter.Button(win, text = 'On (Red)', bg='gold', command = ron).grid(row = 0, column = 0, padx = 15, pady = 15)
b4 = tkinter.Button(win, text = 'Off (Green)', bg='white', command = goff).grid(row = 1, column = 0, padx = 15, pady = 15)

b3 = tkinter.Button(win, text = 'Off (Red)', bg='white', command = roff).grid(row = 1, column = 1, padx = 15, pady = 15)
b2 = tkinter.Button(win, text = 'On (Green)', bg='gold', command = gon).grid(row = 0, column = 1, padx = 15, pady = 15)


b5 = tkinter.Button(win, text = 'Blink RED', bg = 'pink', command = blinkr).grid(row = 2, column = 0, padx = 15, pady = 15)
b6 = tkinter.Button(win, text = 'Blink GREEN', bg = 'lightgreen', command = blinkg).grid(row = 2, column = 1, padx = 15, pady = 15)

win.mainloop()


    
