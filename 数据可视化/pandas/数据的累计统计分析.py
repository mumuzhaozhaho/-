'''
基本累计方法   ：计算之前n个
        .cumsum()      依次给出前1、2、3、n个数的和
        .cumprod()     依次给出前1、2、3、n个数的积
        .cummax()     依次给出前1、2、3、n个数的最大值
        .cummin()     依次给出前1、2、3、n个数的最小值
滚动计算（窗口计算）：计算相邻元素
       .rolling（w）.sum()  依次计算相邻w个元素和
       .rolling（w）.mean() 依次计算相邻w个元素平均值
       .rolling（w）.var()  依次计算相邻w个方差
       .rolling（w）.std() 依次计算相邻w个元素标准差
       .rolling（w）.min().max()  依次计算相邻w个元素最小，最大
'''
import pandas as pd
import numpy as np

b=pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','b','d'])
print(b)
print()
print(b.cumsum())
print()
print(b)
print()
print(b.rolling(2).sum())
