#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of lambda
@Date     :2021/09/16 16:37:00
@Author      :xbMa
'''

#匿名函数lambda
'''
lambda函数使用方法:

lambda pamr1,pamr2: function

pamr1/parm2 代表是参数  function 指的是实现逻辑
'''

# 声明函数
sum = lambda x, y : x+y

# 调用函数
_sum = sum(5,5)

print(_sum)
