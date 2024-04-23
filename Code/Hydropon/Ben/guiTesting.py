from guizero import App, Text, PushButton
import time
import threading

'''
object = threading.Thread(target = function)
object.start()
'''

def poopoo():
    print("haha")
    button.disable()
    time.sleep(2)
    button.enable()

def poopooThread():
    tempThread = threading.Thread(target = poopoo)
    tempThread.start()

def peepee():
    print("haha!")

app = App(title = "Hello World!")
button = PushButton(app, command = poopooThread, align = "left", width = 10, height = 5, text = "shit ass")

welcomeMsg = Text(app, text = "Hello World!", size = 40)
secondButton = PushButton(app, command = peepee)
app.display()