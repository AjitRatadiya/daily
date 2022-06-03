from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from mainlayout import MainLayout


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()

        self.setGeometry(100, 100, 500, 500)
        self.setWindowIcon(QIcon("static/india.png"))
        self.setWindowTitle("Student Form")

        self.setCentralWidget(MainLayout())

        self.show()
