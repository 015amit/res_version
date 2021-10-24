import pyttsx3
import datetime
import speech_recognition as sr 
import os
import webbrowser
import wikipedia
import smtplib
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hr=int(datetime.datetime.now().hour)
    if(hr>=0 and hr<=12):
        speak("Good Morning Sir")
    
    elif(hr>=12 and hr<=17):
        speak("Good afternoon sir")

    else:
        speak("Good night sir")
    speak("How can i help you")

def takeCommand():
    required=-1
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "pulse" in name:
            required= index
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source,phrase_time_limit=4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:",query)

    except Exception as e:
        print("Say that again sir...")
        return "None"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open('google.com')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open firefox' in query:
            pth="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(pth)
        elif 'stop now' in query:
            speak("Thank you sir i hope i helped")
            break
    
        