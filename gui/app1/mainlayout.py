from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QTabWidget, QPushButton
from PyQt5.QtGui import QIcon

from gui.app1.login_layout import Login_class
from gui.app1.tabs import tab1, tab2, tab3


class Main_Layout(QWidget):
    def __init__(self, view):
        super(Main_Layout, self).__init__()

        self._view = view
        self._view.setWindowTitle("Trade Manager")

        self.label = QLabel("lbl", self)
        self.label.setGeometry(20, 10, 250, 100)
        self.pixmap = QPixmap('coretus.png')
        self.label.setPixmap(self.pixmap)

        self.logout_btn = QPushButton("logout", self)
        self.logout_btn.setGeometry(1250, 20, 70, 40)
        self.logout_btn.setStyleSheet("QPushButton {background: #9F141A; color:white; "
                                      "border-radius:4px;border: #27ae60 1px solid ;width:70px; height:40px;}"
                                      "QPushButton::hover {background: black; color:white; "

                                      "border-radius:4px;border: #27ae60 1px solid;}")

        print("h3")
        self.logout_btn.clicked.connect(self.logout)

        self.tabs1 = QTabWidget(self)
        self.tabs1.setStyleSheet("QTabWidget ::Tab {weight:150px; width:150px; font:14px}")
        self.tabs1.setGeometry(10, 100, 1350, 560)

        self.tabs1.addTab(tab1.Tab1(),QIcon("first.png"),"tab1")
        self.tabs1.addTab(tab2.Tab2(), "tab2")
        self.tabs1.addTab(tab3.Tab3(), "tab3")


    def logout(self):
        self._view.setCentralWidget(Login_class(self._view))


