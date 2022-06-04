from PyQt5.QtWidgets import QMainWindow
import login_layout

class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.setWindowTitle("welcome")
        # self.setFixedSize(600, 600)
        self.setMinimumHeight(600)
        self.setMinimumWidth(600)
        self.setStyleSheet("QMainWindow {background: #F2EBE9;}")
        self.setCentralWidget(login_layout.Login_class(self))
        # self.showMaximized()
        self.show()