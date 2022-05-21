#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/20 15:38:54
@Author      : Maxb
'''


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("准备就绪")
        self.setGeometry(500, 200, 400, 300)

        exitAct = QAction("退出(&E)", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("退出程序")
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(exitAct)
        
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())