
#import what we already coded in other files
from text_to_speech import speak
from speech_to_text import listen
from music import *
from news import get_news

#Establish voice assistant:

speak("Hello, I am your Voice Assistant today. How can I help you?")
text = listen()

#1. MUSIC FUNCTIONALITY -- using automation
if "music" or "song" or "video" in text:
    speak("Sorry, can you repeat Which one?")
    song = listen() 
    video = play_song()
    video.play(song)

elif "news" in text:
    speak("Sure, I can read some news for you")
    list = get_news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])


