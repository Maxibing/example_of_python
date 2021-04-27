#coding:utf-8

import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#客户端链接
print('[+]  链接成功')
#链接成功显示
while True:
    msg = input('>>>')
    if msg == 'quit':
        #如果输入的信息是quit  就退出链接
        break
    if len(msg) == 0:#如果直接输入的一个回车的话
    #就重新输入,因为不能发送空 ，发送空的花  客户端会卡住
        continue
    client.sendto(bytes.fromhex(msg), ("192.168.29.128", 35523))
    #客户端发送信息msg  以hex格式发送数据
    data = client.recv(1500).hex().upper()
    if not data:
        #如果数据为空/0
        #服务器主动断开s
        break
        print('[+]  服务器主动断开了链接......')

    print('服务器发来：',data)


print('[+]  链接关闭...')

client.close()