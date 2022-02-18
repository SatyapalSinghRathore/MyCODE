from twilio.rest import Client
import pyttsx3, pyautogui, datetime, os, time, webbrowser, wikipedia, random
import speech_recognition as sr

name='karina'
History=['NULL']
Rand=['yeah,sure, wait for a second','yeah,sure','of course, here we go','here we go']
mistakes=0

a=pyttsx3.init()
voices=a.getProperty('voices')
a.setProperty('voice',voices[2].id)

r=sr.Recognizer()

def speak(command):
    History_Upt(command)
    print('speaking...')
    a.say(command)
    a.runAndWait()

# def command():
#     with sr.Microphone() as source2:
#         r.adjust_for_ambient_noise(source2, duration=0.2)
#         print('listenin...')
#         audio2=r.listen(source2)
#         val=r.recognize_google(audio2,language='en-in')
#         val=val.lower()
#     return val

def call_me():
    try:
        client=Client('AC0b5ce650008c587e22fd0cdc9a384b56','0ab16b7c60f7ffb189b1beb6ae0a9c6b')
        call=client.calls.create(twiml=f'<Response><Say>hello,it is me sir,{name}</Say></Response>',to='+919057584697',from_='+14692146395')
        print(call.sid)
    except:
        speak('we have internet issue,you should connect me to the internet.')

def message_me():
    try:
        client=Client('AC0b5ce650008c587e22fd0cdc9a384b56','0ab16b7c60f7ffb189b1beb6ae0a9c6b')
        message1=client.messages.create(body='Hello,sir it\'s me F.R.I.D.A.Y, someone using me.i thought i inform you.',to='+919057584697',from_='+14692146395')
    except:
        global mistakes
        mistakes=0  

def History_Upt(command):
    History.remove(History[0])
    History.append(command)

def wish():
    b=int(datetime.datetime.now().hour)
    print(f'Time: {b} hr')
    if b>=1 and b<=12:
        speak('good morning,sir')
    elif b>=13 and b<=23:
        speak('good evening,sir')
    else:
        speak('What  Emergency,sir')
    speak('how  may  i  help  you')

if __name__=='__main__':
    while True:
        wish()
        while True:
            value=input('ENTER YOUR COMMAND:')
            # value=input('ENTER COMMAND:')
            if 'open youtube' in value:
                speak(random.choice(Rand))
                webbrowser.open('www.youtube.com')
            elif name==value:
                speak('yes,sir')
            elif 'who are you' in value or 'what is your name' in value:
                speak(f'my name is {name} \nand i am AI(Artificial intelligence)\ni am working for satyapal')
                print('F.R.I.D.A.Y')
            elif 'what you can do' in value:
                speak('if you want send message\nor\ni can open youtube,\nfacebook,\ninstagram and so on\nbut on your command')
            elif 'wikipedia' in value:
                try:
                    value=value.replace('wikipedia','')
                    result=wikipedia.summary(value,sentences=2)
                    print(f'\n{result}\n')
                    speak('according to wikipedia')
                    speak(result)
                except:
                    b=['find information','figure out']
                    k=['here is no this kind of information','i did not got anything']
                    speak(f'it is very difficult to {random.choice(b)},\nsorry sir ,{random.choice(k)}')
                    speak('may be internet issue or may be the way you ask is wrong.')
            elif 'what you said' in value or 'say that again' in value or 'did you say something' in value or 'what did you said' in value or 'repeat again' in value:
                if 'say that again' in value:
                    speak(History[0])
                else:
                    if 'i said,' in History[0]:
                        Hist=History[0]
                        Hist=Hist.replace('i said,',' ')
                        History_Upt(Hist)
                    speak(f'i said, {History[0]}')
            elif 'open facebook' in value:
                speak(random.choice(Rand))
                webbrowser.open('www.facebook.com')
            elif 'open twitter' in value:
                speak(random.choice(Rand))
                webbrowser.open('www.twitter.com')
            elif 'open arduino IDE' in value:
                try:
                    speak(random.choice(Rand))
                    path1="C:\\Program Files (x86)\\Arduino\\arduino.exe"
                    os.startfile(path1)
                except:
                    speak('sorry sir, There is no such kind of application in your device.')
            elif 'open code' in value or 'open vs code' in value or 'open visual studio code' in value:
                try:
                    speak(random.choice(Rand))
                    path1="C:\\Users\Rockstar\\AppData\Local\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(path1)
                except:
                    speak('sorry sir, There is no such kind of application in your device.')
            elif 'open notepad' in value:
                try:
                    speak(random.choice(Rand))
                    path1="C:\\WINDOWS\\system32\\notepad.exe"
                    os.startfile(path1)
                except:
                    speak('sorry sir, There is no such kind of application in your device.')
            elif 'call me' in value:
                call_me()    
            elif 'volume up' in value:
                speak('sure')
                pyautogui.press('volumeup')
            elif 'volume down' in value:
                speak('sure')
                pyautogui.press('volumedown')
            elif 'volume mute' in value or 'mute' in value:
                speak('sure')
                pyautogui.press('volumemute')
            elif 'what time is it' in value or 'tell me the time' in value or 'what time it is' in value:
                hour,minute,second=datetime.datetime.now().hour,datetime.datetime.now().minute,datetime.datetime.now().second
                print(datetime.datetime.now())
                if hour>=13:
                    hour-=12
                    speak(f'it\'s,\n{hour} hour\n{minute} minute\n{second} seconds,PM')
                else:
                    speak(f'it\'s,\n{hour} hour\n{minute} minute\n{second} seconds,AM')
            elif f'bye {name}' in value or 'you should go to sleep' in value:
                b=int(datetime.datetime.now().hour)
                if b>=1 and b<=15:
                    speak('have a good day!')
                    speak(random.choice(['ok,\nsee you later','nice talking with you','great to see you']))
                else:
                    speak(random.choice(['ok,\n\nbye sir','ok,\nsee you later','nice talking with you','great to see you']))
                break
            elif value in ['good morning','good evening','good night',f'good morning {name}',f'good evening {name}',f'good night {name}']:
                wish() 
            elif 'ok'==value or 'well done'==value:
                speak('It\'s my pleasure.')
            elif 'it is my fault' in value or 'i made mistake' in value or 'it\'s my fault' in value or 'sorry' in value:
                speak('Do not worry sir, it is common thing.')
            else:
                if mistakes==0 or mistakes==4:
                    message_me()
                speak('i do not have that kind of information,\nsorry sir')
                mistakes+=1
        break
    time.sleep(3)