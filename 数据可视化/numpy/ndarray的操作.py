import numpy as np
a=np.arange(24)
b=a.reshape((2,3,4))
print(b)
print(b[0,1,2])
print(b[-2,-2,-2])  #从右向左索引，下标从-1开始


#多维数组，以，间隔各个维度，以：间隔各自维度
c=b[:,1,-3]
print(c)
d=b[:,1:3,:]
print(d)
e=b[:,:,::2]
print(e)