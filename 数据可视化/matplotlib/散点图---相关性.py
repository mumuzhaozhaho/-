#颜色 c
#点大小 s
#透明度 alpha
#点的形状 marker
'''x, y, s = s, c = c, marker = marker, cmap = cmap, norm = norm,
vmin = vmin, vmax = vmax, alpha = alpha, linewidths = linewidths,
edgecolors = edgecolors, plotnonfinite = plotnonfinite,
'''

import numpy as np
import matplotlib.pyplot as plt

weight=[50,58,60,67,72]

height=[160,167,170,173,177]
plt.scatter(height,weight,s=200,c='g',marker='*',alpha=0.8)
plt.show()


x=np.random.randn(100)
y=np.random.randn(100)
plt.scatter(x,y,marker='<')
plt.show()

x1=np.random.randn(100)
y1=0.1*np.random.randn(100)+10*x1

plt.scatter(x1,y1,marker='>')
plt.show()
np.random.seed(0)
x=np.random.rand(100)
y=np.random.rand(100)
color=np.random.rand(100)
size=np.random.rand(100)*100
plt.scatter(x,y,c=color,s=size)
plt.show()
