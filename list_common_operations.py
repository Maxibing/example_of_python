#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :List common operations
@Date     :2021/09/18 11:24:46
@Author      :xbMa
'''

# for循环遍历
l = [1,2,3,4]
for i in l:
    print(i)

# 列表推导式 - 普通方式
a = [x for x in range(10)]
print(a)

# 列表推导式 - 在循环过程中添加if判断
b = [x for x in range(100) if x % 10 == 0]
print(b)

# 列表推导式 - 多个fot循环
c = [(x,y) for x in range(4) for y in range(3)]
print(c)

# append() 添加元素
a = [1,2,3,4]
print(a)
a.append(4)
print(a)

# extend() 把一个序列seq的内容添加到列表中
b = [5,6,7]
a.extend(b)
print(a)
a.append(b)
print(a)

# insert() 在指定位置index前插入元素
# insert(index, object)
b.insert(1, 2)
print(b)

# 修改元素 通过下标来确定要修改的是哪个元素
a[-1] = 10
print(a)

# 查找元素 in 和 not in 
print(5 in b)
print(5 not in b)

# 查找元素 index()
c = [1,2,3,4,5]
print(c.index(3, 0, len(c)))

# 查找元素 count()
print(c.count(5))

# 删除元素 del 根据下标进行删除
d = [1,2,3,4]
del d[0]
print(d)

# 删除元素 pop() 删除最后一个元素
d.pop()
print(d)

# 删除元素 remove 根据元素的值进行删除
d.remove(3)
print(d)

# 排序 sort() sort方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。
a =  [2,4,2,1,6,3]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 排序 reverse() 将list逆置
b =[1,2,3,4,5]
b.reverse()
print(b)

# 列表的嵌套
a = [1, [2, 3, 4], 5, 6, [7, 8], [9, 10]]
print(a)
