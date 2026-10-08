import sys
from threading import Thread

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow

from voice.assistant import start_assistant


def start_application():

    app = QApplication(sys.argv)

    # Start NOVA Voice Engine
    Thread(
        target=start_assistant,
        daemon=True
    ).start()

    window = MainWindow()

    window.show()

    sys.exit(app.exec())