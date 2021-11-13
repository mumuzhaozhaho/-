# plt.polar(theta,r)绘制极坐标图
import matplotlib.pyplot as plt
import numpy as np
n=20
theta=np.linspace(0,2*np.pi,n,endpoint=False)
radii=10*np.random.rand(n)
width=np.pi/4*np.random.rand(n)
plt.show()
