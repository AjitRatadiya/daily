import sys
from functools import partial

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 360, 350)
        self.setFont(QFont('ariel', 15))
        self.label = QLabel(self)

        self.uicomponents()
        self.show()

    def uicomponents(self):

        self.label.setGeometry(5, 5, 350, 70)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid grey;"
                                 "background : white;"
                                 "}")
        self.label.setAlignment(Qt.AlignRight)

        self.init("1", 5, 150, 80, 40)
        self.init("2", 95, 150, 80, 40)
        self.init("3", 185, 150, 80, 40)
        self.init("5", 95, 200, 80, 40)
        self.init("4", 5, 200, 80, 40)
        self.init("6", 185, 200, 80, 40)
        self.init("7", 5, 250, 80, 40)
        self.init("8", 95, 250, 80, 40)
        self.init("9", 185, 250, 80, 40)
        self.init("0", 5, 300, 80, 40)

        self.init("+", 275, 250, 80, 40)
        self.init("-", 275, 200, 80, 40)
        self.init("*", 275, 150, 80, 40)
        self.init("/", 185, 300, 80, 40)
        self.init(".", 95, 300, 80, 40)

        self.init("=", 275, 300, 80, 40)
        self.init("clear", 5, 100, 200, 40)
        self.init("del", 210, 100, 145, 40)

    def init(self, val, xval, yval, hval, wval):
        btnname = QPushButton(val, self)
        btnname.setGeometry(xval, yval, hval, wval)
        if val == "=":
            btnname.clicked.connect(self.action_equal)
        elif val == "clear":
            btnname.clicked.connect(self.action_clear)
        elif val == "del":
            btnname.clicked.connect(self.action_del)
        else:
            btnname.clicked.connect(partial(self.act, val))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_1:
            text = self.label.text()
            self.label.setText(text + "1")
        elif event.key() == QtCore.Qt.Key_2:
            text = self.label.text()
            self.label.setText(text + "2")
        elif event.key() == QtCore.Qt.Key_3:
            text = self.label.text()
            self.label.setText(text + "3")
        elif event.key() == QtCore.Qt.Key_4:
            text = self.label.text()
            self.label.setText(text + "4")
        elif event.key() == QtCore.Qt.Key_5:
            text = self.label.text()
            self.label.setText(text + "5")
        elif event.key() == QtCore.Qt.Key_6:
            text = self.label.text()
            self.label.setText(text + "6")
        elif event.key() == QtCore.Qt.Key_7:
            text = self.label.text()
            self.label.setText(text + "7")
        elif event.key() == QtCore.Qt.Key_8:
            text = self.label.text()
            self.label.setText(text + "8")
        elif event.key() == QtCore.Qt.Key_9:
            text = self.label.text()
            self.label.setText(text + "9")
        elif event.key() == QtCore.Qt.Key_0:
            text = self.label.text()
            self.label.setText(text + "0")
        elif event.key() == QtCore.Qt.Key_Plus:
            text = self.label.text()
            self.label.setText(text + "+")
        elif event.key() == QtCore.Qt.Key_Minus:
            text = self.label.text()
            self.label.setText(text + "-")
        elif event.key() == QtCore.Qt.Key_multiply:
            text = self.label.text()
            self.label.setText(text + "*")
        elif event.key() == QtCore.Qt.Key_division:
            text = self.label.text()
            self.label.setText(text + "/")
        elif event.key() == QtCore.Qt.Key_Period:
            text = self.label.text()
            self.label.setText(text + ".")
        elif event.key() == QtCore.Qt.Key_Backspace:
            text = self.label.text()
            self.label.setText(text[:len(text) - 1])
        elif event.key() == QtCore.Qt.Key_Delete:
            self.label.setText("")
        elif event.key() == QtCore.Qt.Key_Enter:
            equation = self.label.text()

            try:
                ans = eval(equation)
                self.label.setText(str(ans))

            except Exception as e:
                self.label.setText(str(e))

    def act(self, val):
        text = self.label.text()
        self.label.setText(text + val)

    def action_equal(self):
        # get the label text
        equation = self.label.text()

        try:
            # getting the ans
            print(equation)
            print("type:", type(equation))
            ans = eval(equation)
            print(type(ans))
            # setting text to the label
            self.label.setText(str(ans))
            # self.label.setPlaceholderText(str(ans))

        except Exception as e:
            self.label.setText(str(e))
            # self.msg_box(str(e))

    def action_clear(self):
        # clearing the label text
        self.label.setText("")

    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        self.label.setText(text[:len(text) - 1])

    def msg_box(self, msg):

        ms_box = QMessageBox(self)
        ms_box.setText(msg)

        ms_box.setStyleSheet("QMessageBox {background: #F2EBE9;} "
                             "QPushButton { QPushButton {background: #063406; color:white; "
                             "border-radius:4px;border: #27ae60 1px solid;}")
        ms_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ms_box.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('breeze')

    obj = MainScreen()
    sys.exit(app.exec())
