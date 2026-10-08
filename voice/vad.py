"""
NOVA Voice Activity Detector
"""

import numpy as np
import torch

from silero_vad import (
    load_silero_vad,
    get_speech_timestamps
)


class VoiceActivityDetector:

    def __init__(self):

        print("Loading Silero VAD...")

        self.model = load_silero_vad()

        print("Silero Ready")

    def has_speech(
        self,
        audio,
        sample_rate=16000
    ):

        # Stereo -> Mono
        if len(audio.shape) > 1:
            audio = audio.mean(axis=1)

        # Convert to float32 numpy
        audio = np.asarray(audio, dtype=np.float32)

        # Convert to Torch Tensor
        audio = torch.from_numpy(audio)

        timestamps = get_speech_timestamps(
            audio,
            self.model,
            sampling_rate=sample_rate
        )

        return len(timestamps) > 0