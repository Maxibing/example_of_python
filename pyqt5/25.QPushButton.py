#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :
@Date            :2022/05/22 19:40:01
@Author          :xbMa
'''


from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMenu
from PyQt5.QtCore import QTimer
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 500, 300)
        bt1 = QPushButton("这是什么",self)
        bt1.setGeometry(20, 100, 150, 50)

        self.bt2 = QPushButton('发送验证码',self)
        self.bt2.setGeometry(250, 100, 150, 50)

        menu = QMenu(self)
        menu.addAction('我是')
        menu.addSeparator()
        menu.addAction('世界上')
        menu.addSeparator()
        menu.addAction('最帅的')

        bt1.setMenu(menu)

        self.count = 10

        self.bt2.clicked.connect(self.Action)

        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)


        self.show()

    def Action(self):
        if self.bt2.isEnabled():
            self.time.start()
            self.bt2.setEnabled(False)
    
    def Refresh(self):
        if self.count > 0:
            self.bt2.setText(str(self.count)+'秒后重发')
            self.count -= 1
        else:
            self.time.stop()
            self.bt2.setEnabled(True)
            self.bt2.setText('发送验证码')
            self.count = 10


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())