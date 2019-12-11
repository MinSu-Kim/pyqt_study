from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QScrollArea, QWidget, QApplication, QDesktopWidget, QGridLayout, \
    QPushButton

from widget.radiobutton import MyRadioButton


class MyApp(QMainWindow):

    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.statusBar()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QWidgets')  # 타이틀바에 나타나는 창의 제목을 설정
        # self.setGeometry(0, 0, 800, 600)
        self.resize(QSize(800, 600))

        grid = QGridLayout()
        grid.addWidget(MyRadioButton(self), 0, 0)

        widget = QWidget()
        widget.setLayout(grid)

        self.setCentralWidget(widget)

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = MyApp()
    app.exec_()
