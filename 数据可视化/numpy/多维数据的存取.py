# a.tofile(frame,sep='',format='')
#不指定分隔符，生成二进制文件
import numpy as np
a=np.arange(100).reshape(5,10,2)
a.tofile('a.dat',sep='#',format='%f')
a.tofile('a1.dat',sep='',format='%d')
# np.fromfile(frame,,dtype=np.float,count=-1,sep=',')
#count=-1表示读入整个文件
b=np.fromfile('a.dat',dtype=np.float64,count=-1,sep='#').reshape(5,10,2)
b1=np.fromfile('a1.dat',dtype=np.int32,count=-1,sep='').reshape(5,20)
print(b)
print(b1)

'''
便捷存取
'''
#np.save(frame,array)/np.savez()
np.save('a.npy',a)
#np.load(frame)
c=np.load('a.npy')
print(c)