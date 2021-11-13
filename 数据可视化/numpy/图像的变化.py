from PIL import Image as im
import numpy as np
a=np.array(im.open('E:\pycharm\数据可视化\\numpy\\2.jpeg'))
print(a.shape,a.ndim,a.dtype)
print(a)
b=[255,255,255]-a
c=im.fromarray(b.astype('uint8'))
c.save('E:\pycharm\数据可视化\\numpy\\3.jpeg')