import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QVBoxLayout, QTabWidget, QPushButton, QLabel, QLineEdit


class MainScreen(QWidget):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.resize(450, 450)

        mainlayout = QGridLayout()
        self.setLayout(mainlayout)

        vlayout1 = QVBoxLayout

        # tab1.1

        self.tab1_1 = QWidget()
        self.tab1_1.layout = QVBoxLayout()

        self.label = QLabel("type something")
        self.lineedit = QLineEdit()
        self.btn = QPushButton("print")

        self.tab1_1.layout.addWidget(self.label)
        self.tab1_1.layout.addWidget(self.lineedit)
        self.tab1_1.layout.addWidget(self.btn)

        self.tab1_1.setLayout(self.tab1_1.layout)

        # tab1.2

        self.tab1_2 = QWidget()
        self.tab1_2.layout = QVBoxLayout()

        self.btn = QPushButton("btn")
        self.btn.clicked.connect(lambda: print("hello"))

        self.tab1_2.layout.addWidget(self.btn)

        self.tab1_2.setLayout(self.tab1_2.layout)


        # tabs 1 parent tab

        self.tabs1 = QTabWidget()
        self.tabs1.addTab(self.tab1_1, "tab1_1")
        self.tabs1.addTab(self.tab1_2, "tab1_2")


        # tabs 2 parent tab
        self.btnpush = QPushButton("just a btn")

        self.tabs2 = QTabWidget()
        self.tabs2.addTab(self.btnpush, "tab2_1")

        # mainlayout manager

        mainlayout.addWidget(self.tabs1, 0, 0)
        mainlayout.addWidget(self.tabs2, 0, 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainScreen()
    m.show()
    sys.exit(app.exec())