from PyQt5.QtWidgets import QWidget, QVBoxLayout
from gui.app1.tabs.tabledesign import TableDesign


class Tab2(QWidget):
    def __init__(self):
        super(Tab2, self).__init__()

        self.tab2_layout = QVBoxLayout(self)
        data = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,33,44,55]]

        headers = ["first", "second", "third", "fourth", "five", "six"]

        self.tab2_layout.addWidget(TableDesign(data, headers))

        self.setLayout(self.tab2_layout)

