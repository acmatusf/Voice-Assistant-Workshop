
#import what we already coded in other files
from text_to_speech import speak
from speech_to_text import listen
from music import *
from news import get_news
from random_facts import fact

#Establish voice assistant:
speak("Hello, I am your Voice Assistant today. How can I help you?")
text = listen()

#1. MUSIC FUNCTIONALITY -- using automation
if ("music" or "song" or "video") in text:
    speak("Can you repeat which one?")
    song = listen() 
    video = play_song()
    video.play(song)
elif "news" in text:
    speak("Sure, I can read some news for you")
    list = get_news()
    for i in range(len(list)):
        print(list[i])
        speak(list[i])
elif "fact" in text:
    random = fact()
    speak(random)

