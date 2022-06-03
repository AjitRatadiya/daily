import sys

from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class file(QWidget):
    def __init__(self):
        super(file, self).__init__()
        filebtn = QPushButton("upload file")
        filebtn.clicked.connect(self.get_file)
        textbtn = QPushButton("upload text")
        textbtn.clicked.connect(self.get_text)

        self.labelimg = QLabel()
        self.texteditior = QTextEdit()

        layout = QVBoxLayout()

        layout.addWidget(filebtn)
        layout.addWidget(self.labelimg)
        layout.addWidget(textbtn)
        layout.addWidget(self.texteditior)

        self.setLayout(layout)

    def get_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"<Default dir>",
                                                   "Image files (*.jpg *.jpeg *.gif)")
        self.labelimg.setPixmap(QPixmap(file_name))

    def get_text(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file_name = dialog.selectedFiles()

            if file_name[0].endswith('.py'):
                with open(file_name[0], 'r') as f:
                    data = f.read()
                    self.texteditior.setPlainText(data)
                    f.close()
            else:
                pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = file()
    a.show()
    sys.exit(app.exec_())

