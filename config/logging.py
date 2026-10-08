"""
NOVA Logging Configuration
--------------------------
Professional logging system for Nova AI Assistant.
"""

from pathlib import Path
import logging
import logging.handlers

# ---------------------------------------
# Paths
# ---------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "nova.log"

# ---------------------------------------
# Logger
# ---------------------------------------

logger = logging.getLogger("NOVA")
logger.setLevel(logging.DEBUG)

# Prevent duplicate handlers
if not logger.handlers:

    formatter = logging.Formatter(
        "[%(asctime)s] | %(levelname)-8s | %(message)s",
        "%d-%m-%Y %H:%M:%S"
    )

    # File Logger
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,   # 5 MB
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Console Logger
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# ---------------------------------------
# Helper Functions
# ---------------------------------------

def info(message: str):
    logger.info(message)


def warning(message: str):
    logger.warning(message)


def error(message: str):
    logger.error(message)


def critical(message: str):
    logger.critical(message)


def debug(message: str):
    logger.debug(message)