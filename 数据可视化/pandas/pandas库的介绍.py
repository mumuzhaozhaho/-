'''
pandas提供两个数据类型
Series     一维
DataFrame
基本，运算，关联，特征值操作
'''
import pandas as pd
a=pd.Series(range(20))   #左边为索引，右边为值
print(a)
print(a.cumsum())  #计算累加和