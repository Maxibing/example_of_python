#!/usr/bin/env python
# -*-coding=utf-8-*-

import sys
import time
import re
import socket
import threading
import ctypes
import inspect

from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QGroupBox, QFormLayout, QLabel, QPushButton, QGridLayout, QLineEdit, QTextEdit, QFormLayout
from PyQt5.QtCore import pyqtSignal, QRect, QRegExp
from PyQt5.QtGui import QColor
from PyQt5.Qt import QRegExpValidator, QIntValidator


class main(QMainWindow):

    # global
    global th_listen
    # 定义log信号
    _singal_log = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # 初始化界面
        self.initUI()
        # log信号与打印函数绑定
        self._singal_log.connect(self.mySingal_log)
        # 界面显示
        self.show()

    # 初始化界面
    def initUI(self):
        # 窗口大小及居中
        self.setGeometry(400, 400, 800, 600)
        self.center()
        # 标题
        self.setWindowTitle("IPv6 UDP Test")
        # 各UI元素
        self.initTextEdit()
        self.initButton()
        self.initLabel()
        self.initLineEdit()
        self.group_log()
        self.group_op()
        self.group_send()
        # 函数绑定
        self.bind_ui_func()

    # 绑定UI和函数
    def bind_ui_func(self):
        # 清空LOG
        self.btn_clear.clicked.connect(self.clear)
        # 发送
        self.btn_send.clicked.connect(self.send)
        # 监听
        self.btn_listen.clicked.connect(self.listen)
        # 停止
        self.btn_stop.clicked.connect(self.stop)

    # 窗口居中
    def center(self):
        # 得到了主窗口的大小
        qr = self.frameGeometry()
        # 获取屏幕的分辨率
        cp = QDesktopWidget().availableGeometry().center()
        # 得到中间点的位置
        qr.moveCenter(cp)
        # 把自己窗口的中心点放到qr的中心点
        self.move(qr.topLeft())

    # 初始化Label
    def initLabel(self):
        self.lab_src_addr = QLabel(self)
        self.lab_src_addr.setText("本地IPv6地址")

        self.lab_src_port = QLabel(self)
        self.lab_src_port.setText("本地端口")

        self.lab_dst_addr = QLabel(self)
        self.lab_dst_addr.setText("远端IPv6地址")

        self.lab_dst_port = QLabel(self)
        self.lab_dst_port.setText("远端端口")

    # 初始化LineEdit
    def initLineEdit(self):
        self.le_src_addr = QLineEdit(self)
        self.le_src_port = QLineEdit(self)
        self.le_dst_addr = QLineEdit(self)
        self.le_dst_port = QLineEdit(self)
        self.le_data = QLineEdit(self)

        # 预置的本机IPv6地址，后续优化成从系统读取
        self.le_src_addr.setText("192:168:137::22")

        # addr 限制
        addr_reg = QRegExp('[:a-fA-F0-9]+')
        addr_validator = QRegExpValidator(self)
        addr_validator.setRegExp(addr_reg)

        self.le_src_addr.setValidator(addr_validator)
        self.le_dst_addr.setValidator(addr_validator)

        # port 限制
        port_validator = QIntValidator(self)
        port_validator.setRange(1, 65535)
        self.le_src_port.setValidator(port_validator)
        self.le_dst_port.setValidator(port_validator)

        # data 限制
        data_reg = QRegExp('[a-fA-F0-9]+')
        data_validator = QRegExpValidator(self)
        data_validator.setRegExp(data_reg)
        self.le_data.setValidator(data_validator)

    # 初始化按钮
    def initButton(self):
        self.btn_send = QPushButton('发送', self)
        self.btn_listen = QPushButton('监听', self)
        self.btn_stop = QPushButton('停止', self)
        self.btn_clear = QPushButton('清空', self)

        # 停止按钮，初始化为不可按
        self.btn_stop.setEnabled(False)

    # log窗口
    def initTextEdit(self):
        self.logWindow = QTextEdit()
        # log窗只读
        self.logWindow.setReadOnly(True)
        # 最多1000行
        self.logWindow.document().setMaximumBlockCount(1000)
        # 底色(0,0,255)
        self.logWindow.setTextColor(QColor(0, 0, 255))

    # log框
    def group_log(self):
        # 定义及title
        group = QGroupBox(self)
        group.setGeometry(QRect(10, 10, 570, 510))
        group.setTitle("打印信息")
        # 添加Log窗
        self.group_log_layout = QGridLayout(group)
        self.group_log_layout.addWidget(self.logWindow, 0, 0)

    # 参数框
    def group_op(self):
        # 定义及title
        group = QGroupBox(self)
        group.setGeometry(QRect(590, 10, 200, 580))
        group.setTitle("参数")
        self.group_op_layout = QFormLayout(group)

        # 添加参数元素到参数框中
        self.group_op_layout.setWidget(0, QFormLayout.LabelRole,
                                       self.lab_src_addr)
        self.group_op_layout.setWidget(1, QFormLayout.LabelRole,
                                       self.le_src_addr)
        self.group_op_layout.setWidget(2, QFormLayout.LabelRole,
                                       self.lab_src_port)
        self.group_op_layout.setWidget(3, QFormLayout.LabelRole,
                                       self.le_src_port)
        self.group_op_layout.setWidget(4, QFormLayout.LabelRole,
                                       self.lab_dst_addr)
        self.group_op_layout.setWidget(5, QFormLayout.LabelRole,
                                       self.le_dst_addr)
        self.group_op_layout.setWidget(6, QFormLayout.LabelRole,
                                       self.lab_dst_port)
        self.group_op_layout.setWidget(7, QFormLayout.LabelRole,
                                       self.le_dst_port)
        self.group_op_layout.setWidget(8, QFormLayout.LabelRole,
                                       self.btn_listen)
        self.group_op_layout.setWidget(9, QFormLayout.LabelRole, self.btn_stop)
        self.group_op_layout.setWidget(10, QFormLayout.LabelRole,
                                       self.btn_clear)

    # 发送框
    def group_send(self):
        # 定义及title
        group = QGroupBox(self)
        group.setGeometry(QRect(10, 520, 570, 70))
        group.setTitle("发送")

        # 添加数据框和发送按钮
        self.group_send_layout = QGridLayout(group)
        self.group_send_layout.addWidget(self.le_data, 0, 0)
        self.group_send_layout.addWidget(self.btn_send, 0, 1)

    # 自定义LOG窗口追加信号
    def mySingal_log(self, str):
        # LOG添加时间戳
        self.logWindow.append(
            time.strftime("%Y-%m-%d %H:%M:%S  ", time.localtime()) + str)

    # 发送数据
    def send(self):
        # 获取远端端口及配置
        host = self.le_dst_addr.displayText()
        port = self.le_dst_port.displayText()
        data = self.le_data.displayText()

        # 判断地址
        ipv6_regex = r"[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){0,7}::[a-f0-9]{0,4}(:[a-f0-9]{1,4}){0,7}"
        if not re.match(ipv6_regex, host):
            self._singal_log.emit(
                "ERROR! Client address is invalid: Check address is right ipv6 address."
            )
            return

        # 判断端口
        if port == "" or int(port) < 1 or int(port) > 65535:
            self._singal_log.emit(
                "ERROR! Client Port is invalid: Check port in  1~65536.")
            return

        # 发送
        self.udpU6Client(host, port, data)

    # 清空Log
    def clear(self):
        self.logWindow.clear()

    # 监听
    def listen(self):
        # 读取输入框内容
        host = self.le_src_addr.displayText()
        port = self.le_src_port.displayText()

        # 判断地址
        ipv6_regex = r"[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){0,7}::[a-f0-9]{0,4}(:[a-f0-9]{1,4}){0,7}"
        if not re.match(ipv6_regex, host):
            self._singal_log.emit(
                "ERROR! Server address is invalid: Check address is right ipv6 address."
            )
            return

        # 判断端口
        if port == "" or int(port) < 1 or int(port) > 65535:
            self._singal_log.emit(
                "ERROR! Server Port is invalid: Check port in  1~65536.")
            return

        # 创建监听服务
        global th_listen
        th_listen = threading.Thread(target=self.udpU6Server,
                                     daemon=True,
                                     args=(host, port))
        th_listen.start()

    # 停止监听
    def stop(self):
        # 停止监听服务
        global th_listen
        self.stop_thread(th_listen)
        self._singal_log.emit("Stop listening IPv6 UDP Port ")

        # 修改按钮状态
        self.btn_listen.setEnabled(True)
        self.btn_stop.setEnabled(False)

    # udp client
    def udpU6Client(self, host, port, data):
        # 创建socket
        udpU6Client = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

        # 类型转换
        dst = (str(host), int(port))
        try:
            data_byte = bytes.fromhex(data)
        except ValueError:
            self._singal_log.emit("ERROR! Check send data must be hex.")
            return

        # 数据发送
        udpU6Client.sendto(data_byte, dst)

        # 打印发送的数据
        log = "Send to: " + str(dst) + "  Data:" + str(data)
        self._singal_log.emit(log)

    # udp server
    def udpU6Server(self, host, port):
        # 创建socket
        try:
            udpU6Server = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            # socket释放后可立刻被使用
            udpU6Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # 绑定端口
            src = (str(host), int(port))
            udpU6Server.bind(src)

            self._singal_log.emit("Start listening IPv6 UDP Port " + port)

            # 修改按钮状态
            self.btn_listen.setEnabled(False)
            self.btn_stop.setEnabled(True)

        except:
            self._singal_log.emit(
                "ERROR! Start listening failure. Check address and port is available."
            )
            return

        # 监听
        while True:
            udpU6Data, udpU6ServerInfo = udpU6Server.recvfrom(1024)

            # 打印监听到的socket及data
            udpU6Data_hex = udpU6Data.hex().upper()
            log = "Receive from: " + str(udpU6ServerInfo) + "  Data:" + str(
                udpU6Data_hex)
            self._singal_log.emit(log)

    # 定义raise
    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)

        if not inspect.isclass(exctype):
            exctype = type(exctype)

        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            tid, ctypes.py_object(exctype))

        if res == 0:
            raise ValueError("invalid thread id")

        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    # 定义杀掉线程的方法
    def stop_thread(self, thread):
        try:
            self._async_raise(thread.ident, SystemExit)
        except Exception as e:
            self._singal_log.emit("NOTE: stop thread raise a Exception: " + e)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())

# th_server = threading.Thread(target=udpU6Server, daemon=True, args=("192:168:137::22", 8002))
# th_server.start()
# time.sleep(20)
# stop_thread(th_server)
