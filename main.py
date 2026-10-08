"""
==================================================
NOVA AI Assistant
Main Entry Point
==================================================
"""

import sys

from config.settings import settings
from config.logging import info, error


def initialize():
    """
    Initialize NOVA
    """

    info("=" * 60)
    info(f"Starting {settings.application.name}")
    info(f"Version : {settings.application.version}")
    info("=" * 60)

    try:

        info("Loading Configuration...")

        info("Configuration Loaded")

        info("Loading AI Engine...")

        info("AI Engine Ready")

        info("Loading Voice Engine...")

        info("Voice Engine Ready")

        info("Loading Memory...")

        info("Memory Ready")

        info("Loading Startup Services...")

        info("Startup Services Ready")

        info("Launching GUI...")

    except Exception as e:

        error(str(e))

        sys.exit(1)


def main():

    initialize()

    # GUI Launch
    from gui.application import start_application

    start_application()


if __name__ == "__main__":
    main()