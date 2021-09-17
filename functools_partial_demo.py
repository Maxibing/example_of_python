#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of functools.partial
@Date     :2021/09/17 16:25:09
@Author      :xbMa
'''
import functools

def foo(x, y, method="add"):
    if method == "add":
        return x + y
    elif method == "mul":
        return x * y

# 定义偏函数
foo_add = functools.partial(foo, method="add")
foo_mul = functools.partial(foo, method="mul")

print(foo_add(3,4))
print(foo_mul(3,4))

