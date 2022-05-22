#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :
@Date            :2022/05/22 19:08:20
@Author          :xbMa
'''

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton,QMessageBox
from PyQt5.QtCore import Qt
import sys

'''
setChecked()	设置复选框的状态，设置为True表示选中，False表示取消选中的复选框
setText()	    设置复选框的显示文本
text()	        返回复选框的显示文本
isChecked()	    检查复选框是否被选中
setTriState()	设置复选框为一个三态复选框
setCheckState()	三态复选框的状态设置，具体设置可以见下表
'''

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 500, 300)
        self.cb1 = QCheckBox('全选',self)
        self.cb2 = QCheckBox('你是',self)
        self.cb3 = QCheckBox('我的',self)
        self.cb4 = QCheckBox('宝贝',self)

        bt = QPushButton('提交',self) 

        self.cb1.setGeometry(20, 20, 100, 50)
        self.cb2.setGeometry(20, 70, 100, 50)
        self.cb3.setGeometry(20, 120, 100, 50)
        self.cb4.setGeometry(20, 170, 100, 50)
        bt.setGeometry(20, 220, 100, 50)

        self.cb1.stateChanged.connect(self.changecb1)
        self.cb2.stateChanged.connect(self.changecb2)
        self.cb3.stateChanged.connect(self.changecb2)
        self.cb4.stateChanged.connect(self.changecb2)
        bt.clicked.connect(self.go)

        self.show()
    
    def go(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self,'I Love U','你是我的宝贝！')
        elif self.cb2.isChecked() and self.cb3.isChecked():
            QMessageBox.information(self,'I Love U','你是我的！')
        elif self.cb2.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self,'I Love U','你是宝贝！')
        elif self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self,'I Love U','我的宝贝！')
        elif self.cb2.isChecked():
            QMessageBox.information(self,'I Love U','你是！')
        elif self.cb3.isChecked():
            QMessageBox.information(self,'I Love U','我的！')
        elif self.cb4.isChecked():
            QMessageBox.information(self,'I Love U','宝贝！') 
        else:
            QMessageBox.information(self,'I Love U','貌似你没有勾选啊！')
    
    def changecb1(self):
        if self.cb1.checkState() == Qt.Checked:
            self.cb2.setChecked(True)
            self.cb3.setChecked(True)
            self.cb4.setChecked(True)
        elif self.cb1.checkState() == Qt.Unchecked:
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)
        
    def changecb2(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            self.cb1.setCheckState(Qt.Checked)
        elif self.cb2.isChecked() or self.cb3.isChecked() or self.cb4.isChecked():
            # tristate属性表示复选框是三种状态还是两种状态，
            # 如果tristate为True，则表示复选框有选中、未选中和半选中三种状态，
            # 如果tristate为False，则表示复选框只有选中、未选中两种状态。
            self.cb1.setTristate()
            # 半Qt.PartiallyChecked -> 选中
            self.cb1.setCheckState(Qt.PartiallyChecked)
        else:
            self.cb1.setTristate(False)
            # Qt.Unchecked --> 未选中
            # Qt.Checked --> 选中
            self.cb1.setCheckState(Qt.Unchecked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())