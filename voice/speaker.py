"""
NOVA Speaker
"""

import asyncio
import os
import tempfile
import time

import edge_tts
from playsound import playsound

from voice.voices import VOICES, DEFAULT_LANGUAGE


class Speaker:

    language = DEFAULT_LANGUAGE

    @staticmethod
    def set_language(language):

        if language in VOICES:
            Speaker.language = language

    @staticmethod
    async def _generate(text, filename):

        voice = VOICES[Speaker.language]

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice
        )

        await communicate.save(filename)

    @staticmethod
    def speak(text):

        if not text:
            return

        text = str(text).strip()

        if not text:
            return

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        temp.close()

        try:

            # Generate speech
            asyncio.run(
                Speaker._generate(
                    text,
                    temp.name
                )
            )

            # Play speech
            playsound(temp.name)

            # Small microphone cooldown
            time.sleep(0.5)

        except Exception as e:

            print(f"⚠️ Speaker Error : {e}")

        finally:

            # Always remove temporary audio
            if os.path.exists(temp.name):

                try:
                    os.remove(temp.name)
                except Exception:
                    pass