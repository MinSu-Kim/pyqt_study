from PyQt5.QtWidgets import QWidget, QApplication
# 필요한 부분들을 불러옵니다. 기본적인 UI 구성요소를 제공하는 위젯(클래스)들은 PyQt5.QtWidgets 모듈에 포함

class MyApp(QWidget):

    def __init__(self):
        #  self는 MyApp 객체를 말함
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')  # 타이틀바에 나타나는 창의 제목을 설정
        self.move(300, 300)     # 위젯을 스크린의 x=300px, y=300px의 위치로 이동
        self.resize(400, 200)   # 위젯의 크기를 너비 400px, 높이 200px로 조절
        self.show()             # show() 메서드는 위젯을 스크린에 보여줌


if __name__ == '__main__':

    app = QApplication([])
    ex = MyApp()
    app.exec_()