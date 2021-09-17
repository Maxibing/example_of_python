#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of type covert
@Date     :2021/06/11 15:44:40
@Author      :xbMa
'''
# str -> bytes
s = "nnABhS4GRDpcDE3y"
b = s.encode()

# bytes -> str
b1 = b"hello world"
s1 = str(b1, encoding="utf-8")

# bytes -> hex
h = b1.hex()

# hex -> bytes
b2 = bytes.fromhex(h)


# hex -> int
i = int("0201200B00",base=16)

# hex -> bin
b=bin(int("0201200B00",16))[2:]

# int -> bits
i1 = int(b, base=2)

# int -> hex
i = 55
h1 = hex(i)

# int -> bytes
b3 = str(i).encode()
b4 = b"55"

# from_bytes
'''
    int.from_bytes() 功能是将字节转化成int型数字,'12'如果没有标明进制，看做ascii码值;
    '1' = 49 = 0011 0001, '2' = 50 = 0011 0010，如果byteorder = 'big', b'12' = 0011 0001 0011 0010 = 12594；
    如果byteorder = 'littlele', b'12' = 0011 0010 0011 0001 = 12849。第三个参数为signed表示有符号和无符号；
'''
i1 = int.from_bytes(b"12", byteorder="big")
i2 = int.from_bytes(b"12", byteorder="little")

# to_bytes
'''
    (number).to_bytes()功能将整数转化成byte
'''
b5 = (22).to_bytes(2, byteorder='big')

