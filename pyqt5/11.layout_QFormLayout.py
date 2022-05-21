#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/20 14:25:37
@Author      : Maxb
'''

'''
表单控件

QFormLayout管理输入型控件和关联的标签组成的那些Form表单。

QFormLayout是一个方便的布局类,其中的控件以两列的形式被布局在表单中。
左列包括标签,右列包含输入控件,例如:QLineEdit、QSpinBox、QTextEdit等。
'''


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QFormLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 300, 200)
        self.setWindowTitle("QFormLayout")

        formlayout = QFormLayout()
        namelabel = QLabel("姓名")
        namelineedit = QLineEdit()
        introductionlabel = QLabel("简介")
        introductiontextedit = QTextEdit()

        formlayout.addRow(namelabel, namelineedit)
        formlayout.addRow(introductionlabel, introductiontextedit)

        self.setLayout(formlayout)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
