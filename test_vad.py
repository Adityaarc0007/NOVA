from voice.recorder import Recorder
from voice.vad import VoiceActivityDetector

import soundfile as sf

print("=" * 50)
print("NOVA VAD Test")
print("=" * 50)

recorder = Recorder()
vad = VoiceActivityDetector()

recorder.record(
    "sample.wav",
    duration=5
)

audio, sr = sf.read("sample.wav")

if vad.has_speech(audio, sr):

    print("✅ Speech Detected")

else:

    print("❌ No Speech")