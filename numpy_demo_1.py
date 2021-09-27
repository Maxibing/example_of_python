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

# 迭代时更改元素类型
# NumPy 不会就地更改元素的数据类型（元素位于数组中），因此它需要一些其他空间来执行此操作，
# 该额外空间称为 buffer，为了在 nditer() 中启用它，我们传参 flags=['buffered']。
arr = np.array([1,2,3])
print(f"Iterate array {arr} with change element's dtype:")
for x in np.nditer(arr, flags=['buffered'], op_dtypes="S"):
    print(x)

# 以不同步长迭代
arr = np.array([[1,2,3,4], [5,6,7,8]])
print(f"Iterate array {arr} with step 2")
for x in np.nditer(arr[:, ::2]):
    print(x)

# 使用ndenumerate()进行枚举迭代
# 枚举是指逐一提及事物的序号
# 有时，我们在迭代时需要元素的相应索引，对于这些用例，可以使用ndenumerate()
arr = np.array([[1,2,3], [4,5,6]])
print(f"Iterate array {arr} with ndenumerate():")
for idx, x in np.ndenumerate(arr):
    print(idx, x)

###################################################################
###################################################################

'''
数组连接

连接意味着将两个或多个数组的内容放在单个数组中。
在 SQL 中，我们基于键来连接表，而在 NumPy 中，我们按轴连接数组。
我们传递了一系列要与轴一起连接到 concatenate() 函数的数组。如果未显式传递轴（axis），则将其视为 0。
'''
# 连接两个1-D数组
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])
arr = np.concatenate((arr_1, arr_2))
print(f"Use np.concatenate() to connect arr_1 {arr_1} and arr_2 {arr_2}, result is:{arr}")

# 沿着行(axis=1)和沿着列(axis=0)连接两个2-D数组：
arr_1 = np.array([[1,2,3], [4,5,6]])
arr_2 = np.array([[7,8,9], [10,11,12]])
arr_axis_0 = np.concatenate((arr_1, arr_2), axis=0)
arr_axis_1 = np.concatenate((arr_1, arr_2), axis=1)
print(f"np.concatenate((arr_1, arr_2), axis=0) =  {arr_axis_0}")
print(f"np.concatenate((arr_1, arr_2), axis=1) = {arr_axis_1}")

# 使用堆栈函数连接数组
# 堆栈与级联相同，唯一的不同是堆栈是沿着新轴完成的。
# 我们可以沿着第二个轴连接两个一维数组，这将导致它们彼此重叠，即，堆叠（stacking）。
# 我们传递了一系列要与轴一起连接到 concatenate() 方法的数组。如果未显式传递轴，则将其视为 0。
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])
arr_axis_0 = np.stack((arr_1, arr_2), axis=0)
arr_axis_1 = np.stack((arr_1, arr_2), axis=1)
print(f"np.stack((arr_1, arr_2), axis=0) =  {arr_axis_0}")
print(f"np.stack((arr_1, arr_2), axis=1) = {arr_axis_1}")

# 沿行堆叠
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(f"np.hstack((arr1, arr2)) = {arr}")

# 沿列堆叠
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(f"np.vstack((arr1, arr2)) = {arr}")

# 沿高度堆叠
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(f"np.dstack((arr1, arr2)) = {arr}")

###################################################################
###################################################################
'''
数组拆分

拆分是连接的反向操作。
连接（Joining）是将多个数组合并为一个，拆分（Spliting）将一个数组拆分为多个。
使用 array_split() 分割数组，将要分割的数组和分割数传递给它。
'''
# 将数组分为3部分
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(f"np.array_split({arr}, 3) = {newarr}")

# 如果数组中的元素少于要求的数量，它将从末尾进行相应调整。
# 也有 split()方法可用，但是当源数组中的元素较少用于拆分时，它将不会调整元素，如下例，array_split() 正常工作，但 split() 会失败。
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(f"np.array_split({arr}, 4) = {newarr}")

# 访问拆分的数组
print(f"newarr[0]: {newarr[0]}")

# 分割二维数组
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(f"np.array_split({arr}, 3) = {newarr}")

# 沿行将2-D拆分为3个数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(f"newarr = np.array_split({arr}, 3, axis=1)\n{newarr}")

# 另一种方法是使用与hstack()相反的hsplit()
newarr = np.hsplit(arr, 3)
print(f"np.hsplit({arr}, 3)\n{newarr}")

###################################################################
###################################################################
'''
数组搜索

可以在数组中搜索（检索）某个值，然后返回获得匹配的索引。
要搜索数组，请使用 where() 方法。
'''
# 查找值为4的索引
arr = np.array([1,2,3,4,4,4,4])
x = np.where(arr == 4)
print(f"np.where(arr == 4): {x}")

# 查找值为偶数的索引
x = np.where(arr%2 == 0)
print(f"np.where(arr%2 == 0): {x}")

# 搜索排序
# 有一个名为 searchsorted() 的方法，该方法在数组中执行二进制搜索，并返回将在其中插入指定值以维持搜索顺序的索引。
# 假定 searchsorted() 方法用于排序数组。
# 定义：
# np.searchsorted(a, v, side='left', sorter=None)
# 在数组a中插入数组v（并不执行插入操作），返回一个下标列表，这个列表指明了v中对应元素应该插入在a中那个位置上
# 查找应插入的一个值，该方法从左侧开始搜索，并返回第一个索引
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(f"np.searchsorted({arr}, 7): {x}")

