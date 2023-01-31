from os import system
system("cls")
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
import sys

class Win(QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("./src/icons/icon-calc.jpg"))
        self.resize(300,300)
        self.move(200,200)
        self.btn = QPushButton("=",self)
        self.btn.move(100,150)
        self.nine = QPushButton("9",self)
        self.nine.move(100,200)
        self.plus = QPushButton("+",self)
        self.plus.move(100,250)
        self.clear = QPushButton("clear",self)
        self.clear.move(100,300)
        self.edit = QLineEdit(self)
        self.edit.move(100,50)

        self.btn.clicked.connect(self.click)
        self.nine.clicked.connect(lambda: self.nineW("9"))
        self.plus.clicked.connect(lambda: self.plusW("+"))
        self.clear.clicked.connect(self.clearW)
        self.setStyleW(self.nine)
        self.setStyleW(self.plus)
        self.setStyleW(self.btn)


    def setStyleW(self, obj):
        obj.setStyleSheet('''
                background-color:orange
                ''')

    def click(self):
        text = self.edit.text()
        try:
            text = str(eval(text))
        except:
            text = "Error"
        self.edit.setText(text)

    def nineW(self, num):
        text = self.edit.text()
        text += num
        self.edit.setText(text)

    def clearW(self):
        self.edit.clear()

    def plusW(self, symbol):
        text = self.edit.text()
        if text[-1] != symbol:
            text +=symbol
            self.edit.setText(text)


app = QApplication(sys.argv)

win = Win()
win.show()

sys.exit(app.exec_())

