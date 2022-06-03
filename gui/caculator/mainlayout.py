from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt


class MainLayout(QWidget):

    def __init__(self):
        super(MainLayout, self).__init__()

        self.gl = QGridLayout(self)

        self.init_label()
        self.init_btn()
        self.set_cells()

        self.setLayout(self.gl)

    def init_label(self):

        self.label = QLabel(self)
        self.label.setFixedWidth(380)
        self.label.setFixedHeight(80)
        self.label.setWordWrap(True)
        self.label.setFont(QFont("arial", 18))
        self.label.setAlignment(Qt.AlignRight)
        self.label.setStyleSheet("QLabel {border: 4px solid gray; background:white}")

    def init_btn(self):

        self.btn9 = QPushButton("9", self)
        self.btn9.setFixedHeight(50)
        self.btn9.clicked.connect(self.action9)

        self.btn8 = QPushButton("8", self)
        self.btn8.setFixedHeight(50)
        self.btn8.clicked.connect(self.action8)

        self.btn7 = QPushButton("7", self)
        self.btn7.setFixedHeight(50)
        self.btn7.clicked.connect(self.action7)

        self.btn_plush = QPushButton("+", self)
        self.btn_plush.setFixedHeight(50)
        self.btn_plush.clicked.connect(self.action_plus)

        self.btn_clear = QPushButton("clear", self)
        self.btn_clear.setFixedHeight(50)
        self.btn_clear.setStyleSheet("QPushButton {border: 4px solid gray; background:red}")
        self.btn_clear.clicked.connect(self.action_clear)

        self.btn6 = QPushButton("6", self)
        self.btn6.setFixedHeight(50)
        self.btn6.clicked.connect(self.action6)

        self.btn5 = QPushButton("5", self)
        self.btn5.setFixedHeight(50)
        self.btn5.clicked.connect(self.action5)

        self.btn4 = QPushButton("4", self)
        self.btn4.setFixedHeight(50)
        self.btn4.clicked.connect(self.action4)

        self.btn_minus = QPushButton("-", self)
        self.btn_minus.setFixedHeight(50)
        self.btn_minus.clicked.connect(self.action_minus)

        self.btn_divide = QPushButton("/", self)
        self.btn_divide.setFixedHeight(50)
        self.btn_divide.clicked.connect(self.action_divide)

        self.btn3 = QPushButton("3", self)
        self.btn3.setFixedHeight(50)
        self.btn3.clicked.connect(self.action3)

        self.btn2 = QPushButton("2", self)
        self.btn2.setFixedHeight(50)
        self.btn2.clicked.connect(self.action2)

        self.btn1 = QPushButton("1", self)
        self.btn1.setFixedHeight(50)
        self.btn1.clicked.connect(self.action1)

        self.btn_multiplay = QPushButton("*", self)
        self.btn_multiplay.setFixedHeight(50)
        self.btn_multiplay.clicked.connect(self.action_multiplay)

        self.btn_equals = QPushButton("=", self)
        self.btn_equals.setFixedHeight(40)
        self.btn_equals.setStyleSheet("QPushButton {border: 4px solid gray; background:green}")
        self.btn_equals.clicked.connect(self.action_equals)

    def set_cells(self):

        self.gl.addWidget(self.label, 0, 0, 1, 9)
        self.gl.addWidget(self.btn9, 1, 0)
        self.gl.addWidget(self.btn8, 1, 1)
        self.gl.addWidget(self.btn7, 1, 2)
        self.gl.addWidget(self.btn_plush, 1, 3)
        self.gl.addWidget(self.btn_clear, 1, 4)
        self.gl.addWidget(self.btn6, 2, 0)
        self.gl.addWidget(self.btn5, 2, 1)
        self.gl.addWidget(self.btn4, 2, 2)
        self.gl.addWidget(self.btn_minus, 2, 3)
        self.gl.addWidget(self.btn_divide, 2, 4)
        self.gl.addWidget(self.btn3, 3, 0)
        self.gl.addWidget(self.btn2, 3, 1)
        self.gl.addWidget(self.btn1, 3, 2)
        self.gl.addWidget(self.btn_multiplay, 3, 3)
        self.gl.addWidget(self.btn_equals, 3, 4)

    '''  ************************     calculator functionality    *******************************    '''

    def action1(self):
        self.act("1")

    def action2(self):
        self.act("2")

    def action3(self):
        self.act("3")

    def action4(self):
        self.act("4")

    def action5(self):
        self.act("5")

    def action6(self):
        self.act("6")

    def action7(self):
        self.act("7")

    def action8(self):
        self.act("8")

    def action9(self):
        self.act("9")

    def action0(self):
        self.act("0")

    def action_plus(self):
        self.act("+")

    def action_minus(self):
        self.act("-")

    def action_multiplay(self):
        self.act("*")

    def action_divide(self):
        self.act("/")

    def action_point(self):
        self.act(".")

    def act(self, val):
        text = self.label.text()
        self.label.setText(text + val)

    def action_clear(self):
        self.label.setText(" ")

    def action_equals(self):
        text = self.label.text()

        try:
            ans = eval(text)
            self.label.setText(str(ans))
        except:
            self.label.setText("invalid input")
