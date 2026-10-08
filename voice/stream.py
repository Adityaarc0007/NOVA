"""
NOVA Live Audio Stream
"""

import sounddevice as sd

from voice.audio_buffer import AudioBuffer


class AudioStream:

    def __init__(
        self,
        samplerate=16000,
        channels=1,
        blocksize=512
    ):

        self.buffer = AudioBuffer()

        self.stream = sd.InputStream(
            samplerate=samplerate,
            channels=channels,
            blocksize=blocksize,
            callback=self.callback
        )

    def callback(
        self,
        indata,
        frames,
        time,
        status
    ):

        self.buffer.append(indata)

    def start(self):

        self.stream.start()

        print("🎤 Live Stream Started")

    def stop(self):

        self.stream.stop()

        self.stream.close()

        print("🛑 Stream Stopped")