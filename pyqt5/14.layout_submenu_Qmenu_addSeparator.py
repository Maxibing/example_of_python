#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/20 16:21:16
@Author      : Maxb
'''


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu


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

        # 使用QMenu创建新菜单
        saveMenu = QMenu("保存方式(&S)", self)
        saveAct = QAction("保存...", self)
        saveAct.setShortcut("Ctrl+S")
        saveAct.setStatusTip("保存文件")
        saveasAct = QAction("另存为...(&O)", self)
        saveasAct.setStatusTip("文件另存为")
        # 两个动作使用addAction()被添加到子菜单中
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        newAct = QAction("新建(&N)", self)
        newAct.setShortcut("Ctrl+N")

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("文件(&F)")
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        # 添加分隔符
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())