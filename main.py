import pyttsx3

#Basic virtual assistant
engine = pyttsx3.init()
engine.say("Hello, my name is Apollo Patrick." + " What's your name, mate?")
engine.runAndWait()
name = input()
engine.say("Hello " + name + ", how are you, mate?")
engine.runAndWait()
status = input()
engine.say("Oh, so you are " + status + " today, mate")
engine.runAndWait()






