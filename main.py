import pygame
from gtts import gTTS
from chatterbot import ChatBot
import logging, os
import speech_recognition as sr 

logging.basicConfig(level=logging.CRITICAL)

bot = ChatBot(
        'Mario',
        storage_adapter='chatterbot.storage.SQLStorageAdapter'
)

os.system("cls")
while True:
    try:
        r = sr.Recognizer()
        audio_data = r.record(sr.Microphone(), duration=5)
        text = r.recognize_google(audio_data, language="en")
        user_input = text
        bot_response = bot.get_response(user_input)
        myobj = gTTS(text=bot_response, lang="en", slow=False)
        myobj.save("bot.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("bot.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
         
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
