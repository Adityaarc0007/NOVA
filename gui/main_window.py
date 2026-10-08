from PySide6.QtWidgets import QMainWindow

from gui.dashboard import Dashboard


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NOVA")

        self.resize(1700, 950)

        self.dashboard = Dashboard()

        self.setCentralWidget(self.dashboard)