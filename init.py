from API import * 
# Imports {
    # sys 
    # textToSpeech {speech_recognition as sr}
    # BOOT {os, pandas as pd, PasswordGenerator}
    # BootMails {SendMails}
    # OpenFile
# }

# Boot()


def Start():
    print("Go ahead! I'm listening ...")
    say("Go ahead! I'm listening ...")
    text = speak()
    # text = "scan"
    print(text)
    Command(text)
    
if __name__ == '__main__':
    # print("Write `python mainboard.py` to run from the GUI Screen...")
    # exit()
    Boot()
    while True:
        c = input("Enter space to start or any other character to exit: ")
        if c == " ":
            Start()
        elif c == "admin":
            AdminLog()
        elif c == "":
            exit()
            