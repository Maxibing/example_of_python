#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :
@Date            :2022/05/22 19:56:02
@Author          :xbMa
'''


'''
QComboBox类属性
editable                                设置是否可编辑
currentText                             设置当前列表框显示内容(前提是先在列表框添加内容)
currentIndex                            设置当前列表框显示内容的索引(前提是先在列表框添加内容)
maxVisibleitems                         当下拉列表弹出时，允许显示的最大子项目
maxCount                                设置下拉选项集合中的数目
insertPolicy                            设置用户在可编辑的组合框中输入一个新的字符串时插入的策略
NoInsert                                不插入
InsertAtTop                             在顶部插入
InsertAtCurrent                         在当前插入
InsertAtBottom                          在底部插入
InsertAfterCurrent                      在当前的后面插入
InsertBeforeCurrent                     在当前的前面插入
InsertAlphabetically                    按字母顺序插入
sizeAdjustPolicy                        大小调节策略
AdjustToContents                        根据所有内容的长度
AdjustToContentsOnFirstShow             根据第一次显示的内容长度
AdjustToMinimumContentsLength           适应最小内容长度
AdjustToMinimumContentsLengthWithIcon   适应最小内容长度与图标
minimumContentsLength                   最小的内容长度
iconSize                                图标大小
duplicatesEnabled                       设置用户在可编辑的组合框中重复添加
frame                                   边框
modelColumn                             设置显示的模型列

QComboBox信号
activated(QString)              与用户交互时，某个条目被选中发出信号，并传递条目的值
activated(int)                  与用户交互时，某个条目被选中发出信号，并传递条目的索引
currentIndexChanged(QString)    当前索引发生改变时发出信号，并传递改变之后的值（用户交互，代码控制）
currentIndexChanged(int)        当前索引发生改变时发出信号，并传递改变之后的索引（用户交互，代码控制）
currentTextChanged(QString)     当前文本内容发生改变时，并传递文本内容
editTextChanged(QString)        编辑的文本发生改变时发出信号，并传递文本内容
highlighted(QString)            在下拉列表中，鼠标移动到某个条目时发出信号，并传递条目的值
highighted(int)                 在下拉列表中，鼠标移动到某个条目时发出信号，并传递条目的索引
'''


import sys
from PyQt5.QtWidgets import QWidget, QComboBox, QApplication, QListWidgetItem, \
                            QListWidget, QCheckBox, QPushButton, QHBoxLayout, QLabel


class ComboxDemo(QWidget):
    def __init__(self):
        super().__init__()
        # 设置标题
        self.setWindowTitle('ComBox例子')
        # 设置初始界面大小
        self.resize(600, 500)

        # 实例化QComBox对象
        self.cb = QComboBox(self)
        self.cb.move(250, 100)

        # 单个添加条目
        self.cb.addItem('C')
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        # 多个添加条目
        self.cb.addItems(['Java', 'C#', 'PHP'])

        # 信号
        self.cb.currentIndexChanged[str].connect(self.print_value) # 条目发生改变，发射信号，传递条目内容
        self.cb.currentIndexChanged[int].connect(self.print_value)  # 条目发生改变，发射信号，传递条目索引
        self.cb.highlighted[str].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目内容
        self.cb.highlighted[int].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目索引

        # 实例化QComBox复选框对象
        self.items = ['a','b','c','d']
        self.box_list = []
        self.comb=QComboBox(self)
        self.comb.move(200, 200)
        self.listwidget = QListWidget(self)

        for i in range(len(self.items)):
            self.box_list.append(QCheckBox(self))
            self.box_list[i].setText(self.items[i])
            item = QListWidgetItem(self.listwidget)
            self.listwidget.setItemWidget(item, self.box_list[i])

        #QComboBox添加模型和视图,QListWidget设置为QComboBox的View，QListWidget的Model设置为QComboBox的Model
        self.comb.setModel(self.listwidget.model())
        self.comb.setView(self.listwidget)

        self.btn=QPushButton('ok',self)
        self.btn.clicked.connect(self.get_selected)
        self.layout=QHBoxLayout()
        self.layout.addWidget(self.comb)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)

    def print_value(self, i):
        print(i)

    def get_selected(self):
        ret = []
        for i in range(len(self.items)):
            if self.box_list[i].isChecked():
                ret.append(self.box_list[i].text())
        print(ret)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = ComboxDemo()
    comboxDemo.show()
    sys.exit(app.exec_())
