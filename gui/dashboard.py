from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

from gui.widgets.ai_orb import AIOrb
from gui.widgets.glass_card import GlassCard
from gui.widgets.voice_wave import VoiceWave
from utils.system_monitor import SystemMonitor
from datetime import datetime

class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_system_info)
        self.timer.start(1000)

        self.update_system_info()
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(
            self.update_datetime
        )
        self.clock_timer.start(1000)
        self.update_datetime()

    def build_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 30, 50, 30)
        layout.setSpacing(25)

        # Greeting
        self.greeting = QLabel("Good Evening, Sir")
        self.greeting.setAlignment(Qt.AlignCenter)

        self.greeting.setStyleSheet("""
            QLabel{
                color:white;
                font-size:34px;
                font-weight:600;
            }
        """)

        layout.addWidget(self.greeting)
        self.clock = QLabel()

        self.clock.setAlignment(Qt.AlignCenter)

        self.clock.setStyleSheet("""
        QLabel{
            color:#00C8FF;
            font-size:28px;
            font-weight:bold;
        }
        """)

        layout.addWidget(self.clock)
        self.date = QLabel()

        self.date.setAlignment(Qt.AlignCenter)

        self.date.setStyleSheet("""
        QLabel{
            color:#AAAAAA;
            font-size:16px;
        }
        """)

        layout.addWidget(self.date)

        # AI Orb
        self.orb = AIOrb()

        layout.addWidget(
            self.orb,
            alignment=Qt.AlignCenter
        )

        # Status
        self.status = QLabel("NOVA is Ready")

        self.status.setAlignment(Qt.AlignCenter)

        self.status.setStyleSheet("""
            QLabel{
                color:#44ff88;
                font-size:18px;
            }
        """)

        layout.addWidget(self.status)

        # Cards
        cards = QHBoxLayout()
        cards.setSpacing(25)
        cards.setAlignment(Qt.AlignCenter)

        self.cpu = GlassCard("CPU", "0%")
        self.ram = GlassCard("RAM", "0%")
        self.battery = GlassCard("Battery", "--")
        self.security = GlassCard("Security", "Safe")

        cards.addWidget(self.cpu)
        cards.addWidget(self.ram)
        cards.addWidget(self.battery)
        cards.addWidget(self.security)

        layout.addLayout(cards)

        # Voice Wave
        self.wave = VoiceWave()

        layout.addWidget(
            self.wave,
            alignment=Qt.AlignCenter
        )

        layout.addStretch()

    # ==============================
    # Live System Update
    # ==============================

    def update_system_info(self):

        self.cpu.set_value(
            SystemMonitor.cpu()
        )

        self.ram.set_value(
            SystemMonitor.ram()
        )

        self.battery.set_value(
            SystemMonitor.battery()
        )

        self.security.set_value(
            SystemMonitor.security()
        )

    # ==============================
    # Live Clock & Greeting
    # ==============================

    def update_datetime(self):

        now = datetime.now()

        self.clock.setText(
            now.strftime("%I:%M:%S %p")
        )

        self.date.setText(
            now.strftime("%A, %d %B %Y")
        )

        hour = now.hour

        if hour < 12:
            greeting = "Good Morning, Sir"

        elif hour < 18:
            greeting = "Good Afternoon, Sir"

        else:
            greeting = "Good Evening, Sir"

        self.greeting.setText(greeting)