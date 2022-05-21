#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/20 08:40:28
@Author      : Maxb
'''

'''
箱式布局

QHBoxLayout和QVBoxLayout是基本的布局类,它们在水平和垂直方向上排列小部件。
为了创建必要的空间，我们添加一个拉伸因子(addstretch())
'''


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 300, 300)
        self.setWindowTitle("Layout")

        bt1 = QPushButton("剪刀", self)
        bt2 = QPushButton("石头", self)
        bt3 = QPushButton("布", self)

        # 创建水平布局
        hbox = QHBoxLayout()
        # 添加拉伸因子和三个按键，这样三个按键就会被推到窗口的右边
        hbox.addStretch(1)
        hbox.addWidget(bt1)
        hbox.addWidget(bt2)
        hbox.addWidget(bt3)

        # 创建垂直布局
        vbox = QVBoxLayout()
        # 添加拉伸因子
        vbox.addStretch(1)
        # 将水平布局添加至垂直布局中，拉伸因子将水平布局推到窗口底部
        vbox.addLayout(hbox)
        
        # 设置窗口的主要布局
        self.setLayout(vbox)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())