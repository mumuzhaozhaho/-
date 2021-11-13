import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

names=['千与千寻','玩具总动员4','黑衣人：全球追缉']
num1=[7580,4013,1673]
num2=[5453,1840,1080]
num3=[4348,2345,1890]
x=np.arange(3)
plt.rcParams['font.family']='SimHei'
plt.bar(x,num1,color='r',width=0.3,label=names[0])
plt.bar(x+0.3,num2,color='k',width=0.3,label=names[1])
plt.bar(x+0.6,num3,color='g',width=0.3,label=names[2])
plt.rcParams['font.family']='SimHei'
plt.ylabel('单日票房数')
plt.xticks(x+0.3,['第一天',' 第二天',' 第三天'],fontproperties='KaiTi')

plt.legend()
plt.show()

