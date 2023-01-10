from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd
import json
from PandasModel import PandasModel

Kword = ''
class Widget(QtWidgets.QWidget):
    def __init__(self, keyword,parent=None):
        self.keyword = keyword
        QtWidgets.QWidget.__init__(self, parent=None)
        vLayout = QtWidgets.QVBoxLayout(self)
        hLayout = QtWidgets.QHBoxLayout()
        self.pathLE = QtWidgets.QLineEdit(self)
        hLayout.addWidget(self.pathLE)
        self.loadBtn = QtWidgets.QPushButton("Begin to Search", self)
        hLayout.addWidget(self.loadBtn)
        vLayout.addLayout(hLayout)
        self.pandasTv = QtWidgets.QTableView(self)
        vLayout.addWidget(self.pandasTv)
        self.loadBtn.clicked.connect(self.loadFile)
        self.pandasTv.setSortingEnabled(True)

    def loadFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv)");
        print(fileName)
        # 读取 JSON 文件
        with open('table.json', 'r') as f:
            data = json.load(f)
        # 将 JSON 数据转换为 DataFrame
        df = pd.DataFrame(data)
        #self.pathLE.setText(fileName)
        #df = pd.read_csv(fileName)
        model = PandasModel(df)
        self.pandasTv.setModel(model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget(Kword)
    w.show()
    sys.exit(app.exec_())