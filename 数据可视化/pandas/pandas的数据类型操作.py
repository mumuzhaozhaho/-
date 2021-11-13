import pandas as pd
import  numpy as np
#增加或重排索引   .reindex（）

a={'w':[1,2,3],'y':[4,5,6]}
b=pd.DataFrame(a,index=['a','b','c'])
print(b)
c=b.reindex(index=['b','c','a'])
print(c)
d=b.reindex(columns=['y','w','x'])
print(d)
e=d.columns.insert(4,'z')
f=d.reindex(columns=e,fill_value=200)
print(f)
# d['z']=200
# print(d)

#使用.ffill或者bfill方法更好
nc=f.columns.delete(2)
print(nc)
ni=f.index.insert(3,'d')
print(ni)
nd=f.reindex(index=ni,columns=nc).ffill()
print(nd)
#删除： drop
q1=pd.Series([9,8,7,6],index=[1,2,3,4])
print(q1)
print(q1.drop([1,2]))
#删除行直接drop，删除列axis=1
print(nd.drop('d'))
print(nd.drop('z',axis=1))

