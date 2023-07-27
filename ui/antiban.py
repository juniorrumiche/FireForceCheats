from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QGridLayout
from PyQt5.QtCore import Qt, QRect
from qfluentwidgets import PillPushButton, FluentIcon, TitleLabel
from game import FreeFire


class AntibanFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.vbox = QVBoxLayout(self)
        self.title = TitleLabel('ANTIBAN CHEATS')
        self.title.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.title)

        self.grid = QGridLayout()
        self.grid.setSpacing(20)

        self.antiban = PillPushButton('Antiban', self, FluentIcon.BRUSH)
        self.antiban.clicked.connect(FreeFire.antiban)
        self.antiban.setFixedHeight(45)

        self.antiblacklist = PillPushButton('Anti Blacklist', self, FluentIcon.BRUSH)
        self.antiblacklist.setToolTip('apply on login screen')
        self.antiblacklist.clicked.connect(FreeFire.antiblacklist)
        self.antiblacklist.setFixedHeight(45)

        self.clear_reports = PillPushButton('Clear Reports', self, FluentIcon.BRUSH)
        self.clear_reports.setToolTip('apply on login screen')
        self.clear_reports.clicked.connect(FreeFire.clear_reports)
        self.clear_reports.setFixedHeight(45)

        self.only_red = PillPushButton('Only Red', self, FluentIcon.BRUSH)
        self.only_red.setToolTip('apply on login screen')
        self.only_red.clicked.connect(FreeFire.onlyred)
        self.only_red.setFixedHeight(45)

        self.grid.addWidget(self.antiblacklist, 0, 0)
        self.grid.addWidget(self.antiban, 0,1)
        self.grid.addWidget(self.clear_reports, 1,1)
        self.grid.addWidget(self.only_red, 1,0)

        self.vbox.addLayout(self.grid)

        self.vbox.addItem(QSpacerItem(100,100, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.setObjectName('antiban-frame')
