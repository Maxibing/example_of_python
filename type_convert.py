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

# hex -> bin
b=bin(int("0201200B00",16))[2:]

