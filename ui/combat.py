from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
)
from PyQt5.QtCore import Qt
from qfluentwidgets import PushButton, FluentIcon, TitleLabel
from game import FreeFire


class CombatFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.vbox = QVBoxLayout(self)
        self.title = TitleLabel("COMBAT CHEATS")
        self.title.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.title)

        self.hbox = QHBoxLayout()
        self.hbox.setSpacing(20)

        self.aimbot_neck = PushButton("Aimbot Neck", self, FluentIcon.HEART)
        self.aimbot_neck.setToolTip("apply in login screen")
        self.aimbot_neck.setFixedHeight(45)
        self.aimbot_neck.clicked.connect(FreeFire.aimneck)

        self.no_recoil = PushButton("No Recoil", self, FluentIcon.BRUSH)
        self.no_recoil.setToolTip("apply in boot camp")
        self.no_recoil.setFixedHeight(45)
        self.no_recoil.clicked.connect(FreeFire.norecoil)

        self.hbox.addWidget(self.aimbot_neck)
        self.hbox.addWidget(self.no_recoil)

        self.vbox.addLayout(self.hbox)
        self.vbox.addItem(
            QSpacerItem(100, 100, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )

        self.setObjectName("combat-frame")
