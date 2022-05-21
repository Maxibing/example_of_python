#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     : 
@Date     : 2022/05/21 10:50:19
@Author      : Maxb
'''


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QFontDialog, QFileDialog, QTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 500, 300)
        self.setWindowTitle("QColorDiag, QFontDialog, QFileDialog")

        self.tx = QTextEdit(self)
        self.tx.setGeometry(30, 30, 300, 260)

        self.bt1 = QPushButton("打开文件", self)
        self.bt1.move(350, 20)

        self.bt2 = QPushButton("选择字体", self)
        self.bt2.move(350, 70)

        self.bt3 = QPushButton("选择颜色", self)
        self.bt3.move(350, 120)

        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)

        self.show()

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, "打开文件", "./")
        if fname[0]:
            with open(fname[0], "r", encoding="utf-8", errors="ignore") as f:
                self.tx.setText(f.read())

    def choicefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)

    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


