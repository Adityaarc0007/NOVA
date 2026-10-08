"""
NOVA Ollama Provider
"""

from ollama import chat
from config.settings import settings


class OllamaAI:

    SYSTEM_PROMPT = """
You are NOVA, a desktop AI assistant.

Rules:
- Keep replies under 3 sentences unless the user asks for details.
- Be direct.
- Do not repeat yourself.
- Do not ask unnecessary follow-up questions.
- For simple questions, answer briefly.
- For desktop commands, respond with a confirmation only.
"""

    def ask(self, prompt: str) -> str:

        response = chat(
            model=settings.ai.ollama_model,
            messages=[
                {
                    "role": "system",
                    "content": self.SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        text = response["message"]["content"]

        # Remove unwanted model tokens
        text = (
            text.replace("<start_of_image>", "")
                .replace("<end_of_image>", "")
                .replace("<|im_start|>", "")
                .replace("<|im_end|>", "")
                .strip()
        )

        return text