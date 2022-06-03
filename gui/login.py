import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QGridLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QGridLayout()
        self.setGeometry(150, 100, 450, 450)

        userlabel = QLabel("username :", self)
        layout.addWidget(userlabel, 0, 0)
        useredit = QLineEdit(self)
        layout.addWidget(useredit, 0, 1)

        emaillabel = QLabel("Email :", self)
        layout.addWidget(emaillabel, 1, 0)
        emailedit = QLineEdit(self)
        layout.addWidget(emailedit, 1, 1)

        btn = QPushButton("Login", self)
        layout.addWidget(btn, 2, 0, 1, 2)
        btn.clicked.connect(self.check_login)

        self.setLayout(layout)

    def check_login(self):
        print("hii")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MainWindow()
    a.show()
    sys.exit(app.exec())