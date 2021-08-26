import smtplib
import time

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('rate', 180)
engine.setProperty('voice', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#speech to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print('Recognizing..')
            Query = r.recognize_google(audio, language='en-in')
            print(f"user said:{Query}")
        except Exception as e:
            speak(' say that again')
            return "none"
        return Query

#to wish me
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak('Good morning sir...')
    elif hour>12 and hour<18:
        speak('Good afternoon sir...')
    else:
        speak('Good evening sir..')
    speak('I am clifford. Please tell me how can I help you..')

if __name__ == "__main__":

    wish()
    while True:
        query = takeCommand().lower()
         #logic building for task performing

        if 'open notepad' in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            speak('I have opened notepad for you sir')

        elif 'vs code' in query:
            vpath = "C:\\Users\\blogn\\AppData\\Local\\Programs\\Microsoft VS Code Insiders\\Code - Insiders.exe"
            speak('opening VS code')
            os.startfile(vpath)
            time.sleep(4.00)
            speak('I have opened VS code editor for you sir..')


        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while 1:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)

                if k==27:
                    break;

            cap.release()
            cv2.destroyAllWindows()

        elif 'play music' in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'ip address' in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'open stack overflow' in query:
            speak('opening stack overflow for you sir..')
            webbrowser.open('www.stackoverflow.com')
            time.sleep(2.00)
            speak('opened, now you can start copy pasting')

        elif 'open google' in query:
            speak('what do you want to search sir..')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'play songs on youtube' in query:
            speak('which song should i play sir..')
            song = takeCommand().lower()
            speak(f"playing {song} for you sir")
            pywhatkit.playonyt(song)

        elif 'no thanks' in query:
            speak('I am glad I was able to help you. Have a good day Sir')
            sys.exit()

        speak('Sir,  do you need anything else ?')
