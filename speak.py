import pyttsx3                      #library to convert text into speech
engine = pyttsx3.init()             #object creation

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 180)
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 1000)
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)   #for male

engine.say("Hello, GitHub")
engine.runAndWait()

engine.setProperty('volume', 50000)
engine.setProperty('rate', 100)
voices=engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[1].id)  #for female

engine.say("Hello, GitHub")
engine.runAndWait()

with open('all lang') as f:
    for item in f.readlines():
        engine.say(item)   #iterate through 'all lang' file and speak every word
engine.runAndWait()

engine.stop()
