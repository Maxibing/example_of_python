#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/21 15:08:45
@Author      : Maxb
'''


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QProgressDialog
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,150)
        self.setWindowTitle("QProgressDialog")

        self.lb = QLabel("文件数量",self)
        self.lb.move(20,40)

        self.bt1 = QPushButton('开始',self)
        self.bt1.move(20,80)

        self.edit = QLineEdit('100000',self)
        self.edit.move(100,40)

        self.show()

        self.bt1.clicked.connect(self.showDialog)
    
    def showDialog(self):
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")  
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")

        # 此属性保留对话框出现之前必须通过的时间。
        # 如果任务的预期持续时间小于minimumDuration，则对话框根本不会出现。
        progress.setMinimumDuration(5)

        # Qt.NonModal：非模态，可以和程序的其他窗口进行交互。
        # Qt.WindowModal:窗口模态，程序在未处理完当前对话框时，将阻止和对话框的父窗口进行交互。
        # Qt.ApplicationModal：应用程序模态，阻止和任何其他窗口进行交互。
        progress.setWindowModality(Qt.WindowModal)

        # 使用setMinimum() 和setMaximum() 或构造函数来设置操作中的“steps”数量，并在操作进行时调用setValue()。
        # setRange(0,num)就是设置其最小和最大值，这里最小值0，最大值num，num是根据输入框中的数字确定的
        progress.setRange(0,num) 
        for i in range(num):
            # setValue()该属性持有当前的进度
            progress.setValue(i) 
            # 通过wasCanceled()判断我们是否按下取消按钮，如果按下则提示失败
            if progress.wasCanceled():
                QMessageBox.warning(self,"提示","操作失败") 
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self,"提示","操作成功")
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())