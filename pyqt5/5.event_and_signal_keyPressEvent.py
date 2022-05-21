#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/19 16:32:49
@Author      : Maxb
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口位置和大小
        self.setGeometry(700, 300, 350, 250)
        # 标题
        self.setWindowTitle("按方向键")
        
        # 初始化标签
        self.lab = QLabel("方向", self)
        self.lab.setGeometry(150, 100, 50, 50)

        self.show()
    
    # 重写按键事件
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.lab.setText("↑")
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        else:
            self.lab.setText('→')
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())