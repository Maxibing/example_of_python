#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/20 15:32:03
@Author      : Maxb
'''


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 要获取状态栏，我们调用QtGui.QMainWindow类的statusBar()方法
        # showMessage()在状态栏上显示一条消息
        self.statusBar().showMessage("准备就绪")
        self.setGeometry(500, 200, 400, 300)
        self.setWindowTitle("QStatusBar")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
