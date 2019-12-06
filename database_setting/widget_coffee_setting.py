from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QWidget

from database_setting.db_connection.coffee_init_service import DBInitService


class WidgetCoffeeSetting(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("coffee.ui")
        self.ui.btn_init.clicked.connect(self.init)
        self.ui.btn_backup.clicked.connect(self.backup)
        self.ui.btn_restore.clicked.connect(self.restore)
        self.ui.show()
        self.db = DBInitService()

    def init(self):
        QMessageBox.about(self, "init", "init")
        self.db.service()

    def backup(self):
        QMessageBox.about(self, "backup", "backup")
        self.db.data_backup("product")
        self.db.data_backup("sale")

    def restore(self):
        QMessageBox.about(self, "restore", "restore")
        self.db.data_restore("product")
        self.db.data_restore("sale")
