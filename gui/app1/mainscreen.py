from PyQt5.QtWidgets import QMainWindow
import mainlayout
from PyQt5.QtGui import QIcon

class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.setWindowTitle("welcome")
        self.setStyleSheet("QMainWindow {background: #F2EBE9;}")
        self.setWindowIcon(QIcon("static/logo.png"))
        self.showMaximized()
        self.setCentralWidget(mainlayout.Main_Layout(self))
        self.show()