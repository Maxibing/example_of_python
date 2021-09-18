#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :String common operations
@Date     :2021/09/18 08:33:46
@Author      :xbMa
'''

mystr = "hello word"


# find() 检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
# mystr.find(str, start=0, end=len(mystr))
print(mystr.find("o"))
print(mystr.find("o", 0, len(mystr)))

# rfind() 类似find()，不过是从右边开始查找
print(mystr.rfind("o"))
print(mystr.rfind("o", 0, len(mystr)))

# index() 跟find()方法一样，只不过如果str不在 mystr中会报一个异常
# mystr.index(str, start=0, end=len(mystr)) 
print(mystr.index("w"))
print(mystr.index("w", 0, len(mystr)))

# rindex() 类似于 index()，不过是从右边开始
print(mystr.rindex("w"))
print(mystr.rindex("w", 0, len(mystr)))

# count() 返回 str在start和end之间 在 mystr里面出现的次数
# mystr.count(str, start=0, end=len(mystr))
print(mystr.count("l"))
print(mystr.count("l", 0, len(mystr)))

# replace() 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次
# mystr.replace(str1, str2,  mystr.count(str1))
print(mystr.replace("o", "oo"))
print(mystr.replace("o", "oo", mystr.count("o")))

# split 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
print(mystr.split("l", 2))

# capitalize() 把字符串的第一个字符大写，其他的变成小写
print(mystr.capitalize())

# title() 把字符串的每个单词首字母大写，其他的改成小写
print(mystr.title())

# startswith() 检查字符串是否是以指定字符串开头, 是则返回 True，否则返回 False
print(mystr.startswith("he"))

# endswith() 检查字符串是否以指定字符串结束，如果是返回True,否则返回 False
print(mystr.endswith("rd"))

# lower() 转换 mystr 中所有大写字符为小写
print(mystr.lower())

# upper() 转换 mystr 中的小写字母为大写
print(mystr.upper())

# ljust() 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# mystr.ljust(width) 
print(mystr.ljust(20))

# rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# mystr.rjust(width)
print(mystr.rjust(30))

# center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
# mystr.center(width)
print(mystr.center(30))

# strip() 去除首位指定字符
print(mystr.strip("h"))
# 去除首位空格
print("  shfgoqgi  ".strip())

# lstrip() 去除开头处指定字符
print(mystr.lstrip("h"))

# rstrip() 去除结尾处指定字符
print(mystr.rstrip("d"))

# partition() 把mystr以str分割成三部分,str前，str和str后
# mystr.partition(str)
print(mystr.partition("o"))

# rpartition() mystr.partition(str)
# mystr.rpartition(str)
print(mystr.rpartition("o"))

# splitlines() 按照行分隔，返回一个包含各行作为元素的列表
# mystr.splitlines()
print(mystr.splitlines())

# isalpha() 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
print("ssautaous".isalpha())

# isdigit() 如果 mystr 只包含数字则返回 True 否则返回 False.
print("18541289".isdigit())

# isalnum() 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
print(mystr.isalnum())

# isspace() 如果 mystr 中只包含空格，则返回 True，否则返回 False.
print(mystr.isspace())

# join() 将序列中的元素以指定的字符连接生成一个新的字符串。
print("-".join(["hello", "word"]))
