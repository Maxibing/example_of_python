#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :
@Date            :2022/05/22 20:26:18
@Author          :xbMa
'''

'''
QAbstractButton提供了大多数用于按钮的状态:
isDown()        指示按钮是否被按下。
isChecked()     指示按钮是否被选中。只有可被选中的按钮才能查看其选中的状态。
isEnabled()     指示按钮是否可以被用户按下。

与其他小部件相反，从QAbstractButton派生的按钮在禁用时接受鼠标和上下文菜单事件:
setAutoRepeat() 设置如果用户按住按钮，按钮是否自动重复。autoRepeatDelay和autoRepeatInterval定义如何自动重复。
setCheckable()  设置按钮是否为开关按钮。

QAbstractButton提供四种信号:
pressed()：当鼠标光标在按钮内时，鼠标左键被按下。
release()：当在释放鼠标左键时发出的。
clicked() ：当按钮第一次被按下，然后被释放；当快捷键被键入时；click()或者animateClick()被调用时。
toggle()：当开关按钮状态发生变化时发出的。

QAbstractButton类是按钮小部件的抽象基类，提供了按钮常见的功能。
这个类实现一个抽象按钮。该类的子类处理用户操作，并指定如何绘制按钮。
QAbstractButton支持普通按钮和开关按钮(按下去不会弹起来的那种按钮)。
按钮可否被选中这个特点在QRadioButton和QCheckBox类中实现的。
普通按钮的特性在QPushButton和QToolButton类中实现；如果有必要它们都提供了开关按钮的功能。

如果按钮是一个文本按钮，带有一个包含’&’的字符串，则QAbstractButton会自动创建一个快捷键。例如:
button = QPushButton('Ro&ck', self)
Alt+C快捷键被分配给按钮，即当用户按Alt+C时，按钮将调用animateClick()。要显示一个实际的“&”，请使用“&&”。

您还可以使用setShortcut()函数设置自定义快捷键。这对于没有任何文本的按钮来说是有用的，因此不能有任何自动的快捷方式。
button.setIcon(QIcon("print.png"))
button.setShortcut("Alt+F7")
'''

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QMessageBox, QGridLayout
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        self.resize(500,300)
        self.setWindowTitle('关注微信公众号：学点编程吧--抽象按钮的学习1（QAbstractButton）')

        label1 = QLabel('密码输入区',self)
        label2 = QLabel('正确密码：麻',self)
        label3 = QLabel('你输入的密码：',self)

        self.label4 = QLabel('  ',self)

        bt1 = QPushButton('芝',self)
        bt2 = QPushButton('麻',self)
        bt3 = QPushButton('开',self)
        bt4 = QPushButton('门',self)

        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 2, 0)
        grid.addWidget(self.label4, 3, 0)
        grid.addWidget(label3, 4, 0)
        grid.addWidget(bt1, 0, 1)
        grid.addWidget(bt2, 0, 2)
        grid.addWidget(bt3, 1, 1)
        grid.addWidget(bt4, 1, 2)

        self.setLayout(grid)
        
        # 此属性保存按钮是否可被选中
        bt1.setCheckable(True)
        bt2.setCheckable(True)
        bt3.setCheckable(True)
        bt4.setCheckable(True)

        # 此属性保存是否启用排它性。
        # 如果启用了自动排它性，那么属于同一个父部件的可选中按钮就会表现得好像它们是相同按钮组一部分一样
        # 在这个唯一按钮组中，任何时候只有一个按钮可以被选中；
        # 选中另一个按钮会自动取消之前选中过的按钮。此属性对属于其它按钮组的按钮没有影响。
        bt1.setAutoExclusive(True)
        bt2.setAutoExclusive(True)
        bt3.setAutoExclusive(True)
        bt4.setAutoExclusive(True)

        bt1.clicked.connect(self.setPassword)
        bt2.clicked.connect(self.setPassword)
        bt3.clicked.connect(self.setPassword)
        bt4.clicked.connect(self.setPassword)

        self.show()

    def setPassword(self):
        word = self.sender().text()
        self.label4.setText(word)
        if word == '麻':
            QMessageBox.information(self,'提示','恭喜，密码正确，可以进入！')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())