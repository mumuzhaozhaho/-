'''

sum(a,axis=none)   axis=none,对所有元素
mean 平均值
average (a,axis,weight=[]) 加权平均值,weight为权重
std 标注差
var 方差

min ,max
argmin,aremax 将数组元素的最小值降维后的下标
ptp   最大数与最小数之差
median 中位数
unravel_index(index,shape)   根据shape将index转为多维下标
'''
import numpy as np
a=np.linspace(11,20,10).reshape(2,5)
print(a)
print(np.sum(a))
print(np.max(a),np.ptp(a),np.median(a),np.argmax(a))
print(np.unravel_index(9,(2.5)))
