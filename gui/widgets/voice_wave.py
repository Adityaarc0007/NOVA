from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget


class VoiceWave(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(90)

        self.bars = [12, 20, 35, 50, 35, 20, 12]
        self.direction = 1

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(60)

    def animate(self):

        if self.direction == 1:
            self.bars = [x + 2 for x in self.bars]

            if max(self.bars) >= 70:
                self.direction = -1

        else:
            self.bars = [x - 2 for x in self.bars]

            if min(self.bars) <= 12:
                self.direction = 1

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(Qt.NoPen)

        painter.setBrush(QColor(0, 200, 255))

        width = self.width()

        gap = 16
        bar_width = 12

        total = len(self.bars)

        start_x = (width - ((bar_width + gap) * total)) // 2

        center = self.height() // 2

        for h in self.bars:

            painter.drawRoundedRect(
                start_x,
                center - h // 2,
                bar_width,
                h,
                6,
                6
            )

            start_x += bar_width + gap