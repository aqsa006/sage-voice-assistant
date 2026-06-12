import pyttsx3
import webbrowser
import speech_recognition as sr
from datetime import date
import os
from notes import save_note,open_note


def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
   
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1
    with sr.Microphone() as source:
           print("Adjusting for ambient noise... Please wait.")
           recognizer.adjust_for_ambient_noise(source, duration=0.5)
           print("Listening... Speak now!")
           audio=recognizer.listen(source,timeout=5)
    
    try:
        command=recognizer.recognize_google(audio,language='en-IN').lower().strip()
        print(f"you said:{command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")

    except sr.RequestError as e:
        print("Error:", e)


def process_command(command):
    if "hello" in command:
        speak("hello ma'am")
    elif "date" in command:
        today=date.today()
        speak(f"the date is {today}")
        
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com/")
    elif "google" in command:
        webbrowser.open("https://www.google.com/")
    elif command=="who are you":
        speak("i am sage! your virtual assistant")
    elif "spotify" in command:
        os.startfile("spotify.exe")
    elif "calculator" in command:
        os.startfile("calc.exe")
    elif "clock" in command:
        os.system("start ms-clock:")
    
    elif "open note" in command:
        speak("opening notes")
        open_note()
        
    elif "note" in command :
        speak("what should I write?")
        note=listen()
        save_note(note)
        speak("note taken successfully!")

    else:
         speak("sorry i don't understand")

if __name__=="__main__":
    speak("initializing sage.")
    recognizer=sr.Recognizer()
    while True:
        
        command=listen()  
        if command=="exit":
           speak("happy to help you. Bye")
           break
        else:
           process_command(command)
        
    
    