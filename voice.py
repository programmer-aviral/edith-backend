import pyttsx3
import threading

engine = pyttsx3.init()

engine.setProperty('rate', 170)

voices = engine.getProperty('voices')

# Female voice
engine.setProperty('voice', voices[1].id)


def speak(text):

    print("EDITH:", text)

    def run():

        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=run).start()
