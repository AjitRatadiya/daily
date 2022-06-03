import  sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QSettings

class MainScreen(QWidget):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.settings = QSettings('MyQtApp', 'App1')

        try:
            self.resize(self.settings.value('window size'))
            self.move(self.settings.value('window position'))
        except:
            self.resize(450, 450)

    def closeEvent(self, event):
        self.settings.setValue('window size', self.size())
        self.settings.setValue('window position', self.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainScreen()
    m.show()
    sys.exit(app.exec())