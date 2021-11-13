import numpy as np
a=np.arange(24).reshape((2,3,4))
print(a)
b=a.mean()       #.mean() 求平均值
print(b,np.mean(a))
print(a/b)
print(np.sqrt(a))
b=np.linspace(12,35,24).reshape((2,3,4))
print(b)
c=a>b
print(c)