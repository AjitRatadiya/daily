from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget, QGridLayout, QPushButton


class Footer(QWidget):
    def __init__(self):
        super(Footer, self).__init__()

        f_layout = QGridLayout()

        fb_label = QLabel(self)
        fb_label.setOpenExternalLinks(True)
        fb_label.setText("<a href='https://github.com/AjitRatadiya'> FB </a>")

