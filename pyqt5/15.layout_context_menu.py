#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/21 08:10:33
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

        self.show()

    # 要使用上下文菜单,我们必须重新实现contextMenuEvent()方法
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("新建")
        opnAct = cmenu.addAction("保存")
        quitAct = cmenu.addAction("退出")
        # 使用exec_()方法显示上下文菜单。 从事件对象获取鼠标指针的坐标。
        # mapToGlobal()方法将窗口小部件坐标转换为全局屏幕坐标。
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

