from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd
import json
from PandasModel import PandasModel

Kword = ''
class Widget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        vLayout = QtWidgets.QVBoxLayout(self)
        hLayout = QtWidgets.QHBoxLayout()
        self.input_box = QtWidgets.QLineEdit(self)
        hLayout.addWidget(self.input_box)
        self.loadBtn = QtWidgets.QPushButton("Begin to Search", self)
        hLayout.addWidget(self.loadBtn)
        vLayout.addLayout(hLayout)
        self.pandasTv = QtWidgets.QTableView(self)
        vLayout.addWidget(self.pandasTv)
        self.loadBtn.clicked.connect(self.on_input_changed)
        self.pandasTv.setSortingEnabled(True)

    def loadFile(self):
        #fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv)");
        #print(fileName)
        # 读取 JSON 文件
        with open('table.json', 'r') as f:
            data = json.load(f)
        # 将 JSON 数据转换为 DataFrame
        df = pd.DataFrame(data)
        ans_df = df[df.iloc[:,0].str.contains(self.keyword)]

        #self.pathLE.setText(fileName)
        #df = pd.read_csv(fileName)
        model = PandasModel(ans_df)
        self.pandasTv.setModel(model)

    def on_input_changed(self):
        # 获取输入框中的文本并保存在 keyword 变量中
        self.keyword = self.input_box.text()
        self.loadFile()
        print(self.keyword)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())