#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/21 14:41:08
@Author      : Maxb
'''

'''
QLineEdit的一些显示方式
+-----------------------------+---------------------------------------------------+
|方式	                      |              描述                                  |
+-----------------------------+---------------------------------------------------+
|QLineEdit.Normal	          |    显示输入的字符。这是默认值。                      |
+-----------------------------+---------------------------------------------------+
|QLineEdit.NoEcho	          | 不要显示任何东西，这可能适用于密码长度保密的密码。     |
+-----------------------------+---------------------------------------------------+
|QLineEdit.Password		      | 显示与系统相关的密码掩码字符，而不是实际输入的字符。   |
+-----------------------------+---------------------------------------------------+
|QLineEdit.PasswordEchoOnEdit |   在编辑时输入时显示字符，否则                       |
+-----------------------------+---------------------------------------------------+

'''


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser, QLineEdit, QDialog, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator


class PasswdDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(350,100)
        self.setWindowTitle("密码输入框")

        self.lb = QLabel("请输入密码：",self)
        
        self.edit = QLineEdit(self)
        # 为密码输入框安装事件过滤器
        self.edit.installEventFilter(self)
        
        self.bt1 = QPushButton("确定",self)
        self.bt2 = QPushButton("取消",self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.bt1)
        hbox.addStretch(1)
        hbox.addWidget(self.bt2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.edit)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)

        # 不允许显示右键菜单
        self.edit.setContextMenuPolicy(Qt.NoContextMenu)
        # 显示灰色的占位符文本
        self.edit.setPlaceholderText("密码不超15位，只能有数字和字母，必须以字母开头")
        # 限定输入框中显示其包含信息的方式，这里设置的是：密码方式，即输入的时候呈现出原点出来
        self.edit.setEchoMode(QLineEdit.Password)

        # 限制输入，字母开头，不超过15位，只能包含字母或数字
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        # 为给定的字符模式构造一个正则表达式对象
        validator = QRegExpValidator(regx, self.edit)
        # 构造一个验证器
        self.edit.setValidator(validator)

        self.bt1.clicked.connect(self.Ok)
        self.bt2.clicked.connect(self.Cancel)
        
        object = QObject()
    
    # 事件过滤器
    # 事件过滤器是一个非常重要的概念。
    # 根据Qt的官方文档，如果对象被安装已监视对象的事件过滤器，则过滤事件。
    # 如果要过滤事件，需重新实现此函数时，若停止进一步处理，返回true； 否则返回false。
    def eventFilter(self, object, event):
        if object == self.edit:
            # 鼠标移动或鼠标双击对应的事件类型，需要过滤掉
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                # 全选、复制、粘贴对应的事件类型，需要过滤掉
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)#继续传递该事件到被观察者，由其本身调用相应的事件
        
    def Ok(self):
        self.text = self.edit.text()
        # 判断长度
        if len(self.text) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
        elif len(self.text) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
        # 最后使用done语句关闭对话框并将其结果设置为一个整数
        # 如果此对话框显示为exec（），那么done（）会导致本地事件循环完成，exec（）返回该整数。
        else:
            self.done(1)          # 结束对话框返回1
    
    def Cancel(self):
        self.done(0)          # 结束对话框返回0


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.resize(380,180)
        self.setWindowTitle('自定义密码输入对话框')
        
        self.lb1 = QLabel('密码在此显示...',self)
        self.lb1.move(20,20)

        
        self.bt1 = QPushButton('输入密码(普通型)',self)
        self.bt1.move(20,60)
        
        self.bt2 = QPushButton('输入密码(普通加强型)',self)
        self.bt2.move(20,100)
        
        self.bt3 = QPushButton('输入密码(特别加强型)',self)
        self.bt3.move(20,140)

        self.show()
          
        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)
        self.bt3.clicked.connect(self.showDialog)
        
    def showDialog(self):
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '密码输入框', '请输入密码：',QLineEdit.Password)
            if ok:
                self.lb1.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getText(self, '密码输入框', '请输入密码：',QLineEdit.PasswordEchoOnEdit)
            if ok:
                self.lb1.setText(text)
        else:
            pwd = PasswdDialog()
            r = pwd.exec_()
            if r:
                self.lb1.setText(pwd.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())