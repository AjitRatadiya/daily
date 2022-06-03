from PyQt5.QtWidgets import QMainWindow

from practis.g.mainlayout import MainLayout


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("practic")
        self.setCentralWidget(MainLayout())
        self.show()
