from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO 
import time
from threading import *
import datetime

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17,GPIO.OUT)
pwm = GPIO.PWM(17,100)
GPIO.setup(20,GPIO.IN)

killCommand = False
stop = 0
pwm.start(stop)

def threadMaintanence():
    stopEverything()
    if t2.is_alive():
        print("thread2 stopped")
        t2.stop()
    t1.start()
    print("thread1 started")

def threadCycle():
    stopEverything()
    if t1.is_alive():
        print("thread1 stopped")
        t1.stop()
    t2.start()
    print("thread2 started")


#cA true keeps cycle running otherwise turns off motor if
#in maintanence mode
def maintanence():
    global killCommand
    killCommand =False
    #setup motor to go up
    if GPIO.input(20) == GPIO.LOW:
        rotate(.50)
        print("motor moving up")
    while GPIO.input(20) == GPIO.LOW and not killCommand:
        #wait
        time.sleep(.25)
        
    #stop motor
    print("motor stopped")
    rotate(0)
    if t1.is_alive():
        print("thread1 stopped")
        t1.kill()
        
def cycle():
    #go to maintanence location
    maintanence()
    #go to top plant
    now = time.time()
    rotate(-.5)
    print("motor moving down")
    later = time.time()
    difference = later - now
    while  difference < 2 and not killCommand:
        #wait
        time.sleep(.25)
        later = time.time()
        difference = later - now
        print("diff = " + str(difference))
    rotate(0)
    if t2.is_alive():
        print("thread2 stopped")
        t2.kill()
    #go to bottom plant
    #go to top plant
    #repeat
    
def on_closing():
    print("cleanup")
    stopEverything()
    time.sleep(1)
    GPIO.cleanup()
    global root
    root.destroy()
    
def stopEverything():
    global killCommand
    killCommand = True
    
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
    
t1=Thread(target=maintanence)
t2=Thread(target=cycle)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Maintenance", command=threadMaintanence).grid(column=0, row=0)
ttk.Button(frm, text="Cycle", command=threadCycle).grid(column=1, row=0)
ttk.Button(root, text="Quit", command=on_closing)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()



