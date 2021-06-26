from os import read
import pyttsx3
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def welcome():
    print(f"            {bcolors.HEADER} OPTIONS {bcolors.ENDC}")
    print(f"             -------                ")
    print(f" {bcolors.OKBLUE} -- SAY SOMETHING (s) {bcolors.ENDC} \n {bcolors.OKGREEN} -- READ FROM A TXT FILE (r) {bcolors.ENDC} \n ")

"""
prompt the user and return the answers as a list
[OPTION, READ_SPEED, VOLUME_INPUT, SAVE ("y" or "n") ]
"""
def prompt():    
    option = input(f"{bcolors.BOLD} r or s? {bcolors.ENDC} ")

    read_speed = int(input(f" {bcolors.OKBLUE} Speed: {bcolors.ENDC} "))
    volume_input = float(input(f" {bcolors.OKBLUE} Volume : {bcolors.ENDC} "))
    save = input(f"{bcolors.OKBLUE} Save mp3? (y/n) ")

    return [option, read_speed, volume_input, save]


def init(option, read_speed, volume_input, save):
    engine = pyttsx3.init()

    engine.setProperty('rate', read_speed)
    engine.setProperty('volume', volume_input)

    if save == "y":
        save_file_name = input(f"{bcolors.OKBLUE} save as ... ") + '.mp3'

    if option == 'r':
        txt_file = input(f"file: ")
        try:
            f_handle = open(txt_file, 'r')
            text = f_handle.read()
            
            if save == 'y':                
                engine.save_to_file(text, save_file_name)
            engine.say(text)
            engine.runAndWait()

        except:
            print(f" {bcolors.WARNING} invalid input {bcolors.ENDC} ")

    elif option == 's':
        to_say = input("SAY: ")

        if save == 'y':
            engine.save_to_file(to_say, save_file_name)

        engine.say(to_say)
        engine.runAndWait()

# entry point to the app
def App():
    welcome()
    choices = prompt()
    init(choices[0], choices[1], choices[2], choices[3])

App()