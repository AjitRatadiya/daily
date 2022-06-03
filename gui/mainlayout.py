from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout, QComboBox


class MainLayout(QWidget):
    def __init__(self):
        super(MainLayout, self).__init__()

        self.fnamel = QLabel("surname:", self)
        self.fnamele= QLineEdit(self)
        self.namel = QLabel("name:", self)
        self.namele= QLineEdit(self)
        self.lname = QLabel("last name:", self)
        self.lnamele= QLineEdit(self)

        self.cname = QLabel("select favorite subject:", self)
        self.combo = QComboBox(self)
        self.comboadd()

        self.showbtn = QPushButton("show info", self)
        self.resetbtn = QPushButton("reset", self)

        self.grid = QGridLayout(self)
        self.gridadd()

        self.showbtn.clicked.connect(self.showinfo)
        self.resetbtn.clicked.connect(self.resetinfo)

    def comboadd(self):
        self.combo.addItems(["c", "c++", "php", "java", "python"])

    def gridadd(self):

        self.grid.setRowStretch(4, 4)
        self.grid.setColumnStretch(4, 4)

        self.grid.addWidget(self.fnamel, 0, 0)
        self.grid.addWidget(self.fnamele, 0, 1)
        self.grid.addWidget(self.namel, 1, 0)
        self.grid.addWidget(self.namele, 1, 1)
        self.grid.addWidget(self.lname, 2, 0)
        self.grid.addWidget(self.lnamele, 2, 1)
        self.grid.addWidget(self.cname, 3, 0)
        self.grid.addWidget(self.combo, 3, 1)
        self.grid.addWidget(self.showbtn, 4, 0)
        self.grid.addWidget(self.resetbtn, 4, 1)

    def showinfo(self):
        first_name = self.fnamele.text()
        middle_name = self.namele.text()
        last_name = self.lnamele.text()

        fav_subject = self.combo.currentText()

        mbox = QMessageBox(self)
        mbox.setText("first name: %s"%str(first_name)+
                     "\n middle name : %s"%str(middle_name)+"last name :%s"%str(last_name)+
                     "favorite subject :%s"%str(fav_subject))
        mbox.exec()

    def resetinfo(self):

        self.fnamele.clear()
        self.namele.clear()
        self.lnamele.clear()

        # self.combo.clear()
        self.combo.setCurrentText("php")
