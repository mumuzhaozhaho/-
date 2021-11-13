'''
pyplot不支持中文显示
1 使用rcParams修改字体实现       修改全局字体
    font.family     字体名称
    font.style   字体风格 正常为normal 斜体为 italic
    font.size     字体大小
2  在有中文输出的地方增加一个属性   fontproperties

'''

import matplotlib.pyplot as plt
import matplotlib
import  numpy as np
plt.rcParams['font.family']='Simhei' #修改全局字体
plt.plot([5,10,15,20])
plt.ylabel('纵坐标')
plt.show()
a=np.arange(0,5,0.01)
plt.plot(a,np.cos(2*np.pi*a))

plt.xlabel('横-时间',fontproperties='KaiTi',fontsize=15)
plt.ylabel('纵-幅值',fontproperties='KaiTi',fontsize=15)
plt.show()