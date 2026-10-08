import tempfile
import os

from voice.recorder import Recorder
from voice.whisper_engine import WhisperEngine


print("=" * 50)
print("NOVA Whisper Test")
print("=" * 50)

recorder = Recorder()
engine = WhisperEngine()

temp = tempfile.NamedTemporaryFile(
    delete=False,
    suffix=".wav"
)

temp.close()

recorder.record(
    temp.name,
    duration=5
)

print("🧠 Processing...")

text = engine.transcribe(
    temp.name
)

os.remove(temp.name)

print(f"\n📝 {text}\n")