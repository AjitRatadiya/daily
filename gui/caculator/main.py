from PyQt5.QtWidgets import QApplication
import sys

from gui.caculator.mainscreen import MainScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = MainScreen()
    sys.exit(app.exec())