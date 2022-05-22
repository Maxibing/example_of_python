#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :
@Date            :2022/05/22 19:14:58
@Author          :xbMa
'''

'''
QButtonGroup
提供一个抽象的按钮容器，可以将多个按钮划分为一组，不具备可视化的效果，一般放的是可以被检查的按钮
QButtonGroup.checkedButton()返回的是被选中的按钮i，如果没有选中按钮，则返回-1
'''

from PyQt5.QtWidgets import QWidget, QRadioButton, QApplication, QPushButton, QMessageBox, QButtonGroup, QGridLayout
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.rb11 = QRadioButton('你是',self)
        self.rb12 = QRadioButton('我是',self)
        self.rb13 = QRadioButton('他是',self)
        self.rb21 = QRadioButton('大美女',self)
        self.rb22 = QRadioButton('大帅哥',self)
        self.rb23 = QRadioButton('小屁孩',self)

        bt1 = QPushButton('提交',self)
    
        self.setGeometry(500, 200, 500, 300)
        grid = QGridLayout(self)
        grid.addWidget(self.rb11, 0, 0)
        grid.addWidget(self.rb12, 1, 0)
        grid.addWidget(self.rb13, 2, 0)
        grid.addWidget(self.rb21, 0, 1)
        grid.addWidget(self.rb22, 1, 1)
        grid.addWidget(self.rb23, 2, 1)
        grid.addWidget(bt1, 3, 0)

        # 将单选按钮添加到分组中，同时分配一个id号
        # 函数默认的id是-1， 自动分配的ID保证为负数，从-2开始。
        # 如果您正在分配自己的ID，请使用正值来避免冲突。
        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.rb11, 11)
        self.bg1.addButton(self.rb12, 12)
        self.bg1.addButton(self.rb13, 13)

        self.bg2 = QButtonGroup(self)
        self.bg2.addButton(self.rb21, 21)
        self.bg2.addButton(self.rb22, 22)
        self.bg2.addButton(self.rb23, 23)

        self.info1 = ''
        self.info2 = ''

        # 当我们在分组中点击给定按钮的时候会发出buttonClicked()信号，
        # 同时我们连接到rbclicked这个槽函数上。
        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bg2.buttonClicked.connect(self.rbclicked)
        bt1.clicked.connect(self.submit)

        self.show()
        
    def submit(self):
        if self.info1 == '' or self.info2 == '':
            QMessageBox.information(self,'What?','貌似有没有选的啊，快去选一个吧！')
        else:
            QMessageBox.information(self,'What?',self.info1+self.info2)
        
    def rbclicked(self):
        # 我们判断到底是点了哪个分组，怎么判断？
        # 使用self.sender()函数将信号的产生对象送过来。
        # 然后根据checkedId()去获得这个按钮的id号，通过id号的判断我们到底是点了哪个单选按钮。
        sender = self.sender()
        if sender == self.bg1:
            if self.bg1.checkedId() == 11:
                self.info1 = '你是'
            elif self.bg1.checkedId() == 12:
                self.info1 = '我是'
            elif self.bg1.checkedId() == 13:
                self.info1 = '他是'            
            else:
                self.info1 = ''
        else:
            if self.bg2.checkedId() == 21:
                self.info2 = '大美女'
            elif self.bg2.checkedId() == 22:
                self.info2 = '大帅哥'
            elif self.bg2.checkedId() == 23:
                self.info2 = '小屁孩'            
            else:
                self.info2 = ''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())