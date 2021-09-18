#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Tuple common operations
@Date     :2021/09/18 14:31:11
@Author      :xbMa
'''

# Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号()，列表使用方括号[]
a = ("sa", "sd", "sc")

# 查找元素 index()
print(a.index("sa", 0, len(a)))

# 查找元素 count()
print(a.count("sc"))
