"""
NOVA Audio Buffer
"""

import numpy as np


class AudioBuffer:

    def __init__(self):

        self.frames = []

    def clear(self):

        self.frames.clear()

    def append(self, audio):

        self.frames.append(audio.copy())

    def get_audio(self):

        if not self.frames:
            return None

        return np.concatenate(
            self.frames,
            axis=0
        )