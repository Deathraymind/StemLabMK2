import RPi.GPIO as GPIO 
import time 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(20,GPIO.IN)

lastState = True
while True:
    if (GPIO.input(20) == GPIO.HIGH): # and (lastState):
        print("a")
       # lastState = not(lastState)
    
    if GPIO.input(20) == GPIO.LOW:
        print("b")
        
      
