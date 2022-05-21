#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/19 16:32:49
@Author      : Maxb
'''

'''
GUI应用程序是事件驱动的。 事件主要由应用程序的用户生成。 但它们也可以通过其他手段产生，例如：网络连接，窗口管理器或定时器。
当我们调用应用程序的exec_()方法时，应用程序进入主循环。 主循环获取事件并将其发送到对象。


在事件模型中，有三个参与者：

    事件来源

    事件对象

    事件目标


事件源是其状态更改的对象。 它会生成事件。 事件对象(event)将状态更改封装在事件源中。 事件目标是要通知的对象。 事件源对象将处理事件的任务委托给事件目标。


PyQt5具有独特的信号和插槽机制来处理事件。 信号和槽用于对象之间的通信。 发生特定事件时发出信号。 槽可以是任何Python可调用的函数。 当发射连接的信号时会调用一个槽。
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QDial, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # LCD数字
        lcd = QLCDNumber(self)
        # 仪表
        dial = QDial(self)
        
        # 设置窗口位置和大小
        self.setGeometry(700, 300, 350, 250)
        # 标题
        self.setWindowTitle("转动仪表")
        
        # 部件的位置和大小
        lcd.setGeometry(100, 50, 150, 60)
        dial.setGeometry(120, 120, 100, 100)
        
        # 转动dial（信号）连接LCD数字显示（槽）
        dial.valueChanged.connect(lcd.display)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())