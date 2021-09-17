#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of set
@Date     :2021/09/17 10:09:05
@Author      :xbMa
'''

# 使用
weekdays = set(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"])

print(weekdays)

# 重复元素会被删除
s = set([1,2,3,3,4,5,6])
print(s)

# add方法
s.add(8)
print(s)

# add已有的元素不会报错
s.add(8)
print(s)

# remove元素，remove不存在的元素会报错
s.remove(8)
print(s)