# 从右侧搜索
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(f"np.searchsorted({arr}, 7, side='right'): {x}")

# 要搜索多个值，请使用拥有指定值的数组。
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(f"np.searchsorted({arr}, [2, 4, 6]): {x}")

###################################################################
###################################################################
'''
数组排序

排序是指将元素按有序顺序排列。
有序序列是拥有与元素相对应的顺序的任何序列，例如数字或字母、升序或降序。
NumPy ndarray 对象有一个名为 sort() 的函数，该函数将对指定的数组进行排序。
'''
# 对数组进行排序
arr = np.array([3,2,7,1])
print(f"np.sort({arr}): {np.sort(arr)}")

# 对数组以字母顺序进行排序
arr = np.array(["banana", "apple", "orange"])
print(f"np.sort({arr}): {np.sort(arr)}")

# 对bool数组进行排序
arr = np.array([False, True, False])
print(f"np.sort({arr}): {np.sort(arr)}")

# 对2-D数组进行排序
arr = np.array([[3,5,1], [6,4,8]])
print(f"np.sort({arr}): {np.sort(arr)}")

###################################################################
###################################################################
'''
数组过滤

从现有数组中取出一些元素并从中创建新数组称为过滤（filtering）。
在 NumPy 中，使用布尔索引列表来过滤数组。
布尔索引列表是与数组中的索引相对应的布尔值列表。
如果索引处的值为 True，则该元素包含在过滤后的数组中；如果索引处的值为 False，则该元素将从过滤后的数组中排除。
'''
# 用索引0,2,4上的元素创建一个数组
arr = np.array([1,2,3,4,5,6,7])
x = [True, False, True, False, True, False, False]
print("arr = np.array([1,2,3,4,5,6,7])")
print("x = [True, False, True, False, True, False, False]")
print(f"newarr = arr[x]: {arr[x]}")

# 创建过滤器数组
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# 创建一个空列表
filter_arr = []
# 遍历 arr 中的每个元素
for element in arr:
  # 如果元素可以被 2 整除，则将值设置为 True，否则设置为 False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# 直接从数组创建过滤器
arr = np.array([61, 62, 63, 64, 65])
filter_arr = arr > 62
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# 创建一个过滤器数组，该数组仅返回原始数组中的偶数元素
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

###################################################################
###################################################################
'''

什么是随机数？
随机数并不意味着每次都有不同的数字。随机意味着无法在逻辑上预测的事物。

伪随机和真随机
计算机在程序上工作，程序是权威的指令集。因此，这意味着必须有某种算法来生成随机数。
如果存在生成随机数的程序，则可以预测它，因此它就不是真正的随机数。
通过生成算法生成的随机数称为伪随机数。

我们可以生成真正的随机数吗？
是的。为了在我们的计算机上生成一个真正的随机数，我们需要从某个外部来源获取随机数据。外部来源通常是我们的击键、鼠标移动、网络数据等。
我们不需要真正的随机数，除非它与安全性（例如加密密钥）有关或应用的基础是随机性（例如数字轮盘赌轮）。
在本教程中，我们将使用伪随机数。
'''
# NumPy 提供了 random 模块来处理随机数。生成一个0~100的随机整数
print(f"np.random.randint(100): {np.random.randint(100)}")

# 生成一个0~1的随机浮点数
print(f"np.random.rand(): {np.random.rand()}")

# 生成随机数组，randint() 方法接受 size 参数，您可以在其中指定数组的形状。
print(f"np.random.randint(100, size=(5): {np.random.randint(100, size=(2,5))}")

# rand()允许指定数组的形状
print(f"np.random.rand(2,3): {np.random.rand(2,3)}")

# 从数组生成随机数，choice()
x = [6,1,7,2,8]
print(f"np.random.choice({x}): {np.random.choice(x)}")

# choice()方法还可以返回一个数组
print(f"np.random.choice({x}, size=(2,4)): {np.random.choice(x, size=(2,4))}")

###################################################################
###################################################################
'''

什么是 ufuncs？
ufuncs 指的是“通用函数”（Universal Functions），它们是对 ndarray 对象进行操作的 NumPy 函数。

为什么要使用 ufuncs？
ufunc 用于在 NumPy 中实现矢量化，这比迭代元素要快得多。
它们还提供广播和其他方法，例如减少、累加等，它们对计算非常有帮助。
ufuncs 还接受其他参数，比如：
where 布尔值数组或条件，用于定义应在何处进行操作。
dtype 定义元素的返回类型。
out 返回值应被复制到的输出数组。

什么是向量化？
将迭代语句转换为基于向量的操作称为向量化。
由于现代 CPU 已针对此类操作进行了优化，因此速度更快。

对两个列表的元素进行相加：
list 1: [1, 2, 3, 4]
list 2: [4, 5, 6, 7]
一种方法是遍历两个列表，然后对每个元素求和。

对此，NumPy 有一个 ufunc，名为 add(x, y)，它会输出相同的结果。
'''
x = [1,2,3,4]
y = [5,6,7,8]
print(f"np.add({x},{y}): {np.add(x,y)}")
