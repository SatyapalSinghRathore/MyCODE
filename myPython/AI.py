import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0.2)
    print('listenin...')
    audio2=r.listen(source2)
    text=r.recognize_google(audio2,language='en-in')
    text=text.lower()
    print('Did you say:',text)