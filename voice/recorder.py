"""
NOVA Production Recorder
"""

import time
import numpy as np
import sounddevice as sd
import soundfile as sf


class Recorder:

    def __init__(
        self,
        samplerate=16000,
        channels=1,
        threshold=0.015,
        silence_duration=0.8,
        blocksize=1024
    ):

        self.samplerate = samplerate
        self.channels = channels
        self.threshold = threshold
        self.silence_duration = silence_duration
        self.blocksize = blocksize

    def _volume(self, audio):

        return np.sqrt(np.mean(audio ** 2))

    def record_until_silence(self, filename):

        print("🎤 Waiting for voice...")

        frames = []
        recording = False
        silence_start = None

        try:
            with sd.InputStream(
                    samplerate=self.samplerate,
                    channels=self.channels,
                    dtype="float32",
                    blocksize=self.blocksize
            ) as stream:

                while True:

                    audio, overflow = stream.read(self.blocksize)

                    if overflow:
                        print("⚠️ Audio overflow")

                    volume = self._volume(audio)

                    # Wait for voice
                    if not recording:

                        if volume > self.threshold:
                            recording = True
                            silence_start = None

                            frames.append(audio.copy())

                            print("🟢 Voice Detected")
                            print("🎙 Recording...")

                    # Recording
                    else:

                        frames.append(audio.copy())

                        if volume < self.threshold:

                            if silence_start is None:
                                silence_start = time.time()

                            elif time.time() - silence_start >= self.silence_duration:

                                print("🔴 Silence Detected")
                                break

                        else:

                            silence_start = None

            if not frames:
                return None

            audio = np.concatenate(frames, axis=0)

            sf.write(
                filename,
                audio,
                self.samplerate
            )

            print(f"💾 Saved : {filename}")

            return filename

        except Exception as e:

            print(f"⚠️ Recorder Error : {e}")

            return None