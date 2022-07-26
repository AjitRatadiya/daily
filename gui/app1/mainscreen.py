from PyQt5.QtWidgets import QMainWindow
import login_layout
from PyQt5.QtGui import QIcon


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()

        self.setWindowTitle("welcome")
        self.setStyleSheet("QMainWindow {background: #F2EBE9;}")
        self.setWindowIcon(QIcon("static/logo.png"))
        self.setCentralWidget(login_layout.Login_class(self))
        self.statusBar().showMessage('''                                            
           
           
           
           
           
           Conditions of Use & SalePrivacy NoticeCookies NoticeInterest-Based Ads Notice© 1996-2022, Coretus.com, Inc. or its affiliates      
                  
                  
                  
                  
                  ''')
        self.statusBar().setStyleSheet("background : gray; height:30px; ")
        self.showMaximized()
        # self.setStyleSheet("QMainWindow { height:100%; width:100%; }")
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.show()