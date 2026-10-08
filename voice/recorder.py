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
        threshold=0.035,
        silence_duration=0.7,
        blocksize=1024,
        max_recording_duration=12,
        start_timeout=10
    ):
        self.samplerate = samplerate
        self.channels = channels
        self.threshold = threshold
        self.silence_duration = silence_duration
        self.blocksize = blocksize
        self.max_recording_duration = max_recording_duration
        self.start_timeout = start_timeout

    def _volume(self, audio):
        """
        Calculate RMS volume.
        """
        return float(np.sqrt(np.mean(audio ** 2)))

    def record_until_silence(self, filename):

        print("🎤 Waiting for voice...")

        frames = []
        recording = False
        silence_start = None

        wait_start = time.monotonic()
        recording_start = None

        try:

            with sd.InputStream(
                samplerate=self.samplerate,
                channels=self.channels,
                dtype="float32",
                blocksize=self.blocksize
            ) as stream:

                while True:

                    try:
                        audio, overflow = stream.read(
                            self.blocksize
                        )

                    except Exception as e:
                        print(f"⚠️ Audio stream error: {e}")
                        return None

                    if overflow:
                        print("⚠️ Audio overflow")

                    volume = self._volume(audio)

                    # ==================================
                    # WAITING FOR VOICE
                    # ==================================

                    if not recording:

                        if volume >= self.threshold:

                            recording = True
                            recording_start = time.monotonic()
                            silence_start = None

                            frames.append(audio.copy())

                            print("🟢 Voice Detected")
                            print("🎙 Recording...")

                        elif (
                            time.monotonic() - wait_start
                            >= self.start_timeout
                        ):

                            print("⌛ Voice timeout.")
                            return None

                    # ==================================
                    # RECORDING
                    # ==================================

                    else:

                        frames.append(audio.copy())

                        # Maximum recording protection
                        if (
                            time.monotonic() - recording_start
                            >= self.max_recording_duration
                        ):

                            print(
                                "⏱ Maximum recording time reached."
                            )
                            break

                        # Silence detection
                        if volume < self.threshold:

                            if silence_start is None:

                                silence_start = time.monotonic()

                            elif (
                                time.monotonic()
                                - silence_start
                                >= self.silence_duration
                            ):

                                print("🔴 Silence Detected")
                                break

                        else:

                            silence_start = None

        except Exception as e:

            print(f"⚠️ Recorder Error: {e}")
            return None

        # ==================================
        # No audio captured
        # ==================================

        if not frames:

            print("⚠️ No voice captured.")
            return None

        # ==================================
        # Save audio
        # ==================================

        try:

            audio = np.concatenate(
                frames,
                axis=0
            )

            sf.write(
                filename,
                audio,
                self.samplerate
            )

            print(f"💾 Saved : {filename}")

            return filename

        except Exception as e:

            print(f"⚠️ Audio save error: {e}")
            return None

    def record(self, filename, duration=5):

        return self.record_until_silence(filename)