from PyQt5.QtWidgets import QMainWindow

from gui.caculator.mainlayout import MainLayout


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.setWindowTitle("calculator")
        self.setFixedHeight(400)
        self.setFixedWidth(400)
        self.setStyleSheet("QMainWindow {background:black}")
        self.setCentralWidget(MainLayout())
        self.show()