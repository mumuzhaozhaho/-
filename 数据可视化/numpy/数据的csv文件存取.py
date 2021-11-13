'''
只适用于一维和二维数据的存取
'''

#np.savetxt(文件,array,fmt：格式,delimiter；分隔符)
import numpy as np
a=np.arange(50).reshape(5,10)
print(a)
np.savetxt('a.csv',a,fmt='%d',delimiter=',')
#np.loadtxt(文件,dtype=np.float,delimiter；分隔符,unpack=false)
b=np.loadtxt('a.csv',dtype=np.float64,delimiter=',',unpack=False)
print(b)