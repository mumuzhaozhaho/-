'''
np.gradient()  计算数组元素的梯度，多维数组返回每个维度的梯度
'''
import numpy as np
a=np.array([1,3,5])
print(np.gradient(a))
b=np.random.randint(0,20,(3,5))
print(b)
print(np.gradient(b))