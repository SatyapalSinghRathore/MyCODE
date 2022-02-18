import sys
import webbrowser
import subprocess
import img as img
import pyttsx3
import time
import query as query
import speech_recognition as sr
import datetime
import os
import cv2
from DateTime.pytz_support import hour
import random
from requests import get
import wikipedia
import smtplib
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 180)

#text to speech

def speak(audio):
    engine.say(audio)
    print("audio")
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening .....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognaizing")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except:
            speak('Sorry,you have some mic or internet issue, you can give me command using text.')
            query=input('ENTER THE COMMAND:')
        return  query


  #speak("hello sir")

#to wish

def wish():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good aftenoon")
    else:
        speak("good evening")
    speak("i am Friday sir . please tell me how can i help you")

#to send mail
def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rvppvr271@gmail.com','password')
    server.sendemail('your email id', to, content)
    server.close()

if __name__ =="__main__":
    wish()
    #while True:
    while 1:
        query = takecommand().lower()
        #logic building for tasks
        if "close" in query:
            query=query.split()
            program="".join(query[query.index('close')+1:])
            speak("okay sir, closing "+program)
            os.system(f"taskkill /f /im {program}.exe")

        elif "note" in query or 'write' in query:
            print("What you want me to write?")
            speak("What you want me to write?")
            date = datetime.datetime.now()
            file_name = str(date).replace(":", "-") + "-note.txt"
            with open(file_name, "w") as f:
                while True:
                    text = takecommand()
                    print("writing...",text)
                    speak(text)
                    if text == 'stop writing':
                        break
                    else:
                        f.write(text + " ")
                        length = len(text)
                os.system(f'notepad.exe {file_name}')
                speak("Content has written in your file.")

        elif "remove file" in query or "remove a file" in query or "delete file" in query or "delete a file" in query:
            if 'name' not in query and 'named' not in query:
                print("Tell me the name of file")
                speak("Tell me the name of file")
                filename = takecommand()
                extension = 'txt'
            else:
                query = query.split()
                try:
                    filename = query[query.index('named') + 1]
                except:
                    filename = query[query.index('name') + 1]
                extension = "txt"
            os.system(f'rm {filename}.{extension}')
            speak("File has been deleted")

        elif "create file" in query or "create a file" in query or "make file" in query or "make a new file" in query:
            if 'name' not in query and 'named' not in query:
                print("Tell me the name of file")
                speak("Tell me the name of file")
                filename = takecommand()
                extension = 'txt'
            else:
                query = query.split()
                try:
                    filename = query[query.index('named') + 1]
                except:
                    filename = query[query.index('name') + 1]
                extension = "txt"
            os.system(f'touch {filename}.{extension}')
            os.system(f'notepad.exe {filename}.{extension}')
            speak("File has been created")

        elif "create a folder" in query or "create folder" in query or "make a folder" in query or "make folder" in query or "make a new folder" in query or "make a new directory" in query:
            if 'name' not in query and 'named' not in query:
                print("Tell me the name of folder")
                foldername = takecommand()
            else:
                query = query.split()
                try:
                    foldername = query[query.index('named') + 1]
                except:
                    foldername = query[query.index('name') + 1]

            os.system(f'mkdir {foldername}')
            pwd = os.getcwd()
            time.sleep(0.5)
            os.system(f'explorer {pwd}\\{foldername}')
            speak(foldername + " has been created")
        elif "remove a folder" in query or "remove folder" in query or "delete a folder" in query or "delete folder" in query or "make a new folder" in query or "make a new directory" in query:
            if 'name' not in query and 'named' not in query:
                print("Tell me the name of folder")
                foldername = takecommand()
            else:
                query = query.split()
                try:
                    foldername = query[query.index('named') + 1]
                except:
                    foldername = query[query.index('name') + 1]
            os.system(f'rm {foldername}')
            pwd = os.getcwd()
            time.sleep(0.5)
            speak(foldername + " has been deleted")


        if "open notepad" in query:
            npath ="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
                cap.release()
                cv2.destroyAllWindows()


        elif "ip address" in query:
            ip = get('https://api.ipify.org')
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentencs=2)
            speak("according to wikipedia")
            speak(result)


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("sir what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open facebook" in query:
            webbrowser.open("www.fb.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")


        elif "send message" in query:
            pywhatkit.sendwhatmsg("+919660877081", "this is tet protocol",22,51)

        elif"play song on youtube" in query:
            pywhatkit.playonyt("see you again")

        elif "email to avi" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to="rvppvr27@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to rvp")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent mail to rvp")

        elif"no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        speak("sir do you have any other work")