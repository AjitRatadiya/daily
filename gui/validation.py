import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QGridLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class MainSceen(QWidget):
    def __init__(self):
        super(MainSceen, self).__init__()

        mainlayout = QGridLayout(self)
        namevalidator = QRegExpValidator(QRegExp(r'^[a-zA-Z]+$'))
        numbervalidator = QRegExpValidator(QRegExp(r'^[0-9]+$'))

        name = QLineEdit(self)
        name.setValidator(namevalidator)

        number = QLineEdit(self)
        number.setValidator(numbervalidator)

        mainlayout.addWidget(name, 0, 0)
        mainlayout.addWidget(number, 1, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = MainSceen()
    obj.show()
    sys.exit(app.exec())