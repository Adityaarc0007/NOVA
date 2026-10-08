"""
NOVA AI Provider
----------------
Selects the active AI provider.
"""

from config.settings import settings


class AIProvider:

    def __init__(self):

        self.provider = settings.ai.provider.lower()

    def ask(self, prompt: str) -> str:

        if self.provider == "ollama":

            from ai.ollama_ai import OllamaAI

            return OllamaAI().ask(prompt)

        elif self.provider == "openai":

            from ai.openai_ai import OpenAI

            return OpenAI().ask(prompt)

        elif self.provider == "gemini":

            from ai.gemini_ai import GeminiAI

            return GeminiAI().ask(prompt)

        else:

            raise ValueError(
                f"Unknown AI Provider : {self.provider}"
            )