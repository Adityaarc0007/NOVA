from voice.recorder import Recorder

recorder = Recorder()

recorder.record(
    "sample.wav",
    duration=5
)

print("Recording Finished")