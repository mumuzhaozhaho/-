'''
       #方法#
.sum
.count   计算非空数值的总量
.mean
.median
.var  方差
.std  标准差
.min
.max
       只适用于series的方法
argmin argmax   计算索引
idxmin idxmax       计算最大值，最小值的索引

        .describe针对0轴的统计汇总（各列）


'''
import pandas as pd
import numpy as np
a=pd.Series([9,8,7,6],index=['a','b','c','d'])
print(a)
print(' ')
print(a.describe())
b=pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','b','d'])
print(b)
print()
print(b.describe())
print(b.describe().loc['max'])
