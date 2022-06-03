from mainscreen import MainScreen
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
import sys


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    app.setFont(QFont("arial", 15))
    ms = MainScreen()
    sys.exit(app.exec())