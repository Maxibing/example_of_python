#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Demo of build-in function of python 3.7
@Date     :2021/09/25 15:21:20
@Author      :xbMa
'''

'''
https://docs.python.org/zh-cn/3.7/library/functions.html

+--------------------------------------------------------------------------+
|    abs()     |   delattr()  |    hash()    | memoryview() |    set()     |    
+--------------------------------------------------------------------------+
|    all()     |   dict()     |    help()    |    min()     |  setattr()   |  
+--------------------------------------------------------------------------+
|    any()     |    dir()     |    hex()     |   next()     |   slice()    |  
+--------------------------------------------------------------------------+
|   ascii()    |  divmod()    |     id()     |   object()   |   sorted()   |  
+--------------------------------------------------------------------------+
|    bin()     |  enumerate() |    input()   |   oct()      |staticmethod()|  
+--------------------------------------------------------------------------+
|   bool()     |   eval()     |    int()     |   open()     |    str()     |  
+--------------------------------------------------------------------------+
| breakpoint() |   exec()     | isinstance() |   ord()      |    sum()     |  
+--------------------------------------------------------------------------+  
|  bytearray() |  filter()    | issubclass() |   pow()      |   super()    |  
+--------------------------------------------------------------------------+  
|  bytes()     |   float()    |    iter()    |   print()    |   tuple()    |  
+--------------------------------------------------------------------------+  
|  callable()  |   format()   |    len()     |  property()  |   type()     |  
+--------------------------------------------------------------------------+  
|  chr()       | frozenset()  |    list()    |   range()    |   vars()     |  
+--------------------------------------------------------------------------+  
| classmethod()|  getattr()   |   locals()   |   repr()     |   zip()      |  
+--------------------------------------------------------------------------+  
|  compile()   |  globals()   |    map()     |  reversed()  | __import__() |  
+--------------------------------------------------------------------------+  
|  complex()   |  hasattr()   |    max()     |   round()    |              |  
+--------------------------------------------------------------------------+  

'''

# abs(x) 返回一个数的绝对值。实参可以是整数或浮点数。如果实参是一个复数，则返回它的模
abs(-4)

# all(iterable) 如果 iterable 的所有元素为真（或迭代器为空），返回 True 。等价于:
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

# any(iterable) 如果 iterable 的任一元素为真则返回 True。 如果迭代器为空，返回 False。 等价于:
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# ascii(object) 与 repr() 类似，返回一个包含对象的可打印表示形式的字符串，但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。
ascii("nihao")
ascii("你好")

# bin(x) 将一个整数转变为一个前缀为“0b”的二进制字符串。结果是一个合法的 Python 表达式。如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数
bin(3)
bin(-3)

# bool([x]) 返回一个布尔值，True 或者 False。 x 使用标准的 真值测试过程 来转换。如果 x 是假的或者被省略，返回 False；其他情况返回 True。
bool()
bool(1)

