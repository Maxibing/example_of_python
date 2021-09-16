#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of filter()
@Date     :2021/09/16 17:00:48
@Author      :xbMa
'''

'''
filter() 函数用于过滤序列，过滤掉不符合条件的元素

    语法：

    filter(function, iterable)

    参数

    function -- 判断函数。

    iterable -- 可迭代对象

    返回值：

    py2：返回结果为True的元素组成的列表
    py3: 返回Python2.x 中返回的是过滤后的列表, 而 Python3 中返回到是一个 filter 类。
    filter 类实现了 __iter__ 和 __next__ 方法, 可以看成是一个迭代器, 有惰性运算的特性, 相对 Python2.x 提升了性能, 可以节约内存。

'''
def _judge(i):
    if i > 7:
        return i

s = [1,2,8,9,10]

print(list(filter(_judge, s)))

# 配合匿名函数lambda使用
print(list(filter(lambda x:x > 5, s)))

