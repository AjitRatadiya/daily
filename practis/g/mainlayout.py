from PyQt5.QtWidgets import QWidget, QPushButton

class MainLayout(QWidget):
    def __init__(self):
        super(MainLayout, self).__init__()
        self.btn = QPushButton("throw me ", self)