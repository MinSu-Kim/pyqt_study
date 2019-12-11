from PyQt5.QtWidgets import QGroupBox, QLabel, QVBoxLayout


class MyGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('제목')
        self.init_ui()

    def init_ui(self):
        label1 = QLabel('First Label', self)

        layout = QVBoxLayout()
        layout.addWidget(label1)

        self.setLayout(layout)