#Imports
import playsound
from playsound import playsound

#comands for audio execution

def welcoming():
    print("-Hello, is nice to meet you.")
    playsound('./hello is nice to meet you.mp3')

def leaving():
    print("-I'll miss you. ") 
    playsound('./goodbye.mp3') 
    
def suddenlyquit():
    print("-¿did I did something wrong?")
    playsound('./suddenlyquit.mp3')

def easteregg():
    print("-you are my best friend forever.")
    playsound('./easteregg.mp3')

#extra def's
def credits():
    x=['https://www.youtube.com/watch?v=W2TE0DjdNqI','https://www.youtube.com/watch?v=HAIDqt2aUek','https://www.youtube.com/watch?v=0LRdp9Dp_n4']
    print("-Our inspiration:",x,"...process done.")


#interactive functions that needs frontend support

def welcoming2():
    while True:
        print("-So, ¿how can i help you?")
        x=input()

        if x=="leave":
            leaving()
            break
        elif x=="commands":
            print("-For now I have just a few commands like this:")
            print("-leave: command to leave Koraii ")
            print("-credits: list of videos that are our inspiration.")
            print("-Information lost")
        elif x=="credits":
         credits()
        elif x=="you are a good girl":
            easteregg()
        else: 
            print("Sorry, ¿What did you said?")