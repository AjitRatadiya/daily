import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget


class MainClass(QWidget):
    def __init__(self):
        super(MainClass, self).__init__()

        self.setWindowTitle("key event")
        self.setFixedSize(600, 600)
        self.show()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_1:
            print("1")
        elif event.key() == QtCore.Qt.Key_Enter:
            print("enter")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    obj = MainClass()

    sys.exit(app.exec())