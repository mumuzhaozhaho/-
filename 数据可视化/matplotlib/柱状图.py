import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# x=[1980,1985,1990,1995,2000,2005,2010,2015]
#
# y=[1000,3000,4000,5000,3500,3500,3500,3500]
# plt.bar(x,y)
# plt.show()
# # plt.bar(x,y,width=3)
# # plt.xlabel('年份',fontproperties='KaiTi',fontsize=15)
# # plt.ylabel('销量',fontproperties='KaiTi',fontsize=25)
# # plt.title('tu',fontproperties='KaiTi',fontsize=25)
# # plt.xticks(x,x)
# # plt.show()
# #
np.random.seed(0)
x=np.arange(5)
y=np.random.randint(-5,5,5)
print(x,y)
plt.subplot(1,2,1)
a=plt.bar(x,y)
#柱状图颜色设置 当y小于0，颜色为绿色
for i,height in zip(a,y):
    print(i)
    if height<0:
        i.set(color='green')
#在0位置水平 画一条蓝线
plt.axhline(0,color='blue',linewidth=20)
plt.subplot(1,2,2)
plt.barh(x,y,color='g')
#在0位置垂直 画一条蓝线
plt.axvline(0,color='r',lw=15)
plt.show()
#柱状图颜色设置



