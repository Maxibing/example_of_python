#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of zip()
@Date     :2021/09/16 17:19:43
@Author      :xbMa
'''

'''
zip函数的原型为：zip([iterable, …])

从参数中的多个迭代器取元素组合成一个新的迭代器
返回：一个zip对象，其内部元素为元组；可以转化成列表或元组
传入参数：元组、列表、字典等迭代器

'''
# 数组组合 
a = [1,2,3,4]
b = [5,6,7,8]
print(list(zip(a,b)))

# 长度不一的迭代器，会按最短的迭代器进行组合
c= (4,3,2,1)
d = (8,7,6)
print(list(zip(c,d)))

# 字典默认会将key进行组合
e = {"one": 1, "two": 2}
f = {"three": 3, "four": 4}
print(list(zip(e,f)))

# 逆操作
_ab = zip(a,b)
print(list(zip(*_ab)))
