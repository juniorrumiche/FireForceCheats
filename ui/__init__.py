import sys
from PyQt5.QtGui import QIcon
from qfluentwidgets import FluentWindow, FluentIcon
from .combat import CombatFrame
from .antiban import AntibanFrame
from .visuals import  VisualsFrame


class MainWindow(FluentWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QIcon('ui/resources/icon.png'))
        self.setWindowTitle('FREE PANEL')

        self.combat_frame = CombatFrame(self)
        self.antiban_frame = AntibanFrame(self)
        self.visual_frame = VisualsFrame(self)

        self.addSubInterface(self.combat_frame, FluentIcon.GAME, 'Combat')
        self.addSubInterface(self.antiban_frame, FluentIcon.BRUSH, 'Antiban')
        self.addSubInterface(self.visual_frame, FluentIcon.VIEW, 'Visual')
        self.show()
