from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QTabWidget, QTabBar, QStylePainter, QStyleOptionTab, QStyle

from gui.app1.tabs import tab1, tab2


class Tab3(QWidget):
    def __init__(self):
        super(Tab3, self).__init__()

        self.tabs1 = QTabWidget(self)
        self.tabs1.setStyleSheet("QTabWidget ::Tab {height:70px; width:100px; font:14px}")
        self.tabs1.setGeometry(10, 10, 1000, 500)
        self.tabs1.setTabBar(TabBar(self))
        self.tabs1.setTabPosition(QTabWidget.West)

        self.tabs1.addTab(tab1.Tab1(),"tab1")
        self.tabs1.addTab(tab2.Tab2(), "tab2")


class TabBar(QTabBar):
    def tabSizeHint(self, index):
        s = QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QStylePainter(self)
        opt = QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QStyle.CE_TabBarTabLabel, opt)
            painter.restore()
