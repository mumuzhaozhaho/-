import matplotlib.pyplot as plt
import numpy as np
#plt.subplot(nrows, ncols, num, **kwargs)(横轴数量，纵轴数量，子区域)
#plt.subplot2grid(gridspec,curspec,colspan,rowspan)
#plt.subplot2grid((3,3),(1,0),colspan=2) 把表格分成3*3的9块，选中第1行第0列，列数为2

plt.subplot(2,2,3)
plt.plot([5,10,2,3])
plt.subplot(2,2,4)
plt.plot([1,2,3,4],[1,2,3,4])
plt.show()

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

a=np.arange(0.0,5.0,0.02)
plt.subplot(2,1,1)
plt.plot(a,f(a))
plt.subplot(2,1,2)
plt.plot(a,np.cos(2*np.pi*a),'--or')
plt.show()

plt.subplot2grid((3,3),(1,1),colspan=2)
plt.plot(a,f(a))
plt.subplot2grid((3,3),(1,0),rowspan=2)
plt.plot(a,np.cos(2*np.pi*a),'--or')
plt.show()