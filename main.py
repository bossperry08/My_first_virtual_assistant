import pyttsx3

#Basic virtual assistant
engine = pyttsx3.init()
engine.say("Hello, my name is Apollo Patrick." + " What's your name, mate?")
engine.runAndWait()
name = input()
engine.say("Hello " + name + ", how old are you, mate?")
engine.runAndWait()
age = input()
engine.say("Well, so you are " + age + " years old. " + "How are you today, mate?")
engine.runAndWait()
status = input()
engine.say("Oh, you are rather " + status + " today, mate.")
engine.runAndWait()






