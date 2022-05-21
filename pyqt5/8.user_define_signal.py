#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/20 08:04:38
@Author      : Maxb
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject


# 创建了一个名为showmouse的信号
class Signal(QObject):
    showmouse = pyqtSignal()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 300, 300)
        self.setWindowTitle("点击鼠标")

        # 将showmouse(信号)连接到about(槽)
        self.s = Signal()
        self.s.showmouse.connect(self.about)

        self.show()

    def about(self):
        QMessageBox.about(self, "鼠标", "你点鼠标了吧！")

    # 重写点击鼠标事件
    def mousePressEvent(self, e):
        self.s.showmouse.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
