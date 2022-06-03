import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QSizePolicy, QMainWindow



class layout(QWidget):

    def __init__(self):
        super(layout, self).__init__()

        self.setWindowTitle("hi")
        self.setGeometry(100,100,500,500)
        values = ["a", "b", "c", "d", "e", "f"]
        positions = [(r, c) for r in range(2) for c in range(2)]
        lay = QGridLayout()
        self.setLayout(lay)
        for position, value in zip(positions, values):
            btn = QPushButton(value)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            lay.addWidget(btn, *position)
        self.show()



class first():

    def __init__(self):
        super(first, self).__init__()
        app = QApplication(sys.argv)
        ms = layout()
        sys.exit(app.exec())

first()