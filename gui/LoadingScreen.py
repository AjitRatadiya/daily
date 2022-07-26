import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie


class MainScreen(QWidget):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.setFixedSize(250, 250)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.l = QLabel(self)

        self.movie = QMovie("static/wait-no.gif")
        self.l.setMovie(self.movie)
        self.movie.start()

    def stop_gif(self):
        timer = QTimer
        timer.singleShot(2000, self.stopanimation)

    def stopanimation(self):
        self.movie.stop()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    m = MainScreen()
    m.setGeometry(100, 100, 250, 250)
    m.show()
    m.stop_gif()
    sys.exit(app.exec())
