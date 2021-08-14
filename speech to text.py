#pip install pipwin then pipwin install pyaudio

import pyaudio
import speech_recognition as sr
r=sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something! ")
    audio=r.listen(source)

try:
    print("Google thinks you said, " + r.recognize_google(audio))
except sr.UnknownValueError:
    print(" could not understand audio")
except sr.RequestError as e:
    print(" error; {0}".format(e))


