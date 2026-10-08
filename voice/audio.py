import speech_recognition as sr


class AudioManager:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.microphone = sr.Microphone()

        self.configure()

    def configure(self):

        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.energy_threshold = 120
        self.recognizer.pause_threshold = 0.5
        self.recognizer.phrase_threshold = 0.15
        self.recognizer.non_speaking_duration = 0.2

    def calibrate(self):

        print("🎤 Calibrating Microphone...")

        with self.microphone as source:

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

        print("✅ Microphone Ready")