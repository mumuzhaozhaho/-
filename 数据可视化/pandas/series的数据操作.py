import pandas as pd
import  numpy as np
b=pd.Series([1,5,8,0.2],index=['a','b','c','d'])
print(b)
print(b.index,b.values)
#自定义索引与原索引并存
print(b['a'],b[0],sep='##')
#自定义索引与原索引并存，但不能共用
print(b[['d','a']])
# print(b[['d','a',0]])
print(b[:'c':2])
print(b[b>b.median()])
print(np.exp(0),np.exp(1))
print(np.exp(b))
#与字典类似的操作  in  .get
print('a'in b)
print(b.get('d'),b.get('e',100))
#series的对齐操作
a=pd.Series([2,3,4],index=['a','c','e'])
print(a)
print(b)
print(a+b)
#series的name属性
print(b.name)
b.name='值'
b.index.name='键'
print(b)
