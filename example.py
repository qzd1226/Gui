from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from main import Widget
import json
import pandas as pd

text = ''
with open('table.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle('新窗口')
        # self.resize(280, 230)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('keyword', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input keyword')
        self.show()
        print("1")


    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input ',
            'Enter the Keyword:')

        if ok:
            self.le.setText(str(text))
            print(text+"searching")
            Search = str(text)
            flag = True
            print("in")

            newWin.show()


app = QApplication(sys.argv)
ex = Example()
newWin = Widget(text)
print("here")
sys.exit(app.exec_())

