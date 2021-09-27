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

'''ndarray 多维数组,同结构数据多维容器'''
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

'''
ndarray 数据类型 --> dtype

    i - 整数
    b - 布尔
    u - 无符号整数
    f - 浮点
    c - 复合浮点数
    m - timedelta
    M - datetime
    O - 对象
    S - 字符串
    U - unicode 字符串
    V - 固定的其他类型的内存块 ( void )
'''
# 检查数组的数据类型
arr = np.array([1, 2, 3, 4, 5])
print("Orgin array %s" % str(arr))
print("Orgin array type： %s" % str(arr.dtype))

# 通过astype方法转化为dtype
float_arr = arr.astype(np.float64)
print("Modify array %s" % str(float_arr))
print("Modify array type： %s" % str(float_arr.dtype))

# 如果字符串数组中，全是数字，也可以使用
numeric_strings = np.array(["1.25", "-9.6", "42"], dtype=np.string_)
array = numeric_strings.astype(float)
print(f"Str array: {array}")
print(f"Str array type: {array.dtype}")

# 对于 i、u、f、S 和 U，也可以定义大小
arr = np.array([1, 2, 3, 4], dtype='i4')
print(f"4 bytes length array: {arr}")
print(f"4 bytes length array type: {arr.dtype}")

###################################################################
###################################################################

'''
副本和视图


副本和数组视图之间的主要区别在于副本是一个新数组，而这个视图只是原始数组的视图。

副本拥有数据，对副本所做的任何更改都不会影响原始数组，对原始数组所做的任何更改也不会影响副本。

视图不拥有数据，对视图所做的任何更改都会影响原始数组，而对原始数组所做的任何更改都会影响视图。
'''
# 进行复制，更改原始数组并显示两个数组：
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 2
print(f"Origin array: {arr}")
print(f"x = arr.copy(). Modify arr[0]=2, x: {x}")

# 创建视图，更改原始数据，然后显示两个数组：
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 2
print(f"Origin array: {arr}")
print(f"x = arr.view(). Modify arr[0]=2, x: {x}")

# 更改视图数据，然后显示两个数组
x[1] = 3
print(f"x = arr.view(). Modify x[1] = 3, x: {x}")
print(f"Origin array: {arr}")

# 检查数组是否拥有数据。
# 每个 NumPy 数组都有一个属性 base，如果该数组拥有数据，则这个 base 属性返回 None。
# 否则，base 属性将引用原始对象。
arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()
print(f"x = arr.copy(), x.base: {x.base}")
print(f"y = arr.view(), y.base: {y.base}")

###################################################################
###################################################################

'''
数组重塑

重塑意味着更改数组的形状。
数组的形状是每个维中元素的数量。
通过重塑，我们可以添加或删除维度或更改每个维度中的元素数量。
'''
# 从1-D重塑为2-D
arr = np.array([i for i in range(12)])
new_arr_4x3 = arr.reshape(4,3)
print(f"Origin array: {arr}")
print(f"Reshape to 2-D, 4*3 new array: {new_arr_4x3}")

# 从1-D重塑为3-D
arr = np.array([i for i in range(12)])
new_arr_2x3x2 = arr.reshape(2,3,2)
print(f"Origin array: {arr}")
print(f"Reshape to 3-D, 2*3*2 new array: {new_arr_2x3x2}")

# 从2-D重塑为3-D
new_arr_3x2x2 = new_arr_4x3.reshape(3,2,2)
print(f"Origin array: {new_arr_4x3}")
print(f"Reshape to 3-D, 3*2*2 new array: {new_arr_3x2x2}")

# 返回的是视图
print(f"4*3 array reshape to 3-D, 3*2*2 new array.base: {new_arr_3x2x2.base}")

# 未知的维：不必在reshape中为维度指定确定的数字，可以传递-1，NumPy会计算该数字
new_arr = arr.reshape(2,2,-1)
print(f"1-D array reshape to 2*2*-1, new array:{new_arr}")

# 展平数组：将多维数组转换为1维数组，使用reshape(-1)来做到这一点
one_D_array = new_arr.reshape(-1)
print(f"Convert 2*2*3 array to 1-D array: {one_D_array}")

###################################################################
###################################################################

'''
数组迭代

迭代意味着逐一遍历元素。
当我们在 numpy 中处理多维数组时，可以使用 python 的基本 for 循环来完成此操作。
如果我们对 1-D 数组进行迭代，它将逐一遍历每个元素。
'''
# 一维迭代
arr_1 = np.array([1, 2, 3])
print(f"Iterate 1-D array: {arr_1}")
for i in arr_1:
    print(i)

# 二维迭代：如果我们迭代一个 n-D 数组，它将逐一遍历第 n-1 维。
arr_2 = np.array([[1, 2, 3], [4,5,6]])
print(f"Iterate 2-D array onece: {arr_2}")
for i in arr_2:
    print(i)

print(f"Iterate 2-D array twice: {arr_2}")
for i in arr_2:
    for j in i:
        print(j)

# 使用nditer()迭代3-D数组
arr_3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"Iterate 3-D array by np.nditer()")
for x in np.nditer(arr_3):
    print(x)

