import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie


class MainScreen(QWidget):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.setFixedSize(250, 250)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.l = QLabel(self)

        self.movie = QMovie("static/wait-no.gif")
        self.l.setMovie(self.movie)

        timer = QTimer(self)

        self.startanimation()
        timer.singleShot(2000, self.stopanimation)

    def startanimation(self):
        self.movie.start()

    def stopanimation(self):
        self.movie.stop()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    m = MainScreen()
    m.setGeometry(100, 100, 250, 250)
    m.label = QLabel("this is main screen", m)
    m.show()

    sys.exit(app.exec())