from PyQt5.QtWidgets import QWidget, QVBoxLayout
from gui.app1.tabs.tabledesign import TableDesign


class Tab1(QWidget):
    def __init__(self):
        super(Tab1, self).__init__()

        self.tab1_layout = QVBoxLayout(self)
        data = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
        # for r in range(len(data)):
        #     for c in range(len(data[r])):
        #         i = data[r][c]

        headers = ["first", "second", "third", "fourth", "five"]

        self.tab1_layout.addWidget(TableDesign(data, headers))

        self.setLayout(self.tab1_layout)

