from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class TableDesign(QTableWidget):
    def __init__(self, data, headers):
        super(TableDesign, self).__init__()
        print(headers)
        self.setRowCount(len(data))
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

        for a in range(len(data)):
            for b in range(len(data[a])):
                self.setItem(a, b, QTableWidgetItem(str(data[a][b])))
