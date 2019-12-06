from PyQt5.QtWidgets import QApplication

from database_setting.widget_coffee_setting import WidgetCoffeeSetting

if __name__ == "__main__":
    app = QApplication([])
    w = WidgetCoffeeSetting()
    app.exec_()