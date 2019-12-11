from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QCheckBox, QVBoxLayout, QRadioButton, QLabel, QButtonGroup, QMessageBox


class MyRadioButton(QGroupBox):

    def __init__(self, parent):  # self는 MyApp 객체
        super().__init__()
        self.QMainWidow = parent
        self.setTitle('QRadioButton')
        self.init_ui()

    def init_ui(self):
        rbtn1 = QRadioButton('First Button', self)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.setText('Second Button')

        rbtn3 = QRadioButton(self)
        rbtn3.setText('status Toggle')

        self.lbl = QLabel('')

        rbtn1.clicked.connect(lambda: self.lbl.setText(rbtn1.text()))
        # rbtn2.clicked.connect(lambda: self.lbl.setText(rbtn2.text()))
        # rbtn1.clicked.connect(lambda state, btn=rbtn1: self.set_lblText(state, btn))
        rbtn2.clicked.connect(lambda state, btn=rbtn2: self.set_lblText(state, btn))

        rbtn3.clicked.connect(lambda state, button=rbtn3: self.show_message(state, button))

        rbtn3.toggled.connect(lambda: self.QMainWidow.statusBar().showMessage('rbtn {}'.format(rbtn3.isChecked())))

        btn_group = QButtonGroup()
        btn_group.addButton(rbtn1)
        btn_group.addButton(rbtn2)
        btn_group.addButton(rbtn3)

        vbox = QVBoxLayout()
        vbox.addWidget(rbtn1)
        vbox.addWidget(rbtn2)
        vbox.addWidget(rbtn3)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

    def set_lblText(self, state, button):
        self.lbl.setText("state {} button {}".format(state, button.text()))

    def show_message(self, state, button):
        QMessageBox.information(self, 'lambda test', 'rbtn3 text ' + button.text(), QMessageBox.Yes)
