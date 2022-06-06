import re
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QMessageBox, QPushButton
import pymongo
import login_layout
import mainlayout
import time
import base64


class Register_class(QWidget):
    def __init__(self, view):
        super(Register_class, self).__init__()

        self._view = view
        self.showMaximized()
        self.register_form()

    def register_form(self):
        '''***label***'''

        self.welcome_label = QLabel("Welcome", self)
        self.welcome_label.setStyleSheet("QLabel {font:46px; color:243A73}")
        self.welcome_label.setGeometry(620, 50, 200, 100)

        self.info_label = QLabel("register your account", self)
        self.info_label.setStyleSheet("QLabel {font:16px;color:243A73;}")
        self.info_label.setGeometry(640, 90, 150, 100)

        '''***inputs***'''

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("username")
        self.username.setStyleSheet("QLineEdit{border-radius: 6px; font:16px; letter-spacing: 0.8px ;"
                                    "font-family: 'Rubik', sans-serif}")
        self.username.setGeometry(570, 230, 280, 40)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("enter password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("QLineEdit{border-radius: 6px; font:16px; letter-spacing: 0.8px ;"
                                    "font-family: 'Rubik', sans-serif}")
        self.password.setGeometry(570, 280, 280, 40)

        '''***buttons***'''
        self.btn_register = QPushButton("register", self)
        self.btn_register.setStyleSheet("QPushButton {background: #063406; color:white; "
                                        "border-radius:4px;border: #27ae60 1px solid;}"
                                        "QPushButton::hover {background: black; color:white; "
                                        "border-radius:4px;border: #27ae60 1px solid;}" )
        self.btn_register.setGeometry(650, 340, 140, 40)
        self.btn_register.clicked.connect(self.register_act)

        self.btn_login = QPushButton("Login", self)
        self.btn_login.setStyleSheet("QPushButton {background: #9F141A; color:white; "
                                     "border-radius:4px;border: #27ae60 1px solid;}"
                                     "QPushButton::hover {background: black; color:white; "
                                     "border-radius:4px;border: #27ae60 1px solid;}")
        self.btn_login.setGeometry(650, 390, 140, 40)
        self.btn_login.clicked.connect(self.login_act)

    def login_act(self):
        self._view.setCentralWidget(login_layout.Login_class(self._view))

    def register_act(self):

        db = pymongo.MongoClient("mongodb://localhost:27017")
        tb = db["users"]
        c = tb.admin_user

        '''**** getting data from form****'''
        form_user = self.username.text()
        print(form_user)
        form_password = self.password.text()
        print(form_password)

        '''**** validating the user data ****'''

        reg_user = "[A-Za-z]{3,20}$"
        reg_password = "^(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        match_user = re.search(reg_user, form_user)
        match_password = re.search(reg_password, form_password)
        print(match_user)
        print(match_password)


        '''**** inserting user in database ***'''

        if match_user != None and match_password != None:

            form_password = bytes(form_password, 'utf-8')
            form_password = base64.b64encode(form_password)
            print("encoded: ", form_password)

            status = True
            expiry_time = time.time()
            print(expiry_time)
            response = c.insert_one({"username": form_user, "password": form_password, "expiry": expiry_time,
                                     "status": status})
            print(response)

            if response == None:

                self.msg_box(" user already exists")

            else:
                self._view.setCentralWidget(mainlayout.MainLayout(self._view))
        else:
            self.msg_box(" username cannot contail space and  password must be of 6 to 20 charecters "
                         "and must contain spycial symbols like @,#,$ and must have numbers in it")

    def msg_box(self, msg):

        ms_box = QMessageBox(self)
        ms_box.setText(msg)

        ms_box.setStyleSheet("QMessageBox {background: #F2EBE9;} "
                             "QPushButton { QPushButton {background: #063406; color:white; "
                             "border-radius:4px;border: #27ae60 1px solid;}")
        ms_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ms_box.exec_()