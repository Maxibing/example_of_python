#coding:utf-8

import socket

client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
#创建一个客户端链接,socket.AF_INET代表ipv4，socket.SOCK_STREAM代表tcp套接字
client.connect(('192:168:26::154', 52235))
#客户端链接
print('[+]  链接成功')
#链接成功显示
while True:
    msg = input('>>>')
    if msg == 'quit':
        #如果输入的信息是quit  就退出链接
        break
    if len(msg) == 0:  #如果直接输入的一个回车的话
        #就重新输入,因为不能发送空 ，发送空的花  客户端会卡住
        continue
    client.send(bytes.fromhex(msg))
    #客户端发送信息msg  以hex格式发送数据
    data = client.recv(1024).hex().upper()
    if not data:
        #如果数据为空/0
        #服务器主动断开s
        break
        print('[+]  服务器主动断开了链接......')

    print('服务器发来：', data)

print('[+]  链接关闭...')

client.close()