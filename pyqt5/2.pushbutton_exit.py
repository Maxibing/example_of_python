#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/19 14:31:03
@Author      : Maxb
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class PushButton_Exit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 标题
        self.setWindowTitle("PushButton Exit")

        # 初始化按钮
        qbtn = QPushButton("退出", self)
        # 点击退出按钮（信号）连接退出（槽）
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 鼠标放到按钮上时的提示
        qbtn.setToolTip("点击退出")
        # 设置按钮大小
        qbtn.resize(70, 30)
        # 设置按钮位置
        qbtn.move(50, 50)
        
        # 界面显示
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PushButton_Exit()
    sys.exit(app.exec_())
