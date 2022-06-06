from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget

from gui.app1.login_layout import Login_class


class Header(QWidget):
    def __init__(self, view):
        super(Header, self).__init__()
        self._view = view

        self.vlayout = QHBoxLayout(self)

        print("header")
        self.label = QLabel()
        self.pixmap = QPixmap('../static/logo.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(40, 40)

        print("h1")
        print("h2")

        self.logout_btn = QPushButton("logout")
        self.logout_btn.setStyleSheet("QPushButton {background: #9F141A; color:white; "
                                      "border-radius:4px;border: #27ae60 1px solid ;width:70px; height:50px;}"
                                      "QPushButton::hover {background: black; color:white; "

                                      "border-radius:4px;border: #27ae60 1px solid;}")

        print("h3")
        self.logout_btn.clicked.connect(self.logout)
        self.vlayout.addWidget(self.label)
        self.vlayout.addWidget(self.logout_btn)
        self.vlayout.setAlignment(Qt.AlignRight)

    def logout(self):
        self._view.setCentralWidget(Login_class(self._view))
