
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, QMainWindow

def mesbox():
    # creating messagebox
    mbox = QMessageBox()
    mbox.setText("hii this is first step")
    mbox.setDetailedText("welcome to our new home")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    mbox.exec_()


def vbox():

    w = QWidget()
    w.resize(300, 300)
    w.setWindowTitle("vertical box")

    btn1 = QPushButton("a")
    btn2 = QPushButton("b")
    btn3 = QPushButton("c")

    vb = QHBoxLayout(w)

    vb.addWidget(btn1)
    vb.addWidget(btn2)
    vb.addWidget(btn3)

    w.show()


def hbox():

    w = QWidget()
    w.resize(300, 300)
    w.setWindowTitle("horizontal")

    btn1 = QPushButton("a")
    btn2 = QPushButton("b")
    btn3 = QPushButton("c")

    vb = QHBoxLayout(w)

    vb.addWidget(btn1)
    vb.addWidget(btn2)
    vb.addWidget(btn3)

    w.show()
class guidisplay(QMainWindow):

    def __init__(self):
        super(guidisplay, self).__init__()
        self.setGeometry()
        self.setCentralWidget(QWidget)
    # app = QApplication(sys.argv)
    # w = QWidget()
    # w.resize(300, 300)
    # w.setWindowTitle("hello")
    #
    #
    # l = QLabel(w)
    # l.setText("welcome to giu")
    # l.move(100, 130)
    # l.show()
    #
    # vbtn = QPushButton(w)
    # vbtn.setText("vertical")
    # vbtn.move(50, 100)
    # vbtn.show()
    # vbtn.clicked.connect(vbox)
    #
    # hbtn = QPushButton(w)
    # hbtn.setText("horizontal")
    # hbtn.move(100, 150)
    # hbtn.show()
    # hbtn.clicked.connect(hbox)
    #
    # btn = QPushButton(w)
    # btn.setText("click me")
    # btn.move(150, 200)
    # btn.show()
    # btn.clicked.connect(mesbox)
    #
    # w.show()
    # sys.exit(app.exec_())


obj = guidisplay()




