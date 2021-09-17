#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of strip()
@Date     :2021/09/17 14:58:17
@Author      :xbMa
'''

'''
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
'''

origin_str = "2sahfgioag2"

# 去除首位指定字符
print(origin_str.strip("2"))

# 去除开头处指定字符
print(origin_str.lstrip("2"))

# 去除结尾处指定字符
print(origin_str.rstrip("2"))

# 去除首位空格
print("  shfgoqgi  ".strip())

