from voice.listener import Listener
from voice.wake_word import WakeWord

listener = Listener()
wake = WakeWord()

print("=" * 50)
print("NOVA Wake Word Test")
print("=" * 50)

while True:

    text = listener.listen()

    if not text:
        continue

    if wake.detected(text):

        print("✅ Wake Word Detected")

    else:

        print("❌ Wake Word Not Detected")