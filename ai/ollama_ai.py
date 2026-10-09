
"""
NOVA Ollama Provider
--------------------
Fast, concise responses from the configured local Ollama model.
"""

from ollama import chat
from config.settings import settings


class OllamaAI:

    SYSTEM_PROMPT = """
You are NOVA, a concise Windows desktop AI assistant.

Rules:
- Answer directly and accurately.
- For simple questions, use 1-2 short sentences.
- Do not repeat the question or yourself.
- Do not add unnecessary introductions or follow-up questions.
- For desktop action confirmations, keep the response brief.
- Give detailed explanations only when the user asks for them.
""".strip()

    def ask(self, prompt: str) -> str:
        """Generate a concise response using the configured Ollama model."""

        prompt = str(prompt or "").strip()

        if not prompt:
            return ""

        try:
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
                ],
                options={
                    "num_predict": 100,
                    "temperature": 0.3
                },
                stream=False
            )

            message = response.get("message", {})
            text = str(message.get("content", "") or "").strip()

            # Remove unwanted model tokens
            unwanted_tokens = [
                "<start_of_image>",
                "<end_of_image>",
                "<|im_start|>",
                "<|im_end|>"
            ]

            for token in unwanted_tokens:
                text = text.replace(token, "")

            return text.strip()

        except Exception as exc:
            print(f"Ollama Error: {exc}")

            return (
                "Sorry Sir, I couldn't get a response from Ollama. "
                "Please check that Ollama is running and the configured "
                "model is available."
            )
