# 核心数据对象
# ndarry       整数，浮点数，复数
# 常用函数
import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a,type(a))

print(a.ndim)  #.ndim维数
print(a.shape)
print(a.dtype)
print(a.size)
print(a.itemsize)#每个元素的内存（#以字节为单位）