from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class MenuBar(QMainWindow):
    def __init__(self):
        super(MenuBar, self).__init__()
        self.setGeometry(100, 100, 450, 450)
        menu = self.menuBar()
        filemenu = menu.addMenu("File")
        Editmenu = menu.addMenu("Edit")
        save_filemenu = filemenu.addAction("save")
        undo_editmenu = Editmenu.addAction("undo")

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = MenuBar()
    sys.exit(app.exec())