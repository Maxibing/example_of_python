#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/19 11:11:47
@Author      : Maxb
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication

class SigSolt(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # 设置标题
        self.setWindowTitle("SigSolt")

        # LCD样式的数字
        lcd = QLCDNumber(self)
        # 滑块
        slider = QSlider(Qt.Horizontal, self)

        # 垂直布局
        vbox = QVBoxLayout()
        # 添加部件
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        # 设置布局
        self.setLayout(vbox)

        # 滑块数字变化（信号）连接数字显示（槽）
        slider.valueChanged.connect(lcd.display)
        
        # 调整大小
        self.resize(350, 250)


if  __name__ == "__main__":
    app = QApplication(sys.argv)
    qb = SigSolt()
    qb.show()
    sys.exit(app.exec_())