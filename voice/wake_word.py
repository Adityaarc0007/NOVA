"""
NOVA Wake Word Detection
"""


class WakeWord:

    def __init__(self):

        self.keywords = [

            "nova",
            "hello nova",
            "hey nova",
            "hi nova",

        ]

    def detected(self, text):

        if not text:
            return False

        text = text.lower().strip()

        return any(
            keyword in text
            for keyword in self.keywords
        )