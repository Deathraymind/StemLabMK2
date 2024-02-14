import RPi.GPIO as GPIO 
import time 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17,GPIO.OUT)
pwm = GPIO.PWM(17,100)

pwm.start(14.1)

print("positive numbers are CW, 0 = N, negative numbers are CCW")
direct = float(input("Please enter a number from -1 to 1"))
t = int(input ("How long as an integer?"))



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
        pwm.ChangeDutyCycle(14.1)
        print ("pwm = 14.1")



rotate(direct)
time.sleep(t)
rotate(0)

GPIO.cleanup()

    
    
