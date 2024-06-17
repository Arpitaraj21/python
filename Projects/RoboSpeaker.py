#  Robo Speaking

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Arpita")
    while True:
        x = input("Enter what you want to speak: ")
        if x.lower() == 'q':
            break
        speak(x)
