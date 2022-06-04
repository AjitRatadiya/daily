from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
import pymongo


class MainLayout(QWidget):
    def __init__(self, view):
        super(MainLayout, self).__init__()

        self._view = view
        self.label = QLabel("Hii", self)
        self.label.setStyleSheet("QLabel {font:46px; color:243A73}")
        self.label.setGeometry(220, 50, 200, 100)
        self._view.showMaximized()




