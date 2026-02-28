from voice import speak, listen
from camera import open_camera
from memory import save_memory, load_memory


speak("EDITH activated")

name = load_memory("name")

if name:
    speak(f"Welcome back {name}")
else:
    speak("What is your name?")
    name = listen()
    save_memory("name", name)
    speak(f"Nice to meet you {name}")


while True:

    command = listen()

    if "camera" in command:
        speak("Opening camera")
        open_camera()

    elif "hello" in command:
        speak(f"Hello {name}")

    elif "stop" in command:
        speak("Shutting down")
        break

    elif "who am i" in command:
        speak(f"You are {name}")

    else:
        speak("Command not recognized")
