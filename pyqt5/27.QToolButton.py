#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :
@Date            :2022/05/22 20:16:55
@Author          :xbMa
'''

'''
QToolButton属性
ToolButtonIconOnly	        只显示图标
ToolButtonTextOnly	        只显示文字
ToolButtonTextBesideIcon	文字出现在图标旁边
ToolButtonTextUnderIcon	    文字出现在图标下方
ToolButtonFollowStyle	    遵循QStyle.StyleHint

QToolButton.DelayedPopup	按下按钮一定时间后，显示菜单。一个典型案例：浏览器中工具栏的“后退”按钮。
QToolButton.MenuButtonPopup	这种模式下，工具按钮显示一个特殊的箭头以指示菜单是否存在，按下按钮的箭头部分时显示菜单。
QToolButton.InstantPopup	按下工具按钮时菜单显示，无延迟。这种模式下，按钮自身的动作不触发。
'''


from PyQt5.QtWidgets import QWidget, QApplication, QToolButton, QMenu, QAction
from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtCore import QUrl, Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 500, 500)
        # 新建一个QToolButton对象。
        tb = QToolButton(self)
        # 该属性保持工具按钮是仅显示图标，仅显示文本，还是显示图标旁边/下方的文本
        tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # tb.setArrowType(Qt.DownArrow)
        # 这个很好理解，就是一个小贴士，当鼠标移动到按钮的时候就会显示信息。
        tb.setToolTip('选择适合你的支付方式')
        # 描述了弹出式菜单与工具按钮一起使用的方式:
        tb.setPopupMode(QToolButton.MenuButtonPopup)
        # 设置图标和文字。
        tb.setText('支付方式')
        tb.setIcon(QIcon('icon/bank.ico'))
        # 此属性保持是否启用自动升起。默认是禁用的（即False）。
        # 当使用QMacStyle时，此属性在macOS上当前被忽略。
        tb.setAutoRaise(True)
        tb.setGeometry(150, 100 ,200, 50)

        menu = QMenu(self)
        self.alipayAct = QAction(QIcon('icon/alipay.ico'),'支付宝支付', self)
        self.wechatAct = QAction(QIcon('icon/wechat.ico'),'微信支付', self)
        self.visaAct = QAction(QIcon('icon/visa.ico'),'Visa卡支付', self)
        self.master_cardAct = QAction(QIcon('icon/master_card.ico'),'万事达卡支付', self)

        menu.addAction(self.alipayAct)
        menu.addAction(self.wechatAct)
        menu.addSeparator()
        menu.addAction(self.visaAct)
        menu.addAction(self.master_cardAct)

        tb.setMenu(menu)
        self.show()

        self.alipayAct.triggered.connect(self.on_click)
        self.wechatAct.triggered.connect(self.on_click)
        self.visaAct.triggered.connect(self.on_click)
        self.master_cardAct.triggered.connect(self.on_click)
        
    def on_click(self):
        if self.sender() == self.alipayAct:
            QDesktopServices.openUrl(QUrl('https://www.alipay.com/'))
        elif self.sender() == self.wechatAct:
            QDesktopServices.openUrl(QUrl('https://pay.weixin.qq.com/index.php'))
        elif self.sender() == self.visaAct:
            QDesktopServices.openUrl(QUrl('https://www.visa.com.cn/'))
        else:
            QDesktopServices.openUrl(QUrl('https://www.mastercard.com.cn/zh-cn.html'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())