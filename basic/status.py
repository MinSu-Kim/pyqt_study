from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class MyStatusBar(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("status.ui")
        self.statusBar = self.ui.statusBar()
        self.statusBar.showMessage("Ready", 3000)
        self.ui.rb_show_message.clicked.connect(self.showMsg)
        self.ui.rb_current_message.clicked.connect(self.curMsg)
        self.ui.show()

    def curMsg(self):
        cur_msg = self.statusBar.currentMessage()
        QMessageBox.information(self, 'Message', 'Current Message =>' + cur_msg, QMessageBox.Yes)

    def showMsg(self):
        self.statusBar.showMessage("Clicked Show Message Radio Button")


if __name__ == "__main__":
    app = QApplication([])
    w = MyStatusBar()
    app.exec_()