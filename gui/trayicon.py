import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget
from PyQt5.QtGui import QIcon


class MainScreen(QWidget):
    """
            main screen
    """
    def __init__(self):
        super(MainScreen, self).__init__()
        ti = QSystemTrayIcon(QIcon("static/india.png"), self)
        ti.setToolTip("demo")
        ti.show()

        menu = QMenu()
        exitact = menu.addAction("Exit App")
        exitact.triggered.connect(app.quit)

        ti.setContextMenu(menu)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainScreen()
    m.show()
    sys.exit(app.exec())