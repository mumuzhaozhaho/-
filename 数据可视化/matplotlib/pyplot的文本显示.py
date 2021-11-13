'''
plt.xlabel():对x轴增加文本标签；
plt.ylabel():对y轴增加文本标签；
plt.title():对图形整体增加文本标签；
plt.text():在任意位置增加文本；
plt.annotate(s,xy,xytext,arrowprops=dicts):在图形中增加带箭头的注解；s要注解的字符串， xy表示箭头位置,xytext文本位置，
plt.savefig('result.jpg') #如果直接写成 plt.savefig('cos') 会生成cos.png
plt.axis([0,5,-2,2])  x轴0-5 y-2 到2
plt.xlim（）
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
a=np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a))
plt.xlabel('横轴——时间',fontproperties='SimHei',fontsize=20,color='g')
plt.ylabel('纵轴——幅值',fontproperties='SimHei',fontsize=20,color='r')
plt.title('正弦波',fontproperties='SimHei',fontsize=20,color='b')

plt.text(2.5,0.5,'t=2.5')          #文本对应的坐标值
plt.annotate('t=1s',xy=(1,1.0),xytext=(2,1.5),arrowprops=dict(facecolor='y',shrink=0.1,width=20))
plt.axis([0,5,-2,2])
plt.grid(True)         #有无栅格
plt.show()