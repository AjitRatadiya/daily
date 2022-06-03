import os.path
import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPlainTextEdit, QVBoxLayout, \
    QAction, QFileDialog, QMessageBox, QToolBar
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFontDatabase, QIcon, QKeySequence
from PyQt5.QtPrintSupport import QPrintDialog


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.path = None
        self.setWindowTitle("My Pad")
        self.setWindowIcon(QIcon("static/notepad.ico"))
        self.resize(450, 450)
        self.filterTypes = " text document (*.txt);; python (*.py) "
        fixedFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedFont.setPointSize(14)

        mainlayout = QVBoxLayout()

        # editor
        self.editor = QPlainTextEdit()
        self.editor.setFont(fixedFont)

        mainlayout.addWidget(self.editor)

        # apps
        container = QWidget()
        container.setLayout(mainlayout)

        self.setCentralWidget(container)

        # file menu

        file_menu = self.menuBar().addMenu("&file")

        # file toolbar

        file_toolbar = QToolBar("file")
        file_toolbar.setIconSize(QSize(60, 60))
        self.addToolBar(Qt.BottomToolBarArea, file_toolbar)

        # open , save and save As

        file_open_action = QAction(QIcon("./static/file_open.ico"), "open file...", self)
        file_open_action.setShortcut(QKeySequence.Open)
        file_open_action.triggered.connect(self.file_open)

        file_save_action = QAction(QIcon("./static/file_save.ico"), "save file...", self)
        file_save_action.setShortcut(QKeySequence.Save)
        file_save_action.triggered.connect(self.file_save)

        file_save_as_action = QAction(QIcon("./static/saveas.png"), "open file...", self)
        file_save_as_action.setShortcut(QKeySequence("Ctrl+Shift+S"))
        file_save_as_action.triggered.connect(self.file_save_as)

        file_print_action = QAction(QIcon("./static/print.ico"), "print file...", self)
        file_print_action.setShortcut(QKeySequence.Print)
        file_print_action.triggered.connect(self.file_print)

        file_menu.addActions([file_open_action, file_save_action, file_save_as_action, file_print_action])
        file_toolbar.addActions([file_open_action, file_save_action, file_save_as_action, file_print_action])

        # file menu

        edit_menu = self.menuBar().addMenu("&edit")

        # file toolbar

        edit_toolbar = QToolBar("edit")
        edit_toolbar.setIconSize(QSize(60, 60))
        self.addToolBar(Qt.BottomToolBarArea, edit_toolbar)

        # undo , redo and clear

        undo_action = QAction(QIcon("./static/undo.png"), "undo", self)
        undo_action.setShortcut(QKeySequence.Undo)
        undo_action.triggered.connect(self.editor.undo)

        redo_action = QAction(QIcon("./static/redo.png"), "redo", self)
        redo_action.setShortcut(QKeySequence.Redo)
        redo_action.triggered.connect(self.editor.redo)

        clear_action = QAction(QIcon("./static/clear.ico"), "clear text", self)
        clear_action.setShortcut(QKeySequence("Shift+C"))
        clear_action.triggered.connect(self.clear_text)

        edit_menu.addActions([undo_action, redo_action, clear_action])
        edit_toolbar.addActions([undo_action, redo_action, clear_action])

        edit_menu.addSeparator()
        edit_toolbar.addSeparator()

        # copy , past and select all

        copy_action = QAction(QIcon("./static/copy.png"), "copy", self)
        copy_action.setShortcut(QKeySequence.Copy)
        copy_action.triggered.connect(self.editor.copy)

        paste_action = QAction(QIcon("./static/past.png"), "paste", self)
        paste_action.setShortcut(QKeySequence.Paste)
        paste_action.triggered.connect(self.editor.paste)

        select_action = QAction(QIcon("./static/select.png"), "select", self)
        select_action.setShortcut(QKeySequence.SelectAll)
        select_action.triggered.connect(self.editor.selectAll)

        edit_menu.addActions([copy_action, paste_action, select_action])
        edit_toolbar.addActions([copy_action, paste_action, select_action])

        edit_menu.addSeparator()
        edit_toolbar.addSeparator()

    def updatetitle(self):
        self.setWindowTitle("{0}-MyPad".format(os.path.basename(self.path) if self.path else 'Untitled'))

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(parent=self, caption="open File", filter=self.filterTypes)
        if self.path:
            try:

                with open(path, 'r') as f:
                    text = f.read()
                    f.close()


            except Exception as e:
                print(e)
                self.dialog_message(str(e))
            else:
                self.path = path
                self.editor.setPlainText(text)
                self.updatetitle()

    def file_save(self):

        if self.path is None:
            self.file_save_as()
        else:
            try:
                text = self.editor.toPlainText()
                with open(self.path, 'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))

    def file_save_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "save file", self.filterTypes)
        text = self.editor.toPlainText()

        if not path:
            return
        else:
            try:
                with open(self.path, 'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))
            else:
                self.path = path
                self.updatetitle()

    def file_print(self):
        print = QPrintDialog()
        if print.exec_():
            self.editor.print_(print.printer())

    def dialog_message(self, msg):
        dlg = QMessageBox(self)
        dlg.setText(msg)
        # dlg.setIcon(QMessageBox.critical)
        dlg.show()


    def clear_text(self):
        self.editor.setPlainText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = MainScreen()
    obj.show()
    sys.exit(app.exec_())
