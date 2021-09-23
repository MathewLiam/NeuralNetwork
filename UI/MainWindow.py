from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from UI.Shared import MenuBar

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMenuBar(MenuBar.MenuBar())
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget.plot(hour, temperature, pen=pen)