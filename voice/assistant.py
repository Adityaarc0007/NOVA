"""
NOVA Assistant Engine
"""

from voice.listener import Listener
from voice.speaker import Speaker
from voice.wake_word import WakeWord

from ai.brain import Brain
from skills.executor import Executor
import time

def remove_wake_word(text: str) -> str:
    """
    Remove wake word from the beginning of a command.
    Handles punctuation produced by Whisper.
    """

    text = text.lower().strip()

    # Normalize punctuation
    for char in ",.!?;:":
        text = text.replace(char, " ")

    text = " ".join(text.split())

    wake_words = [
        "hello nova",
        "hey nova",
        "hi nova",
        "nova"
    ]

    for wake_word in wake_words:

        if text.startswith(wake_word):

            return text[len(wake_word):].strip()

    return text


def start_assistant():

    print("=" * 50)
    print("NOVA Assistant Started")
    print("=" * 50)

    # -------------------------
    # Core Components
    # -------------------------

    listener = Listener()
    wake = WakeWord()

    brain = Brain()
    executor = Executor()

    # -------------------------
    # Startup Voice
    # -------------------------

    Speaker.set_language("english")

    Speaker.speak(
        "Hello Sir. Nova is online."
    )



    # -------------------------
    # Main Loop
    # -------------------------

    while True:

        try:

            text = listener.listen()

            if not text:
                continue

            print(f"Heard : {text}")

            # -------------------------
            # Wake Word
            # -------------------------

            if not wake.detected(text):
                continue

            # -------------------------
            # Remove Wake Word
            # -------------------------

            command = remove_wake_word(text)

            # -------------------------
            # Wake Word Only
            # -------------------------

            if not command:

                Speaker.speak(
                    "Yes Sir?"
                )

                command = listener.listen()

                if not command:
                    continue

            print(f"Command : {command}")

            # -------------------------
            # Brain
            # -------------------------

            plan = brain.ask(command)

            print(f"Plan : {plan}")

            # -------------------------
            # Skill
            # -------------------------
            if plan["type"] == "skill":
                success, message = executor.execute(plan)

                print(f"Result : {message}")

                Speaker.speak(message)

                time.sleep(0.8)

            # -------------------------
            # AI
            # -------------------------

            elif plan["type"] == "ai":

                response = plan.get(

                    "response",

                    "I couldn't generate a response."

                )

                print(f"NOVA : {response}")

                Speaker.speak(response)

                time.sleep(0.8)

            # -------------------------
            # Memory
            # -------------------------

            elif plan["type"] == "memory":

                print("Memory command detected.")

                Speaker.speak(
                    "I detected a memory command, "
                    "but the memory system is not connected yet."
                )

            # -------------------------
            # Automation
            # -------------------------

            elif plan["type"] == "automation":

                print("Automation command detected.")

                Speaker.speak(
                    "The automation system is not connected yet."
                )

            else:

                print(
                    f"Unknown plan type: {plan.get('type')}"
                )

                Speaker.speak(
                    "I don't know how to handle that yet."
                )

        except KeyboardInterrupt:

            print("\nNOVA shutting down.")

            break

        except Exception as e:

            print(
                f"Assistant Error : {e}"
            )

            Speaker.speak(
                "Sorry Sir, I encountered an error."
            )