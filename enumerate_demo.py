#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of enumerate()
@Date     :2021/09/16 17:32:52
@Author      :xbMa
'''

'''
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
'''

s = ["a", "b", "c", "d", "e"]

print(list(enumerate(s)))

_s = enumerate(s)

for i, element in _s:
    print(f"{i}, {element}")

