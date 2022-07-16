#imports
from pygame import mixer
import json, time
#vars
Commands = ''
mixer.init()
with open('./Commands.json') as json_file:
    Commands = json.load(json_file)
    json_file.close()
Command_List = [
        "Commands",
        "",
        "-------------",
        "1. Leave",
        "2. Creddits",
        "-------------"
        ]
def GetAudioCommand(Command:str):
    for Index in Commands:
        if(Index["Name"] == Command):
            return Index["Mp3"], Index["Msg"]
    return ''
def GetCommandList():
    for i in Command_List:
        print(i)
    return ''
def PlayAudio(cmd:str):
    AUDIO,MSG = GetAudioCommand(cmd)
    mixer.music.load(AUDIO)
    mixer.music.play()
    print(MSG)
    time.sleep(2)
    return ''

    
