import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
#计算x和y的相交点a
X,Y=np.meshgrid(x,y)
print(X,Y)
# 计算Z的坐标
Z=np.sqrt(X**2+Y**2)
# contour和contourf都是画三维等高线图的，不同点在于contour() 是绘制轮廓线，contourf()会填充轮廓。除非另有说明，否则两个版本的函数是相同的。
plt.contourf(X,Y,Z)
plt.contour(X,Y,Z)
plt.show()

# 颜色越深表示值越小，中间的黑色表示z=0.

