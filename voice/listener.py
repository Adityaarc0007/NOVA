"""
NOVA Voice Listener
"""

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

            # Record voice
            result = self.recorder.record_until_silence(
                temp.name
            )

            # Nothing was recorded
            if not result:
                return None

            print("🧠 Processing...")

            # Whisper transcription
            text = self.whisper.transcribe(
                temp.name
            )

            if not text:
                return None

            text = text.strip()

            if not text:
                return None

            print(f"You : {text}")

            return text

        except Exception as e:

            print(f"⚠️ Listener Error : {e}")

            return None

        finally:

            if os.path.exists(temp.name):

                try:
                    os.remove(temp.name)
                except Exception:
                    pass