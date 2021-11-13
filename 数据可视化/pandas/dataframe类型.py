#pandas 多维类型，由共用相同索引的一组列组成
# 纵向axis=0，横向为1
import pandas as pd
import  numpy as np
d=pd.DataFrame(np.arange(10).reshape(2,5))
print(d)
#从字典创建
a={'1':pd.Series([1,2,3]),'2':pd.Series([4,5,6],index=['a','b','c'])}
print(pd.DataFrame(a))
print(pd.DataFrame(a,index=range(6),columns=['1','2']))
b={'w':[1,2,3],'y':[4,5,6]}
c=pd.DataFrame(b,index=['a','b','c'])
print(c)
print(c['w']['a'])
print(c.loc['b'])
print(c['w'])
