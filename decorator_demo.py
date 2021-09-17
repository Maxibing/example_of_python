#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of decorator
@Date     :2021/09/17 15:28:19
@Author      :xbMa
'''

'''
@wraps(view_func)的作用: 不改变使用装饰器原有函数的结构(如name, doc)
'''

import time

from functools import wraps

# 定义修饰器1
def log(func):
    @wraps(func)
    def fn(*args, **kw):
        print(f"Call {func.__name__}")
        return func(*args, **kw)
    return fn

# 定义修饰器2
def cost_time(func):
    @wraps(func)
    def fn(*args,**kw):
        _start_time = time.time()
        re = func(*args, **kw)
        print(f"Excute {func.__name__} cost {time.time() - _start_time}")
        return re
    return fn

# 调用修饰器
@log
@cost_time
def _add(x,y):
    time.sleep(0.1)
    print(x+y)


_add(1,2)

    