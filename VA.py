import speech_recognition as sr
from gtts import gTTS
import pyglet
from time import sleep
import os

r = sr.Recognizer()

def tts(text, lang):
    file = gTTS(text=text, lang=lang)
    filename = 'sp1.mp3'
    file.save(filename)

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    sleep(music.duration)
    os.remove(filename)

with sr.Microphone() as source:
    print('Speak Password: ')
    audio = r.listen(source)

    try:
        #Assistant speak here...
        
        text = r.recognize_google(audio)
        lang = 'en'

        tts(text, lang)

        if text == '1234':
            print('You said : {}'.format(text))

            lang = 'en'
            text2 = 'System Unlocked. Welcome to the R A programming world !'
            print(text2)
            file2 = gTTS(text=text2, lang=lang)
            filename = 'new.mp3'
            file2.save(filename)
            music = pyglet.media.load(filename, streaming=False)
            music.play()
            sleep(music.duration)
            os.remove(filename)
            print()
        else:
            print('Incorrect password')
    except:
        print('Sorry, voice is not clear.')
