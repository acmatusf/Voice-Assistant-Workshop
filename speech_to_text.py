#Dependencies:
#pip install SpeechRecognition
#pip install PyAudio -- used to capture audio when we speak...

#Import dependencies -- speech recognition library
import speech_recognition as sr

#Initialization : Recognizer() helps retrieve audio from microphone
r = sr.Recognizer()

def listen():
    #Source of audio? -- microphone 
    with sr.Microphone() as source:

        #background properties -- spectrum and noise cancelation
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source,1.2)

        print("listening")

        #CONVERSION
        audio = r.listen(source) #make computer listen to us and store in audio var
        text = r.recognize_google(audio) #uses google api engine to convert audio to text

        #check audio is converted to text
        print(text)
        return text