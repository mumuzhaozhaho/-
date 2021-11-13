'''
算术运算    根据行列索引，补齐后计算，浮点数
维度不同，广播运算
除了+-*/外，可以使用方法.add .sub .mul.div
'''
import pandas as pd
import  numpy as np
a=pd.DataFrame(np.arange(12).reshape(3,4))
print(' '*30+'a')
print(a)
b=pd.DataFrame(np.arange(20).reshape(4,5))
print(' '*30+'b')
print(b)
print(' '*30+'a+b')
print(a+b)
#除了+-*/外，可以使用方法.add .sub .mul.div
print(' '*30+'add')
print(b.add(a,fill_value=100))
c=pd.Series(range(5))
print(c-10)

print(a)
print(c)
print(a-c)
'''
比较运算   只比较相同索引的元素，不进行补齐，
维度不同，广播运算
除了+-*/外，可以使用方法.add .sub .mul.div
'''