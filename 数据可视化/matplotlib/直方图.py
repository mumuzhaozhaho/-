#plt.hist(x,bins,normed)绘制直方图
#bins 表示直方的个数，density=1，归一化表示出现的概率
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
loc,si=100,20
a=np.random.normal(loc,si,100)
plt.subplot(2,2,1)
plt.hist(a,10)
plt.subplot(2,2,2)
plt.hist(a,20)
plt.subplot(2,2,3)
plt.hist(a,50)
plt.subplot(2,2,4)
plt.hist(a,50,facecolor='r',density=1)
plt.show()
