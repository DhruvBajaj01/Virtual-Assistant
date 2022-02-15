import os
import subprocess as sp

paths = {
    'notepad': "C:/Program Files (x86)/Notepad++/notepad++.exe",
    'discord': "C:\\Users\\Dhruv Bajaj\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe"
   
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.run('start microsoft.windows.Calculator:', shell=True)


