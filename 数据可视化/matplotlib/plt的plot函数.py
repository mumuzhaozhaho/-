import matplotlib.pyplot as plt
import numpy as np
# plt.plot(x,y,format_string,**kwargs) 颜色  线形 标记
'''
plt.plot(x, y, ls='-', lw=2,  color='g' )
x： x轴上的值
y： y轴上的值
ls：线条风格 (linestyle)
lw：线条宽度 (linewidth)
label：标签文本
plt.legend()  图例 默认位置是左上角 
添加图例右下角lower right   边框  透明度  阴影  边框宽度
plt.legend(loc='lower right',fancybox=True,framealpha=1,shadow=True,borderpad=1)

'''
#绘制多条曲线
a=np.arange(0,10,2)
plt.plot(a,a,'r-*',a,a*2,'-.b1',a,a*3,'k:^',a,a*4,'y p')
plt.show()
plt.plot([1,2,3,4],[1,2,2,4],ls='--',lw=10,color='k',label='--')
plt.legend(loc='lower center',fancybox=True,framealpha=1,shadow=True,borderpad=10)
plt.show()
help(plt.legend)