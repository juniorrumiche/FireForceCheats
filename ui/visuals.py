from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QGridLayout,
)
from PyQt5.QtCore import Qt
from qfluentwidgets import PillPushButton, FluentIcon, TitleLabel
from game import FreeFire


class VisualsFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.vbox = QVBoxLayout(self)
        self.title = TitleLabel("VISUAL CHEATS")
        self.title.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.title)

        self.grid = QGridLayout()
        self.grid.setSpacing(20)

        self.female_hand = PillPushButton("Antena Female Hand", self, FluentIcon.PEOPLE)
        self.female_hand.clicked.connect(FreeFire.female_hand)
        self.female_hand.setFixedHeight(45)

        self.female_head = PillPushButton("Antena Female Head", self, FluentIcon.PEOPLE)
        self.female_head.clicked.connect(FreeFire.female_head)
        self.female_head.setFixedHeight(45)

        self.male_hand = PillPushButton("Antena Male Hand", self, FluentIcon.PEOPLE)
        self.male_hand.clicked.connect(FreeFire.male_hand)
        self.male_hand.setFixedHeight(45)

        self.male_head = PillPushButton("Antena Male Head", self, FluentIcon.PEOPLE)
        self.male_head.clicked.connect(FreeFire.male_head)
        self.male_head.setFixedHeight(45)

        self.antena = PillPushButton("Antena", self, FluentIcon.PEOPLE)
        self.antena.clicked.connect(FreeFire.antena)
        self.antena.setFixedHeight(45)

        self.grid.addWidget(self.female_head, 0, 0)
        self.grid.addWidget(self.female_hand, 0, 1)
        self.grid.addWidget(self.male_hand, 1, 0)
        self.grid.addWidget(self.male_head, 1, 1)
        self.grid.addWidget(self.antena, 2, 0)

        self.vbox.addLayout(self.grid)

        self.vbox.addItem(
            QSpacerItem(100, 100, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )

        self.setObjectName("visual-frame")
