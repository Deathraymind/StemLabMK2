from guizero import App, Text, PushButton
import RPi.GPIO as GPIO 
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
# motor pin
GPIO.setup(17,GPIO.OUT)
pwm = GPIO.PWM(17,100)
# switch pin
GPIO.setup(20, GPIO.IN)

pwm.start(14.1)

cycleMode = False
UpTrueDownFalse = False
numOfCycles = 0

"""
global cycleMode
global UpTrueDownFalse
global numOfCycles
"""

def rotate (speed):
    if speed < 0:
        #output range to motor 14.2 - 19.6 stop to full
        #input range from user 0 - (-1)
        pwm.ChangeDutyCycle(14.2 + 5.6*(-speed))
        #print ("pwm = " + str(14.2 + 5.6*(-speed)))
    elif speed > 0:
        #output 10.2-14 max to stop CW
        #input 0 - 1 max
        pwm.ChangeDutyCycle(14 - 3.8*speed)
        #print ("pwm = " + str(14 - 3.8*speed))
    else:
        pwm.ChangeDutyCycle(14.1)
        #print ("pwm = 14.1")

def rotationRoutine(speedR, rotateTime):
    rotate(speedR)
    time.sleep(rotateTime)
    rotate(0)

'''
object = threading.Thread(target = function)
object.start()
'''


def exitMaintenASS():
    #declares global variables
    global cycleMode
    global UpTrueDownFalse
    global numOfCycles
    #sets global variables to their "default" states
    cycleMode = True
    UpTrueDownFalse = False
    numOfCycles = 0
    #prevents user from inputting anything
    InMainButton.disable()
    ExitMainButton.disable()
    #moves the pulley down a set distance.
    rotationRoutine(-0.3, 5)
    #prevents this function from being accessed again
    ExitMainButton.disable()
    #allows the accessing of maintenace mode
    InMainButton.enable()

def enterMaintenass():
    #declares global variables
    global cycleMode
    global UpTrueDownFalse
    global numOfCycles
    #sets global variables to their default states.
    #redundant, but don't think they'll cause errors.
    cycleMode = False
    UpTrueDownFalse = False
    numOfCycles = 0
    #prevents user from inputting anything
    InMainButton.disable()
    ExitMainButton.disable()
    #i is a debugging variable.
    i = 0
    #continues until switch is pressed.
    while True:
        #GPIO.LOW indicates the switch has not been activated.
        if GPIO.input(20) == GPIO.LOW:
            #moves a set distance from 0.1 seconds.
            rotationRoutine(0.3, 0.1)
            #debugging purposes.
            print("switch low")
            print(i)
            i = i+1
        #indicates that switch has been pressed.
        if GPIO.input(20) == GPIO.HIGH:
            #debugging function.
            print("breaked")
            #ends movement.
            break
    #allows exit maintenace button to be accessed.
    ExitMainButton.enable()

def movementCycle():
    #declares global variables.
    global cycleMode
    global UpTrueDownFalse
    global numOfCycles
    """
    because this function is accessed regardless of if
    maintenace is on or off, so the function is placed in
    an if statement to prevent it from moving when
    maintenace mode is on.
    """
    if cycleMode:
        #debugging function.
        print("return True")
        #uses UpTrueDownFalse to govern movement up or down.
        if UpTrueDownFalse:
            rotationRoutine(0.3, 1)
        else:
            rotationRoutine(-0.3, 1)
        #adds 1 to cycle counter.
        Cycles = Cycles + 1
    #changes direction if 12 cycles are done.
    if numOfCycles == 12:
        UpTrueDownFalse = True
    #enters and exits maintenace mode if 24 cycles are done.
    elif numOfCycles == 24:
        enterMaintenass()
        exitMaintenASS()
    #debugging function.
    print("cycle Active")

#gui window is created as an object.
app = App(title = "Motor Controller")
#creates top msg
welcomeMsg = Text(app, text = "Motor Controller", size = 36)
#creates enter maintenace button
InMainButton = PushButton(app, command = enterMaintenass, width = 10, height = 5, text = "MaintenASS")
#creates exit maintenace button
ExitMainButton = PushButton(app, command = exitMaintenASS, width = 10, height = 5, text = "Leave MaintenASS")
#enters and exit maintenace mode in the case of a power outage.
enterMaintenass()
exitMaintenASS()
#repeats movementCycle() every 3600000 milliseconds, or hour.
app.repeat(3600000, movementCycle)
#actually displays the gui
app.display()

#last thing possible
GPIO.cleanup()

    
    
