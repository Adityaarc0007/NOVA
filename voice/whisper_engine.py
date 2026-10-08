from faster_whisper import WhisperModel


class WhisperEngine:

    def __init__(self):

        print("Loading Whisper Model...")

        self.model = WhisperModel(
            model_size_or_path="small",
            device="cuda",
            compute_type="float16",
            cpu_threads=8,
            num_workers=2
        )

        print("Whisper Ready")

    def transcribe(self, audio_path):

        segments, info = self.model.transcribe(
            audio_path,

            language="en",

            beam_size=5,

            best_of=5,

            temperature=0.0,

            vad_filter=True,

            condition_on_previous_text=False,

            initial_prompt=(
                "This is a voice assistant named Nova. "
                "Recognize English commands accurately like "
                "'Open Chrome', "
                "'Open VS Code', "
                "'Open YouTube', "
                "'Search Google'."
            )
        )

        text = " ".join(
            segment.text.strip()
            for segment in segments
        )

        return text.strip()