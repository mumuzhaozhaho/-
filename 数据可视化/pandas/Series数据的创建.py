import pandas as pd
a=pd.Series([5,1,50,12])
print(a)
b=pd.Series([5,1,50,12],index=[4,3,2,1])#更改原有的索引
print(b)
#从标量值创建
c=pd.Series(25,index=[1,2,3])
print(c)
#从字典创建
d=pd.Series({'姓名':'张三','年龄':24,'性别':'男'},index=['娃哈哈','年龄','性别','姓名'])
print(d)
#从ndarray创建
import numpy as np
e=pd.Series(np.arange(5),index=np.arange(5,0,-1))
print(e)