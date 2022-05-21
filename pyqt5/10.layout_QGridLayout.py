#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/20 09:16:01
@Author      : Maxb
'''

'''
QGridLayout - 格栅布局,网格布局,多行多列

栅格布局将位于其中的窗口部件放入一个网状的栅格之中。QGridLayout需要将提供给它的空间划分成的行和列,并把每个窗口部件插入并管理到正确的单元格。

栅格布局是这样工作的:它计算了位于其中的空间,然后将它们合理的划分成若干个行(row)和列(column),并把每个由它管理的窗口部件放置在合适的单元之中,
这里所指的单元(cell)即是指由行和列交叉所划分出来的空间。

坐标分布是这样的:
        +-----+-----+-----+-----+-----+
        | 0,0 | 0,1 | 0,2 | 0,3 | 0,4 |
        +-----+-----+-----+-----+-----+
        | 1,0 | 1,1 | 1,2 | 1,3 | 1,4 |
        +-----+-----+-----+-----+-----+
        | 2,0 | 2,1 | 2,2 | 2,3 | 2,4 |
        +-----+-----+-----+-----+-----+
        | 3,0 | 3,1 | 3,2 | 3,3 | 3,4 |
        +-----+-----+-----+-----+-----+
        | 4,0 | 4,1 | 4,2 | 4,3 | 4,4 |
        +-----+-----+-----+-----+-----+

'''


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry(500, 200, 400, 300)
        self.setWindowTitle("GridLoyout")

        self.lcd = QLCDNumber()
        grid.addWidget(self.lcd, 0, 0, 3, 0)
        grid.setSpacing(10)

        names = ['cls', 'bc', '', 'close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '3', '2', '1', '-',
                '0', '.', '=',  '+']

        positions = [(i,j) for i in range(4,9) for j in range(4,8)]

        for position, name in zip(positions, names):
            if name == "":
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.cli)

        self.show()

    def cli(self):
        sender = self.sender().text()
        ls = ['/', '*', '-', '+']
        if sender in ls:
            self.lcd.display("A")
        else:
            self.lcd.display(sender)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())