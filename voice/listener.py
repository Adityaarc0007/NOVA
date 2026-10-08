import os
import tempfile

from voice.recorder import Recorder
from voice.whisper_engine import WhisperEngine


class Listener:

    def __init__(self):

        self.recorder = Recorder()
        self.whisper = WhisperEngine()

    def listen(self):

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        )

        temp.close()

        try:

            self.recorder.record_until_silence(
                temp.name,
            )

            print("🧠 Processing...")

            text = self.whisper.transcribe(
                temp.name
            )

            text = text.strip()

            if not text:
                return None

            print(f"You : {text}")

            return text

        finally:

            if os.path.exists(temp.name):
                os.remove(temp.name)