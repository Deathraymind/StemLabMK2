from tkinter import *
from tkinter import ttk
import tkinter as tk
import RPi.GPIO as GPIO 
import time
from threading import *
import datetime

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17,GPIO.OUT)
pwm = GPIO.PWM(17,100)
GPIO.setup(20,GPIO.IN, pull_up_down=GPIO.PUD_UP)

killCommand = False
stop = 0
moving = False
pwm.start(stop)

def killCommand():
    global killCommand
    killCommand = True
    print("sent kill command")
    rotate(0)

def threadMoveUp():
    global moving
    global killCommand
    if moving:
        killCommand = True
        moving = False
    else:
        moving = True
        t3=Thread(target=moveUp)
        killCommand = False
        t3.start()
        print("thread3 started : " + str(current_thread()))
        
def threadMoveDown():
    global moving
    global killCommand
    if moving:
        killCommand = True
        moving = False
    else:
        moving = True
        t4=Thread(target=moveDown)
        killCommand = False
        t4.start()
        print("thread4 started : " + str(current_thread()))

def threadMaintanence():
    global moving
    global killCommand
    if moving:
        killCommand = True
        moving = False
        time.sleep(2)
    else:
        moving = True
        t3=Thread(target=moveUp)
        killCommand = False
        t3.start()
        print("thread3 started : " + str(current_thread()))

def threadCycle():
    global killCommand
    time.sleep(1)
    t2=Thread(target=cycle)
    killCommand = False
    t2.start()
    print("thread2 started : " + str(current_thread()))
    
def moveUp():
    global moving
    global killCommand
    if GPIO.input(20) == GPIO.LOW:
        rotate(-.75)
        print("motor moving up")
    while GPIO.input(20) == GPIO.LOW and not killCommand:
        #wait
        time.sleep(.1)
        #print(GPIO.input(20))
    #stop motor
    if killCommand == False:
        killCommand = True
        moving = False
    print("motor stopped")
    rotate(0)
    
def moveDown():
    global killCommand
    rotate(.50)
    print("motor moving down")
    while GPIO.input(20) == GPIO.HIGH and not killCommand:
        #wait
        time.sleep(.1)
    while GPIO.input(20) == GPIO.LOW and not killCommand:
        #wait
        time.sleep(.1)
    #stop motor
    print("motor stopped")
    rotate(0)
    
def cycle():
    global killCommand
    while not killCommand:
        #go to maintanence location
        moveUp()
        time.sleep(1)
        killCommand = False
        #go to top plant
        now = time.time()
        rotate(.5)
        #print("motor moving down")
        later = time.time()
        difference = later - now
        while  difference < 5 and not killCommand:
            #wait
            time.sleep(.1)
            later = time.time()
            difference = later - now
            #print("diff = " + str(difference))
            if killCommand:
                return
        rotate(0)
        #time.sleep(5)
        
        #go to bottom plant
        i = 0
        while i<21 and not killCommand:
            if killCommand:
                return
            i = i + 1
            rotate(.5)
            print("motor moving down " + str(i))
            now = time.time()
            later = time.time()
            difference = later - now
            while  difference < 1 and not killCommand:
                if killCommand:
                    return
                #wait
                time.sleep(.25)
                later = time.time()
                difference = later - now
                #print("diff = " + str(difference))
            rotate(0)
            print("motor not moving down")
            now = time.time()
            later = time.time()
            difference = later - now
            while  difference < 2057 and not killCommand:
            #while  difference < 2 and not killCommand:
                if killCommand:
                    return
            #wait
                time.sleep(1)
                later = time.time()
                difference = later - now
                #print("diff = " + str(difference))
        rotate(0)
        
        #go to top plant
        i = 0
        while i<18 and not killCommand:
            if killCommand:
                return
            i = i + 1
            rotate(-.75)
            print("motor moving up " + str(i))
            now = time.time()
            later = time.time()
            difference = later - now
            while  difference < 1 and not killCommand:
                if killCommand:
                    return
                #wait
                time.sleep(.25)
                later = time.time()
                difference = later - now
                #print("diff = " + str(difference))
            rotate(0)
            #print("motor not moving up")
            now = time.time()
            later = time.time()
            difference = later - now
            while  difference < 2400 and not killCommand:
            #while  difference < 2 and not killCommand:
                if killCommand:
                    return
                #wait
                time.sleep(1)
                later = time.time()
                difference = later - now
                #print("diff = " + str(difference))
    #repeat
    
def on_closing():
    global killCommand
    killCommand = True
    print("cleanup")
    time.sleep(1)
    GPIO.cleanup()
    global root
    root.destroy()
    
def rotate (speed):
    if speed < 0:
        #output range to motor 14.2 - 19.6 stop to full
        #input range from user 0 - (-1)
        pwm.ChangeDutyCycle(14.2 + 5.6*(-speed))
        print ("pwm = " + str(14.2 + 5.6*(-speed)))
    elif speed > 0:
        #output 10.2-14 max to stop CW
        #input 0 - 1 max
        pwm.ChangeDutyCycle(14 - 3.8*speed)
        print ("pwm = " + str(14 - 3.8*speed))
    else:
        pwm.ChangeDutyCycle(stop)
        print ("pwm = " + str(stop))

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
tk.Button(frm, text="Maintenance", command=threadMaintanence, width=45, height=11).grid(column=0, row=0)
tk.Button(frm, text="Cycle", command=threadCycle, width=45, height=11).grid(column=1, row=0)
tk.Button(frm, text="Move Up", command=threadMoveUp, width=45, height=11).grid(column=0, row=1)
tk.Button(frm, text="Move Down", command=threadMoveDown, width=45, height=11).grid(column=1, row=1)
ttk.Button(root, text="Quit", command=on_closing)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()