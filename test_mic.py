import speech_recognition as sr

print("=" * 50)
print("Available Microphones")
print("=" * 50)

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")