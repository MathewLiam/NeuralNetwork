from PyQt5.QtWidgets import QApplication
import sys
from Modules.UI import MainWindow

def main():
    app = QApplication([])
    main = MainWindow.MainWindow()
    main.show()
    app.exec()

if __name__ == '__main__':
    main()