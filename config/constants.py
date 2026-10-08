"""
==================================================
NOVA AI Assistant
Constants
==================================================
"""

from pathlib import Path

# ==================================================
# Application
# ==================================================

APP_NAME = "NOVA"
APP_VERSION = "1.0.0"

# ==================================================
# Directories
# ==================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

CONFIG_DIR = ROOT_DIR / "config"
LOGS_DIR = ROOT_DIR / "logs"
MEMORY_DIR = ROOT_DIR / "memory"
VOICE_DIR = ROOT_DIR / "voice"
GUI_DIR = ROOT_DIR / "gui"
CODING_DIR = ROOT_DIR / "coding"
OFFICE_DIR = ROOT_DIR / "office"
SECURITY_DIR = ROOT_DIR / "security"

# ==================================================
# Files
# ==================================================

ENV_FILE = ROOT_DIR / ".env"

LOG_FILE = LOGS_DIR / "nova.log"

# ==================================================
# AI Providers
# ==================================================

GEMINI = "gemini"
OPENAI = "openai"
OLLAMA = "ollama"

SUPPORTED_AI = [
    GEMINI,
    OPENAI,
    OLLAMA,
]

# ==================================================
# Voice
# ==================================================

DEFAULT_WAKE_WORD = "nova"

DEFAULT_VOICE = "en-IN-NeerjaNeural"

# ==================================================
# Themes
# ==================================================

DARK_THEME = "dark"
LIGHT_THEME = "light"

# ==================================================
# Startup Scan
# ==================================================

BATTERY = "battery"

CPU = "cpu"

RAM = "ram"

STORAGE = "storage"

NETWORK = "network"

TEMPERATURE = "temperature"

MALWARE = "malware"

FIREWALL = "firewall"

# ==================================================
# Office
# ==================================================

WORD = "word"

EXCEL = "excel"

POWERPOINT = "powerpoint"

PDF = "pdf"

# ==================================================
# Coding Languages
# ==================================================

PYTHON = "python"

CPP = "cpp"

JAVA = "java"

JAVASCRIPT = "javascript"

TYPESCRIPT = "typescript"

HTML = "html"

CSS = "css"

CSHARP = "csharp"

GO = "go"

RUST = "rust"

PHP = "php"

SWIFT = "swift"

KOTLIN = "kotlin"

# ==================================================
# Status
# ==================================================

READY = "READY"

LISTENING = "LISTENING"

THINKING = "THINKING"

SPEAKING = "SPEAKING"

OFFLINE = "OFFLINE"

ONLINE = "ONLINE"

ERROR = "ERROR"

# ==================================================
# Exit Codes
# ==================================================

SUCCESS = 0

FAILED = 1