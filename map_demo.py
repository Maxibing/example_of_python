#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of map()
@Date     :2021/09/16 16:43:49
@Author      :xbMa
'''

'''
map(function,iterable,…)

    参数说明：

    function：函数
    iterable：一个或者多个序列

    返回值：

    py2返回列表
    py3 返回可迭代对象

'''

# 定义函数
def _add(k):
    return k + 1

lt = [1,2,3,4]

print(list(map(_add, lt)))
