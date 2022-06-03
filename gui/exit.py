import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "close window", "are you really want to exit the Application",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    a = MainWindow()
    a.show()

    sys.exit(app.exec())