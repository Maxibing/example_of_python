#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/19 17:09:37
@Author      : Maxb
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # 启用鼠标跟踪(默认是关闭的)，开启后，即使没有按钮被按下，小部件也会接收鼠标移动事件。
        # 当然不启用的话，在这里也可以按住鼠标左键
        self.setMouseTracking(True)

    def initUI(self):
        # 设置位置和大小
        self.setGeometry(500, 200, 1000, 500)
        # 标题
        self.setWindowTitle("移动鼠标")
        # 初始化标签
        self.lab = QLabel(self)
        self.lab.resize(500, 40)
        self.show()
        # 初始化位置属性
        self.pos = None
    
    # 重写鼠标移动事件
    def mouseMoveEvent(self, event):
        # 计算到中心点的距离，通过勾股定理
        distance_from_center = round(((event.y()-250)**2 + (event.x()-500)**2)**0.5)
        self.lab.setText(f"坐标: (x: {event.x()}, y: {event.y()})  离中心点距离: {distance_from_center}")
        # 将鼠标位置赋给位置属性
        self.pos = QPoint(event.pos())
        # 更新QWidget，必须调用函数update（）才能更新图形
        self.update()
    
    # QWidget类中的虚函数，用于ui的绘制，会在多种情况下被其他函数自动调用，比如update()时
    # 重写该事件
    def paintEvent(self, event):
        # 如果位置属性是QPoint类型，则更新线条
        if isinstance(self.pos, QPoint):
            q = QPainter(self)
            q.drawLine(0, 0, self.pos.x(), self.pos.y())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())