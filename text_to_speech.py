#1. pip install setuptools
#2. pip install pyttsx3

#CODE
#import libary
import pyttsx3 as p

#Initialization: getting information from current driver
engine = p.init()

#Check if its working
#engine.say("Hello World")
#engine.runAndWait()

#SPEED and VOICE
#Speed -- can use getProperty to get default speed
engine.setProperty('rate',180)
#Change voice -- change to female voice:
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

#Create function for speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("Hello there")