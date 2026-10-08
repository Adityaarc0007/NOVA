import asyncio
import os
import tempfile

import edge_tts
from playsound import playsound

from voice.voices import (
    VOICES,
    DEFAULT_LANGUAGE
)


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

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        temp.close()

        asyncio.run(
            Speaker._generate(
                text,
                temp.name
            )
        )

        playsound(temp.name)

        os.remove(temp.name)