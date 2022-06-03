import sys
from PyQt5.QtWidgets import QApplication

from practis.g.mainscreen import MainScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ms = MainScreen()
    sys.exit(app.exec())