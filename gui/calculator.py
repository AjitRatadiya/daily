import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QGraphicsColorizeEffect
from PyQt5.QtCore import Qt


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 360, 350)
        self.setFont(QFont('ariel', 15))

        self.uicomponents()
        self.show()

    def uicomponents(self):

        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 350, 70)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")
        self.label.setAlignment(Qt.AlignRight)

        self.init("push1", self.action1, "1", 5, 150, 80, 40)
        self.init("push2", self.action2, "2", 95, 150, 80, 40)
        self.init("push3", self.action3, "3", 185, 150, 80, 40)
        self.init("push4", self.action4, "4", 5, 200, 80, 40)
        self.init("push5", self.action5, "5", 95, 200, 80, 40)
        self.init("push6", self.action6, "6", 185, 200, 80, 40)
        self.init("push7", self.action7, "7", 5, 250, 80, 40)
        self.init("push8", self.action8, "8", 95, 250, 80, 40)
        self.init("push9", self.action9, "9", 185, 250, 80, 40)
        self.init("push0", self.action0, "0", 5, 300, 80, 40)

        self.init("push_plus", self.action_plus, "+", 275, 250, 80, 40)
        self.init("push_minus", self.action_minus, "-", 275, 200, 80, 40)
        self.init("push_milti", self.action_multi, "*", 275, 150, 80, 40)
        self.init("push_divi", self.action_divi, "/", 185, 300, 80, 40)
        self.init("push_point", self.action_point, ".", 95, 300, 80, 40)

        self.init("push_equal", self.action_equal, "=", 275, 300, 80, 40)
        self.init("push_clear", self.action_clear, "clear", 5, 100, 200, 40)
        self.init("push_del", self.action_del, "del", 210, 100, 145, 40)

    def init(self, btnname, actname, val, xval, yval, hval, wval):
        btnname = QPushButton(val, self)
        btnname.setGeometry(xval, yval, hval, wval)

        if btnname == "push_equal":
            c_effect = QGraphicsColorizeEffect()
            c_effect.setColor(Qt.blue)
            btnname.setGraphicsEffect(c_effect)
        btnname.clicked.connect(actname)

    def action1(self): self.act("1")
    def action2(self): self.act("2")
    def action3(self): self.act("3")
    def action4(self): self.act("4")
    def action5(self): self.act("5")
    def action6(self): self.act("6")
    def action7(self): self.act("7")
    def action8(self): self.act("8")
    def action9(self): self.act("9")
    def action0(self): self.act("0")

    def action_plus(self): self.act("+")
    def action_minus(self): self.act("-")
    def action_multi(self): self.act("*")
    def action_divi(self): self.act("/")
    def action_point(self): self.act(".")


    def act(self, val):
        text = self.label.text()
        self.label.setText(text + val)


    def action_equal(self):
        # get the label text
        equation = self.label.text()

        try:
            # getting the ans
            ans = eval(equation)

            # setting text to the label
            self.label.setText(str(ans))

        except:
            # setting text to the label
            self.label.setText("Wrong Input")

    def action_clear(self):
        # clearing the label text
        self.label.setText("")

    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        self.label.setText(text[:len(text) - 1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('breeze')

    obj = MainScreen()
    sys.exit(app.exec_())