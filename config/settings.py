"""
NOVA Configuration Loader
-------------------------
Loads all application settings from .env
"""

from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
import os

# -------------------------------------------------
# Load .env
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


# -------------------------------------------------
# Application
# -------------------------------------------------

@dataclass
class ApplicationSettings:
    name: str = os.getenv("APP_NAME", "NOVA")
    version: str = os.getenv("APP_VERSION", "1.0.0")
    author: str = os.getenv("AUTHOR", "Aditya")


# -------------------------------------------------
# User
# -------------------------------------------------

@dataclass
class UserSettings:
    name: str = os.getenv("USER_NAME", "Sir")
    title: str = os.getenv("USER_TITLE", "Sir")


# -------------------------------------------------
# AI
# -------------------------------------------------

@dataclass
class AISettings:
    provider: str = os.getenv("AI_PROVIDER", "gemini")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-5")
    temperature: float = float(os.getenv("AI_TEMPERATURE", "0.7"))

# -------------------------------------------------
# Voice
# -------------------------------------------------

@dataclass
class VoiceSettings:
    enabled: bool = os.getenv("VOICE_ENABLED", "true").lower() == "true"
    wake_word: str = os.getenv("WAKE_WORD", "nova")
    voice: str = os.getenv("VOICE_NAME", "en-IN-NeerjaNeural")
    rate: int = int(os.getenv("VOICE_RATE", "-10"))
    volume: int = int(os.getenv("VOICE_VOLUME", "100"))


# -------------------------------------------------
# UI
# -------------------------------------------------

@dataclass
class UISettings:
    fullscreen: bool = os.getenv("FULLSCREEN", "true").lower() == "true"
    theme: str = os.getenv("THEME", "dark")


# -------------------------------------------------
# Startup
# -------------------------------------------------

@dataclass
class StartupSettings:
    auto_launch: bool = os.getenv("AUTO_LAUNCH", "true").lower() == "true"
    startup_scan: bool = os.getenv("STARTUP_SCAN", "true").lower() == "true"


# -------------------------------------------------
# Security
# -------------------------------------------------

@dataclass
class SecuritySettings:
    antivirus_scan: bool = os.getenv("ANTIVIRUS_SCAN", "true").lower() == "true"
    malware_scan: bool = os.getenv("MALWARE_SCAN", "true").lower() == "true"


# -------------------------------------------------
# Master Settings
# -------------------------------------------------

class Settings:

    def __init__(self):

        self.application = ApplicationSettings()
        self.user = UserSettings()
        self.ai = AISettings()
        self.voice = VoiceSettings()
        self.ui = UISettings()
        self.startup = StartupSettings()
        self.security = SecuritySettings()


settings = Settings()