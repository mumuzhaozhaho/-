'''
rand（d0，d1，...dn）根据d0到dn创建随机数组，浮点数，均匀分布,[0,1)
randn（d0，d1，...dn）根据d0到dn创建随机数组，标准正态分布
randint（low，high，shape）根据shape创建数或数组，范围是低到高
seed（s）随机数种子，s是给定的种子值
'''
import numpy as np
a=np.random.randn(3,4)
print(a)
b=np.random.randint(10,50,(5,2))
print(b)

'''
shuffle(a),根据a的第一轴进行随机排列，改变数组
permutation(a)       不改变
choice(a,size,replace,p) 从a中以概率p抽取元素，形状为size，replace代表是否可以重用元素，默认false
'''
# np.random.shuffle(b)
# print(b)
c=np.random.permutation(b)
print(c)
print(b)

# c=np.random.randint(100,200,(10))
# print(c)
# d=np.random.choice(c,(5,2))
# print(d)

'''
uniform(low,high,size)#均匀分布  
normal(loc,scale,size)正态分布  loc均值 scale标准差
poisson(lam,size)泊松分布   lam 为随机事件发生率
'''
# e=np.random.uniform(10,20,(10))
# print(e)
e1=np.random.normal(10,2,(10))
print(e1)
# e1=np.random.poisson()