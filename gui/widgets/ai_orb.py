from PySide6.QtCore import (
    Qt,
    QTimer
)

from PySide6.QtGui import (
    QColor,
    QPainter,
    QRadialGradient
)

from PySide6.QtWidgets import QWidget


class AIOrb(QWidget):

    def __init__(self):

        super().__init__()

        self.setFixedSize(260, 260)

        self.radius = 70
        self.direction = 1

        self.color = QColor(0, 200, 255)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(25)

    def animate(self):

        self.radius += self.direction

        if self.radius > 78:
            self.direction = -1

        if self.radius < 70:
            self.direction = 1

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        center_x = self.width() / 2
        center_y = self.height() / 2

        gradient = QRadialGradient(
            center_x,
            center_y,
            self.radius + 40
        )

        gradient.setColorAt(
            0,
            QColor(
                self.color.red(),
                self.color.green(),
                self.color.blue(),
                255
            )
        )

        gradient.setColorAt(
            0.55,
            QColor(
                self.color.red(),
                self.color.green(),
                self.color.blue(),
                120
            )
        )

        gradient.setColorAt(
            1,
            QColor(
                self.color.red(),
                self.color.green(),
                self.color.blue(),
                0
            )
        )

        painter.setBrush(gradient)

        painter.setPen(Qt.NoPen)

        painter.drawEllipse(
            int(center_x - self.radius),
            int(center_y - self.radius),
            self.radius * 2,
            self.radius * 2
        )

        def listening(self):
            self.color = QColor(0, 180, 255)
            self.update()

        def thinking(self):
            self.color = QColor(255, 180, 0)
            self.update()

        def speaking(self):
            self.color = QColor(0, 255, 120)
            self.update()

        def idle(self):
            self.color = QColor(0, 200, 255)
            self.update()