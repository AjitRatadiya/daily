import pymongo, sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget, QHeaderView, QPushButton, QVBoxLayout, \
    QTableWidgetItem, QHBoxLayout, QMessageBox


# noinspection SpellCheckingInspection,PyMissingOrEmptyDocstring
class MainLayout(QWidget):
    def __init__(self):
        super(MainLayout, self).__init__()

        self.new_rows = None
        db = pymongo.MongoClient("mongodb://localhost:27017")
        tb = db["student"]
        self.c = tb.result

        self.filed = ["name", "rollno", "maths", "science", "english"]

        self.table = QTableWidget(1, 5, self)
        self.table.setFixedSize(600, 400)
        self.table.setHorizontalHeaderLabels(["name", "rollno", "maths", "science", "english"])
        self.table.horizontalHeader().setDefaultSectionSize(100)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.verticalHeader().setDefaultSectionSize(30)

        tablelayout = QVBoxLayout(self)
        tablelayout.addWidget(self.table)
        self.setLayout(tablelayout)

        self.load_data()

        self.table.itemChanged.connect(self.item_changed)

        self.currentrow = self.table.rowCount()
        self.totalrow = self.currentrow
        print("current row count:", self.currentrow)

        self.add = QPushButton("add row", self)
        self.add.setFixedSize(100, 50)
        self.add.setStyleSheet("QPushButton" "{" "border: 4px solid yellow;" "background:gray;" "}")
        self.add.clicked.connect(self.add_row)

        self.save = QPushButton("save", self)
        self.save.setFixedSize(100, 50)
        self.save.setStyleSheet("QPushButton" "{" "border: 4px solid yellow;" "background:gray;" "}")
        self.save.clicked.connect(self.save_row)

        btnlayout = QHBoxLayout(self)
        tablelayout.addLayout(btnlayout)
        btnlayout.addWidget(self.add)
        btnlayout.addWidget(self.save)

    def load_data(self):

        self.data = list(self.c.find())
        row = 0

        self.table.setRowCount(len(self.data))
        # print(data)
        for d in self.data:
            print(d)
            self.table.setItem(row, 0, QTableWidgetItem(d["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(str(d["rollno"])))
            self.table.setItem(row, 2, QTableWidgetItem(str(d["maths"])))
            self.table.setItem(row, 3, QTableWidgetItem(str(d["science"])))
            self.table.setItem(row, 4, QTableWidgetItem(str(d["english"])))

            row = row + 1

    def add_row(self):
        rowcount = self.table.rowCount()
        self.table.insertRow(rowcount)

        self.totalrow += 1
        print("total row after add:", self.totalrow)

    def item_changed(self, item):
        try:
            row = item.row()
            col = item.column()
            print("row:", row)
            print("column:", col)
            updated_data = self.table.item(row, col).text()
            print("updated data:", updated_data)
            response_data = self.data[row]
            print("rep data:", response_data)
            uid = response_data["_id"]

            dic = {}

            if col == 0:
                dic["name"] = updated_data
            elif col == 1:
                dic["rollno"] = int(updated_data)
            elif col == 2:
                dic["maths"] = int(updated_data)
            elif col == 3:
                dic["science"] = int(updated_data)
            else:
                dic["english"] = int(updated_data)

            print("dictionry data:", dic)
            update_info = self.c.update_one({"_id": uid}, {"$set": dic})
            print(update_info)
        except Exception as e:
            print("error:", e)

    def save_row(self):
        count = 0
        self.new_rows = self.totalrow - self.currentrow
        print("new rows:", self.new_rows)

        for new_row in reversed(range(self.new_rows)):
            print(new_row)
            row = self.totalrow - (new_row + 1)
            print(row)
            table_roll_no = int(self.table.item(row, 1).text())
            print("table roll no:", table_roll_no)
            result = self.c.find_one({"rollno": table_roll_no})
            print(result)
            if result:
                msg = f" rollno :{table_roll_no} already Exist"
                self.mesbox(msg)
                count = 1
                self.table.removeRow(row)
                self.totalrow -= 1
            else:
                dic = {}
                for c in range(self.table.columnCount()):
                    data = self.table.item(row, c).text()
                    if data:
                        if c == 0:
                            dic[self.filed[c]] = data
                        else:
                            dic[self.filed[c]] = int(data)

                    else:
                        dic[self.filed[c]] = "Null"
                print("before insert of data")
                self.c.insert_one(dic)
                print(" after insert of data", dic)

        if count == 0:
            self.currentrow = self.table.rowCount()

    def mesbox(self, msg):
        # creating messagebox

        mbox = QMessageBox()
        mbox.setText(msg)
        mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mbox.exec_()


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()

        self.setWindowTitle("data table")
        self.setGeometry(400, 150, 450, 450)
        self.setCentralWidget(MainLayout())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = MainScreen()
    obj.show()
    sys.exit(app.exec_())
