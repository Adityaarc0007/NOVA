from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QGraphicsDropShadowEffect
)


class GlassCard(QFrame):

    def __init__(self, title, value):

        super().__init__()

        self.setFixedSize(180, 120)

        self.setStyleSheet("""
        QFrame{
            background: rgba(40,40,40,180);
            border:1px solid rgba(255,255,255,35);
            border-radius:20px;
        }

        QLabel{
            background:transparent;
            color:white;
        }
        """)

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(40)

        shadow.setOffset(0)

        shadow.setColor(QColor(0,200,255,120))

        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)

        layout.setAlignment(Qt.AlignCenter)

        layout.setSpacing(12)

        self.title = QLabel(title)

        self.title.setStyleSheet("""
        font-size:18px;
        color:#AAAAAA;
        """)

        self.value = QLabel(value)

        self.value.setStyleSheet("""
        font-size:28px;
        font-weight:bold;
        color:#00C8FF;
        """)

        layout.addWidget(self.title)

        layout.addWidget(self.value)

    def set_value(self, value):

        self.value.setText(value)