'''
根据索引排序 .sort_index（axis=0，ascending=True）  默认升序
根据数据排序 .sort_values  （axis=0，ascending=True）默认升序
              若是dataframe（by,axis=0，ascending=True）

空值放在排序末尾

'''
import pandas as pd
import numpy as np
a=pd.DataFrame(np.arange(20).reshape(4,5),index=['d','a','b','c'])
print(a)
print()
# print(a.sort_index(axis=1,ascending=False))
# print()
# print(a.sort_values(2,axis=0,ascending=False))#第0轴第二列
# print()
print(a.sort_values('c',axis=1,ascending=False))
print(a.count())

