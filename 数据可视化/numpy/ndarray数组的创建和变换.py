import numpy as np
###从列表元组创建
a=[1,2,3]
b=(1,0.5,2)
x=[a,b]
x1=np.array(x)
c=np.array(a)
d=np.array(b)
print(c,type(c),d,type(d))
print(x1)
###使用numpy中的函数
x2=np.arange(10)       #序列
print(x2)
x3=np.ones((2,3))      #全一二行三列
print(x3)
x3=np.zeros((2,3))       #全0二行三列
print(x3)
x4=np.eye(5)
print(x4)
x5=np.full((2,3),5)         #全5 二行三列
print(x5)
x6=np.linspace(1,10,10)
print(x6)
x7=np.concatenate((x6,x2))
print(x7)
#数组的变换
#.reshape(shape)   原数组不变
#.resize(shape)     修改原数组
#.swapaxes(ax1,ax2) 调换两个维度
#.flatten()       降维
#.astype(new stype) 类型转换
q=np.ones((2,3),dtype=np.int32)
q1=q.astype(np.float64)
print(q,q1)