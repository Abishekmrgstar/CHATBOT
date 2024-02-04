import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import wikipedia



engine=pyttsx3.init('sapi5')
  
voices=engine.getProperty('voices')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

    try:
        print("ACCESSING...")
        query = r.recognize_google(audio)
        print(f"You just said: {query}\n")
    except Exception as e:
        print(e)
        speak("Come again..BOSS")
        query = "none"
    return query.lower()
def wishings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning BOSS!")
        print("Good morning BOSS!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon BOSS!")
        print("Good Afternoon BOSS!")
    elif hour>=17 and hour<21:
        speak("Good Evening BOSS!")
        print("Good Evening BOSS!")
if __name__=="__main__":
    wishings()
    query=commands().lower()
    if 'time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir, the time is {strTime}")
        print(strTime)
    elif "open google" in query:
        speak("Firing up Google sir..")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "search for" or "what's" in query:
        try:
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia, ")
            print(results)
            speak(results)
        except:
            speak("No results found...")
            print("No results found..")
    else:
        speak("I am not ready to provide such assistance at the moment")







