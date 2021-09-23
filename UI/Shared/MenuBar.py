from PyQt5 import QtGui
from PyQt5.QtWidgets import QMenuBar

class MenuBar(QMenuBar):
    def __init__(self):
        super(QMenuBar, self).__init__()
        self.addMenu("something")