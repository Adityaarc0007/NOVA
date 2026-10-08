from ai.ollama_ai import OllamaAI

ai = OllamaAI()

while True:

    prompt = input("You : ")

    if prompt.lower() == "exit":
        break

    answer = ai.ask(prompt)

    print("\nNOVA :", answer)
    print()