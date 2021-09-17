#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of reduce
@Date     :2021/09/16 17:38:49
@Author      :xbMa
'''

'''
    reduce()函数在库functools里，如果要使用它，要从这个库里导入。

    语法：
    reduce(function,iterable,[,initializer])

        function: 函数，有两个参数
        interable: 可迭代对象
        initializer: 初始化值，可选
    
    
    reduce的工作过程是 ：
    在迭代sequence(tuple ，list ，dictionary， string等可迭代物)的过程中，
    首先把 前两个元素传给 函数参数，函数加工后，然后把得到的结果和第三个元素作为两个参数传给函数参数，
    函数加工后得到的结果又和第四个元素作为两个参数传给函数参数，依次类推。 如果传入了 initial 值， 
    那么首先传的就不是 sequence 的第一个和第二个元素，而是 initial值和 第一个元素。
    经过这样的累计计算之后合并序列到一个单一返回值
'''

from functools import reduce

# 累加
def _add(x, y):
    return x + y
print(reduce(_add, [1,2,3,4]))

# 把整数列表拼成整数
print(reduce(lambda x,y:x*10+y, [1,2,3,4,5]))

# 按性别分组
scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},
             {'name':'Dennis Ritchie', 'age':76, 'gender':'male'},
             {'name':'Ada Lovelace', 'age':202, 'gender':'female'},
             {'name':'Frances E. Allen', 'age':84, 'gender':'female'})

def group_by_gender(accumulator , value):
    accumulator[value['gender']].append(value['name'])
    return accumulator
    
grouped = reduce(group_by_gender, scientists, {'male':[], 'female':[]})
print(grouped)

