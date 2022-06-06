from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QTabWidget

from gui.app1.footer.footer import Footer
from gui.app1.header.header import Header


class Main_Layout(QWidget):
    def __init__(self, view):
        super(Main_Layout, self).__init__()

        self._view = view
        self.showMaximized()
        self.Mlayout = QVBoxLayout(self)


        # tab1

        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout(self)
        self.label_1 = QLabel("tab 1 ", self)
        self.tab1_layout.addWidget(self.label_1)
        self.tab1.setLayout(self.tab1_layout)

        # tab2

        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout(self)
        self.label_2 = QLabel("tab 2 ", self)
        self.tab2_layout.addWidget(self.label_2)
        self.tab2.setLayout(self.tab2_layout)

        # tab3

        self.tab3 = QWidget()
        self.tab3_layout = QVBoxLayout(self)
        self.label_3 = QLabel("tab 3 ", self)
        self.tab3_layout.addWidget(self.label_3)
        self.tab3.setLayout(self.tab3_layout)

        # tab4

        self.tab4 = QWidget()
        self.tab4_layout = QVBoxLayout(self)
        self.label_4 = QLabel("tab 4 ", self)
        self.tab4_layout.addWidget(self.label_1)
        self.tab4.setLayout(self.tab4_layout)

        # tab5

        self.tab5 = QWidget()
        self.tab5_layout = QVBoxLayout(self)
        self.label_5 = QLabel("tab 5 ", self)
        self.tab5_layout.addWidget(self.label_5)
        self.tab5.setLayout(self.tab5_layout)

        # tab6

        self.tab6 = QWidget()
        self.tab6_layout = QVBoxLayout(self)
        self.label_6 = QLabel("tab 6 ", self)
        self.tab6_layout.addWidget(self.label_6)
        self.tab6.setLayout(self.tab6_layout)

        # tabs 1 parent tab

        self.tabs1 = QTabWidget(self)
        self.tabs1.setFixedSize(1350, 500)

        self.tabs1.addTab(self.tab1, "tab1")
        self.tabs1.addTab(self.tab2, "tab2")
        self.tabs1.addTab(self.tab3, "tab3")
        self.tabs1.addTab(self.tab4, "tab4")
        self.tabs1.addTab(self.tab5, "tab5")
        self.tabs1.addTab(self.tab6, "tab6")

        self.Mlayout.addWidget(Header(self._view))
        self.Mlayout.addWidget(self.tabs1)
        self.Mlayout.addWidget(Footer())
        self.setLayout(self.Mlayout)

