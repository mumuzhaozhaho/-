import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
lables='wo','ni','ta','ta'
size=[25,20,25,30]
explode=[0,0,0,0.1]
plt.pie(size,explode=explode,labels=lables,shadow=True)
plt.axis('equal')   #使得饼图为正圆形
plt.show()
man=945684
woman=262156
m=man/(man+woman)
wo=woman/(man+woman)
plt.rcParams['font.family']='SimHei'
label=['男','女']
# labels 名称 colors：颜色，explode=分裂  autopct显示百分比
plt.pie([m,wo],explode=[0,0.2],labels=label,colors=['b','r'],autopct='%1.1f%%')
plt.show()

# paches,texts,autotexts=plt.pie([man_perc,woman_perc],labels=labels,colors=colors,explode=(0,0.05),autopct='%0.1f%%')
#
# #设置饼状图中的字体颜色
# for text in autotexts:
#     text.set_color('white')
#
# #设置字体大小
# for text in texts+autotexts:
#     text.set_fontsize(20)
