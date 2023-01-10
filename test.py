import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.input_box = QLineEdit(self)
        self.input_box.resize(200, 40)
        self.input_box.move(50, 50)
        self.input_box.textChanged.connect(self.on_input_changed)

    def on_input_changed(self):
        # 获取输入框中的文本并保存在 keyword 变量中
        self.keyword = self.input_box.text()

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())