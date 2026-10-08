from voice.speaker import Speaker
from voice.language import Language

Speaker.set_language(Language.ENGLISH)
Speaker.speak("Hello Sir.")

Speaker.set_language(Language.HINDI)
Speaker.speak("नमस्ते सर।")

Speaker.set_language(Language.JAPANESE)
Speaker.speak("こんにちは。私はノヴァです。")

Speaker.set_language(Language.KOREAN)
Speaker.speak("안녕하세요.")

Speaker.set_language(Language.CHINESE)
Speaker.speak("你好。")

Speaker.set_language(Language.FRENCH)
Speaker.speak("Bonjour.")

Speaker.set_language(Language.GERMAN)
Speaker.speak("Guten Tag.")