#Imports
from time import sleep
import methods
txt = ''
with open('./Logo.txt') as file:
    txt = file.read()
    file.close()
#main func
Control = 0
while True:
    #start Msg
    if (Control < 1):
        print(txt)
        methods.PlayAudio('Hi')
    Control =+ 1
    sleep(.6)
    #get commands   
    methods.GetCommandList()
    #get input
    command_terminal = str(input())
    #in case you leave.
    
    #try executing command.
    try:
        if(command_terminal.lower() == 'leave'):
            methods.PlayAudio(command_terminal)
            break
        methods.PlayAudio(command_terminal)
    except:
        print('Error tracked -- either a bug or none ' + command_terminal + ' Command Found.')

