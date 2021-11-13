from PIL import Image as im
import numpy as np
a=np.asarray(im.open('E:\pycharm\数据可视化\\numpy\\2.jpeg').convert('L')).astype('float')
depth=10      # (0-100)
grand=np.gradient(a)
grand_x,grand_y=grand    #取图像灰度的梯度值 grad_x, grad_y = grad  #分别取横纵图像梯度值

grand_x=depth*grand_x/100
grand_y=depth*grand_y/100

A=np.sqrt(grand_x**2+grand_y**2+1.) #构造x和y轴梯度的三维归一化单位坐标系
uni_x=grand_x/A
uni_y=grand_y/A
uni_z=1./A
vec_el=np.pi/2.2 # 光源的俯视角度，弧度值
vec_az=np.pi/4.# 光源的方位角度，弧度值
dx=np.cos(vec_el)*np.cos(vec_az) #光源对x 轴的影响
dy=np.cos(vec_el)*np.sin(vec_az) #光源对y 轴的影响
dz=np.sin(vec_el)#光源对z 轴的影响
b=255*(dx*uni_x+dy*uni_y+dz*uni_z) #光源归一化，将梯度转化为灰度
b=b.clip(0,255)
c=im.fromarray(b.astype('uint8'))  #重构图像
c.save('E:\pycharm\数据可视化\\numpy\\4.jpeg')