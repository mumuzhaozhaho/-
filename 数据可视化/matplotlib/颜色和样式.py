import matplotlib.pyplot as plt
import numpy as np

#设置x，y
x=np.linspace(-10,10,100)
y1=2*x
#设置x，y的范围
plt.xlim(0,5)
plt.ylim(0,10)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y1)
ax = plt.gca()
ax.spines['top'].set_color('red')
ax.spines['bottom'].set_linewidth(0)
plt.show()
#设置边框     ax = plt.gca() gca : get current axis
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
# ax.spines['bottom'].set_linewidth(bwith)
# ax.spines['left'].set_linewidth(bwith)
# ax.spines['top'].set_linewidth(bwith)
# ax.spines['right'].set_linewidth(bwith)
# plt.grid( color = 'black',linestyle='-.',linewidth = 1)
