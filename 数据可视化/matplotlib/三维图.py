import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
X=[1,1,2,2]
Y=[3,4,4,3]
Z=[1,100,1,1]
fig = plt.figure()
# 创建了一个Axes3D的子图放到figure画布里面
ax = Axes3D(fig)
ax.plot_trisurf(X, Y, Z)
plt.show()


