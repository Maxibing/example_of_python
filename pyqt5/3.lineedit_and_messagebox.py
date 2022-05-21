#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/19 15:20:33
@Author      : Maxb
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
from random import randint
'''
    弹窗类型：
    QMessageBox.question
    QMessageBox.about
    QMessageBox.critical
    QMessageBox.warning
    QMessageBox.information
'''

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):
        # 窗口位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 标题
        self.setWindowTitle("猜数字")

        # 按钮
        self.bt1 = QPushButton("我猜", self)
        # 按钮大小
        self.bt1.setGeometry(115, 110, 70, 30)
        # 按钮提示
        self.bt1.setToolTip("<b>点击这里猜数字</b>")
        # 按钮按下（信号）连接弹窗提示（槽）
        self.bt1.clicked.connect(self.showMessage)

        # 单行文本输入框
        self.text = QLineEdit("在这里输入数字", self)
        # 选中所有文字
        self.text.selectAll()
        # 焦点置于文本输入框上
        self.text.setFocus()
        # 大小和位置
        self.text.setGeometry(80, 50, 150, 30)

        # 界面显示
        self.show()

    def showMessage(self):
        # 获取文本输入框中的数字
        guessnumber = int(self.text.text())
        print(self.num)

        # 判断数字大小并进行弹对话窗
        if guessnumber > self.num:
            QMessageBox.about(self, "结果", "猜大了")
            self.text.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, "结果", "猜小了")
            self.text.setFocus()
        else:
            QMessageBox.about(self, "结果", "猜对了！进入下一轮!")
            self.num = randint(1, 100)
            # 文本输入框清空
            self.text.clear()
            # 焦点置于文本输入框上
            self.text.setFocus()
    
    # 如果关闭QWidget就会生成QCloseEvent，这里重写closeEvent方法
    def closeEvent(self, event):
        # 弹确认提示框
        # 第一个参数是标题（不算self）
        # 第二个是内容
        # 第三个参数指定出现在的按钮组合
        # 最后一个是默认按钮
        reply = QMessageBox.question(self, "确认", "确认退出吗", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())