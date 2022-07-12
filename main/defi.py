
import playsound
from playsound import playsound

#comandos de ejecucion de audio

def welcoming():
    print("Hello, is nice to meet you.")
    playsound('./hello is nice to meet you.mp3')

def leaving():
    print("I'll miss you. ") 
    playsound('./goodbye.mp3') 
    

def suddenlyquit():
    print("¿did I did something wrong?")
    playsound('./suddenlyquit.mp3')

def easteregg():
    print("you are my best friend forever.")
    playsound('./easteregg.mp3')

#fuciones de interaccion que requieren del frontend
def welcoming2():
    print("¿How can I help you?")
    