'''PIL库
图像处理能力的第三方库
'''
from PIL import Image  as im
import numpy as np
a=np.array(im.open('E:\pycharm\数据可视化\\numpy\\2.jpeg'))
print(a.shape,a.ndim,a.dtype)
print(a)