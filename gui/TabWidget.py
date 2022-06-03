import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QPushButton


class MainLayout(QWidget):
    def __init__(self):
        super(MainLayout, self).__init__()

        tabs = QTabWidget(self)

        tab1 = QWidget(self)
        loginlayout = QVBoxLayout(self)

        tab2 = QWidget(self)

        label = QLabel("this is lable", self)
        btn = QPushButton("fix", self)

        loginlayout.addWidget(label)
        loginlayout.addWidget(btn)
        tab1.setLayout(loginlayout)

        tabs.addTab(tab1, "Login")
        tabs.addTab(tab2, "register")

        vlayout = QHBoxLayout(self)
        vlayout.addWidget(tabs)
        self.setLayout(vlayout)


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.setWindowTitle("tab bar ")
        self.setFixedSize(450, 450)
        self.setCentralWidget(MainLayout())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = MainScreen()
    obj.show()

    sys.exit(app.exec_())