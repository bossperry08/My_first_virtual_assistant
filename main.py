import pyttsx3
from chatterbot import ChatBot
import logging, os
import speech_recognition as sr 

logging.basicConfig(level=logging.CRITICAL)

bot = ChatBot(
        'Mario',
        storage_adapter='chatterbot.storage.SQLStorageAdapter'
)

os.system("cls")
r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 150)

while True:
    try:
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=5)
            text = r.recognize_google(audio_data)
        user_input = text
        bot_response = bot.get_response(user_input)
        text = bot_response
        engine.say(text)
        engine.runAndWait()
         
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
