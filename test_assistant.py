from voice.listener import Listener
from voice.speaker import Speaker

listener = Listener()

Speaker.set_language("english")

Speaker.speak("Hello Sir. I am listening.")

while True:

    text = listener.listen()

    if not text:
        continue

    print(f"You : {text}")

    if text.lower() == "exit":

        Speaker.speak("Goodbye Sir.")

        break

    Speaker.speak(f"You said {text}")