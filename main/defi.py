#Imports

import playsound
from playsound import playsound

#comands for audio execution

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

#extra def's
def credits():
    x=["https://www.youtube.com/watch?v=W2TE0DjdNqI","https://www.youtube.com/watch?v=HAIDqt2aUek","https://www.youtube.com/watch?v=0LRdp9Dp_n4"]
    print("Our inspiration:",x)



#interactive functions that needs frontend support
def welcoming2():
    print("¿How can I help you?")

    x=input()

    if x=="leave":
            leaving()

    
