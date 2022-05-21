#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/21 09:35:44
@Author      : Maxb
'''


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("准备就绪")
        self.setGeometry(500, 200, 400, 300)
        self.setWindowTitle("Context Menu")

        exitAct = QAction("退出(&E)", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("退出")
        exitAct.triggered.connect(qApp.quit)

        saveMenu = QMenu("保存方式(&S)", self)
        saveAct = QAction("保存...", self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        saveasAct = QAction('另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        newAct = QAction('新建(&N)',self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar("工具栏")
        toolbar.addAction(newAct)
        toolbar.addAction(exitAct)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())