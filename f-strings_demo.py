#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :formatting_string(f_string) usage
@Date     :2021/04/28 11:41:10
@Author      :xbMa
'''

name = "xbMa"
age = 31

# The oldest method
print("%s is %d years old" % (name, age))
# After python 3.0, can use format()
print("{} is {} years old".format(name, age))
# After python 3.6, can use f""
print(f"{name} is {age} years old")

# Use expressions in {}
bags = 3
apples_in_bag = 12

print(f"There are total {bags * apples_in_bag} apples")

# Use dict
user = {"name": "xbMa", "age": 31}
print(f"{user['name']} is {user['age']} years old")

# Print few line
city = "NanJing"
print(f"Name: {name}\n" f"Age: {age}\n" f"City: {city}")

# Call function
def ret_max(x, y):
    
    return x if x > y else y

a = 3
b = 5
print(f"Max of {a} and {b} is {ret_max(a, b)}")

# Escape '\'
print(f"Python use {{}} to evaluate variables in f-strings")
print(f'This is a \'great\' film')

# Format datetime
import datetime
now = datetime.datetime.now()
print(f'{now:%Y-%m-%d %H:%M:%S}')

# Format float
val = 1.5687
print(f'{val:.2f}')
print(f'{val:.5f}')

# Format width
num = "Nu"
sq = "squ"
cube = "cube"
print(f"{num:>2} {sq:>5} {cube:>7}")
for i in range(1, 21, 3):
    print(f"{i:02} {i*i:5} {i*i*i:7}")
    
# Format string
s1 = 'a'
s2 = 'bb'
s3 = 'ccc'
s4 = 'dddd'
print(f'{s1:>16}')
print(f'{s2:>16}')
print(f'{s3:>16}')
print(f'{s4:>16}')

# Format notations
a = 300
print(f"int: {a:d}")
print(f"hex: {a:#x}")
print(f"oct: {a:#o}")
print(f"sci: {a:e}")

'''
格式描述符 含义与作用 适用变量类型
s 普通字符串格式 字符串
b 二进制整数格式 整数
c 字符格式，按unicode编码将整数转换为对应字符 整数
d 十进制整数格式 整数
o 八进制整数格式 整数
x 十六进制整数格式（小写字母） 整数
X 十六进制整数格式（大写字母） 整数
e 科学计数格式，以 e 表示 ×10^ 浮点数、复数、整数（自动转换为浮点数）
E 与 e 等价，但以 E 表示 ×10^ 浮点数、复数、整数（自动转换为浮点数）
f 定点数格式，默认精度（precision）是6 浮点数、复数、整数（自动转换为浮点数）
F 与 f 等价，但将 nan 和 inf 换成 NAN 和 INF 浮点数、复数、整数（自动转换为浮点数）
g 通用格式，小数用 f，大数用 e 浮点数、复数、整数（自动转换为浮点数）
G 与 G 等价，但小数用 F，大数用 E 浮点数、复数、整数（自动转换为浮点数）
% 百分比格式，数字自动乘上100后按 f 格式排版，并加 % 后缀 浮点数、整数（自动转换为浮点数）
常用的特殊格式类型：标准库 datetime 给定的用于排版时间信息的格式类型，适用于 date、datetime 和 time 对象

格式描述符 含义 显示样例
%a 星期几（缩写） 'Sun'
%A 星期几（全名） 'Sunday'
%w 星期几（数字，0 是周日，6 是周六） '0'
%u 星期几（数字，1 是周一，7 是周日） '7'
%d 日（数字，以 0 补足两位） '07'
%b 月（缩写） 'Aug'
%B 月（全名） 'August'
%m 月（数字，以 0 补足两位） '08'
%y 年（后两位数字，以 0 补足两位） '14'
%Y 年（完整数字，不补零） '2014'
%H 小时（24小时制，以 0 补足两位） '23'
%I 小时（12小时制，以 0 补足两位） '11'
%p 上午/下午 'PM'
%M 分钟（以 0 补足两位） '23'
%S 秒钟（以 0 补足两位） '56'
%f 微秒（以 0 补足六位） '553777'
%z UTC偏移量（格式是 ±HHMM[SS]，未指定时区则返回空字符串） '+1030'
%Z 时区名（未指定时区则返回空字符串） 'EST'
%j 一年中的第几天（以 0 补足三位） '195'
%U 一年中的第几周（以全年首个周日后的星期为第0周，以 0 补足两位） '27'
%w 一年中的第几周（以全年首个周一后的星期为第0周，以 0 补足两位） '28'
%V 一年中的第几周（以全年首个包含1月4日的星期为第1周，以 0 补足两位） '28'

< 左对齐（字符串默认对齐方式）
> 右对齐（数值默认对齐方式）
^ 居中
数字符号相关格式描述符
格式描述符 含义与作用
+ 负数前加负号（-），正数前加正号（+）
- 负数前加负号（-），正数前不加任何符号（默认）
（空格） 负数前加负号（-），正数前加一个空格
注：仅适用于数值类型。

数字显示方式相关格式描述符
格式描述符 含义与作用
# 切换数字显示方式
注1：仅适用于数值类型。
注2：# 对不同数值类型的作用效果不同，详见下表：

数值类型 不加#（默认） 加# 区别
二进制整数 '1111011' '0b1111011' 开头是否显示 0b
八进制整数 '173' '0o173' 开头是否显示 0o
十进制整数 '123' '123' 无区别
十六进制整数（小写字母） '7b' '0x7b' 开头是否显示 0x
十六进制整数（大写字母） '7B' '0X7B' 开头是否显示 0X
宽度与精度相关格式描述符
格式描述符 含义与作用
width 整数 width 指定宽度
0width 整数 width 指定宽度，开头的 0 指定高位用 0 补足宽度
width.precision 整数 width 指定宽度，整数 precision 指定显示精度
注1：0width 不可用于复数类型和非数值类型，width.precision 不可用于整数类型。
注2：width.precision 用于不同格式类型的浮点数、复数时的含义也不同：用于 f、F、e、E 和 % 时 precision 指定的是小数点后的位数，用于 g 和 G 时 precision 指定的是有效数字位数（小数点前位数+小数点后位数）。
注3：width.precision 除浮点数、复数外还可用于字符串，此时 precision 含义是只使用字符串中前 precision 位字符。
'''