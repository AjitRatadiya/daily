from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QMessageBox, QPushButton
import pymongo
import mainlayout
import register_layout
from cryptography.fernet import Fernet

class Login_class(QWidget):
    def __init__(self, view):
        super(Login_class, self).__init__()

        self._view = view
        self.login_form()


    def login_form(self):
        '''***label***'''

        self.welcome_label = QLabel("Welcome", self)
        self.welcome_label.setStyleSheet("QLabel {font:46px; color:243A73}")
        self.welcome_label.setGeometry(220, 50, 200, 100)

        self.info_label = QLabel("login to your account", self)
        self.info_label.setStyleSheet("QLabel {font:16px;color:243A73;}")
        self.info_label.setGeometry(240, 90, 150, 100)

        '''***inputs***'''

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("username")
        self.username.setStyleSheet("QLineEdit{border-radius: 6px; font:16px; letter-spacing: 0.8px ;"
                                    "font-family: 'Rubik', sans-serif}")
        self.username.setGeometry(210, 230, 180, 40)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("enter password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("QLineEdit{border-radius: 6px; font:16px; letter-spacing: 0.8px ;"
                                    "font-family: 'Rubik', sans-serif}")
        self.password.setGeometry(210, 280, 180, 40)

        '''***buttons***'''

        self.btn_login = QPushButton("Login", self)
        self.btn_login.setStyleSheet("QPushButton {background: #9F141A; color:white; "
                                     "border-radius:4px;border: #27ae60 1px solid;}"
                                     "QPushButton::hover {background: black; color:white; "
                                     "border-radius:4px;border: #27ae60 1px solid;}")
        self.btn_login.setGeometry(250, 330, 100, 40)
        self.btn_login.clicked.connect(self.login_act)

        self.btn_register = QPushButton("register", self)
        self.btn_register.setStyleSheet("QPushButton {background: #063406; color:white; "
                                     "border-radius:4px;border: #27ae60 1px solid;}"
                                        "QPushButton::hover {background: black; color:white; "
                                     "border-radius:4px;border: #27ae60 1px solid;}")
        self.btn_register.setGeometry(250, 380, 100, 40)
        self.btn_register.clicked.connect(self.register_act)


    def login_act(self):
        db = pymongo.MongoClient("mongodb://localhost:27017")
        tb = db["users"]
        c = tb.admin_user

        '''**** getting data from form****'''
        form_user = self.username.text()
        print(form_user)
        form_password = self.password.text()
        print(form_password)

        '''******decoding passoword****'''

        key= Fernet.generate_key()
        f = Fernet(key)
        encrypted_password_from_user = f.encrypt(bytes(form_password, 'utf-8'))
        print(encrypted_password_from_user)



        '''**** checking user in database ***'''

        isvalid_user = c.find_one({"username": form_user, "password": form_password})
        print(isvalid_user)

        if isvalid_user == None:

            self.msg_box("invalid username or password")
            self.username.setPlaceholderText("username")
            self.password.setPlaceholderText("enter password")
        else:
            self._view.setCentralWidget(mainlayout.MainLayout(self._view))

    def register_act(self):

        self._view.setCentralWidget(register_layout.Register_class(self._view))

    def msg_box(self, msg):

        ms_box = QMessageBox(self)
        ms_box.setText(msg)

        ms_box.setStyleSheet("QMessageBox {background: #F2EBE9;} "
                             "QPushButton { QPushButton {background: #063406; color:white; "
                             "border-radius:4px;border: #27ae60 1px solid;}")
        ms_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ms_box.exec_()