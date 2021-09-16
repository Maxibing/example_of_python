#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of callback function
@Date     :2021/09/16 14:33:05
@Author      :xbMa
'''

# 定义回调函数double()
def double(x):
    print(f"double()被调用")
    return x * 2

# 定义回调函数quadruple()
def quadruple(x):
    print("quadruple()被调用")
    return  x * 4

# 定义中间函数getOddNumber(k, getEvenNumber)
def getOddNumber(k, getEvenNumber):
    k = k + 1
    print(f"k: {k}")
    print(f"将k传递给{getEvenNumber.__name__}")
    return 1 + getEvenNumber(k)

# 主函数
def main():
    print("调用main()函数")
    k = 1
    # 返回2k+1形式的奇数
    i = getOddNumber(k, double)
    print(f"i: {i}")
    # 返回4k+1形式的奇数
    i = getOddNumber(k, quadruple)
    print(f"i: {i}")
    # 返回8k+1形式的奇数
    i = getOddNumber(k, lambda k: k*8)
    print(f"i: {i}")


if __name__ == "__main__":
    main()

