import numpy as np
import time


'''numpy的大数组运算和python大数组运算比较'''
my_arr = np.arange(1000000)
my_list = list(range(1000000))
# numpy大数组运算时间
curtime = time.time()
for _ in range(10): 
    my_arr2 = my_arr * 2
print("Cost time: %s\n" % str(time.time() - curtime))
# python大数组运算时间
for _ in range(10): 
    my_list2 = [x*2 for x in my_list]
print("Cost time: %s\n" % str(time.time() - curtime))

###################################################################
###################################################################

'''ndarray 多维数组 ,同结构数据多维容器'''
# 生成随机二维数组
data = np.random.randn(2, 3)
print("二维数组：\n %s\n" % str(data))
# 乘10
data *= data
print("乘10：\n %s\n" % str(data))
# 自相加
data += data
print("自相加：\n %s\n" % str(data))

# 创建ndarry-->np.array
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
# 数组属性
print("arr1.ndim: %s \narr2.ndim: %s\n" % (str(arr1.ndim), str(arr2.ndim)))
print("arr1.shape: %s \narr2.shape: %s\n" % (str(arr1.shape), str(arr2.shape)))
print("arr1.dtype: %s \narr2.dtype: %s\n" % (str(arr1.dtype), str(arr2.dtype)))

# 创建ndarry-->np.zeros
print("np.zeros(10)：")
print(np.zeros(10))

# 创建ndarry-->np.ones
print("np.ones(10)：")
print(np.ones(10))

# 创建ndarry-->np.arange
print("np.arange(15)：")
print(np.arange(15))

# 创建ndarry-->np.eye
print("np.eye(10)：")
print(np.eye(10))

'''
np.array    -->     将输入数据（列表、元组、数组或其他序列类型）转为ndarray
np.asarray    -->     将输入转为ndarray，如果输入本身就是ndarray就不进行复制
np.arange    -->     类似于内置的range，但返回的是一个ndarray而不是列表
np.ones/np.ones_like    -->     根据指定的形状和dtype创建一个全1数组。one_like以另一个数组为参数，根据其形状和dtype创建一个全1数组
np.zeros/np.zeros.like    -->     类似ones
np.empty/np.empty_like    -->     创建新数组，只分配内存空间，但不填充任何值
np.full/np.full_like    -->     用full value中的所有值，根据指定的形状和dtype创建一个数组。full_like使用另一个数组，用相同的形状和dtype创建
np.eye/np.indentity    -->     创建一个正方的NXN的单位矩阵（对角线为1，其余为0）
'''
###################################################################
###################################################################

'''ndarray 数据类型 --> dtype'''
# 通过astype方法转化为dtype
arr = np.array([1, 2, 3, 4, 5])
print("Orgin type： %s" % str(arr.dtype))
float_arr = arr.astype(np.float64)
print("Modify type： %s" % str(float_arr.dtype))

# 如果字符串数组中，全是数字，也可以使用
numeric_strings = np.array(["1.25", "-9.6", "42"], dtype=np.string_)
array = numeric_strings.astype(float)
print(array)